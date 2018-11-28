import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Stock


class StockType(DjangoObjectType):
    class Meta:
        model = Stock


class Query(graphene.ObjectType):
    stocks = graphene.List(StockType, search=graphene.String())

    def resolve_stocks(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(symbol__icontains=search) |
                Q(name__icontains=search)
            )
            return Stock.objects.filter(filter)

        return Stock.objects.all()
