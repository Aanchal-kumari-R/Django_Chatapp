from django.shortcuts import render 
from .models import ChatRoom

def index(request):  
    chatRooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'chatRooms':chatRooms})  

def chatRoom(request,slug): 
    chatRoom = ChatRoom.objects.get(slug=slug) 
    return render(request,'chatapp/room.html',{'chatRoom' : chatRoom})  
 