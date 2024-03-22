from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
# import 
from product.models import Product
# def home(request):
#     template_name = 'home.html'
#     return render(request, template_name)
#     # return HttpResponse('Hello world')

class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        # print('===========>', products)
        context['products'] = list(products)
        return context