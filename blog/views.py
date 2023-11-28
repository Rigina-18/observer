from django.shortcuts import render, redirect

from blog.forms import ReviewEditForm
from blog.models import Review, Like
from django.http import JsonResponse


def review_detail(request, id):
    review = Review.objects.get(id=id)
    user = request.user
    like_count = review.like_set.count()
    self_like = Like.objects.filter(user_id=user.id, review_id=id).exists()
    if self_like:
        label = 'unlike'
    else:
        label = 'like'

    return render(request, 'blog/review_detail.html',
                  {'review': review, 'user': user, 'like_count': like_count, 'label': label})


def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewEditForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            previous_page = request.session.get('previous_page')
            if previous_page:
                return redirect(previous_page)
            else:
                return redirect('index')
    else:
        form = ReviewEditForm(instance=review)
        request.session['previous_page'] = request.META.get('HTTP_REFERER')

    return render(request, 'blog/edit_review.html', {'form': form})


def add_like(request):
    referer = request.META.get('HTTP_REFERER')
    review_id = request.POST.get('review')
    user_id = request.POST.get('user')
    self_like = Like.objects.filter(user_id=user_id, review_id=review_id).exists()
    review = Review.objects.get(id=review_id)
    if self_like:
        # удаление лайка
        self_like = Like.objects.filter(user_id=user_id, review_id=review_id)
        self_like.delete()
        label = 'like'
    else:
        like = Like(user_id=user_id, review_id=review_id)
        like.save()
        label = 'unlike'

    like_count = review.like_set.count()
    # return redirect(referer)
    return JsonResponse({'like_count': like_count, 'label': label})