from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from creativeproject.models import CategoryModel, ProductModel, CartModel
from .forms import SearchForm
from creativeproject.handler import bot


# def home_page(request):
#     categories = CategoryModel.objects.all()
#     products = ProductModel.objects.all()
#     form = SearchForm
#     context = {'categories': categories, 'products': products, 'form': form}
#     return render(request, template_name='index.html', context=context)

class HomePage(ListView):
    form = SearchForm
    template_name = 'index.html'
    model = ProductModel
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["products"] = ProductModel.objects.all()
        return context


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def search(request):
    if request.method == "POST":
        get_product = request.POST.get('search_product')
        try:
            exact_product = ProductModel.objects.get(pr_name__icontains=get_product)
            return redirect(f'/product/{exact_product.id}')
        except:
            return redirect('/')


def product_page(request, pk):
    product = ProductModel.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'products.html', context)


def category_page(request, pk):
    category = CategoryModel.objects.get(id=pk)
    current_products = ProductModel.objects.filter(product_category=category)
    context = {'product': current_products}
    return render(request, 'category.html', context)


def add_products_to_user_cart(request, pk):
    if request.method == 'POST':
        checker = ProductModel.objects.get(pk=pk)

        if checker.product_count >= int(request.POST.get('pr_count')):
            CartModel.objects.create(user_id=request.user.id,
                                     user_product=checker,
                                     user_product_quantity=int(request.POST.get('pr_count'))
                                     ).save()
            print('Success added to cart')
            return redirect('/user_cart')
        else:
            return redirect('/')


def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'New order\n'
        for i in cart:
            main_text += f'Product:{i.user_product}\n' \
                         f'Quantity: {i.user_product_quantity}' \
                         f'Buyer:{i.user_id}' \
                         f'Price of product: {i.user_product.product_price}'
            bot.send_message(-1002028813063, main_text)
            cart.delete()
            return redirect('/')
    else:
        return render(request, template_name='cart.html', context={'cart': cart})


def delete_user_cart(request, pk):
    product_delete = ProductModel.objects.get(pk=pk)

    CartModel.objects.filter(user_id=request.user.id,
                             user_product=product_delete
                             ).delete()
    return redirect('/user_cart')


def about(request):
    return render(request, 'about.html')


def products(request):
    products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context=context)


def singleproduct(request, pk):
    product = ProductModel.objects.filter(id=pk)
    context = {'product': product}
    return render(request, 'single-product.html', context)


def watch(request):
    watch_category = CategoryModel.objects.get(category_title='Watch')
    watch_products = ProductModel.objects.filter(product_category=watch_category)
    context = {'products': watch_products}
    return render(request, 'watch.html', context)


def necklaces(request):
    # Получаем объект категории "Necklaces"
    necklaces_category = CategoryModel.objects.get(category_title='Necklaces')

    # Фильтруем продукты по категории "Necklaces"
    necklaces_products = ProductModel.objects.filter(product_category=necklaces_category)

    # Передаем отфильтрованные продукты в контекст
    context = {'products': necklaces_products}

    return render(request, 'necklaces.html', context)


def earrings(request):
    earrings_category = CategoryModel.objects.get(category_title='Earrings')
    earrings_products = ProductModel.objects.filter(product_category=earrings_category)
    context = {'products': earrings_products}
    return render(request, 'earrings.html', context)


def rings(request):
    rings_category = CategoryModel.objects.get(category_title='Rings')
    rings_products = ProductModel.objects.filter(product_category=rings_category)
    context = {'products': rings_products}
    return render(request, 'rings.html', context)


def bracelets(request):
    bracelets_category = CategoryModel.objects.get(category_title='Braceletes')
    bracelets_products = ProductModel.objects.filter(product_category=bracelets_category)
    context = {'products': bracelets_products}
    return render(request, 'bracelets.html', context)






# def product_detail(request, product_id):
#     product = ProductModel.objects.filter_by(id=product_id)
#     context = {'product': product}
#     return render(request, 'single-product.html', context)
