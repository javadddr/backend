
from django.conf.urls import url
from django.contrib import admin
from customers import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/customers/',views.customers, name='customers')
]
