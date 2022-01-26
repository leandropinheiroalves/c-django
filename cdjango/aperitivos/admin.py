from django.contrib.admin import ModelAdmin, register

from cdjango.aperitivos.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creations', 'vimeo_id')
    ordering = ('creations',)
    prepopulated_fields = {'slug': ('titulo',)}
