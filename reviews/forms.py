import datetime

from django import forms

email_setup = {
    "label": "email",
    "max_length": 100,
    "error_messages": {
        "required": "email must not be empty",
        "max_length": "Please enter a valid email"
    }
}


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Username",
                                max_length=100,
                                error_messages={
                                    "required": "username must not be empty",
                                    "max_length": "Please enter a shorter username"
                                },
                                widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(**email_setup)
    day = forms.DateField(initial=datetime.date.today)
