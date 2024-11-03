from django.urls import path, include
from .views import CandidateViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('candidates', CandidateViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
