from django.urls import path
from controllers import generation_controller


urlpatterns = [
    path("chat/", generation_controller.GenerationController.chat, name="chat"),
]