from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["user_name", "review_text", "rating"]  #* "__all__" or exclude = ["user_name",...]
        labels = {"user_name": "Your name", "review_text": "Your Feedback", "rating": "Your Rating"}
        error_messages = {
            "user_name": {
                "required": "username must not be empty",
                "max_length": "Please enter a shorter username"
            }
        }
