from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductVariation


class Order(models.Model):
    """ order model class """
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Inprogress', 'Inprogress'),
        ('Dipatch', 'Dipatch'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    address = models.TextField()
    mobile = models.CharField(max_length=12)
    payment = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        """ Object order string representation """
        return str(self.id)


class OrderDetails(models.Model):
    """ orderdetails models class """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    variation = models.ForeignKey(
        ProductVariation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """ Object orderdetails string representation """
        return f"{self.order.id} {self.product}"
