"""
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Album

    

def homepage(request):
    all_albums=Album.objects.all()
    context={'all_albums':all_albums,}
    return render(request,'music/index.html',context)

def detail(request, album_id):
    try:
        album= Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")  
    return render(request,'music/detail.html',{'album': album})        

def favorite(request, album_id):    
    try:
        album= Album.objects.get(pk=album_id)
        selected_song = album.song_set.get(pk=request.POST['song'])
    except Album.DoesNotExist:
        raise Http404("Album does not exist") 
    except:
        return render(request,'music/detail.html',{'album': album}) 
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album': album})  
    in details.html
    {% if error_message %}
        <p><strong>{{ error_message }}</strong></p>
    {% endif %} 
    <form action="{% url 'music:favorite' album.id %}" method="post">
        {% csrf_token %}
        {% for song in album.song_set.all %}
            <input type="radio" id="song{{ forloop.counter }}" name="song" value="{{song.id}}" />
            <label for="song{{ forloop.counter }}">
                {{ song.song_title }}
                {% if song.is_favorite %}
                    <img src="http://i.imgur.com/b9b13Rd.png">
                {% endif %} 
            </label><br> 
        {% endfor %}
        <input type="submit" value="Favorite" >  
    </form>       
        """
from django.views import generic 
from django.views.generic import ListView
from django.views.generic import DetailView,UpdateView,DeleteView
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm
from django.contrib import messages

def songs(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })   


class IndexView(ListView):
    template_name="music/index.html"
    context_object_name='all_Albums'

    def get_queryset(self):
        return Album.objects.all()     

class DetailView(DetailView):
      model=Album
      template_name="music/detail.html"  

class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo'] 


class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    #display blank form
    def get(self , request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process from data
    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            #cleaned (normalized) data
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
        
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct

            user=authenticate(username=username,password=password)
            messages.success(request,'Your account has been created! You are now able to log in.')
            return redirect('music:login')
        return render(request,self.template_name,{'form':form})            
                   




