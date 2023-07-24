import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Logique de connexion, par exemple, vérification des autorisations
        await self.accept()

    async def disconnect(self, close_code):
        # Logique de déconnexion
       await self.close()

    async def receive(self, text_data):
        # Logique de réception des messages
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.send_message(text_data)


    async def send_message(self, text_data):
        # Logique d'envoi des messages à tous les clients connectés
     await self.send(text_data=text_data)