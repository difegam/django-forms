from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Username",
#                                 max_length=100,
#                                 error_messages={
#                                     "required": "username must not be empty",
#                                     "max_length": "Please enter a shorter username"
#                                 },
#                                 widget=forms.TextInput(attrs={"placeholder": "Username"}))
#     review_text = forms.CharField(label="review",
#                                   max_length=200,
#                                   widget=forms.Textarea(attrs={"placeholder": "Type your message here"}))
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["user_name" , "review_text", "rating"] #* "__all__" or exclude = ["user_name",...]
        labels = {"user_name": "Your name", "review_text": "Your Feedback", "rating": "Your Rating"}
        error_messages = {
            "user_name": {
                "required": "username must not be empty",
                "max_length": "Please enter a shorter username"
            },
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
