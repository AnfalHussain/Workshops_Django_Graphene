import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Workshop


class WorkshopType(DjangoObjectType):
    class Meta:
        model = Workshop


class Query(graphene.ObjectType):
    workshop = DjangoListField(WorkshopType)
