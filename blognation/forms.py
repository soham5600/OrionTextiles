from django.forms import ModelForm,TextInput,IntegerField
from .models import Data
class Queryform(ModelForm):
	class Meta:
		model=Data
		fields="__all__"
		widgets={
		"name":TextInput(attrs={"class":"form-control","placeholder":"Enter Your Name"}),
		"email":TextInput(attrs={"class":"form-control","placeholder":"Enter Your Email"}),
		"cloth":TextInput(attrs={"class":"form-control","placeholder":"Enter The Cloth That You Need"}),
		"dimension":TextInput(attrs={"class":"form-control"})
		}