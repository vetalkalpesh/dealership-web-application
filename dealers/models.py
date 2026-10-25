from django.conf import settings
from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=160)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=80)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=40, blank=True)
    website = models.URLField(blank=True)
    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, related_name="reviews", on_delete=models.CASCADE)
    name = models.CharField(max_length=120, default="Guest")
    review = models.TextField()
    sentiment = models.CharField(max_length=20, default="neutral")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"Review for {self.dealer.name} by {self.name}"
