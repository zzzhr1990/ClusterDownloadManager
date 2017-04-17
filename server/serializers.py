from .models import OnlineServer
from rest_framework import serializers


class ServerSerializer(serializers.HyperlinkedModelSerializer):
    """ServerSerializer"""
    id = serializers.ReadOnlyField()
    class Meta:
        """Meta Data"""
        model = OnlineServer
        fields = ('id', 'server_type', 'server_uid', 'server_name', \
        'start_date', 'update_date', 'current_download', 'finish_count', \
        'error_count')
    def create(self, validated_data):
        """Try to find one"""
        server_uid = validated_data.get('server_uid')
        query = OnlineServer.objects.filter(server_uid=server_uid)# pylint: disable=E1101
        if query:
            return self.update(query[0], validated_data)
        else:
            return super(ServerSerializer, self).create(validated_data)
        #fields = ('url', 'username', 'email', 'groups')
