from django import template
from movie.models import Category, Movie
register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register_inclusion_tag('movie/tags/last_movie.html')
def get_last_movies():
    movies = Movie.objects.order_by("id")[:5]
    return {'last_movies': movies}
