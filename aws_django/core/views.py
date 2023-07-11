from django.views.generic import ListView

from .models import Album


# Create your views here.
class AlbumListView(ListView):
    model = Album
