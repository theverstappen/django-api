from django.urls import path
from .views import AllProjectsView, ProjectDetail
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('projects/', AllProjectsView.as_view(), name="projects-all"),
    path('projects/<int:pk>', ProjectDetail.as_view(), name="project-detail")
]