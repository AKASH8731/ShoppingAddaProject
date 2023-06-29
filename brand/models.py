from django.db import models


class Brand(models.Model):
    """ Brand models class  """
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ Object brand string representation """
        return (self.name)
