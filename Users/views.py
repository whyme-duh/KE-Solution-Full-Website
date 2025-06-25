from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm
from . models import Profile
from django.views.generic.detail import DetailView

def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.all()
    return render(request, 'users/profile.html', {'profile': profile})

# class ProfileDetailedView(DetailView):
#     model = Profile
#     template_name = 'users/profile.html'

