from django.contrib import admin
from django.utils.text import Truncator
from .models import Project

# Project class
class ProjectAdmin(admin.ModelAdmin):
    # List configuration
    # list_filter and ordering are of type list, that's why there's a "useless" space.
    list_display   = ('name', 'date', 'overview')
    # Automatic slug filling
    prepopulated_fields = {'slug': ('name', ), }
    list_filter    = ('name', )
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('name', 'desc')

    def overview(self, project):
        # If the description exceeds 30 characters, cut
        return Truncator(project.desc).chars(30, truncate='..')

    overview.short_description = 'Description du projet'

    # Form configuration
    fieldsets = (
       ('Général', {
            'fields': ('name', 'slug', 'image')
        }),
        ('Contenu du projet', {
           'description': 'Courte description du projet. Le formulaire accepte les balises HTML.',
           'fields': ('desc', )
        }),
    )

admin.site.register(Project, ProjectAdmin)