# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from logbook.models import WorkoutLog, ExerciseLog
from logbook.serializers import WorkoutLogSerializer, ExerciseLogSerializer
from datetime import datetime

class WorkoutLogListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutLog.objects.filter(user=self.request.user)
    
    def get(self, request):
        workout_logs = self.get_queryset()
        # Filter by date if provided
        date = request.query_params.get('date')
        if date:
            workout_logs = workout_logs.filter(date=date)
        serializer = WorkoutLogSerializer(workout_logs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkoutLogSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutLogDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return WorkoutLog.objects.get(pk=pk, user=self.request.user)
        except WorkoutLog.DoesNotExist:
            return None

    def get(self, request, pk):
        workout_log = self.get_object(pk)
        if workout_log is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutLogSerializer(workout_log)
        return Response(serializer.data)

class ExerciseLogView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, workout_log_id):
        try:
            workout_log = WorkoutLog.objects.get(
                id=workout_log_id, 
                user=request.user
            )
        except WorkoutLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        exercise_logs = ExerciseLog.objects.filter(workout_log=workout_log)
        serializer = ExerciseLogSerializer(exercise_logs, many=True)
        return Response(serializer.data)

    def post(self, request, workout_log_id):
        try:
            workout_log = WorkoutLog.objects.get(
                id=workout_log_id, 
                user=request.user
            )
        except WorkoutLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ExerciseLogSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(workout_log=workout_log)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PreviousExerciseLogsView(APIView):
    """View to get previous logs for a specific exercise"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, exercise_id):
        # Get the last 5 logs for this exercise
        previous_logs = ExerciseLog.objects.filter(
            exercise_id=exercise_id,
            workout_log__user=request.user
        ).order_by('-workout_log__date')[:5]
        
        serializer = ExerciseLogSerializer(previous_logs, many=True)
        return Response(serializer.data)