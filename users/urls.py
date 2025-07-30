from django.urls import path
from .views import UserListCreateView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView

app_name = "users"

urlpatterns = [
    path("api/users/", UserListCreateView.as_view(), name="user-list-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("api/token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
