from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from songadmin.views import *
from songadmin.models import addsongs
from songadmin.templates import *
from ashler.models import *
# Create your views here.


def Home(request):
    
   
        
     
     return render(request,'Home.html')


def autosearch(request):
     cx=""
     cy=""
     if 'term' in request.GET:
          qs=addsongs.objects.filter(song_name__istartswith=request.GET.get('term'))
          titles=list()
          for product in qs:
               titles.append(str(product.song_name))
               cx=str(product.song_name)
               cy=str(product.artist_name)
          
          return JsonResponse(titles,safe=False)
          
     data=request.GET.get('autosearch')
     cx=str(data)
     selected_song=addsongs.objects.filter(song_name__istartswith=data)
     allsong2=[]
     for song in selected_song:
         allsong2.append(int(song.id))

     allsong=addsongs.objects.filter(id=allsong2[0])
     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
     context={'allsong':allsong,
              'currel':allsong2,
              'y':y
              }
     
     return render(request,'play.html',context)

def fwd(request):
     allsong2=[]
     
     data=request.POST
     allsong=data.getlist('num')      
     cnt=0
     for song in allsong:
     
      if cnt!=0:
        z=int(song)
        allsong2.append(z)
   
      cnt=cnt+1
          
     x=allsong[0]
    
     z=int(x)
     allsong2.append(z)
     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
     allsong3=addsongs.objects.filter(id=allsong2[0])
    
     context={'allsong':allsong3,
              'currel':allsong2,
              'y':y
              }
     return render(request,'play.html',context)
def pre(request):
     allsong2=[]
     
     data=request.POST
     allsong=data.getlist('num2')  
     ln=len(allsong)    
     ln=ln-1
     cnt=0
     x=allsong[ln]
    
     z=int(x)
     allsong2.append(z)
     for song in allsong:
      if cnt!=ln:
        z=int(song)
        allsong2.append(z)
   
      cnt=cnt+1
          
     
     allsong3=addsongs.objects.filter(id=allsong2[0])
     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
    
     context={'allsong':allsong3,
              'currel':allsong2,
              'y':y
              }
     return render(request,'play.html',context)

def Browse(request):
    elems=addsongs.objects.all()
    allsong2=[]
    for c in elems:
        allsong2.append(int(c.id))
    allsong3=[]        
    x=-1
    y=0
    context={
        'allsong':elems,
        'currel':allsong2,
        'allsong2':allsong3,
        'x':x,
        'y':y

    }
    return render(request,'Browse.html',context)

def bpre(request):
     allsong2=[]
     
     data=request.POST
     allsong=data.getlist('bnum2')  
     ln=len(allsong)    
     ln=ln-1
     cnt=0
     x=allsong[ln]
    
     z=int(x)
     allsong2.append(z)
     for song in allsong:
      if cnt!=ln:
        z=int(song)
        allsong2.append(z)
   
      cnt=cnt+1
          
     
     allsong3=addsongs.objects.filter(id=allsong2[0])
     x=allsong2[0]
     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
     context={'allsong2':allsong3,
              'currel':allsong2,
               'allsong':addsongs.objects.all(),
               'x':x,
               'y':y
              }
     return render(request,'browse.html',context)


def bfwd(request):
     allsong2=[]
     
     data=request.POST
     allsong=data.getlist('bnum')   
   
     cnt=0
     for song in allsong:
      if cnt!=0:
        z=int(song)
        allsong2.append(z)
   
      cnt=cnt+1
          
     x=allsong[0]
    
     z=int(x)
     allsong2.append(z)
     allsong3=addsongs.objects.filter(id=allsong2[0])
     x=allsong2[0]
     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
     context={'allsong2':allsong3,
              'currel':allsong2,
              'allsong':addsongs.objects.all(),
              'x':x,
              'y':y
              }
     return render(request,'browse.html',context)

