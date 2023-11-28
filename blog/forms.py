from django import forms

from blog.models import Review


class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['body']
