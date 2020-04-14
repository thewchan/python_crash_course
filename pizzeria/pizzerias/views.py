from django.shortcuts import render

from .models import Pizza


# Create your views here.
def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzerias/index.html')


def pizzas(request):
    """Show all pizzas."""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizzas.html', context)


def pizza(request, pizza_id):
    """Show a single pizza and all its toppings."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzerias/pizza.html', context)
