from . import views
from . views import register
from django.urls import path

urlpatterns = [
    path('register',views.register,name="register"),
]
