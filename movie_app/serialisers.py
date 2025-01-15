from rest_framework import serializers
from movie_app.models import Movie, Director, Review
from django.db.models import Avg
from rest_framework.exceptions import ValidationError




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


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=1)
    description = serializers.CharField(max_length=200, required=False, default="Great movie!!")
    duration = serializers.IntegerField(required=False, min_value=10, default=120)
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except:
            raise serializers.ValidationError("Director does not exist")
        return director_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, min_length=5)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=200, min_length=10)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1)