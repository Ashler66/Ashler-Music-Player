from django.shortcuts import render,redirect
from .models import *
def adds(request):
    
    if request.method=="POST":
        data=request.POST
        song_name=data.get('song_name')
        artist_name=data.get('artist_name')
        song_link=request.FILES.get('song_link')
        song_image=request.FILES.get('song_image')
        song_lyric=request.FILES.get('song_lyric')
        addsongs.objects.create(
            song_name=song_name,
            artist_name=artist_name,
            song_link=song_link,
            song_image=song_image,
            song_lyric= song_lyric
        )
        return redirect('/adds/')
    queryset=addsongs.objects.all()
    context={'songs': queryset}
    return render(request,'addsongs.html',context)

def delete(request,id):
    queryset=addsongs.objects.get(id=id)
    queryset.delete()
    return redirect('/adds/')

def update(request,id):
    queryset=addsongs.objects.get(id=id)
    context={'elem':queryset}
    if request.method=='POST':
         data=request.POST
         song_name=data.get('song_name')
         artist_name=data.get('artist_name')
         song_link=request.FILES.get('song_link')
         song_image=request.FILES.get('song_image')
         song_lyric=request.FILES.get('song_lyric')
         op=song_name
         
         if (not song_name.isspace()) and song_name!="":
             queryset.song_name=song_name
         if (not artist_name.isspace()) and artist_name!="":
             queryset.artist_name=artist_name
         if song_link:
             queryset.song_link=song_link 
         if song_image:  
             queryset.song_image=song_image          
         if song_lyric: 
             queryset.song_lyric=song_lyric            
             
         queryset.save()
         return redirect('/adds/')

    
    return render(request,'updatesongdata.html',context)

def search(request):
   if request.method=='GET':
    query=request.GET['search']
    queryset=addsongs.objects.filter(song_name__icontains=query)
    queryset2=addsongs.objects.filter(artist_name__icontains=query)
    context={'allsong':queryset|queryset2}
    return render(request,'search.html',context)
   


   
