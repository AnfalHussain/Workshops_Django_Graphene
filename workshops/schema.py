import graphene
import workshops_api.schema


class Query(workshops_api.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    update_workshop = graphene.Field(workshops_api.schema.EditWorkshopMutation)


schema = graphene.Schema(query=Query, mutation=Mutation)
