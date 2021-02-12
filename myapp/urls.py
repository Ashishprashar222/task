
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('login/', views.loginPage,name="login"),
    path('register/', views.registerPage,name="register"),
    path('logout/', views.logoutUser,name="logout"),
]
