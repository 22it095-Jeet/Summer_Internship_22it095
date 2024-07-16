from django.urls import path,include
from .views import first,table,cattable,form,catform,update,index,allproduct,register,login,logout

urlpatterns = [
     path('first/',first,name='first'),
     path('table/',table,name='table'),
     path('cattable/',cattable,name='cattable'),
     path('form/',form,name='form'),
     path('catform/',catform,name='catform'),
     path('update/',update,name='update'),
     path('',index,name='index'),
     path('allproduct/',allproduct,name='allproduct'),
     path('register/',register,name='register'),
     path('login/',login,name='login'),
     path('logout/',logout,name='logout')
    
]