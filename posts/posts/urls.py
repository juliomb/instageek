from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet

router = SimpleRouter()
router.register(r'post', PostViewSet)

urlpatterns = router.urls
