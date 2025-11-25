from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate
        
        return None
    
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1900.')
        return value   