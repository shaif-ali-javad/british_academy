from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    movie_data={
        'movies' : [
        {
        'title':"The Shawshank Redemption",
        'year':'1994',
        'summery':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'success':True
    },
    {
        'title':"The Shawshank Redemption",
        'year':'1994',
        'summery':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'success':True
    },
    {
        'title':"The Shawshank Redemption",
        'year':'1994',
        'summery':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'success':True
    },
    {
        'title':"The Shawshank Redemption",
        'year':'1994',
        'summery':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'success':True
    },
    {
        'title':"The Shawshank Redemption",
        'year':'1994',
        'summery':'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
        'success':True
    },
    ]}
    return render(request,"index.html",movie_data)
