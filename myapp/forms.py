from django import forms
from django.core import validators
from django.contrib.auth.models import User
from myapp.models import UserInfo


class UserForm(forms.ModelForm):
    username = forms.CharField(validators=[validators.MinLengthValidator(6),
                                           validators.MaxLengthValidator(16)])
    password = forms.CharField(widget=forms.PasswordInput,
                               validators=[validators.MinLengthValidator(6)])
    re_password = forms.CharField(widget=forms.PasswordInput,
                                  validators=[validators.MinLengthValidator(6)])

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError("Passwords does not match")

class UserInfoForm(forms.ModelForm):
    email = forms.EmailField()
    prof_pic = forms.ImageField(required=False)
    class Meta():
        model = UserInfo
        fields = ('email', 'prof_pic')
