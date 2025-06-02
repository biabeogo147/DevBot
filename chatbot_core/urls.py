from django.urls import path
from .controllers.chat_view import ChatController

chat_controller = ChatController()


urlpatterns = [
    path("chat/", chat_controller.chat, name="chat"),
]