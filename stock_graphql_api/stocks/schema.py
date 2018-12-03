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


class StockInput(graphene.InputObjectType):
    symbol = graphene.String(required=True)
    name = graphene.String(required=True)
    bid = graphene.Float(required=False)
    ask = graphene.Float(required=False)
    target = graphene.Float(required=False)
    day_high = graphene.Float(required=False)
    day_low = graphene.Float(required=False)
    share_volume = graphene.Int(required=False)
    average_volume = graphene.Int(required=False)
    previous_close = graphene.Float(required=False)
    year_high = graphene.Float(required=False)
    year_low = graphene.Float(required=False)
    market_cap = graphene.Int(required=False)
    pe = graphene.Float(required=False)
    forward_pe = graphene.Float(required=False)
    eps = graphene.Float(required=False)
    dividend = graphene.Float(required=False)
    ex_dividend_date = graphene.String(required=False)
    dividend_date = graphene.String(required=False)
    current_yield = graphene.Float(required=False)
    beta = graphene.Float(required=False)
    open_price = graphene.Float(required=False)
    close_price = graphene.Float(required=False)


class CreateStock(graphene.Mutation):
    class Arguments:
        stock_data = StockInput(required=True)

    stock = graphene.Field(StockType)

    @staticmethod
    def mutate(self, info, stock_data=None):
        stock = Stock(
            symbol = stock_data.symbol,
            name = stock_data.name,
            bid = stock_data.bid,
            ask = stock_data.ask,
            target = stock_data.target,
            day_high = stock_data.day_high,
            day_low = stock_data.day_low,
            share_volume = stock_data.share_volume,
            average_volume = stock_data.average_volume,
            previous_close = stock_data.previous_close,
            year_high = stock_data.year_high,
            year_low = stock_data.year_low,
            market_cap = stock_data.market_cap,
            pe = stock_data.pe,
            forward_pe = stock_data.forward_pe,
            eps = stock_data.eps,
            dividend = stock_data.dividend,
            ex_dividend_date = stock_data.ex_dividend_date,
            dividend_date = stock_data.dividend_date,
            current_yield = stock_data.current_yield,
            beta = stock_data.beta,
            open_price = stock_data.open_price,
            close_price = stock_data.close_price,
        )
        stock.save()

        return CreateStock(stock=stock)


class Mutation(graphene.ObjectType):
    create_stock = CreateStock.Field()
