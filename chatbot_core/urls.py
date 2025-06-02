from django.urls import path
from .controllers import chat_controller

chat_controller = chat_controller.ChatController()


urlpatterns = [
    path("chat/", chat_controller.chat, name="chat"),
]