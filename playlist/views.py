from django.shortcuts import render
from .models import Video

# Create your views here.
def playlist(request):
    all_videos = Video.objects.all()
    return render(request, 'playlist/playlist.html', {'all_videos': all_videos})

def create_video(request):
    if request.method == 'POST':
        name = request.POST['name']
        embed_code = request.POST['embed_code']
        is_published = bool(request.POST.get('is_published'))
        Video.objects.create(name=name, embed_code=embed_code, is_published=is_published)
        all_videos = Video.objects.all()
        return render(request, 'playlist/playlist.html', {'all_videos': all_videos})
    else:
        return render(request, 'playlist/create_video.html', )