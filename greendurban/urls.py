
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import greendurban.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', greendurban.views.home, name='home'),
    #path('blog/', include('blog.urls')),
    path('albums/', include('albums.urls')),
    #path('events/', include('events.urls')),
    #path('history/', include('history.urls')),
    #path('spots/', include('spots.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
