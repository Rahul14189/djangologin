from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('aboutus', views.aboutus, name = 'aboutus'),
    # path('sign_up', views.sign_up, name = 'sign_up'),
    # path('logout', views.logout, name = 'logout'),
    # path('profile', views.profile, name = 'profile'),
]