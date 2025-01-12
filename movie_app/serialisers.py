from rest_framework import serializers
from movie_app.models import Movie, Director, Review
from django.db.models import Avg




class MovieItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class DirectorItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class ReviewItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = 'id title description duration director reviews average_rating'.split()

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg=Avg('stars'))['avg']
        return avg if avg is not None else 0


class DirectorSerializer(serializers.ModelSerializer):
    # movie_count = MovieSerializer(many=True)
    class Meta:
        model = Director
        fields = 'id name movie_count'.split()


