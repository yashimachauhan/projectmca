from django.conf.urls import url
from nutritionapp import views
#from userapp import views

app_name="nutritionapp"

urlpatterns=[

    url(r'^nutritionlogin',views.nutritionlogin,name="nutritionlogin"),
    url(r'^nutritionindex',views.nutritionindex,name="nutritionindex"),
    url(r'dietplan',views.dietplan,name="dietplan"),
    url(r'weightloss',views.weightloss,name="weightloss"),

]
