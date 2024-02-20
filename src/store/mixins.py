from src.store.models import Category


class DataMixin:
    def get_context_data(self, *args, **kwargs):
        context = kwargs
        context['categories'] = Category.objects.all()
        return context

