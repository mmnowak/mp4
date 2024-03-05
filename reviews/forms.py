from django import forms
from .models import Review

RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class ReviewForm(forms.ModelForm):
    """Form for Review Model"""

    class Meta:
        model = Review
        fields = (
            "title",
            "content",
            "rating",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "title": "Review Title",
            "content": "Write your review here",
        }

        self.fields["title"].widget.attrs["autofocus"] = True
        self.fields["title"].widget.attrs["aria-label"] = "Review Title"
        self.fields["content"].widget.attrs["aria-label"] = (
            "Write your review here")
        self.fields["rating"] = forms.ChoiceField(
            label="Your rating", widget=forms.RadioSelect,
            choices=RATING_CHOICES
        )
        self.fields["rating"].widget.attrs[
            "aria-label"
        ] = "Rating: Choose a value between 1-5"
