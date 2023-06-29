from django.db import models
from order.models import Order


class Payments(models.Model):
    """ payment models class """
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Inprogress', 'Inprogress'),
        ('Success', 'Success'),
        ('Failed', 'Failed')
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    transaction_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        """ object Payment string representation """
        return f"{self.transaction_id} {self.status}"
