from django.urls import path


from .views import index, detail



app_name = "sevo_sites2"
urlpatterns = [
    path("", index, name="index"),
    path("<slug:slug>/", detail, name="detail")
]
