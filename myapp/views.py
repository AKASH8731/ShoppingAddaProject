from django.shortcuts import render, redirect
from cms.models import Slider
from product.models import (ProductCategory, Product, ProductTag)
from cms.models import (WebsiteSetting, About_Us, Blog, ContactUs)
from django.views import View

# Create your views here.

# ! HomePage---


def home_page(request):
    """ home page of k-mart """

    sliders = Slider.objects.filter(status=True)
    product_categories = ProductCategory.objects.filter(
        status=True, show_on_homepage=True)
    fashion_products_one = Product.objects.filter(status=True)[0:2]
    fashion_products_two = Product.objects.filter(status=True)[2:4]
    product_tags = ProductTag.objects.filter(status=True)[0:2]
    blogs = Blog.objects.filter(status=True)[4:7]

    # if request.GET.get('search'):
    #     print(request.GET.get('search'))

    context = {
        'sliders': sliders,
        'product_categories': product_categories,
        'fashion_products_one': fashion_products_one,
        'fashion_products_two': fashion_products_two,
        'product_tags': product_tags,
        'blogs': blogs,
    }

    return render(request, 'home.html', context)

# ! Product-listing---


def product_listing(request, product_category_slug):
    """ Product listing of K-Mart"""

    products = Product.objects.filter(
        status=True, product_category__slug=product_category_slug)

    context = {

        'products': products
    }

    return render(request, 'product/product_listing.html', context)


# ! Product-Details --(view Class based)

class ProductDetails(View):

    def get(self, request, product_slug):

        try:
            product = Product.objects.get(slug=product_slug)
            similar_products = Product.objects.filter(
                status=True, product_category=product.product_category).exclude(id=product.id)
            context = {

                'product': product,
                'similar_products': similar_products,
            }
            return render(request, 'product/product_details.html', context)
        except Product.DoesNotExist:
            pass

# ! About us Page


def about_us(request):
    team = About_Us.objects.filter()
    product_tags = ProductTag.objects.filter(status=True)[0:2]
    context = {
        'team': team,
        'product_tags': product_tags,
    }
    return render(request, "about_us.html", context)


# !Blog Page----


def blog(request):

    blog = Blog.objects.filter(status=True)

    context = {
        'blog': blog
    }

    return render(request, "blog.html", context)

# ! Blog Details---


def blog_details(request, blog_details_slug):
    blog = Blog.objects.get(status=True, slug=blog_details_slug)
    recent_blogs = Blog.objects.filter(status=True).exclude(id=blog.id)
    popular_blogs = Blog.objects.filter(status=True).exclude(id=blog.id)

    context = {
        "blog": blog,
        "recent_blogs": recent_blogs,
        "popular_blogs": popular_blogs,
    }

    return render(request, "blog_details.html", context)

# !Contact Us Page---


def contact_us(request):
    """contact us function"""
    address = WebsiteSetting.objects.all()
    context = {"address": address}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, email, phone, message)
        enquiry = ContactUs.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        enquiry.save()
        return redirect("home_page")
    return render(request, "contact/contact_us.html", context)
