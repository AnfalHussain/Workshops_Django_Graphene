# from graphene import List, Field, Int, String
# from graphene_django import DjangoObjectType, DjangoListField

# from .models import Workshop


# class WorkshopType(DjangoObjectType):
#     class Meta:
#         model = Workshop


# class Query(object):
#     workshop = DjangoListField(WorkshopType)

import graphene

import workshops_api.schema


class Query(workshops_api.schema.Query, graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="world"))
    goodbye = graphene.String()

    def resolve_hello(self, info, name):
        return f"Hello {name}!"

    def resolve_goodbye(self, info):
        return "Goodbye cruel world!"


schema = graphene.Schema(query=Query)
