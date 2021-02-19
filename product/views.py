from django.http import Http404
from django.shortcuts import render, get_object_or_404


from .models import Category, Product


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'product/index.html', {'categories': categories})

# def products_list(request, category_slug):
#     products = get_list_or_404(Product, category_id=category_slug)
#     return render(request, 'product/products_list.html', {'products':products})
#
def products_list(request, category_slug):
    if not Category.objects.filter(slug=category_slug).exists():
        raise Http404('Нет такой категории')
    products = Product.objects.filter(category_id=category_slug)
    return render(request, 'product/products_list.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})







# TODO: сделать перход из категории в листинг продуктов
# TODO: Добавить детали продукта
# TODO: переписать вьюшки на CBV (Class-Based Views)




# def products_list_2(request):
#     category_slug = request.GET.get('category')
#     products = Product.objects.all()
#     if category_slug is not None:
#         products = products.filter(category_id=category_slug)
#

# all() - выводит все обьекты модели
# select * from table;

# Category.objets.filter(...).all()

# filter() - фильтрует результаты запросы queryseta
# select * FROM table where ...;

# exclude(category_id=1) - исключает из результатов обьект = условию
# select * from table where  category != 1;

# exclude(title__startwith='Apple')
# select * from product where title not like 'Apple%';

# order_by() - сортировка результатов запроса
# Product.objects.order_by('price');
# select * from product order by price ASC;

# Product.objects.order_by("-price")
# select * from product order by price DESC;

# Product.objects.order_by('price','popularity')
# select * from product order by price ASC, popularity ASC;

# Product.objects.order_by('?') - рандомная сортировка

# Product.objects.all() ->
# <Queryset: ["Мясо", "Картошка","Молоко"]

# distinct() = исключает повторение
# Product.objects.values_list('category',flat=True).distinct()

# values()
# Product.object.all() ->
# <QuerySet: [obj1.obj2,object3]>

# values_list() - обькты представляет в виде кортежей
# Product.objects.values_list() ->
# <QuerySet: [(1,'milk','jogurt',)]>

# Product.objects.values.list('id','title') ->
# <QuerySet:

# none() - пустой queryset

# Product.objects.none() ->
# <QuerySet:[]>

# select_related()
# prod = Product.object.get(id=1)
# prod.category
#
# prod = Product.objects.select_related('category').get(id=1)
# prod.category - запроса нет

# prefetch_related()

# defer()

# id,title,description, price, category_id
# Product.objects.all() ->
# Select * from product:

# Product.objects.defer('price', 'category_id')- >
# select id, title, description from product

# only()

# Product.objects.only('price', 'category_id') ->
# select price, category_id from product;

# first(),last()
# Product.object.order_by('price').first() - первое значение

# earliest, latest()
# Product.objects.earliest('price') - Первое значение по цене

# exists() - Проверяет ,есть ли в квуерисет хоть один результат

# delete() - удаляет результаты квуерисета
# explain() - возвращает SQL запрос queryset