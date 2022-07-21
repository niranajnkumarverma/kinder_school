from django import forms
from superadmin.models import Notification

class TestNotification(forms.Form):
	title = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter your publish title',

            }
        ))
	body = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter your body tage',

            }
        ))
	icon_url = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Image to display.',

            }
        ))
	url = forms.CharField(required=True, widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Url to open by clicking.',

            }
        ))

	# def save(self,request,commit=True):
	# 	notification = Notification.objects.create(user=request.user
	# 		# self.cleaned_data['user_id'],
	# 		# self.cleaned_data['title'],
	# 		# self.cleaned_data['body'],
	# 		# self.cleaned_data['icon_url'],
	# 		# self.cleaned_data['url'],

	# 	)
	# 	notification.save()
	# 	return notification

	class Meta:
		model = Notification
		fields = ['title', 'body', 'icon_url', 'url']

	# def __init__(self, *args, **kwargs):
	# 		super(TestNotification, self).__init__(*args, **kwargs)
	# 		for field in self.fields:
	# 			self.fields[field].widget.attrs.update({
	# 			'class': 'form-control'})
