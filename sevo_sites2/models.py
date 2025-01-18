from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.utils.translation import gettext as _
from tinymce import models as tinymce_models




from sevo_media.models import Picture

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Title"))
    description = models.TextField(max_length=255, verbose_name=_("Description"), blank=True)
    content = tinymce_models.HTMLField(verbose_name=_("Content"))


    css_id = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("CSS ID"))
    css_class = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("CSS Classes"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    @property
    def rendered_content(self):
        from django.template import Template, Context
        #from django.template.loader import render_to_string
        try:
            tpl = Template("{% load sevo_tags %}" + self.content)
            return tpl.render(Context({}))
        except:
            return self.content
        
    

    def __str__(self):
        return f"#{self.id} {self.title} [{self.description}]"
    
    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")



class Site2(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("Title"), unique=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_("Slug"))
    #menu_type = models.CharField(max_length=10, choices=MENU_TYPES, default=MENU_TYPES["MAIN"], verbose_name=_("Menu Type"))
    order = models.PositiveBigIntegerField(default=0, verbose_name=_("Order"))

    meta_keywords = models.TextField(max_length=160, verbose_name="Meta Keywords", blank=True, null=True)
    meta_description = models.TextField(max_length=160, verbose_name=_("Meta Description"), blank=True, null=True)


    picture = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Picture"))
    url_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("URL Path"))
    is_reverse = models.BooleanField(default=False, verbose_name=_("Is Reverse"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))
    is_home = models.BooleanField(default=False, verbose_name=_("Is Home"))

    available = models.BooleanField(default=True)


    css_class = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("CSS Classes"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))


    def __str__(self):
        return f"#{self.id} {self.title}"
    
    
    def get_site_articles(self, published=False):
        sa = self.site_articles.all()
        if published == True:
            return sa.filter(published=True)
        return sa
        

    def get_published_site_articles(self):
        return self.get_site_articles(published=True)
    
    @admin.display(description="Has Subsites")
    def has_sub_sites(self):
        if self.get_sub_sites().count() > 0:
            return True
        return False

    @admin.display(description="Site Picture")
    def get_image_tag(self):
        if self.picture:
            return self.picture.get_image_tag()
        return None
    


    
    def get_absolute_url(self):
        if self.url_path != None:
            if self.is_reverse:
                path = reverse(self.url_path)
            else:
                path = self.url_path

            return path
        if self.is_home:
            return reverse("index")
        return reverse("sevo_sites2:detail", kwargs={"slug": self.slug})
    

    @classmethod
    def get_home_page(cls):
        try:
            home = cls.objects.get(is_home=True)
        except:
            home = cls.objects.first
        return home
    
    def save(self, *args, **kwargs):
        #super().save(*args, **kwargs)
        if self.is_home:
            sites = Site2.objects.all()
            for site in sites:
                site.is_home = False
                site.save()
            self.is_home = True
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Site2")
        verbose_name_plural = _("Sites2")

        ordering = [
            "order"
        ]



class Site2Article(models.Model):
    site2 = models.ForeignKey(Site2, null=True, blank=True, on_delete=models.SET_NULL, related_name="site_articles", verbose_name=_("Site2"))
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Article"))
    css_id = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("CSS ID"))
    css_class = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("CSS Classes"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Order"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))

    def __str__(self):
        return f"#{self.article.id} {self.article.title}"
    
    class Meta:
        verbose_name = _("Site2 Article")
        verbose_name_plural = _("Site2 Articles")
    


class Menu(models.Model):
    MENU_TYPES = {
        "PRIMARY": "Primary",
        "SECONDARY": "Secondary",
        "META": "Meta",
        "OTHER": "Other"
    }

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    menu_type = models.CharField(max_length=50, choices=MENU_TYPES, default=MENU_TYPES["PRIMARY"], verbose_name=_("Menu Type"))

    def __str__(self):
        return f"#{self.id} {self.title} [{self.menu_type}]"
    
    def get_menu_sites(self, published=False):
        ms = self.menu_sites.all()
        if published == True:
            return ms.filter(published=True)
        return ms
    
    def get_published_menu_sites(self):
        return self.get_menu_sites(published=True)
    
    @admin.display(description="Sites")
    def get_sites_str(self):
        pass


    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


class MenuSite2(models.Model):
    menu = models.ForeignKey(Menu, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Menu"), related_name="menu_sites")
    site2 = models.ForeignKey(Site2, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_("Site2"), related_name="sites")
    subsites2 = models.ManyToManyField(Site2, blank=True, verbose_name=_("Subsites2"), related_name="subsites")
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    def __str__(self):
        return f"#{self.site2.id} {self.site2.title}"
    

    
    def has_subsites(self):
        if self.subsites2.count() > 0:
            return True
        return False
    
    def get_subsites(self):
        return self.subsites2.all()
    
    def get_published_subsites(self):
        ss = self.get_subsites().filter(published=True)
        return ss

    @admin.display(description="Subsites2 String")
    def get_subsites_str(self):
        ss = self.get_subsites()
        if ss.count() == 0:
            return "-"
        ss_list = [str(item) for item in ss]
        return ", ".join(ss_list)

    
    class Meta:
        verbose_name = _("Menu Site2")
        verbose_name_plural = _("Menu Sites2")










    

