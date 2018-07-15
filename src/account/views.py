from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .forms import signupForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        if username is not "":
            try:
                user = auth.authenticate(username=username.lower(), password=password)
                if user is not None:
                    auth.login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    return redirect("conference:welcome")
                else:
                    messages.error(request, "Username and password did not match")
            except auth.ObjectNotExist:
                messages.error(request, "User does not exit")
        else:
            messages.error(request, "Enter Username and Password")
    return render(request, "login.html", {})

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            auth.models.User.objects.create_user(username=username.lower(),first_name=firstName,last_name=lastName,email=email.lower(),password=password)

            messages.success(request, 'user registration successfully.')
            return redirect("account:signup")
    else:
        form = signupForm()
    return render(request, "signup.html", {'form': form})

@login_required(login_url="account:login")
def logout(request):
    auth.logout(request)
    return redirect("home")

@login_required(login_url="account:login")
def profile(request):
    return render(request,"profile.html",{})

@login_required(login_url="account:login")
def edit_profile(request):
    return render(request,"profile.html",{})

@login_required(login_url="account:login")
def change_password(request):
    return render(request,"profile.html",{})