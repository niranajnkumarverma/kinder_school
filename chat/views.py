from django.shortcuts import render

from chat.models import Message, Room
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'user/chat_index.html', {'rooms':Room.objects.all(),})

def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter()
    return render(request, 'user/room.html', {
        'room': chat_room,'messages':messages
    })


# def index_view(request):
#     return render(request, 'user/chat_index.html', {
#         'rooms': Room.objects.all(),
#     })


