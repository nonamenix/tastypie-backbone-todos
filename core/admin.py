from django.contrib import admin
from core.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('owner','title','done','order')
admin.site.register(Todo, TodoAdmin)