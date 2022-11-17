from rest_framework import serializers


class ConverterSerializer(serializers.Serializer):
    status = serializers.CharField()
    num_in_english = serializers.CharField()
