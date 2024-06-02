from django.contrib.auth.models import User
from .models import Profile
from django.forms import EmailField, CharField, ModelForm, IntegerField, ImageField


class UserUpdateForm(ModelForm):
    username = CharField(max_length=20, required=False, label="username", help_text="Max 20 letters long")

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
    age = IntegerField(required=False)
    gender = CharField(required=False)
    profile_pic = ImageField(required=False)
    
    class Meta:
        model = Profile
        fields = ['age', 'gender', 'profile_pic']