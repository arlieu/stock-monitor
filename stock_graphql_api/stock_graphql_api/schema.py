import graphene

import stocks.schema


class Query(stocks.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)