from django.urls import path
from . import views  

urlpatterns = [
    path('', views.login_view, name='login'),  # URL for the login view
    path('question_list/', views.success_view, name='question_list'),  # URL for the success view
    path('admin_login',views.admin_login,name="admin_login"),

]

