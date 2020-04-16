from django.urls import path
from . import views
from .forms import PhotoForm


urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.article_create, name="create"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

]