from django.db import models


class Conversation(models.Model):
    topic = models.CharField(max_length=255)

    def __str__(self):
        return f"Conversation: {self.id} - {self.topic}"