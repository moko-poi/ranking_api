from rest_framework import viewsets
from ranking.models import Score, RankingUser
from ranking.serializers import UserSerializer, ScoreSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for users"""
    queryset = RankingUser.objects.all()
    serializer_class = UserSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    """API endpoint for users"""
    queryset = Score.objects.select_related('user').order_by('-score')
    serializer_class = ScoreSerializer
