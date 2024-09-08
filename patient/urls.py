from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewset,RegistrationApiView, activate, UserLoginView, UserLogoutView

router= DefaultRouter()

router.register('list', PatientViewset)
urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', activate, name='activate'),
]
