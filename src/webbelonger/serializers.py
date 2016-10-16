from rest_framework import serializers
from models import Belonger


class BelongerSerializer(serializers.HyperlinkedModelSerializer):
    pass
    '''owner = serializers.ReadOnlyField()
    create_date =  serializers.ReadOnlyField()
    edit_date =  serializers.ReadOnlyField()'''
