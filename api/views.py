from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from api.serializers import ReviewSerializers, TopicSerializers, LikeSerializers
from blog.models import Review, Topic, Like
from rest_framework.permissions import IsAuthenticated


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializers
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class TopicViewSet(ModelViewSet):
    serializer_class = TopicSerializers
    queryset = Topic.objects.all()


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializers
    queryset = Like.objects.all()
