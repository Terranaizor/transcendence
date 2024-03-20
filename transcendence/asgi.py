"""
ASGI config for transcendence project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import transcendence.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transcendence.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # HTTP protocol (default Django application)
    "http": django_asgi_app,

    # WebSocket protocol (Django Channels application)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            transcendence.routing.websocket_urlpatterns
        )
    ),
})