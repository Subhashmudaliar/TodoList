from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
	text = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control text-center', 'id':'exampleInputEmail1' ,'aria-describedby':'emailHelp', 'placeholder':'Enter Todo'}))
	class Meta:
		model=Todo
		fields=('text',)	



