from django import forms
from .models import *

class MessageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['sender_name'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        self.fields['phone'].widget.attrs['readonly'] = True

    class Meta:
        model = Message
        fields = ('sender_name', 'email', 'phone', 'action_taken')