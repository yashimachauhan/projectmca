from django.shortcuts import render,redirect
from userapp.models import UserInfo
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

def nutritionindex(request):

    try:
        auth=au.authriseuser(request.session["authenticated"],request.session["roleid"],2)
    except:
        return redirect("/notlogin/")
    if(auth):
        return render(request,'nutritionindex.html')
    else:
        aut,message=auth
        if(message=="Wrong User"):
            return redirect("/wrong user/")
        elif(message=="Not Login"):
            return redirect("/notlogin/")



def nutritionlogin(request):
    if (request.method == "POST"):
        uemail = request.POST["email"]
        upassword = request.POST["password"]
        #try:
        userdata = UserInfo.objects.get(user_email=uemail)
        dp = userdata.user_password
        if (dp == upassword):
                request.session['authenticated']=True
                request.session['roleid']=userdata.role_id_id
                request.session['useremail']=userdata.user_email
        return redirect("/nutrition/nutritionindex")
        #except:
        #    return render(request, "nutritionlogin.html")
    return render(request,"nutritionlogin.html")

def signup(request):
    return render(request,"signup.html")

