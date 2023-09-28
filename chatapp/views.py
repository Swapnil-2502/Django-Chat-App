from django.shortcuts import render,HttpResponse,redirect
from chatapp.models import AppUsers
# Create your views here.
def home(request):
    return HttpResponse("This is home Page")

def register(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        registration = AppUsers(username=username,password=password)
        registration.save()
        # return redirect("register")
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')
    # return HttpResponse("This is login Page")