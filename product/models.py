from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class ProductCategory(models.Model):
    """ Product category model class """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_categories')
    status = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=False)

    def __str__(self):
        """ Object product string representation """
        return self.name

    def save(self, *args, **kwargs):
        """ overriding method of supermodel """
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)


class ProductVariation(models.Model):
    """ Product variation models """
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ Object Product variation string representation"""
        return self.name


class ProductTag(models.Model):
    """ Product tag models """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ Object Product tag string representation"""
        return self.name

    def save(self, *args, **kwargs):
        """ overriding method of supermodel """
        self.slug = slugify(self.name)
        super(ProductTag, self).save(*args, **kwargs)


class Product(models.Model):
    """ Product models class """
    product_category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    cover_image = models.ImageField(upload_to="products")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    variation = models.ManyToManyField(ProductVariation)
    tags = models.ManyToManyField(ProductTag)
    status = models.BooleanField(default=True)

    def __str__(self):
        """ Object Product string representation """
        return self.name

    def save(self, *args, **kwargs):
        """ overriding method of supermodel """
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='ProductImage')
    image = models.ImageField(upload_to="products")

    def __str__(self):
        """ Object Product string representation """
        return str(self.id)
