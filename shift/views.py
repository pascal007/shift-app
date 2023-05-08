from rest_framework import status, viewsets
from rest_framework.response import Response

from shift.models import Shift
from shift.serializers import ShiftSerializer
from user.permissions import WorkerPermission


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.select_related('worker')
    serializer_class = ShiftSerializer
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [WorkerPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

