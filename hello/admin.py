from django.contrib import admin

from . import models

#admin.site.register(models.LogMessage)
#admin.site.register(models.Application)

@admin.register(models.LogMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'applicationname')
    ordering = ('severity',)
    search_fields = ('subject',)
    list_filter = ('log_date','severity')

@admin.register(models.Application)
class AppAdmin(admin.ModelAdmin):
    list_display = ('description', 'applicationname')
    ordering = ('applicationname',)
    search_fields = ('applicationname',)