from django.shortcuts import render,redirect
from userapp.models import UserInfo, SignUpUser
from userapp.forms import SignUpForm
from miscellaneous.otp import otpgenerate
from miscellaneous.mail import emailsend
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

def about(request):
    return render(request,"about.html")

def signup(request):
    if (request.method=="POST"):
        form=SignUpUser(request.POST)
        f=form.save(commit=False)
        f.first_name=request.POST["first_name"]
        f.last_name=request.POST["last_name"]
        f.email=request.POST["email"]
        f.confirm_password=request.POST["confirm_password"]
        f.save()
        return render(request,"signup.html",{'inserted':True})
    return render(request,"signup.html")

def afterlog(request):
    return render(request,"afterlog.html")

def video(request):
    return render(request,"video.html")



def forgot(request):
    getemail=request.session["useremail"]
    if request.method=="POST":
        pass
    else:
        otp,time=otpgenerate()
        emailsend(otp, getemail)
        update=UserInfo(user_email=getemail,otp=otp,otp_time=time)
        update.save(update_fields=['otp','otp_time'])
    return render(request,"forgot.html")