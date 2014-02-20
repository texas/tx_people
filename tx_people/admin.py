from django.contrib import admin

from . import models


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


class PeopleAdmin(admin.ModelAdmin):
    raw_id_fields = ('identifiers', 'contact_details', 'links', 'sources', )
    search_fields = ('name', 'email', )


admin.site.register(models.Identifier, IdentifierAdmin)
admin.site.register(models.Membership, MembershipAdmin)
admin.site.register(models.Person, PeopleAdmin)
