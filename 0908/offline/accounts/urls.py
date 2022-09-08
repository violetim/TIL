from django.urls import path
from . import views


app_name = 'accounts'
#어느 앱에서 관리하는지 경로를 보여주기 위해

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
