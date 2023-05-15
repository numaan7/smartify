from django.urls import path
from . import views

urlpatterns = [
   path('',views.index),
   path('signup',views.signup),
   path('login',views.loginhandle),
    path('logout', views.handelLogout, name="handleLogout"),
       path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'), 
       path('<url:str>/')
]