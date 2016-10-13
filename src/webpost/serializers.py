from models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    create_date = serializers.ReadOnlyField()
    author_id = serializers.ReadOnlyField()
    author_type = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ('author_type', 'author_id', 'text', 'create_date', 'num_comments', 'num_likes')
