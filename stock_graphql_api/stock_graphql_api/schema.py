import graphene

import stocks.schema


class Query(stocks.schema.Query, graphene.ObjectType):
    pass


class Mutation(stocks.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)