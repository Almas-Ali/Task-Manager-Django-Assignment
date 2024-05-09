from django.contrib import admin

from tasks.models import Gallery, Task


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """The gallery admin class"""

    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """The task admin class"""

    list_display = ("title", "due_date", "priority", "is_completed", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at", "due_date", "priority", "is_completed")
    filter_horizontal = ("photos",)
    ordering = ("-priority",)
