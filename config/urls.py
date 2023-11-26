
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from playlist.views import *
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/post_list/', post_list, name='post_list'),
    path('guess_numbers/', guess_numbers),
    path('create/', create),
    path('playlist/', playlist,  name='playlist'),
    path('playlist/create_video/', create_video, name='create_video'),
    path('blog/post_like/', post_like, name='post_like'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
