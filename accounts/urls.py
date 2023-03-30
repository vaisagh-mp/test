from django.urls import path
from .import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("Login/",views.Login,name="Login"),
    path("Logout/",views.Logout,name="Logout"),
    path("change_password/",views.change_password,name="change_password"),

    path('activate/<uidb64>/<token>',views.activate,name="activate"),
]
