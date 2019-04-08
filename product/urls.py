from django.conf.urls import url
from product import views



app_name="product"

urlpatterns=[

    url(r'^productindex',views.productindex,name="productindex"),
]
