from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.indexfunction, name="index"),
    path('checkadmin/',views.checkadmin,name="checkadmin"),
    path('adminhome/',views.adminhome,name="adminhome"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('checkuser/',views.checkuser,name="checkuser"),
    path('userreg/', views.userreg, name="userreg"),
    path('userhome/', views.userhome, name="userhome"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('viewcategory/',views.viewcategory,name="viewcategory"),
    path('addmovie/',views.addmovie,name="addmovie"),
    path('viewmovies/',views.viewmovies,name="viewmovies"),
    path('search/',views.search,name="search"),
    path('userlog/',views.userlog,name="userlog"),
    path('analysis/',views.analysis,name="analysis"),
    path('recommendations/',views.recommendations,name="recommendations"),
    path('viewdetails/<int:id>',views.viewdetails,name="viewdetails"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('userlogout/',views.userlogout,name="userlogout"),




]