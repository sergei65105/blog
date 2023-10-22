from django.shortcuts import render
from .models import Video

# Create your views here.
def playlist(request):
    all_videos = Video.objects.all()
    return render(request, 'playlist/playlist.html', {'all_videos': all_videos})

