from django.shortcuts import render

def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        order_date = Product.objects.all()
    else:
        data = Product.objects.filter(amount__gt=1)
        order_date = data.order_by('category', 'name')
    return render(request, 'index.html', context={
        'products': order_date,
        'category': CATEGORY_CHOICE
    })
