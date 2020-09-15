from graphene import List, Field, Int, String
from graphene_django import DjangoObjectType, DjangoListField

from .models import Workshop


class WorkshopType(DjangoObjectType):
    class Meta:
        model = Workshop


class Query(object):
    workshop = DjangoListField(WorkshopType)
