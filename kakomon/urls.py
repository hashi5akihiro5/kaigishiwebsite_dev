from django.urls import path

from . import views

app_name = "kakomon"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "<exam_type>/<navigation_or_engineering>/<grade>/",
        views.ExamListView.as_view(),
        name="list_exam",
    ),
]
