from django.contrib.auth.models import User
from tastypie.authentication import ApiKeyAuthentication, SessionAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from core.models import Todo

__author__ = 'nonamenix'
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from core.models import Todo

class TodoResource(ModelResource):
    def get_object_list(self, request):
        return super(TodoResource, self).get_object_list(request).filter(owner=request.user)

    def obj_create(self, bundle, **kwargs):
        return super(TodoResource, self).obj_create(bundle, owner=bundle.request.user)

    class Meta:
        queryset = Todo.objects.all()
        authorization = DjangoAuthorization()
        always_return_data = True

