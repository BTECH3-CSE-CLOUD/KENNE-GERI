from django.urls import path
from .views import ReservationListCreateView, CommentCreateView

urlpatterns = [
    path('reservations/', ReservationListCreateView.as_view()),
    path('comments/', CommentCreateView.as_view()),
] 