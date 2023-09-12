from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_email, name="list_email"),
    path("create/", views.create_email, name="create_email"),
    path("inQ/", views.in_progress, name="in_progress"),
    path("email/<int:id>/", views.get_email, name="get_email"),
]
