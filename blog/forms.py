from django import forms

from blog.models import Review
from django_summernote.widgets import SummernoteWidget

class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields =['body']
        widgets = {'body': SummernoteWidget()}
