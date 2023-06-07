from . import views
from django.urls import path

urlpatterns = [
    path('login',views.login,name='login'),
    path('',views.home,name='home'),
    path('home2',views.home2,name='home2'),
    path('signup',views.signup,name='signup'),
    path('stock',views.stock,name='stock'),
    path('stock2',views.stock2,name='stock2'),
    path('exchange',views.exchange,name='exchange'),
    path('exchange2',views.exchange2,name='exchange2'),
    path('blog',views.blog,name='blog'),
    path('blog2',views.blog2,name='blog2'),
   


]