from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from boilerplate.bases import mixins
from boilerplate.apps.posts.models import Post
from boilerplate.apps.posts.serializers import PostSerializer


# Main Section
class PostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Post.available.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_id="게시글 리스트 조회",
        responses={200: PostSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
