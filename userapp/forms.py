from django import forms

from userapp.models import SignUpUser

class SignUpForm(forms.ModelForm):
    class Meta():
        model=SignUpUser
        exclude=["first_name","last_name","email","confirm_password","SignUp_date","SignUp_time"]