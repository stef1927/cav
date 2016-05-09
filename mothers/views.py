from django.views.generic import CreateView, DetailView, ListView, UpdateView, TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import force_text
from rest_framework import generics, permissions

from mothers.models import Children, Donations, Mothers, Operators
from mothers.serializers import ChildSerializer, DonationSerializer, \
    MotherSerializer, MotherDetailsSerializer, OperatorSerializer


class SafeMethodsOnlyPermission(permissions.BasePermission):
    """Only can access non-destructive methods (like GET and HEAD)"""
    def has_permission(self, request, view):
        return self.has_object_permission(request, view)

    def has_object_permission(self, request, view, obj=None):
        return request.method in permissions.SAFE_METHODS


class CanEditPermission(SafeMethodsOnlyPermission):
    def has_object_permission(self, request, view, obj=None):
        can_edit = True  # FIXME
        return can_edit or super(CanEditPermission, self).has_object_permission(request, view, obj)


class MotherMixin(object):
    model = Mothers
    queryset = Mothers.objects.all()
    serializer_class = MotherSerializer
    permission_classes = [
        CanEditPermission
    ]


class MothersList(MotherMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class MotherDetails(MotherMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MotherDetailsSerializer


class ChildMixin(object):
    model = Children
    queryset = Children.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [
        CanEditPermission
    ]


class ChildrenList(ChildMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class ChildDetails(ChildMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'


class DonationMixin(object):
    model = Donations
    queryset = Donations.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [
        CanEditPermission
    ]


class DonationsList(DonationMixin, generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]


class DonationDetails(DonationMixin, generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'


class OperatorsList(generics.ListCreateAPIView):
    model = Operators
    queryset = Operators.objects.all()
    serializer_class = OperatorSerializer

    permission_classes = [
        permissions.AllowAny
    ]