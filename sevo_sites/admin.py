from django.contrib import admin

from .models import Article, Site, Subsite

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



class SubsiteInline(admin.StackedInline):
    model = Subsite
    extra = 0
    fk_name = "mastersite"

    raw_id_fields = [
        "subsite"
    ]





class SiteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "get_image_tag",
        "title",
        "slug",
        "menu_type",


        "is_home",
        "get_sub_sites_str",
        "get_master_sites_str",
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
        "available",
        "published"
    ]

    readonly_fields = [
        "get_image_tag", 
        "get_sub_sites_str",
        "get_master_sites_str"
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

    inlines = [
        SubsiteInline
    ]




admin.site.register(Article, ArticleAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Subsite)