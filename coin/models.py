from django.db import models



class Coin(models.Model):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} ({self.symbol})"


