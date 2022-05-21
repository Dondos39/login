from django.urls import re_path
from myapp import views

app_name = 'myapp'

urlpatterns = [
re_path(r'^$',views.index,name='homepage'),
re_path('login/', views.user_login,name='login'),
re_path('logout/$', views.user_logout,name='logout'),
re_path('registration', views.register,name='registration'),
]
