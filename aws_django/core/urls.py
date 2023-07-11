from django.urls import path

from .views import AlbumListView

app_name = "core"
urlpatterns = [path("list/", AlbumListView.as_view(), name="list")]
