from django.http import HttpResponse
from django.shortcuts import render
from .models import Film, Director


def index(request):
    num_films = Film.objects.all().count()
    num_directors = Director.objects.all().count()

    return render(

        request,
        'index.html',
        context={

            'num_films': num_films,
            'num_directors': num_directors,

        }

    )


def films_saved(request):
    all_films = Film.objects.all()
    html = ''
    for film in all_films:
        url = '/films/' + str(film.title) + '/'
        html += '<a href="' + url + '">' + film.title + '</a><br>'
    return HttpResponse(html)


