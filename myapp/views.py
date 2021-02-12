from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.forms import CreateUserForm
# Create your views here.
def home(request):
    return render(request,'tem/home.html')

def services(request):
    return render(request,'tem/services.html')

def about(request):
    return render(request,'tem/about.html')

def contact(request):
    return render(request,'tem/contact.html')

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request,'tem/login.html', context)

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'tem/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')