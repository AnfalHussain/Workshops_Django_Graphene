import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Workshop


class WorkshopType(DjangoObjectType):
    class Meta:
        model = Workshop


class Query(graphene.ObjectType):
    workshop = DjangoListField(WorkshopType)
    workshop_by_name = graphene.Field(WorkshopType, name=graphene.String())

    def resolve_workshop_by_name(self, info, name):
        if name is not None:
            return Workshop.objects.get(name=name)

        return None


class WorkshopInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    image = graphene.String()
    price = graphene.Int()

# EVIIIILLLLLLLLLLL
# class AddWorkshopMutation(graphene.Mutation):
#     class Arguments:
#         input = WorkshopInput(required=True)

#     workshop = graphene.Field(WorkshopType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         workshop = Workshop(
#             name=input.name,
#             description=input.description,
#             image=input.image,
#             price=input.price)
#         workshop.save()
#         return AddWorkshop(workshop=workshop)


class AddWorkshopMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        image = graphene.String()
        price = graphene.Int()

    workshop = graphene.Field(WorkshopType)

    def mutate(self, info, name, description, image, price):
        workshop = Workshop(
            name=name,
            description=description,
            image=image,
            price=price)
        workshop.save()
        return AddWorkshopMutation(workshop=workshop)


class EditWorkshopMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        name = graphene.String()
        description = graphene.String()
        image = graphene.String()
        price = graphene.Int()

    # The class attributes define the response of the mutation
    workshop = graphene.Field(WorkshopType)

    def mutate(self, info, id, name, description, image, price):
        workshop = Workshop.objects.get(pk=id)
        print("workshop", workshop)
        workshop.name = name
        workshop.description = description
        workshop.image = image
        workshop.price = price
        workshop.save()
        # Notice we return an instance of this mutation
        return EditWorkshopMutation(workshop=workshop)
