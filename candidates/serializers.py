from .models import Candidate
from rest_framework.serializers import ModelSerializer


class CandidateSerializer(ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
