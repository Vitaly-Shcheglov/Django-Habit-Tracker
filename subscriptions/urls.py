from django.urls import path

from .views import SubscriptionViewSet

app_name = "subscriptions"

urlpatterns = [
    path("", SubscriptionViewSet.as_view({"get": "list", "post": "create"}), name="subscription-list"),
    path(
        "<int:pk>/", SubscriptionViewSet.as_view({"get": "retrieve", "delete": "destroy"}), name="subscription-detail"
    ),
]
