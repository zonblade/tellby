from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

#from obrolan.consumers import ChatConsumer
application = ProtocolTypeRouter({
    'websocket':AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    #url(r"^websocket/(?P<username>[\w.@+-]+)/$", ChatConsumer()),
                ]
            )
        )
    )
})