from .models import OnlineServer
from rest_framework import viewsets
from .serializers import ServerSerializer


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = User.objects.all().order_by('-date_joined')
    #queryset = User.objects.all().order_by('-date_joined')
    queryset = OnlineServer.objects.all() # pylint: disable=E1101
    serializer_class = ServerSerializer
#
#class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer