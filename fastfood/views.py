from django.shortcuts import render
from .models import Dishes, Booking_food
from .forms import OrderingForms

# Create your views here.

def food(request):

    # dish3 = Dishes()
    # dish3.name = 'Rices'
    # dish3.desc = 'Fried Rice with chicken'
    # dish3.price = '500'
    # dish3.offer = False
    #
    # dish1 = Dishes()
    # dish1.name = 'Sugar'
    # dish1.desc = 'Fried Rice with chicken'
    # dish1.price = '200'
    # dish1.offer = True
    #
    # dish2 = Dishes()
    # dish2.name = 'Milk'
    # dish2.desc = 'Fried Rice with chicken'
    # dish2.price = '300'
    # dish2.offer = False

    dishes = Dishes.objects.all()
    return render(request, "dish.html", {'dishes': dishes})


def food_delivery_form(request):
    if request.POST:
        form = OrderingForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['fullname']
            address = form.cleaned_data['address']
            phone_no = form.cleaned_data['phoneno']
            print(name, address, phone_no)

    else:
        form = OrderingForms()
        dishName = Dishes.objects.values_list('id', 'name')

        form.dish_name = dishName[1][1]
        print(form.dish_name)

        return render(request, "food_delivery_form.html", {'form': form, 'dish_name': form.dish_name})


