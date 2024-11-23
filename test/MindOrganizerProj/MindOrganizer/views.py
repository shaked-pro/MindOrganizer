from django.shortcuts import render , redirect
from .forms import CreateUserForm

# home view for the home page
def home(request):
    return render(request, 'MindOrganizer/home.html')

# login view for the login page
def login(request):
    return render(request, 'MindOrganizer/login.html')

# register view for the register page
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'register_form':form}
    return render(request, 'MindOrganizer/register.html', context)

# dashboard view for the dashboard page
def dashboard(request):
    return render(request, 'MindOrganizer/dashboard.html')