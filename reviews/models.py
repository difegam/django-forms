from django.db import models


# Create your models here.
class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __repr__(self) -> str:
        return f"Review(user_name='{self.user_name}', review_text='{self.review_text}', rating={self.rating})"

    def __str__(self) -> str:
        return f"{self.user_name} ({self.rating})"
