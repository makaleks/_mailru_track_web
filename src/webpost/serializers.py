from models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author_object = serializers.ReadOnlyField(source='author_object.id')
    class Meta:
        model = Post
        #fields = ('author_object', 'text', 'feed')
