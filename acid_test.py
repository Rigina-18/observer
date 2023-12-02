# import os
# import django
# from django.db import transaction
#
#
# Указать путь к файлу settings.py в переменной окружения
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "observer.settings")
# django.setup()
#
#
# from blog.models import Review, Like
#
# review = Review.objects.create(topic_id=1, title='BMV',)
# like = Like.objects.create(user_id=1, review_id=3)