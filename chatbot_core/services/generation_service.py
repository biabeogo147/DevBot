from typing import List
from django.shortcuts import get_object_or_404
from chatbot_core.models.conversation import Conversation
from chatbot_core.models.chat_template import ChatTemplate


def generate_answer(chat_history: List[ChatTemplate]) -> str:
    return f"Generated response based on chat history. {len(chat_history)} messages processed."


def generate_topic(message: str) -> str:
    """
    Generates a topic based on the provided message.

    Args:
        message (str): The message to generate a topic from.

    Returns:
        str: A generated topic string.
    """
    return f"Testing Topic {message[:10]}..."


def on_chat_request(
        message: str,
        is_insert: bool = False,
        conversation_id: int = None,
        is_new_conversation: int = 0,
) -> List[ChatTemplate]:
    """
    Processes the chat request by generating a response based on the message and conversation ID.

    Args:
        message (str): The message to process.
        conversation_id (int): The ID of the conversation.
        is_new_conversation (bool): Flag indicating whether this is a new conversation.
        is_insert (bool): Flag indicating whether to insert the message into the database.

    Returns:
        List[ChatTemplate]: A list of ChatTemplate objects associated with the conversation.
    """

    conversation = get_object_or_404(Conversation, pk=conversation_id)

    if is_new_conversation and conversation is None:
        conversation = Conversation.objects.create(topic=generate_topic(message))

    chat_template_query = ChatTemplate.objects.filter(conversation__exact=conversation_id)
    list_chat_templates = list(chat_template_query) + [ChatTemplate(message=message, conversation_id=conversation_id)]
    assistant_response = ChatTemplate(role="Assistant", message=generate_answer(list_chat_templates), conversation_id=conversation_id)

    if is_insert:
        ChatTemplate.objects.create(role="User", message=message, conversation_id=conversation.id)
        ChatTemplate.objects.create(role="Assistant", message=assistant_response.message, conversation_id=conversation.id)

    return list_chat_templates + [assistant_response]