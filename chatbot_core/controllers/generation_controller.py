from base.base_controller import BaseController
from chatbot_core.services.generation_service import on_chat_request


class GenerationController(BaseController):
    def chat(self, request):
        """
        Handles chat requests by processing the message and conversation ID.
        """
        body = request.body.decode("utf-8")
        result = on_chat_request(message=body['message'], conversation_id=body['conversation_id'], is_insert = request.method == 'POST')
        return self.handle_success(data=result)