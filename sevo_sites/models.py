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

    meta_keywords = models.TextField(max_length=160, verbose_name="Meta Keywords", blank=True, null=True)
    meta_description = models.TextField(max_length=160, verbose_name=_("Meta Description"), blank=True, null=True)

    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL)

    picture = models.ForeignKey(Picture, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Picture"))
    url_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("URL Path"))
    is_reverse = models.BooleanField(default=False, verbose_name=_("Is Reverse"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))
    is_home = models.BooleanField(default=False, verbose_name=_("Is Home"))

    available = models.BooleanField(default=True)




    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))


    def __str__(self):
        return f"#{self.id} {self.title}"
    

    def get_sub_sites(self):
        return self.master_site.filter(mastersite=self)
    
    # get_master_site_subsites
    def get_master_sites(self):
        if self.has_sub_sites():
            return
        else:
            subsites_all = Subsite.objects.all()
            subsites = subsites_all.filter(subsite=self)
            return subsites
        
    def get_master_sites_ids(self):
        subsites = self.get_master_sites()
        mastersites_list = [item.mastersite.id for item in subsites]
        return mastersites_list
    
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
    
    @admin.display(description="Subsites")
    def get_sub_sites_str(self):
        if not self.has_sub_sites():
            return
        else:
            subsites_all = self.get_sub_sites()
            subsites_list = [f"#{item.subsite.id} {item.subsite.title}" for item in subsites_all]
            return ", ".join(subsites_list)
        
    @admin.display(description="Mastersites")
    def get_master_sites_str(self):
        if self.has_sub_sites():
            return
        else:
            subsites_all = Subsite.objects.all()
            #print(subsites_all)
            subsites = subsites_all.filter(subsite=self)
            mastersites_list = [f"#{item.mastersite.id} {item.mastersite.title}" for item in subsites]
            print(mastersites_list)
            return ", ".join(mastersites_list)

    

    
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



class Subsite(models.Model):
    mastersite = models.ForeignKey(Site, blank=True, null=True, on_delete=models.SET_NULL, related_name="master_site")
    subsite = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL, related_name="sub_sites")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"#{self.id}, mastersite={self.mastersite}, subsite={self.subsite}"
    
    class Meta:
        ordering = [
            "order"
        ]







    
