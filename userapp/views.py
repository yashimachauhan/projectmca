from django.shortcuts import render,redirect
from userapp.models import UserInfo, SignUpUser
from userapp.forms import SignUpForm
import authorize as au

# Create your views here.
def notlogin(request):
    return render(request,'notlogin.html')

def wronguser(request):
    return render(request,'wronguser.html')

def basemaster(request):
    return render(request, "basemaster.html")

def logout(request):
    request.session['authenticated']=False
    return redirect("/")


def signup(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        f=form.save(commit=False)
        f.first_name=request.POST["first_name"]
        f.last_name=request.POST["last_name"]
        f.email=request.POST["email"]

        f.confirm_password=request.POST["confirm_password"]
        f.save()
        return render(request,"signup.html",{'registered':True})
    return render(request,"signup.html")

