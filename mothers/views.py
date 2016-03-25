from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse

from mothers.models import Children, Donations, Mothers


class ListMothersView(ListView):
    model = Mothers
    template_name = 'mothers-list.html'


class CreateMotherView(CreateView):
    model = Mothers
    fields = '__all__'
    template_name = 'edit-mothers.html'

    def get_success_url(self):
        return reverse('mothers-list')

    # class Meta:
    #     model = Author
    #     fields = '__all__'


class ListChildrenView(ListView):
    model = Children


class ListDonationsView(ListView):
    model = Donations



