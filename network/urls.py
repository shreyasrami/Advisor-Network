from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import AdvisorView, RegisterUserView, LoginUserView, AllBookingsView, MakeBookingView


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v3",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('',schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui",),
    path('user/register/', RegisterUserView.as_view(),name='register_user'),
    path('user/login/', LoginUserView.as_view(), name='token_obtain_pair'),
    path('admin/advisor/', AdvisorView.as_view(),name='add_advisor'),
    path('user/<user_id>/advisor/', AdvisorView.as_view(),name='view_advisors'),
    path('user/<user_id>/advisor/booking/', AllBookingsView.as_view(),name='view_bookings'),
    path('user/<user_id>/advisor/<advisor_id>/', MakeBookingView.as_view(),name='view_advisors'),


    
]
