from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/base.html'
    links = {
        'login': '#',
        'logout': '#',
        'register': '#',
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links'] = self.links
        return context
