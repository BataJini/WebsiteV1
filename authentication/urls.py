from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.home, name='home'),  # Ensure 'home' view exists
    path('jobs/', views.jobs, name='jobs'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),

]
