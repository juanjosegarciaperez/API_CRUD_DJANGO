from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()

router.register('programmers', views.ProgrammerViewSet)
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]