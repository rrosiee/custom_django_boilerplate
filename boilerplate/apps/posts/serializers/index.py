from rest_framework import serializers

from boilerplate.apps.posts.models import Post


# Main Section
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
