from django.urls import path
from .import views

urlpatterns = [
    path('loginUser/', views.loginUser, name = 'loginUser'),
    path('logoutUser/', views.logoutUser, name = 'logoutUser'),
    path('registerUser/', views.registerUser , name = 'registerUser'),
    path('', views.main, name='main'),
    path('bov', views.bov, name='bov'),
    path('leo', views.leo, name='leo'),
    path('lin', views.lin, name='lin'),
    path('mic', views.mic, name='mic'),
    path('tob', views.tob, name='tob'),
    
    
]
