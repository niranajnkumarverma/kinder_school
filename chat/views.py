from email import message
from django.shortcuts import render

from chat.models import Message, Room

# Create your views here.
def index(request):
    return render(request, 'user/chat_index.html', {'rooms':Room.objects.all(),})



def room_view(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter()[0.25]
    return render(request, 'user/room.html', {
        'room': room,'messages':messages
    })