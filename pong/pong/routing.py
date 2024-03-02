from django.urls import path
from .consumers import MyConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    path('ws/my_consumer/', MyConsumer.as_asgi()),
]
# application = ProtocolTypeRouter({
#     'websocket': URLRouter(websocket_urlpatterns),
# })
