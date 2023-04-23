import graphene

import airlines.schema


class Query(airlines.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
