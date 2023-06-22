from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.

def first_page(request):
    object_list = Order.objects.all()
    object_form = OrderForm()
    return  render(request, './index.html', {
        'object_list': object_list,
        'form': object_form
        })


def thanks_page(request):
    # на странице будет приходить то что было отправлено с формы.
    # т.е. тут можно перехватить данные и отбработать
    #
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_prone=phone)
    element.save()
    return render(request, './thanks_page.html', {
        'name': name,
        'phone': phone
    }) 