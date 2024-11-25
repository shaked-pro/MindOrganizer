from django.shortcuts import render , redirect
from .forms import CreateUserForm , LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# home view for the home page
def home(request):
    return render(request, 'MindOrganizer/home.html')

# login view for the login page
def authLogin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request , data =request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, 'Welcome ' + username)
                login(request, user)
                return redirect('dashboard')
            else:
                print ('Invalid username or password')
                return render(request, 'MindOrganizer/login.html', {'login_form': form, 'error': 'Invalid username or password'})
            
    context = {'login_form':form}
    return render(request, 'MindOrganizer/login.html', context)

# register view for the register page
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
            form.save()
            return redirect('login')
    context = {'register_form':form}
    return render(request, 'MindOrganizer/register.html', context)

# dashboard view for the dashboard page
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'MindOrganizer/dashboard.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

