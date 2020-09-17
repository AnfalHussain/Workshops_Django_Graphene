import graphene
import workshops_api.schema


class Query(workshops_api.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    add_workshop = workshops_api.schema.AddWorkshopMutation.Field()
    update_workshop = workshops_api.schema.EditWorkshopMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
