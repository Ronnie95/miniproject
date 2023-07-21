from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Movie, Director
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
    
@method_decorator(login_required, name='dispatch')
class MovieList(TemplateView):
    template_name = "movie_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["movies"] = Movie.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["movies"] = Movie.objects.filter(user=self.request.user)
            context["header"] = "Trending Artists"
        return context

class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'img']
    template_name = "movie_create.html"
    success_url = "/movies/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MovieCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('movie_detail', kwargs={'pk': self.object.pk})


class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'img',]
    template_name = "movie_update.html"
    success_url = "/movies/"

class MovieDelete(DeleteView):
    model = Movie
    template_name = "movie_delete_confirmation.html"
    success_url = "/movies/"

class DirectorCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        age = request.POST.get("age")
        img = request.POST.get("img")
        movie = Movie.objects.get(pk=pk)
        Director.objects.create(name=name, age=age, img=img, movie=movie)
        return redirect('movie_detail', pk=pk)
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("Movies")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Movies:
    def __init__(self, title, image, director):
        self.title = title
        self.image = image
        self.director = director 



movie = [
    Movies("Malibus Most Wanted", "https://m.media-amazon.com/images/M/MV5BODM3NzE0NTMxOF5BMl5BanBnXkFtZTYwMTIzNTk5._V1_.jpg", "Fax Bahr"),
    Movies("Paid in Full", "https://upload.wikimedia.org/wikipedia/en/7/72/Paidinfullposter.jpg", "Charles Stone"),
    Movies("Four Brothers", "https://m.media-amazon.com/images/M/MV5BMTU4NzM3Njg2NV5BMl5BanBnXkFtZTcwNjU4NDczMw@@._V1_.jpg", "John Singleton"),
    Movies("Biker Boyz", "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQlJs3tshdsVcBFmB1wCTxwflFaU2JUTKLQnnGpz5RWQaOs4IM9", "Reggie Rock BytheWood" ),
    Movies("Baby Boy", "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQQAj4-kJ9RkZtNar8DUHkYWYpZ7B8dpsmqkRLeQo6xiT5mt95i", "John Singleton"),
    Movies("Rush Hour", "https://m.media-amazon.com/images/I/51XJkccUkOL._AC_UF894,1000_QL80_.jpg", "Brett Ratner"),
]