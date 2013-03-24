from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.conf.urls import *
from tastypie.api import Api
from core.api import TodoResource

v1_api = Api(api_name='v1')
v1_api.register(TodoResource())

urlpatterns = patterns('',
   url(r'^api/', include(v1_api.urls)),
   url(r'^$', login_required(TemplateView.as_view(template_name="core/todo.html")))
)