from django.urls import path,include
from .views import UserProfileView

urlpatterns = [
	path('profile/',UserProfileView.as_view()),
	
]