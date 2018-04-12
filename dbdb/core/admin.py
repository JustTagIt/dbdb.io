# django imports
from django.contrib import admin
# local imports
from .models import *


# inlines

class FeatureOptionsInlines(admin.StackedInline):
    model = FeatureOption
    extra = 0


# model admins

class FeatureAdmin(admin.ModelAdmin):
    inlines = [FeatureOptionsInlines]

class SystemAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('name', 'created', 'modified', 'ver', 'view_count')
    list_filter = ['created', 'modified' ]
    search_fields = ('name', )

class SystemVersionAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('system', 'ver', 'created')
    list_filter = ['created']


# registrations

admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureOption)
admin.site.register(License)
admin.site.register(OperatingSystem)
admin.site.register(ProgrammingLanguage)
admin.site.register(ProjectType)
admin.site.register(Publication)
admin.site.register(SuggestedSystem)
admin.site.register(System, SystemAdmin)
admin.site.register(SystemFeature)
admin.site.register(SystemVersion, SystemVersionAdmin)
admin.site.register(SystemVersionMetadata)