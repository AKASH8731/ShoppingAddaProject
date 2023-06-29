from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about_us/', views.about_us, name="about_us"),
    path('blog/', views.blog, name="blog"),
    path('blog_details/<slug:blog_details_slug>',
         views.blog_details, name="blog_details"),

    path("contact_us/", views.contact_us, name="contact_us"),

    path('product-listing/<slug:product_category_slug>',
         views.product_listing, name="product_listing"),

    path('product-details/<slug:product_slug>',
         views.ProductDetails.as_view(), name="ProductDetails")

]
