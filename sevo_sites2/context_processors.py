#from . import settings

from .models import Menu, Site2



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


def menu_context(request):
    menus_all = Menu.objects.all()
    menu_primary = menus_all.filter(menu_type="PRIMARY").first()
    menu_secondary = menus_all.filter(menu_type="SECONDARY").first()
    menu_meta = menus_all.filter(menu_type="META").first()
    menu_other = menus_all.filter(menu_type="OTHER").first()

    print(menu_primary.get_menu_sites)

    

    homepage = Site2.get_home_page()

    return {
        "menus": menus_all,
        "menu_primary": menu_primary,
        "menu_secondary": menu_secondary,
        "menu_meta": menu_meta,
        "menu_other": menu_other, 
        "homepage": homepage
    }
    

    