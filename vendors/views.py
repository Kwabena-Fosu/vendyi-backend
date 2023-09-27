from rest_framework import generics, filters, pagination, mixins
from .serializers import VendorSerializer
from rest_framework.response import Response
from .models import Vendor

class VendorList(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['shop_name', 'description', 'location']
    ordering_fields = ['shop_name', 'location']
    pagination_class = pagination.PageNumberPagination

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)