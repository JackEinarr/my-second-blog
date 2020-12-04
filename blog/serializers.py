from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    text = serializers.CharField()
    created_date = serializers.CharField()
    published_date = serializers.CharField()