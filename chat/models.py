from django.db import models
from home.models import User


class Room(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    online = models.ManyToManyField(to=User, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'


class Message(models.Model):
    user = models.ForeignKey(to=User, related_name="messages" ,on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, related_name="messages" , on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("date_added",)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.date_added}]'
