from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductVariation


class Cart(models.Model):
    """ cart models class """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)

    def __str__(self):
        """ object cart string representation """
        return f"{self.product}"
