from django.forms import ModelForm
from django import forms
from .models import *


class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widget = {
            'body' : forms.TextInput(attrs={ 'placeholder': 'Type your message here...', 'class': 'p-4 text-black', 'maxlength': '300', 'autofocus': True}),
        }


class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widget = {
            'groupchat_name' : forms.TextInput(attrs={
                'placeholder': 'Enter group name...',
                'class' : 'p-4 text-black',
                'max_length': '300',
                'auto_focus': True,
            })
        }



class ChatRoomEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name' : forms.TextInput(attrs={
                'class' : 'p-4 text-xl font-bold mb-4',
                'max_length' : '300',
            }),
        }