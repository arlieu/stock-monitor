import graphene
from graphene_django import DjangoObjectType

from .models import Stock


class StockType(DjangoObjectType):
    class Meta:
        model = Stock


class Query(graphene.ObjectType):
    stocks = graphene.List(StockType)

    def resolve_stocks(self, info, **kwargs):
        return Stock.objects.all()

