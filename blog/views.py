from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .models import Post
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Now you can log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form' : form})



@login_required
def blogs(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/blogs.html', context)

# Create your views here.
