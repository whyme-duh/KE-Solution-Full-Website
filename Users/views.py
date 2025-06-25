from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm
from . models import Profile
from django.contrib.auth import logout, login, authenticate
from django.views.generic.detail import DetailView
from django.contrib import messages

def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Sucessfully registered the account. You can login now!')
            return redirect('login')
        else:
            messages.error(request, f'Error, try again!')

            form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.all()
    return render(request, 'users/profile.html', {'profile': profile})

# class ProfileDetailedView(DetailView):
#     model = Profile
#     template_name = 'users/profile.html'

def logout_view(request):
    logout(request)
    messages.success(request, f'Logout sucessfully')
    return redirect('login')






