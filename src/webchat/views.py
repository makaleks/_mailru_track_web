from models import Chat
from webbelonger.views import BelongerViewSet

from serializers import ChatSerializer
from models import Chat

from django.shortcuts import render
from django.http import HttpResponse


class ChatViewSet(BelongerViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

def render_chat_list(request):
    return render(request, 'chat_list.html', {
            'chat_list': Chat.objects.all(),
        })

def render_chat(request, pk):
    return render(request, 'chat.html', {
            'chat': Chat.objects.get(id = pk),
        })
