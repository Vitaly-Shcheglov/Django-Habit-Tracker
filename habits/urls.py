from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (HabitCreateView, HabitDeleteView, HabitUpdateView,
                    HabitViewSet, PublicHabitListView, UserHabitListView)

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
