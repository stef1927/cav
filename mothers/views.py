from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.core.urlresolvers import reverse

from mothers.models import Children, Donations, Mothers, Operators

import forms


class ListMothersView(ListView):
    model = Mothers
    template_name = 'mothers-list.html'


class CreateMotherView(CreateView):
    model = Mothers
    template_name = 'mothers-detail.html'
    form_class = forms.MotherForm

    @staticmethod
    def get_success_url():
        return reverse('mothers-list')

    def get_context_data(self, **kwargs):
        context = super(CreateMotherView, self).get_context_data(**kwargs)
        context['action'] = reverse('mother-new')
        return context


class UpdateMotherView(UpdateView):
    model = Mothers
    template_name = 'mothers-detail.html'
    form_class = forms.MotherForm

    @staticmethod
    def get_success_url():
        return reverse('mothers-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateMotherView, self).get_context_data(**kwargs)
        context['action'] = reverse('mother-edit', kwargs={'pk': self.get_object().id})
        return context


class MotherDetailsView(UpdateView):
    model = Mothers
    template_name = 'mothers-detail.html'
    form_class = forms.MotherForm

    @staticmethod
    def get_success_url():
        return reverse('mothers-list')

    def get_context_data(self, **kwargs):
        context = super(MotherDetailsView, self).get_context_data(**kwargs)
        context['action'] = reverse('mother-view', kwargs={'pk': self.get_object().id})

        form = context['form']
        form.disabled = True

        return context


class ListChildrenView(ListView):
    model = Children
    template_name = 'children-list.html'


class ListDonationsView(ListView):
    model = Donations
    template_name = 'donations-list.html'


class ListOperatorsView(ListView):
    model = Operators
    template_name = 'operators-list.html'


