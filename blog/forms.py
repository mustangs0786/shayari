from django import forms
from .models import Post
from django.contrib.auth.models import User

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
