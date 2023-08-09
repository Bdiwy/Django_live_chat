from django.shortcuts import render,redirect
from chat.models import Room , Message
# Create your views here.
def index(request):
        return render(request,'index.html')


def room(request,room):
        return render(request,'room.html')



def check(request):
    if request.method == 'POST':
        room =request.POST['room_name']
        username = request.POST['username']


        if Room.objects.filter(name=room).exists():
              return redirect('/',room,'/?username=',username)
        else:
              new_room = Room.objects.create(name=room)
              new_room.save()
              return redirect('/',room,'/?username=',username)