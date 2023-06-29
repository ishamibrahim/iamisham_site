from django.urls import path, include
from rest_framework import routers

from auth.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)


urlpatterns = [
     path('users', include(router.urls)),
     path('users/login', UserViewSet.as_view({'post': 'login_user'}), name='login'),
     path('users/logout', UserViewSet.as_view({'post': 'logout_user'}), name='logout')
]
