from django import forms
from home.models import Image, Video





class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile",]

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "schoolimage",]
