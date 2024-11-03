from rest_framework.viewsets import ModelViewSet
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = []
    authentication_classes = []
