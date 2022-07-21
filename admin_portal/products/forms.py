from django import forms
from product.models import Author, Publisher, Book
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AddBookForm(forms.ModelForm):
    author_name = forms.CharField(label='Author*', required=True, widget=forms.TextInput(

        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Author Name',
           
        }

    ))
    publisher_name = forms.CharField(label='Publisher*', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ' Enter publisher name',

        }
    ))
    book_name = forms.CharField(label='Books Name*', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ' Enter Book name',

        }
    ))
    book_description = forms.CharField(label='Book description*', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ' Enter Book description',

        }
    ))
    book_price = forms.IntegerField(label='Publisher*', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ' Enter publisher name',

        }
    ))
    book_image = forms.IntegerField(label='Book Image*', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Upload Book Image',

        }
    ))
   
    
    def save(self, commit=True):
        book = Book.objects.create_book(
            self.cleaned_data['author_name'],
            self.cleaned_data['publisher_name'],
            self.cleaned_data['book_name'],
            self.cleaned_data['book_description'],
            self.cleaned_data['book_price'],
            self.cleaned_data['book_image']
            
        )
        return book
    class Meta():
        model = Book
        fields = ['author_name','publisher_name','book_name','book_description', 'book_price', 'book_image']

    def __init__(self, *args, **kwargs):
            super(AddBookForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({
                'class': 'form-control'})
              
        

class AddPublisherForm(forms.ModelForm):
    class Meta():
        model = Publisher
        fields = ['publisher_name',]

class UpdatePublisherForm(forms.ModelForm):
    class Meta():
        model = Publisher
        fields = ['publisher_name',]

class AddAuthorForm(forms.ModelForm):
    class Meta():
        model = Author
        fields = ['author_name',]        
   

