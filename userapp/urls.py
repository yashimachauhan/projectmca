from django.conf.urls import url
from userapp import views

app_name="userapp"

urlpatterns=[

    url(r'^signup',views.signup,name="signup"),
    url(r'^forgot',views.forgot,name="forgot"),

]
