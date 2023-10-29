
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from playlist.views import *
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/posts_list/', posts_list),
    path('guess_numbers/', guess_numbers),
    path('create/', create),
    path('playlist/', playlist),
    path('playlist/create_video/', create_video),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
