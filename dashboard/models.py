from django.db import models
from accounts.models import Users


# Create your models here.
class Transactions(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="client")
    recipient_or_sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="recipient_or_sender")

    amount = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    transfer_type = models.CharField(max_length=255, choices=[('debit', ('debit')), ('credit', ('credit'))])
    date = models.DateField(auto_now_add=True)
