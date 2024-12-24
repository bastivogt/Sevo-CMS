from django.db import models
from django.utils.translation import gettext as _
from tinymce import models as tinymce_models
from django.contrib import admin
from django.urls import reverse

from sevo_media.models import Picture





class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=_("Title"))
    content = tinymce_models.HTMLField(verbose_name=_("Content"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))

    def __str__(self):
        return f"#{self.id} {self.title}"


class Site(models.Model):

    MENU_TYPES = {
        "MAIN": "Main",
        "META": "Meta",
        "NONE": "None"
    }

    title = models.CharField(max_length=50, verbose_name=_("Title"), unique=True)
    slug = models.SlugField(max_length=100, unique=True, verbose_name=_("Slug"))
    menu_type = models.CharField(max_length=10, choices=MENU_TYPES, default=MENU_TYPES["MAIN"], verbose_name=_("Menu Type"))
    order = models.PositiveBigIntegerField(default=0, verbose_name=_("Order"))

    meta_keywords = models.CharField(max_length=160, verbose_name="Meta Keywords", blank=True, null=True)
    meta_description = models.CharField(max_length=160, verbose_name=_("Meta Description"), blank=True, null=True)

    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL)

    picture = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Picture"))
    url_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("URL Path"))
    is_reverse = models.BooleanField(default=False, verbose_name=_("Is Reverse"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))
    is_home = models.BooleanField(default=False, verbose_name=_("Is Home"))

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))


    def __str__(self):
        return f"#{self.id} {self.title}"

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
            return reverse("homepage")
        return reverse("sevo-pages-detail", kwargs={"slug": self.slug})
    

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
            sites = Site.objects.all()
            for site in sites:
                site.is_home = False
                site.save()
            self.is_home = True
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Site")
        verbose_name_plural = _("Sites")

        ordering = [
            "menu_type",
            "order"
        ]







    
