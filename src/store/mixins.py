from src.store.models import Category


class ContextDataMixin:
    def get_context_for_nav(self, *args, **kwargs):
        context = kwargs
        context['nav_panel_categories'] = Category.objects.filter(is_show_on_index=True)
        return context

