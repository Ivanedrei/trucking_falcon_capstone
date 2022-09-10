from rest_framework.decorators import action
from truckingfalconapi.models import Employee, PermissionType
from rest_framework.response import Response
from rest_framework import Response, status


@action(methods=['post'], detail=True)
def signup(self, request, pk):
    """Post request for a user to sign up for an event"""

    employee = Employee.objects.get(user=request.auth.user)
    permission_type = PermissionType.objects.get(pk=pk)
    permission_type.attendees.add(employee)
    return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
