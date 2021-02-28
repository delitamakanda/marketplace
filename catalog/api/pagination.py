from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class CategoryPagination(LimitOffsetPagination):
    default_limit = 20
    max_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'
