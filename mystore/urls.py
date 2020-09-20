from django.contrib import admin
from django.urls import path
from mystore import views
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = "mystore"

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^shop/$',views.shop,name='shop'),
]