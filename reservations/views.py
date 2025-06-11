from django.shortcuts import render
from rest_framework import generics
from .models import Reservation, Comment
from .serializers import ReservationSerializer, CommentSerializer

# Create your views here.

class ReservationListCreateView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()
        table_id = self.request.query_params.get('table')
        if table_id:
            queryset = queryset.filter(table_id=table_id)
        return queryset

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
