from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django.db.models import Q


from core.serializers import LeadSerializer, IndustrySerializer
from core.models import Lead, Industry


class LeadFilter(filters.FilterSet):
    is_favorite = filters.BooleanFilter(field_name="is_favorite")
    class Meta:
        model = Lead
        fields = ["is_favorite"]

class LeadViewSet(viewsets.ModelViewSet):
    model = Lead
    filterset_class = LeadFilter
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    ordering_fields = [
        "business__name",
        "business__description",
    ]

class IndustryViewSet(viewsets.ModelViewSet):
    model = Industry
    filterset_class = LeadFilter
    serializer_class = IndustrySerializer
    queryset = Industry.objects.all()
