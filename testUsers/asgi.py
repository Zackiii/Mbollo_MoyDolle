# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from messaging.routing import websocket_urlpatterns
from messaging import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testUsers.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
