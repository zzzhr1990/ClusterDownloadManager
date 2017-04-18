from .models import OnlineServer
from rest_framework import viewsets
from .serializers import ServerSerializer


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows online servers to be viewed or edited.
    """
    queryset = OnlineServer.objects.all() # pylint: disable=E1101
    serializer_class = ServerSerializer
#
#class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer