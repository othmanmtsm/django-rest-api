from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer

class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

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