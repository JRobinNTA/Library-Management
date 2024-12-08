from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserViewSet
from books.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User registration endpoint
    path('api/register/', UserViewSet.as_view({'post': 'register'}), name='user_register'),
    
    # Include router URLs
    path('api/', include(router.urls)),
]