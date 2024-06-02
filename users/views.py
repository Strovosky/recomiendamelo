from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import not_logged_user
from .forms import UserUpdateForm, ProfileUpdateForm
from main.models import Post
from django.contrib.auth.models import User

# Create your views here.

@not_logged_user
def signup(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
        else:
            return redirect("/signup")
    elif response.method == "GET":
        form = UserCreationForm()
        return render(response, "users/signup.html", {"form":form})


@login_required
def profile(request):
    context = {}
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        context.update({"user":user})
        if request.POST.get("new_post") == "clicked":
            new_title, new_category = request.POST.get("title"), request.POST.get("category")
            new_post = Post.objects.create(user=user, title=new_title, category=new_category)
            new_post.save()
            context.update({"new_post":new_post})
    else:
        context.update({"user":request.user})
    return render(request, "users/profile.html", context=context)


@login_required
def profile_update(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
    else:
        user_update_form = UserUpdateForm()
        profile_update_form = ProfileUpdateForm()
    context = {'u_form': user_update_form, 'p_form': profile_update_form}
    return render(request, 'users/profile_update.html', context=context)

