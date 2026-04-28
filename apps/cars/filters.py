from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'brand',
            'year'
        )
    )
