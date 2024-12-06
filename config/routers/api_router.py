from rest_framework import routers
from boilerplate.apps.posts.views import PostViewSet

# Base Router
router = routers.SimpleRouter(trailing_slash=False)

# Register URL
router.register("posts", PostViewSet)

# 최종적으로 'api/v1/' 경로에 등록
app_name = "api"

urlpatterns = router.urls
