from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ranking.views import UserViewSet, ScoreViewSet


router = routers.DefaultRouter()

# users/*にRankingUser系のAPIを追加
router.register(r'users', UserViewSet)
# scores/*にScore系のAPIを追加
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
