from django.db import models


class Message(models.Model):
    sender_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=12, null= True)
    message = models.TextField()
    action_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.sender_name + self.message
