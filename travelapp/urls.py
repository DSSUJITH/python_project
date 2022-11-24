from . import views
from django.urls import path

urlpatterns = [
    path('demo',views.demo,name='demo'),
    path('register',views.register,name="register"),
    path('',views.login,name="login"),
    path('logout',views.logout,name="logout"),
]
