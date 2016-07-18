from django import forms
from .models import Join

# This is non-inhereting django form 
class EmailForm(forms.Form):
	email = forms.EmailField(required=True)














# This is a form inhereting from the model 

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ('email',)