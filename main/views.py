from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(response):
    posts = Post.objects.all()[:20]
    context = {"posts":posts}
    return render(response, "main/index.html", context)


def about(request):
    return render(request, "main/about.html", {})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=subject,
            message=f"{name}/n{message}",
            from_email=email,
            recipient_list=[User.objects.get(username="strovosky1").email] #Who will receive the email (You)
        )
    return render(request, "main/contact.html", {})


def categories(request):
    if request.method == "POST":
        if request.POST.get("search_btn") == "clicked":
            q = request.POST.get("post_search")
            return HttpResponseRedirect(reverse("main:posts_query", args=(q,)))
            
    return render(request, "main/categories.html", {})

@login_required
def my_posts(request):
    my_posts = Post.objects.filter(user_id=request.user.id).reverse()
    context = {"my_posts":my_posts}

    pagination =    Paginator(my_posts, 3)
    page = request.GET.get("page")
    paginated_posts = pagination.get_page(page)

    context.update({"paginated_posts":paginated_posts})    

    return render(request, "main/my_posts.html", context)


def individual_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get("delete_post_btn") == f"{post.id}":
            post.delete()
            return HttpResponseRedirect(reverse('main:my_posts'))
        elif request.POST.get("create_comment") == f"{post.id}":
            new_comment = Comment.objects.create(post=post, user=User.objects.get(id=request.user.id), text=request.POST.get("comment_text"))
            new_comment.save()
        context = {"post":post}
        return render(request, "main/individual_post.html", context)
    context = {"post":post}
    return render(request, "main/individual_post.html", context)


def category(request, categ):
    posts = Post.objects.filter(category=categ).reverse()
    context = {"posts":posts}

    pagination = Paginator(posts, 3)
    page = request.GET.get("page")
    paginated_posts = pagination.get_page(page)

    context.update({"paginated_posts":paginated_posts, "category":categ})

    return render(request, "main/category.html", context)


def category_processor(request, categ):
    return HttpResponseRedirect(reverse("main:category", args=(categ,)))


def posts_query(request, q):
    posts = Post.objects.filter(title__icontains=q)

    pagination = Paginator(posts, 5)
    page = request.GET.get("page")
    paginated_posts = pagination.get_page(page)

    context = {"paginated_posts":paginated_posts}

    return render(request, "main/posts.html", context)
    


