from webbelonger.serializers import BelongerSerializer
from models import Post


class PostSerializer(BelongerSerializer):
    class Meta:
        model = Post
