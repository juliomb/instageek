from rest_framework.routers import SimpleRouter

from followers.views import FollowViewSet

router = SimpleRouter()
router.register(r'follow', FollowViewSet)

urlpatterns = router.urls
