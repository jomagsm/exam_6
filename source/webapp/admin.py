from django.contrib import admin

from webapp.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'created_at',]
    list_filter = ['name',]


admin.site.register(Note, NoteAdmin)
