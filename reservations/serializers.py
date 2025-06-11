from rest_framework import serializers
from .models import Reservation, Comment

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment cannot be empty.")
        return value 