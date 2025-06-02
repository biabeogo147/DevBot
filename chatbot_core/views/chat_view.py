import json
from base.base_view import BaseController
from django.views.decorators.csrf import csrf_exempt
from chatbot_core.services.chat_service import on_chat_request


class ChatController(BaseController):

    @csrf_exempt
    def chat(self, request):
        """
        Handles chat requests by processing the message and conversation ID.
        """
        body_str = request.body.decode('utf-8')
        body = json.loads(body_str)
        result = on_chat_request(
            message=body['message'],
            is_insert = request.method == 'POST',
            conversation_id=int(body['conversation_id']),
            is_new_conversation=int(body['is_new_conversation']),
        )
        return self.handle_success(data=result)