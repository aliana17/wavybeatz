from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="music"

urlpatterns=[
    #/music/
    path('',views.IndexView.as_view(),name='index'),

    path('register/',views.UserFormView.as_view(),name='register'),

    # /music/<album_id>/
    path('<pk>/',views.DetailView.as_view(),name='detail'),

    #/music/album/add/
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),



    ]
    # /music/<album_id>/favorite/
    #path('<pk>/favorite/',views.favorite,name='favorite'),
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)