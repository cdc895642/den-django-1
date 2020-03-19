from .models import Post
def price_list(request):
    #TODO смотрел урок,не понял
    price = Post.objects.filter(is_active=True)
    return {'price_list': price}