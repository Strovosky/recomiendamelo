from django.db.models import Model, CharField, IntegerField, ForeignKey, DateTimeField, ManyToManyField, ForeignKey, SET_NULL, CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Post(Model):

    CATEGORY_CHOICES = [
        ("producto","Producto"),
        ("empresa","Empresa"),
        ("música","Música"),
        ("pelicula","Pelicula"),
        ("famoso","Famoso"),
        ("vida","Vida"),
    ]

    user = ForeignKey(to=User, on_delete=SET_NULL, null=True)
    title = CharField(verbose_name="title", max_length=300, help_text="What is your post about?", unique=True)
    category = CharField(verbose_name="category", max_length=8, choices=CATEGORY_CHOICES, default="vida", help_text="what category is it?")
    date_created = DateTimeField(verbose_name="date", auto_now_add=True, help_text="when this post was created")

    def __str__(self) -> str:
        return self.title



class Tag(Model):

    name = CharField(verbose_name="name", max_length=20, help_text="the name of the tag")
    posts = ManyToManyField(to=Post)

    def __str__(self) -> str:
        return self.name


class Comment(Model):
    post = ForeignKey(to=Post, on_delete=CASCADE)
    user = ForeignKey(to=User, on_delete=SET_NULL, null=True)
    text = CharField(verbose_name="text", max_length=300)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.post.title}"



