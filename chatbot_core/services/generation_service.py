from typing import List
from chatbot_core.models.chat_template import ChatTemplate


def generate_answer(chat_history: List[ChatTemplate]) -> str:
    return "Generated response based on chat history."


def on_chat_request(message: str, conversation_id: int, is_insert: bool = False) -> List[ChatTemplate]:
    """
    Processes the chat request by generating a response based on the message and conversation ID.

    Args:
        message (str): The message to process.
        conversation_id (int): The ID of the conversation.
        is_insert (bool): Flag indicating whether to insert the message into the database.

    Returns:
        List[ChatTemplate]: A list of ChatTemplate objects associated with the conversation.
    """
    chat_template_query = ChatTemplate.objects.filter(conversation__exact=conversation_id)
    list_chat_templates = list(chat_template_query) + [ChatTemplate(message=message, conversation_id=conversation_id)]
    assistant_response = ChatTemplate(role="Assistant", message=generate_answer(list_chat_templates), conversation_id=conversation_id)

    if is_insert:
        ChatTemplate.objects.create(role="User", message=message, conversation_id=conversation_id)
        ChatTemplate.objects.create(role="Assistant", message=assistant_response.message, conversation_id=conversation_id)


    return list_chat_templates + [assistant_response]