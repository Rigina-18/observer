from django.urls import path, include
from rest_framework import routers

from api.views import ReviewViewSet, TopicViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register('review', ReviewViewSet)
router.register('topic', TopicViewSet)
router.register('like', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]