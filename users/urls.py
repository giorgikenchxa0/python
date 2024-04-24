from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from users.views import UserCreateView , profileview


urlpatterns = [
    path(
        'sign-in/',
        LoginView.as_view(
            template_name ='user/sign_in.html',
            redirect_authenticated_user = True
            
        ),
        name='sign_in'
        
    ),

    path(
        'sign-out/',
        LogoutView.as_view(),
        name= 'sign_out'
    ),

    path('sign-up/', UserCreateView.as_view(), name='sign_up'),
    path('profile/<int:pk>/', profileview.as_view(), name= 'user_profile'),

    
]
