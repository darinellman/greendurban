from django.shortcuts import render, get_object_or_404
from .models import Album

# Create your views here.
def allalbums(request):
    albums = Album.objects.order_by('-end_date')
    return render(request, 'albums/allalbums.html', {'albums':albums})
