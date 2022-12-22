from django.views.generic import TemplateView, ListView

from .models import Product, WorkSchedule


class IndexTemplateView(TemplateView):
    template_name = 'main/index.html'


class ProductListView(ListView):
    template_name = 'main/products.html'
    context_object_name = 'products'
    model = Product

    def get_queryset(self):
        from itertools import zip_longest
        objs = Product.objects.filter(is_published=True)
        objs = iter(objs)
        return list(zip_longest(objs, objs))


class WorkScheduleListView(ListView):
    template_name = 'main/store.html'
    context_object_name = 'week'
    model = WorkSchedule
