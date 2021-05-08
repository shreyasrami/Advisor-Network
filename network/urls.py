from django.urls import path
from .views import AdvisorView, RegisterUserView, LoginUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('user/register/', RegisterUserView.as_view(),name='register_user'),
    path('user/login/', LoginUserView.as_view(), name='token_obtain_pair'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/advisor/', AdvisorView.as_view(),name='add_advisor'),
    path('user/<user_id>/advisor/', AdvisorView.as_view(),name='view_advisors'),

    
]
