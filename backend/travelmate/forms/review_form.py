from django import forms
from backend.travelmate.models.review import Review


class ReviewForm(forms.ModelForm):
    """
    Form for adding and editing user reviews.
    """

    class Meta:
        model = Review
        fields = ['location', 'description', 'rating', 'photos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Write your review here...'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})
        self.fields['photos'].widget.attrs.update({'class': 'form-control-file'})
