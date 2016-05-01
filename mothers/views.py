from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import force_text
from rest_framework import generics, permissions

from mothers.models import Children, Donations, Mothers, Operators
from mothers.serializers import ChildSerializer, DonationSerializer, MotherSerializer, OperatorSerializer


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class MotherCanEditPermission(SafeMethodsOnlyPermission):
    def has_object_permission(self, request, view, obj=None):
        can_edit = True  # FIXME
        return can_edit or super(MotherCanEditPermission, self).has_object_permission(request, view, obj)


class MothersListView(TemplateView):
    template_name = "mothers-list.html"


class MotherDetailsView(TemplateView):
    template_name = "mother-details.html"


class MotherMixin(object):
    model = Mothers
    queryset = Mothers.objects.all()
    serializer_class = MotherSerializer
    permission_classes = [
        MotherCanEditPermission
    ]

    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)


class MothersList(MotherMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class MotherDetails(MotherMixin, generics.RetrieveAPIView):
    lookup_field = 'id'


class ChildrenListView(ListView):
    model = Children
    template_name = 'children-list.html'


class ChildrenList(generics.ListCreateAPIView):
    model = Children
    queryset = Children.objects.all()
    serializer_class = ChildSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class DonationsListView(ListView):
    model = Donations
    template_name = 'donations-list.html'


class DonationsList(generics.ListCreateAPIView):
    model = Donations
    queryset = Donations.objects.all()
    serializer_class = DonationSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class OperatorsListView(ListView):
    model = Operators
    template_name = 'operators-list.html'


class OperatorsList(generics.ListCreateAPIView):
    model = Operators
    queryset = Operators.objects.all()
    serializer_class = OperatorSerializer

    permission_classes = [
        permissions.AllowAny
    ]