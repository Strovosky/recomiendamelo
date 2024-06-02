from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = "main"

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="about", view=views.about, name="about"),
    path(route="contact", view=views.contact, name="contact"),
    path(route="categories", view=views.categories, name="categories"),
    path(route="profile/my_posts", view=views.my_posts, name="my_posts"),
    path(route="profile/my_posts/<int:id>", view=views.individual_post, name="individual_post"),
    path(route="categories/<str:categ>", view=views.category, name="category"),
    path(route="categories/category_processor/<str:categ>", view=views.category_processor, name="category_processor"),
    path(route="posts/<str:q>", view=views.posts_query, name="posts_query")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

