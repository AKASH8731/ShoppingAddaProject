from django.db import models


class WebsiteSetting(models.Model):
    """ websitesetting models class """
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    address = models.TextField()

    def __str__(self):
        """ Object websitesetting string representation """
        return self.title


class Slider(models.Model):
    """ Sldier models class """
    heading = models.CharField(max_length=50)
    sub_heading = models.CharField(max_length=50)
    image = models.ImageField(upload_to="slider")
    status = models.BooleanField(default=True)

    def __str__(self):
        """ Object slider string representation """
        return self.heading


class Blog(models.Model):
    """ blog model class """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    image = models.ImageField(upload_to="blog")
    status = models.BooleanField(default=True)

    def __str__(self):
        """ Object Blog string representation """
        return f"{self.title}{self.author}"


class FAQs(models.Model):
    """ FAQ model class """
    question = models.CharField(max_length=255)
    answer = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class About_Us(models.Model):
    """ About us Models """
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About_Us'
        verbose_name_plural = 'About_Us'


class ContactUs(models.Model):
    """Model for CustomerInquiry"""

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact_Us'
        verbose_name_plural = 'Contact_Us'
