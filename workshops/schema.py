import graphene
import workshops_api.schema


class Query(workshops_api.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
