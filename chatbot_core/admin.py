from django.contrib import admin
from chatbot_core.models.conversation import Conversation
from chatbot_core.models.chat_template import ChatTemplate

admin.site.register(Conversation)
admin.site.register(ChatTemplate)
