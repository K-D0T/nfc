from django.urls import path
from . import views

urlpatterns = [
    path('ajskdlfjkajfkldsjfajsflkasjflkdsjfadjfklasjf;asd;fkldsjafkasdfsadlkfjasdfl;ksdjfaklf', views.home, name="home"),
    path('signup/', views.SignUp, name="SignUp"),
    path('SignUp_save/', views.SignUp_save, name='SignUp_save'),
    path('login/', views.login, name='login'),

]