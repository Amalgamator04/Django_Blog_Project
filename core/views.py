from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, UserRegistrationForm
from .models import Post


class CustomLoginView(LoginView):
    template_name = 'core/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'core/logout.html'


def home(request):
    posts = Post.objects.order_by('-created_at')[:6]
    if not posts.exists():
        posts = [
            Post(title='Stylish Photography', summary='A placeholder for your first blog post or portfolio highlight.', image_url='https://via.placeholder.com/600x400'),
            Post(title='Cinematic Videography', summary='Display your ad and video projects with rich storytelling.', image_url='https://via.placeholder.com/600x400'),
            Post(title='Creative Campaigns', summary='Showcase photography and ad campaigns to attract clients.', image_url='https://via.placeholder.com/600x400'),
        ]
    return render(request, 'core/home.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created and you are now logged in.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully.')
            return redirect('profile')
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete this post.')
        return redirect('profile')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('profile')

    return render(request, 'core/delete_post.html', {'post': post})


@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'core/profile.html', {'user_posts': user_posts})
