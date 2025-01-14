from django.contrib import admin
from django.utils.html import format_html

from . models import PictureTag, Picture, FileTag, File

# Register your models here.


class PictureTagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title"
    ]

    list_display_links = [
        "id",
        "title"
    ]


class PictureAdmin(admin.ModelAdmin):

    fields = [
        "id",
        "title",
        "image",
        "get_image_tag",
        "get_image_url",
        "tags",
    ]

    list_display = [
        "id",
        "get_image_tag",
        "title",
        "get_tags_as_str",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "id",
        "title",
        "get_image_tag"
    ]

    readonly_fields = [
        "get_image_tag",
        "get_link_image_tag",
        "get_image_url",
        "id"
    ]

    list_filter = [
        "tags",
        "created_at",
        "updated_at"
    ]



class FileTagAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title"
    ]

    list_display_links = [
        "id",
        "title"
    ]


class FileAdmin(admin.ModelAdmin):
    fields = [
        "id",
        "title",
        "file",
        "get_file_url",
        "tags",
    ]

    list_display = [
        "id",
        "title",
        "get_tags_as_str",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "id",
        "title"
    ]

    readonly_fields = [
        "get_file_url",
        "id"
    ]

    list_filter = [
        "tags",
        "created_at",
        "updated_at"
    ] 



admin.site.register(FileTag, FileTagAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(PictureTag, PictureTagAdmin)
admin.site.register(Picture, PictureAdmin)

