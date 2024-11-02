from django.urls import path

from order.views import OrderCreate


urlpatterns = [
    path("create/", OrderCreate.as_view())
]
