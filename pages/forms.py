from django.forms import ModelForm
from django import forms
from .models import Project, Certificate

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'


class ContactForm(forms.Form):
	your_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)


class CertificateForm(ModelForm):
	class Meta:
		model = Certificate
		fields = '__all__'