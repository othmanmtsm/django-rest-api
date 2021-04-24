from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            return JsonResponse({'token':'asdasfefqwe'}, status=201)
        except IntegrityError:
            return JsonResponse({'error':'username taken'}, status=400)

class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationCreate(generics.CreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        room = Room.objects.get(pk=self.kwargs['pk'])
        return Reservation.objects.filter(user=user, room=room)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already reserved this room')
        serializer.save(user=self.request.user, room=Room.objects.get(pk=self.kwargs['pk']))