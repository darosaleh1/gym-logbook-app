from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from logbook.models import Exercise
from logbook.serializers import ExerciseSerializer
from rest_framework.views import APIView
from django.db import models

class ExerciseListView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        return Exercise.objects.filter(
            models.Q(created_by=user) |
            models.Q(is_custom=False)
        ).distinct().order_by('is_custom')
    
    def get(self,request):
        exercises = self.get_queryset()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ExerciseSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)