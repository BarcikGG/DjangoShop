from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, CategoryForm
from .models import Product, Category, Tag

def index(request):
    return render(request, 'index.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product

def catalog(request):
    all_products = Product.objects.all()

    items_per_page = 3

    paginator = Paginator(all_products, items_per_page)

    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'catalog.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()

    return render(request, 'addProduct.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'editProduct.html', {'product': product})

def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'viewProduct.html', {'product': product})

def contact(request):
    return render(request, 'contact.html')

# def api(request):
#     return render(request, 'api.html')
#
# def edit_APIproduct(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'apiEdit.html', {'product': product})
#
# def add_APIproduct(request, product_id):
#     return render(request, 'apiAdd.html', {'product_id': product_id})
#
# def delete_APIproduct(request, product_id):
#     return render(request, 'apiDelete.html', {'product_id': product_id})
#
# def view_APIproduct(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'apiView.html', {'product': product})

def account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')

def category_list(request):
    all_categories = Category.objects.all()

    items_per_page = 4

    paginator = Paginator(all_categories, items_per_page)

    page = request.GET.get('page')

    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    return render(request, 'category_list.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'add_category.html', {'form': form})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

def tag_list(request):
    all_tags = Tag.objects.all()

    items_per_page = 4

    paginator = Paginator(all_tags, items_per_page)

    page = request.GET.get('page')

    try:
        tags = paginator.page(page)
    except PageNotAnInteger:
        tags = paginator.page(1)
    except EmptyPage:
        tags = paginator.page(paginator.num_pages)

    return render(request, 'tag_list.html', {'tags': tags})

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = Product.objects.filter(tags=tag)
    return render(request, 'tag_detail.html', {'tag': tag, 'products': products})
