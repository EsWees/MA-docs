from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request, name="No any name defined"):
    return render(request, "blog/base.html", context={"name": name})


def posts(request):
    pq = Post.objects.all().order_by('-publish')
    return render(request, "blog/page.html", context={"posts": pq})


def create(request):
    if request.method == 'POST':
        p = Post.objects.create(title=request.POST['title'],
                                slug=request.POST['slug'],
                                body=request.POST['body'])
        return render(request, "blog/info.html", context={"post": p})
    return render(request, "blog/create.html")


def info(request):
    if request.method == 'POST':
        p = ""
        search = request.POST['search']
        if Post.objects.filter(slug__contains=search):
            p = Post.objects.filter(slug__contains=search)
        elif Post.objects.filter(title__contains=search):
            p = Post.objects.filter(title__contains=search)
        elif Post.objects.filter(body__contains=search):
            p = Post.objects.filter(body__contains=search)

        if p[0].id:
            return render(request, "blog/info.html", context={"post": p})

    if request.method == 'GET':
        return render(request, "blog/search.html")

    return render(request, "blog/404.html", status=404)


def delete(request, slug=None):
    if request.method == 'POST' and slug:
        p = Post.objects.delete(slug=slug)
        return True # REDIRECT to /
    return render(request, "blog/")