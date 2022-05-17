from email import message
import json
from os import sync
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room,Message
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.room = Room.objects.get(name=self.room_name)


        # connection has to be accepted
        await self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    async def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data=None, bytes_data=None):
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            username = text_data_json['username']
            room = text_data_json['room']

            await self.save_message(username,room, message)
        
            # send chat message event to the room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username':username,
                    'room':room,
                }
            )

    async def chat_message(self, event):
            message = event['message']
            username = event['username']
            room = event['room']
            await self.send(text_data=json.dumps({
                'message':message,
                'username':username,
                'room':room,
            }))
    @async_to_sync
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)   
        room = Room.objects.get(slug = room)
        Message.objects.create(user=user, room=room,content=message)     