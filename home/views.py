from django.views.generic import ListView
# import 
from product.models import Product

class HomePageView(ListView):
    template_name = "home.html"
    model = Product
    context_object_name = "products"
    paginate_by = 12

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "product-list.html"
        else:
            return self.template_name
