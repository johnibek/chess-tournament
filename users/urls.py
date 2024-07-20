from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", views.UserListAPIView.as_view(), name='users'),
    path("<int:id>/", views.UserRetrieveUpdateDeleteAPIView.as_view(), name='user_detail'),
    path("register/", views.RegisterAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]