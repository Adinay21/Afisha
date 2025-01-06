from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialisers import MovieSerializer, DirectorSerializer, ReviewSerializer
from .models import Movie, Director, Review
from rest_framework import status



@api_view(['GET'])
def movie_detail_list_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    list_ = MovieSerializer(instance=movies, many=True).data
    return Response(data=list_)


@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()
    list_ = DirectorSerializer(instance=directors, many=True).data
    return Response(data=list_)

@api_view(http_method_names=['GET'])
def director_detail_list_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(instance=reviews, many=True).data
    return Response(data=list_)

@api_view(http_method_names=['GET'])
def review_detail_list_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)