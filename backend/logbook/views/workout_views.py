from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from logbook.models import Workout
from logbook.serializers import WorkoutSerializer, WorkoutExerciseSerializer

class WorkoutListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(created_by=self.request.user)
    
    def get(self, request):
        workouts = self.get_queryset()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkoutSerializer(
            data=request.data, 
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Workout.objects.get(pk=pk, created_by=self.request.user)
        except Workout.DoesNotExist:
            return None

    def get(self, request, pk):
        workout = self.get_object(pk)
        if workout is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data)

    def put(self, request, pk):
        workout = self.get_object(pk)
        if workout is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutSerializer(
            workout, 
            data=request.data, 
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workout = self.get_object(pk)
        if workout is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WorkoutExercisesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Workout.objects.get(pk=pk, created_by=self.request.user)
        except Workout.DoesNotExist:
            return None

    def get(self, request, pk):
        workout = self.get_object(pk)
        if workout is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        exercises = workout.workoutexercise_set.all().order_by('order')
        serializer = WorkoutExerciseSerializer(exercises, many=True)
        return Response(serializer.data)