import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.receiver_username = self.scope['url_route']['kwargs']['receiver_username']
        self.sender = self.scope['user']

        # Vérifiez ici si l'utilisateur est autorisé à se connecter au chat avec le destinataire spécifié
        # Vous pouvez utiliser self.sender et self.receiver_username pour effectuer les vérifications nécessaires

        self.chat_group_name = f'chat_{self.receiver_username}'

        # Rejoindre le groupe de chat
        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        # Accepter la connexion WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Quitter le groupe de chat lorsque la connexion WebSocket est fermée
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        # Récupérer le nom d'utilisateur du sender
        sender_username = data['sender']

        # Récupérer l'instance de modèle User correspondant au sender (utiliser sync_to_async ici)
        sender = await sync_to_async(User.objects.get)(username=sender_username)

        # Récupérer le nom d'utilisateur du receiver
        receiver_username = data['receiver']
        # Récupérer l'instance de modèle User correspondant au receiver (utiliser sync_to_async ici)
        receiver = await sync_to_async(User.objects.get)(username=receiver_username)

        # Enregistrez le message dans la base de données (utiliser sync_to_async ici)
        await sync_to_async(Message.objects.create)(
            message_content=message,
            sender=sender,
            receiver=receiver,
        )

        # Envoyer le message à tous les membres du groupe de chat (destinataire inclus)
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender_username,  # Utilisez le nom d'utilisateur du sender ici
                'receiver': receiver_username,  # Utilisez le nom d'utilisateur du receiver ici
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']
        print(f"Received message: {message} from {sender}")

        # Envoyer le message à l'utilisateur connecté via la connexion WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'receiver': receiver,
        }))
