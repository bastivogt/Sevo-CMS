from django.contrib import admin

from .models import Article, Site

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "created",
        "updated"
    ]

    list_display_links =  [
        "id",
        "title"
    ]







class SiteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "get_image_tag",
        "title",
        "article",
        "slug",
        "menu_type",

        "created",
        "updated",
        "is_home",
        "published",
        "order"
    ]

    list_display_links = [
        "id",
        "title",
        "get_image_tag"
    ]

    list_editable = [
        "is_home",
        "published",
        "menu_type",
        "order"

    ]

    fields = [
        "title",
        "slug",
        "menu_type",
        "meta_keywords",
        "meta_description",
        "article",
        "picture",
        "get_image_tag",
        "url_path",
        "is_reverse",
        "is_home",
        "published"
    ]

    readonly_fields = [
        "get_image_tag"
    ]

    raw_id_fields = [
        "picture",
        "article"
    ]

    prepopulated_fields = {
        "slug": ["title"]
    }

    list_filter = [
        "menu_type",
        "published",
        "created",
        "updated"
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Site, SiteAdmin)