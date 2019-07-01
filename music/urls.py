from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name="music"

urlpatterns=[
    #/music/
    path('',views.IndexView.as_view(),name='index'),

    path('register/',views.UserFormView.as_view(),name='register'),

    path('login/',auth_views.LoginView.as_view(template_name='music/login.html'),name='login'),

    path('logout/',auth_views.LogoutView.as_view(template_name='music/logout.html'),name='logout'),

    # /music/<album_id>/
    path('<pk>/',views.DetailView.as_view(),name='detail'),

    path('songs/<pk>', views.songs, name='songs'),

    #/music/album/add/
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),



    ]
    # /music/<album_id>/favorite/
    #path('<pk>/favorite/',views.favorite,name='favorite'),
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)