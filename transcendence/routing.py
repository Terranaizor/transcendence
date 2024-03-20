from django.urls import path
from game.consumers import MyConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    path('ws/my_consumer/', MyConsumer.as_asgi()),
]
