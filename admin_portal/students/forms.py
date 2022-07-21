
from django import forms
from home.models import  User
from student.models import Student



class StudentListForm(forms.ModelForm):
    
    class Meta():
        model = Student
        fields = ['prof_image','mobile','gender','country','state','city','pincode' ]
        
class AddUserForm(forms.ModelForm):
    
    class Meta():
        model = Student
        fields = ['prof_image','mobile','gender','country','state','city','pincode' ]
        
     


