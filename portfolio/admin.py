from django.contrib import admin
from .models import Technology, Project

# Register your models here.
class TechnologyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    search_fields = ('title', 'description', 'tecnologies')
    list_per_page = 25

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Project, ProjectAdmin)
