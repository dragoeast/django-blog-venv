from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, message=f'Your account has been created! You are able to log in now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request=request, template_name='users/register.html', context={'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request=request, template_name='users/profile.html', context=context)


