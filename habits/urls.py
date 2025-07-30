from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HabitViewSet,
    UserHabitListView,
    PublicHabitListView,
    HabitCreateView,
    HabitUpdateView,
    HabitDeleteView,
)

app_name = "habits"

router = DefaultRouter()
router.register(r"habits", HabitViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("user/", UserHabitListView.as_view(), name="user-habits"),
    path("public/", PublicHabitListView.as_view(), name="public-habits"),
    path("create/", HabitCreateView.as_view(), name="create-habit"),
    path("<int:pk>/edit/", HabitUpdateView.as_view(), name="edit-habit"),
    path("<int:pk>/delete/", HabitDeleteView.as_view(), name="delete-habit"),
]
