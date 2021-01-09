from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import AddItemForm
from.models import ListItem, Shop

class ShoppingList(CreateView):
    template = 'shopping_list.html'

    def get(self, request):
        shops = Shop.objects.filter()
        data = {}
        summary = 0
        for shop in shops:
            list_of_products = ListItem.objects.filter(shop=shop)
            if list_of_products:
                total_value = 0
                for product in list_of_products:
                    total_value += round(product.amount * product.price, 2)

                data[shop.name] = {'total_value':total_value, 'list_of_products':list_of_products}
                summary += total_value

        return render(request, self.template, {'data': data, 'summary': summary})

    def post(self, request):

        try:
            bought_list = dict(self.request.POST)['action']
        except:
            bought_list = []

        list_of_products = ListItem.objects.filter()
        for item in list_of_products:
            status = str(item.id) in bought_list
            if item.bought != status:
                item.bought = status
                item.save()

        return redirect('shopping_list')


class AddItem(CreateView):
    template = 'add_item.html'
    form = AddItemForm()
    def get(self, request):
        return render(request, self.template, {'form': self.form})

    def post(self, request):
        form = AddItemForm(data=self.request.POST)
        if form.is_valid():
            messages.success(self.request, 'Produkt dodany')
            form.save()
        return render(request, self.template, {'form': self.form})
