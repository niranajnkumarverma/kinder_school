from cProfile import Profile
from django import forms
from student.models import Profile
from home.models import User

class StudentListForm(forms.ModelForm):
    
    class Meta():
        model = Profile
        fields = ['image','mobile','gender','country','state','city','pincode' ]
        
class AddUserForm(forms.ModelForm):
    
    class Meta():
        model = Profile
        fields = ['image','mobile','gender','country','state','city','pincode' ]
        
     


