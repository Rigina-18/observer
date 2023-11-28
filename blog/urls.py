from django.urls import path

from blog.views import edit_review, review_detail, add_like

urlpatterns = [
    path('review/<int:id>/', review_detail, name='review_detail'),
    path('add_like/', add_like, name='add_like'),
    path('edit/<int:review_id>/', edit_review, name='edit_review')
]