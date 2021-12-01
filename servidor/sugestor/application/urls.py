
from django.urls import path
from . import views 

urlpatterns = [
    path('<str:index_da_sugestao>', views.home, name='home'),
    #path('sub',views.subtraction, name='sub'),
    #path('multi',views.multiplication, name='multi'),
    #path('div',views.division, name='div')
    path('login/', views.login, name='login'),
    path('', views.nav, name='nav'),
    path('perfil/', views.perfil, name='perfil')
]
