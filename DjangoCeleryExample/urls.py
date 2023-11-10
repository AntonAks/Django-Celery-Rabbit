from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('button1/', views.view1, name='view1'),
    path('button2', views.view2, name='view2'),
]
