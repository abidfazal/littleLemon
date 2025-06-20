from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerialzer
from .models import Menu, Booking
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    # pagination_class = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerialzer
    
    
@api_view()
@permission_classes([IsAuthenticated])
def secured_view(request):
    return Response('only for authenticated user')
    

