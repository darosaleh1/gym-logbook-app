from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from logbook.models import WorkoutPlan, WorkoutPlanDay
from logbook.serializers import WorkoutPlanSerializer, WorkoutPlanDaySerializer

class WorkoutPlanListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WorkoutPlan.objects.filter(created_by=self.request.user)
    
    def get(self,request):
        workout_plans = self.get_queryset()
        serializer = WorkoutPlanSerializer(workout_plans, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WorkoutPlanSerializer(
            data=request.data,
            context= {'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutPlanDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self,pk):
        try:
            return WorkoutPlan.objects.get(pk=pk, created_by=self.request.user)
        except WorkoutPlan.DoesNotExist:
            return None
    
    def get(self,request,pk):
        workout_plan = self.get_object(pk)
        if workout_plan is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutPlanSerializer(workout_plan)
        return Response(serializer.data)
    
    def put(self, request,pk):
        workout_plan = self.get_object(pk)
        if workout_plan is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WorkoutPlanSerializer(
            workout_plan,
            data=request.data,
            context={'request':request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        workout_plan = self.get_object(pk)
        if workout_plan is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        workout_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class WorkoutPlanScheduleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return WorkoutPlan.objects.get(pk=pk, created_by=self.request.user)
        except WorkoutPlan.DoesNotExist:
            return None

    def get(self, request, pk):
        workout_plan = self.get_object(pk)
        if workout_plan is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        schedule = workout_plan.workoutplanday_set.all().order_by('day_of_week')
        serializer = WorkoutPlanDaySerializer(schedule, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        workout_plan = self.get_object(pk)
        if workout_plan is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WorkoutPlanDaySerializer(data=request.data, many=True)
        if serializer.is_valid():
            # Delete existing schedule
            workout_plan.workoutplanday_set.all().delete()
            # Create new schedule
            serializer.save(workout_plan=workout_plan)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)