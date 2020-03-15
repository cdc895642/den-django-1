from .models import Post
def price_list(request):
    '''Прайс лист'''
    price = Post.objects.filter(is_active=True)
    return {'price_list': price}