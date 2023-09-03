from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request=request, template_name='users/register.html', context={'form': form})
