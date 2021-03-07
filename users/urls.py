from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('editprofile/', views.edit_profile, name="edit_profile")
]
