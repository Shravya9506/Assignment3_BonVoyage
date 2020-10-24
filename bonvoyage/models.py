from django.db import models


class Messages(models.Model):
    sender_name = models.CharField(max_length=60, verbose_name='Vacation name')
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + self.message
