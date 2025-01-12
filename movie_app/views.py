from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialisers import (MovieSerializer, DirectorSerializer, ReviewSerializer,
                          MovieItemSerializer, DirectorItemSerializer, ReviewItemSerializer)
from .models import Movie, Director, Review
from rest_framework import status



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_list_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie).data
        return Response(data=data)
    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieItemSerializer(movie).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        list_ = MovieSerializer(instance=movies, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data=MovieItemSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        list_ = DirectorSerializer(instance=directors, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def director_detail_list_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(director).data
        return Response(data=data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorItemSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        list_ = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=list_)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')

        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(data=ReviewItemSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def review_detail_list_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewItemSerializer(review).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)