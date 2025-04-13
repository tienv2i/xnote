from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'tag_list', 'is_pinned', 'is_archived')
    list_filter = ('is_pinned', 'is_archived', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'tags__name')
    autocomplete_fields = ('user',)
    date_hierarchy = 'updated_at'
    ordering = ['-updated_at']

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
    tag_list.short_description = "Tags"
