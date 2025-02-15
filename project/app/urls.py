from django.urls import path
from .views import *

urlpatterns = [
    path('', page, name="home"),  # Home page (root)
    path('base/', page, name="base"),  # Base page
    path('course/', Course, name="course"),  # Course books page
    path('general-books/', general, name="general_books"),  # General books page
    path('profile/', profile1, name="profile"),  # Profile page
    path('finished-books/', Finished_books, name="finished_books"),  # Finished books
    path('unfinished-books/', Unfinished_books, name="unfinished_books"),  # Unfinished books
    path('login/', login, name="login"),  # Login page
    path('register/', register, name="register"),  # Register page
]
