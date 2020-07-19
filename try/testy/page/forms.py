from django import forms
from page.models import page

class pageForm(forms.ModelForm):
	"""fullname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	emailid=forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	address=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	qualification=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	education=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	interest=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	references=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
	Extraskills=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))	
	"""
	class Meta:
		model= page
		fields= "__all__"
