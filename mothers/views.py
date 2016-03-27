from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse

from mothers.models import Children, Donations, Mothers


class ListMothersView(ListView):
    model = Mothers
    template_name = 'mothers-list.html'


class CreateMotherView(CreateView):
    model = Mothers
    fields = '__all__'
    template_name = 'edit-mothers.html'

    @staticmethod
    def get_success_url():
        return reverse('mothers-list')

    def get_context_data(self, **kwargs):

        context = super(CreateMotherView, self).get_context_data(**kwargs)
        context['action'] = reverse('mother-new')

        return context


class UpdateMotherView(UpdateView):
    model = Mothers
    fields = '__all__'
    template_name = 'edit-mothers.html'

    @staticmethod
    def get_success_url():
        return reverse('mothers-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateMotherView, self).get_context_data(**kwargs)
        context['action'] = reverse('mother-edit',
                                    kwargs={'pk': self.get_object().id})

        return context


class MotherDetailView(DetailView):
    model = Mothers
    template_name = 'mother.html'
    context_object_name = 'mother'

    # def get_context_data(self, **kwargs):
    #     context = super(MotherDetailView, self).get_context_data(**kwargs)
    #     return context


class ListChildrenView(ListView):
    model = Children


class ListDonationsView(ListView):
    model = Donations



