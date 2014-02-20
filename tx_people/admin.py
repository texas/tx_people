from django.contrib import admin
from django.db.models import Count
from django.utils.translation import ugettext_lazy as _

from . import models


class ParentOrganizationFilter(admin.SimpleListFilter):
    title = _('Parent Organization')
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        return list(models.Organization.objects
                .annotate(children_count=Count('children'))
                .filter(children_count__gt=1)
                .values_list('pk', 'name')) + [('none', 'No Parent', ), ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'none':
            return queryset.filter(parent_id__isnull=True)
        elif value:
            return queryset.filter(parent__id=value)
        return queryset


class ContactDetailAdmin(admin.ModelAdmin):
    raw_id_fields = ('sources', )


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ('scheme', 'identifier', )
    list_display_links = ('identifier', )
    list_filter = ('scheme', )
    search_fields = ('identifier', 'people__name', )


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('person', 'organization', 'post', )
    list_filter = ('organization', )
    raw_id_fields = ('links', 'sources', )
    search_fields = ('person__name', 'organization__name', 'post__label', )


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', )
    list_filter = (ParentOrganizationFilter, )
    raw_id_fields = ('identifiers', 'contact_details', 'links', 'sources', )
    search_fields = ('name', )


class PeopleAdmin(admin.ModelAdmin):
    raw_id_fields = ('identifiers', 'contact_details', 'links', 'sources', )
    search_fields = ('name', 'email', )


class PostAdmin(admin.ModelAdmin):
    list_display = ('label', 'organization', )
    search_fields = ('label', 'organization__name', )


class SourceAdmin(admin.ModelAdmin):
    search_fields = ('link', )


admin.site.register(models.ContactDetail, ContactDetailAdmin)
admin.site.register(models.Identifier, IdentifierAdmin)
admin.site.register(models.Membership, MembershipAdmin)
admin.site.register(models.Organization, OrganizationAdmin)
admin.site.register(models.Person, PeopleAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Source, SourceAdmin)
