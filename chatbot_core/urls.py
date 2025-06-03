from django.urls import path
from .views.chat_view import ChatView

chat_controller = ChatView()


urlpatterns = [
    path("chat/", chat_controller.chat, name="chat"),
]