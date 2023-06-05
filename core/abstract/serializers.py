from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.URLField(source='public_id', read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)