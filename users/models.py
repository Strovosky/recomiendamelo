from django.db.models import Model, OneToOneField, CASCADE, IntegerField, TextField, ImageField
from django.contrib.auth.models import User

# Create your models here.


class Profile(Model):

    GENDER_CHOICES = [
        ('Male','male'),
        ('Female','female'),
        ('Other','other')
    ]

    user = OneToOneField(to=User, on_delete=CASCADE)
    age = IntegerField(verbose_name="age", blank=True, null=True)
    gender = TextField(verbose_name='gender', blank=True, null=True, choices=GENDER_CHOICES)
    profile_pic = ImageField(verbose_name='profile picture', default='profile_pic.jpg', upload_to='profile_pics')

    def __str__(self) -> str:
        return f'{self.user.username} - Profile'

