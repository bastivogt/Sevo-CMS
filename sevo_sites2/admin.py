from django.contrib import admin

from .models import Article, Site2, Site2Article, Menu, MenuSite2

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "created",
        "updated"
    ]

    list_display_links =  [
        "id",
        "title"
    ]

    list_filter = [
        "created",
        "updated"
    ]

    search_fields = [
        "title",
        "description",
        "content"
    ]


class Site2ArticleInline(admin.StackedInline):
    model = Site2Article
    extra = 0

    raw_id_fields = [
        "article"
    ]









class Site2Admin(admin.ModelAdmin):
    list_display = [
        "id",
        "get_image_tag",
        "title",
        "slug",


        "is_home",
        "available",
        "published",
        "order",
        "created",
        "updated",
    ]

    list_display_links = [
        "id",
        "title",
        "get_image_tag"
    ]

    list_editable = [
        "is_home",
        "published",
        "order"

    ]

    fields = [
        "title",
        "slug",

        "meta_keywords",
        "meta_description",

        "picture",
        "get_image_tag",
        "url_path",
        "is_reverse",
        "is_home",
        "available",
        "css_class",
        "published"
    ]

    readonly_fields = [
        "get_image_tag"
    ]

    raw_id_fields = [
        "picture",
    ]

    prepopulated_fields = {
        "slug": ["title"]
    }

    list_filter = [
        "published",
        "created",
        "updated"
    ]

    inlines = [
        Site2ArticleInline
    ]



class MenuSite2Inline(admin.StackedInline):
    model = MenuSite2
    extra = 0

    raw_id_fields = [
        "site2",
        "subsites2"
    ]




class MenuAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "menu_type"
    ]

    list_display_links = [
        "id",
        "title"
    ]

    list_filter = [
        "menu_type"
    ]

    inlines = [
        MenuSite2Inline
    ]




admin.site.register(Article, ArticleAdmin)
admin.site.register(Site2, Site2Admin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuSite2)