def imsel(request):
   data=request.POST.get('imsel')

   allsongs=addsongs.objects.all()
   allsong2=[]
   allsong3=[]
   x=0
   z=-1
   for song in allsongs:
      if song.id==int(data):
         x=1
      if x==0:
         allsong3.append(int(song.id))
      else:
         allsong2.append(int(song.id))

  

   for y in allsong3:
         allsong2.append(y)
        
   allsong4=addsongs.objects.filter(id=int(data)) 
   y=0  
   for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
   context={
         'allsong2':allsong4,
              'currel':allsong2,
              'allsong':addsongs.objects.all(),
              'x':int(data),
              'y':y
      }
   
   return render(request,'Browse.html',context)

def Library(request):
  set=Lib.objects.all()
  allsong=[]
  for x in set:
     allsong.append(int(x.song_id))
  
  allsong2=addsongs.objects.filter(pk__in=allsong)
  y=0
  
  context={
     'allsong':allsong2,
     'currel':allsong,
     'y':y
  }
  return  render (request,'Library.html',context)





def AddToLib(request):
  if request.method == 'POST':
        # Extract the song ID from the POST data
        song_ig= request.POST.get('song_id')
        song_gg=int(song_ig)
      
        x=0
        for song in Lib.objects.all():
           if int(song.song_id)==int(song_gg):
              x=1
        if x==0:      
         Lib.objects.create(song_id=song_gg)
        else:
           lg=Lib.objects.get(song_id=song_gg)
           lg.delete()
           
        
        return JsonResponse({'message': f'Song with ID added to library successfully'})
  else:
        # If the request method is not POST, return a 405 Method Not Allowed response
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
  

def lfwd(request):
     allsong2=[]
     
     data=request.POST
     allsong=data.getlist('bnum')   
   
     cnt=0
     for song in allsong:
      if cnt!=0:
        z=int(song)
        allsong2.append(z)
   
      cnt=cnt+1
          
     x=allsong[0]
    
     z=int(x)
     allsong2.append(z)
     allsong3=addsongs.objects.filter(id=allsong2[0])
     

     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1
     
     set=Lib.objects.all()
     allsongx=addsongs.objects.filter(pk__in=allsong2)
     print(allsong3)
     
     context={'allsong2':allsong3,
              'currel':allsong2,
              'allsong':allsongx,
              'y':y
              }
     return render(request,'Library.html',context)


def lpre(request):
     allsong2=[]
     
     data=request.POST
     allsong=data.getlist('bnum2')  
     ln=len(allsong)    
     ln=ln-1
     cnt=0
     x=allsong[ln]
    
     z=int(x)
     allsong2.append(z)
     for song in allsong:
      if cnt!=ln:
        z=int(song)
        allsong2.append(z)
   
      cnt=cnt+1
          
     
     allsong3=addsongs.objects.filter(id=allsong2[0])
     x=allsong2[0]
     y=0
     for c in Lib.objects.all():
        if int(c.song_id)==int(allsong2[0]):
           y=1

     allsongx=addsongs.objects.filter(pk__in=allsong2)
     context={'allsong2':allsong3,
              'currel':allsong2,
               'allsong':allsongx,
               'y':y
              }
     return render(request,'Library.html',context)
def libsel(request):
 print('hello')
 data=request.POST.get('libsel')
 print(data)
 ig=Lib.objects.all()
 allsong=[]
 allsong2=[]
 x=0
 for song in ig:
    z=int(song.song_id)
    op=int(data)
    if z==op:
       x=1
    if x==1:
       allsong.append(z)
    else:
       allsong2.append(z)     
 for song in allsong2:
    allsong.append(song)
 y=0
 for c in Lib.objects.all():
        if int(c.song_id)==int(allsong[0]):
           y=1   

 allsongx=addsongs.objects.filter(pk__in=allsong)   
 allsong3=addsongs.objects.filter(id=allsong[0])
 context={
    'currel':allsong,
    'allsong':allsongx,
    'allsong2':allsong3,
    'y':y


 }         
 return render(request,'Library.html',context)

   
   



                    
                    
          
     
      
      

      
      

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
