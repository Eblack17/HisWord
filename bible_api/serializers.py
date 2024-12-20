from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField(required=True)

class GuidanceResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField()
    guidance = serializers.CharField()
    scenario = serializers.CharField()
    analysis = serializers.CharField()
