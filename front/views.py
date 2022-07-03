from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from sportshub.views import front


# Create your views here.
def frontpage(request):

    return render(request,'front.html')

def login(request):
    if request.method == 'POST':
         username=request.POST['username']
         password=request.POST['password']

         user=auth.authenticate(username=username,password=password)

         if user is not None:
            auth.login(request,user)
            return redirect(front)
         else:
            messages.info(request,"invalid username password")
            return redirect('login')

    else:
        return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        conform_password=request.POST['conform_password']

        if password==conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                  user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                  user.save();
                  print('user created')
                  return redirect('login')


        else:
           messages.info(request,'password not matching..')
           return redirect('register')
        return redirect('/')

    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect("/")