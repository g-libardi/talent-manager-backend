from rest_framework.serializers import Serializer, CharField


class ErrorNotAuthorizedSerializer(Serializer):
    detail = CharField()
