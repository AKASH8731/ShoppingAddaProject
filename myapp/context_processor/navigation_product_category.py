from product.models import ProductCategory


def navigation_product_category(request):
    """context processor for navigation categories dropdown in navbar"""
    navigation_Categories = ProductCategory.objects.filter(status=True)
    context = {
        'navigation_Categories': navigation_Categories
    }
    return (context)
