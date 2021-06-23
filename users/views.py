from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
			print("username/email already taken")
			return redirect('signup')
		else:
			user = User.objects.create_user(username = username, email = email,password= password)
			user.save()
			return redirect('login')

	else:
		return render(request, 'signup.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username = username, password = password)

		if user is not None:
			auth.login(request, user)
			print("logged in ")
			return redirect('/')
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')