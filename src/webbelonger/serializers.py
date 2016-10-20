from rest_framework import serializers
from models import Belonger
from webuser.serializers import WebuserSerializer


class BelongerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.id")
    #owner = WebuserSerializer()
    #owner = serializers.ModelField(read_only = True)
    create_date =  serializers.ReadOnlyField()
    edit_date =  serializers.ReadOnlyField()
    class Meta:
        model = Belonger
        #fields = ('owner', 'create_date', 'edit_date')
        #read_only_fields = ('owner')
