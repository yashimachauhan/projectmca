from django.conf.urls import url
from userapp import views

app_name="nutritionapp"

urlpatterns=[

    url(r'^nutritionlogin',views.nutritionlogin,name="nutritionlogin"),
    url(r'^nutritionindex',views.nutritionindex,name="nutritionindex"),
    url(r'^logout',views.logout,name="logout"),
]
