from rest_framework import serializers

class DummyGenderRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)

class DummyGenderResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=7)


class DummyDetailSerializer(serializers.Serializer):
    detail = serializers.CharField(max_length=256)
    
