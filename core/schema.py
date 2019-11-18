import graphene
from graphene_django import DjangoObjectType
from .models import Page, Category


class PageType(DjangoObjectType):
    class Meta:
        model = Page


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.ObjectType):
    page = graphene.Field(PageType, id=graphene.Int(required=True))
    pages = graphene.List(PageType)
    categories = graphene.List(CategoryType)

    def resolve_page(self, info, id):
        return Page.objects.get(id=id)

    def resolve_pages(self, info):
        return Page.objects.all()

    def resolve_categories(self, info):
        return Category.objects.all()


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        cat = Category(name=name)
        cat.save()
        return CreateCategory(category=cat)


class CreatePage(graphene.Mutation):
    page = graphene.Field(PageType)

    class Arguments:
        category = graphene.Int()
        title = graphene.String()
        views = graphene.Int()
        url = graphene.String()
    
    def mutate(self, info, **kwargs):
        cat_id = kwargs.get('category')
        category = Category.objects.get(id=cat_id)
        title = kwargs.get('title')
        views = kwargs.get('views')
        url = kwargs.get('url')
        page = Page(category=category, title=title, views=views, url=url)
        page.save()
        return CreatePage(page=page)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_page = CreatePage.Field()