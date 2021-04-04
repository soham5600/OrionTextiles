from django.forms import ModelForm,TextInput,IntegerField,EmailInput,Select
from .models import Data, Feedback
CLOTH_CHOICES = ( 
    ("1", "100% Cotton"), 
    ("2", "Polycotton"), 
    ("3", "Polyviscos"), 
    ("4", "100% Polycotton")
)
class Queryform(ModelForm):
	class Meta:
		model=Data
		fields="__all__"
		widgets={
		"name":TextInput(attrs={"class":"form-control","placeholder":"Enter Your Name"}),
		"email":EmailInput(attrs={"class":"form-control"}),
		"cloth":Select(attrs={"class":"form-control"},choices=CLOTH_CHOICES),
		"dimension":TextInput(attrs={"class":"form-control"})
		}
class Feedbackform(ModelForm):
	class Meta:
		model=Feedback
		fields="__all__"
		widgets={
		"name2":TextInput(attrs={"class":"form-control","placeholder":"Enter Your Company's Name"}),
		"review":TextInput(attrs={"class":"form-control","placeholder":"Write your review"}),
		
		}


		##placeholder":"Enter Your Email",   "placeholder":"Enter The Cloth That You Need"