#from . import settings

from .models import Site



# def menus_context(request):
#     menus = Menu.objects.all()
#     menu_main = menus.get(name=settings.SEVO_PAGES_MENU_MAIN)
#     menu_meta = menus.get(name=settings.SEVO_PAGES_MENU_META)

#     homepage = Page.get_home_page()


#     return {
#         "menus": menus,
#         "menu_main": menu_main,
#         "menu_meta": menu_meta, 
#         "homepage": homepage
#     }


def sites_context(request):
    sites_all = Site.objects.all()
    sites_pub = sites_all.filter(published=True)
    sites_main_pub = sites_pub.filter(menu_type="MAIN")
    sites_meta_pub = sites_pub.filter(menu_type="META")
    sites_none_pub = sites_pub.filter(menu_type="NONE")
    home_page = Site.get_home_page()

    return {
        "sites_all": sites_all,
        "sites_pub": sites_pub,
        "sites_main_pub": sites_main_pub,
        "sites_meta_pub": sites_meta_pub,
        "sites_none_pub": sites_none_pub,
        "home_page": home_page
    }

    