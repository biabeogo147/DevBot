from django.urls import path
from .views.chat_view import ChatController

chat_controller = ChatController()


urlpatterns = [
    path("chat/", chat_controller.chat, name="chat"),
]