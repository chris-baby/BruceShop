# from django.contrib import admin
from django.urls import path,include
import xadmin

urlpatterns = [
       path('xadmin/', xadmin.site.urls),
]
