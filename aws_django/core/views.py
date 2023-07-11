from django.views.generic import ListView

from .models import Album
from .tasks import add


# Create your views here.
class AlbumListView(ListView):
    model = Album

    def get_context_data(self, **kwargs):
        add.delay(2, 4)
        return super().get_context_data(**kwargs)
