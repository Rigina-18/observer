from rest_framework import serializers

from blog.models import Review, Topic, Like


class TopicSerializers(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = [
            'name',
            'id'
        ]


class ReviewSerializers(serializers.ModelSerializer):
    topic = TopicSerializers()
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [
            'id',
            'topic',
            'title',
            'cover',
            'body',
            'date_create',
            'date_update',
            'date_schedule',
            'to_publish',
            'like_count',
            'file',

        ]

    @staticmethod
    def get_like_count(obj):
        return obj.like_set.all().count()


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'user',
            'review',
        ]
