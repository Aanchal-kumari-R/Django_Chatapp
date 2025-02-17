from django.shortcuts import render 
from .models import ChatRoom

def index(request):  
    chatRooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html',{'chatRooms':chatRooms})