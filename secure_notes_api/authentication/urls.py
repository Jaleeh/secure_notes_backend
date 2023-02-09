
from django.urls import path
from .views import RegisterAPIView,LoginAPView,UserListAPIView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
     TokenVerifyView
)


urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/',LoginAPView.as_view(),name = 'login'),
    path('userlist/',UserListAPIView.as_view(), name = 'list')
   


]
