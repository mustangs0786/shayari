from django import forms
from .models import Post,Contact,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
class CreateForm(forms.ModelForm):	
	class Meta:
		model = Post
		fields={
		'title',
		'body',
		'image',
		}
	def clean(self):
		title = self.cleaned_data.get('title')
		body = self.cleaned_data.get('body')
		if len(title)<2:
			raise forms.ValidationError("Dont Write One Character ,Write Proper Title")
		if len(body)<2:
			raise forms.ValidationError("Take Your heart Properly, Please Write more")
		
		return self.cleaned_data


class ContactForm(forms.ModelForm):
	

	class Meta:
		model= Contact
		fields = {
		'Name',
		'Email',
		'Telephone',
		'Subject',
		'Message',
		}
	def cleaned(self):
		Name=request.POST.get('Name')
		Email=request.POST.get('Email')
		Telephone=request.POST.get('Telephone')
		Subject=request.POST.get('Subject')
		Message=request.POST.get('Message')
		return self.cleaned_data
		
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = {
		'content',
		}
		
class UserLoginForm(forms.Form):
	def cleaned(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
   # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2', )
	def cleaned_data(self):
		username=request.POST.get('username')
		first_name=request.POST.get('first_name')
		email=request.POST.get('email')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')	
		
		if password1 != password2:
			raise forms.ValidationError("Password Mismatch")
		return self.cleaned_data		
