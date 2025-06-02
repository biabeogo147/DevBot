from django.db import models


class ChatTemplate(models.Model):
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=50, choices=[('user', 'User'), ('assistant', 'Assistant'), ('system', 'System')])
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE, related_name='belongs_to_conversation')

    def __str__(self):
        return f"Chat: {self.id} - {self.role} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {{{self.conversation}}}"