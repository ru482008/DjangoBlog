from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.


def index(request):
    article_records = Post.objects.all()
    article_list = list()
    for count, article in enumerate(article_records):
        article_list.append("#{}: {}<br><br>".format(str(count), str(article)))
        article_list.append("<small>{}</small><br>".format(article.content))
        article_list.append("{}<br><hr>".format(article.slug))
    return HttpResponse(article_list)


def about(request):
    return HttpResponse("HELLO")


from datetime import datetime


def index_use_template(requests):
    now = datetime.now()
    article_records = Post.objects.all()
    # list_data = ["1", "2", "3"]
    # dict_data = {'key':1,'key':1,}
    # return render(requests, "index.html", {'now':now})
    # return render(requests, "index.html", locals())
    return render(requests, "pages/home.html", locals())


def showPost(requests, slug):
    article = Post.objects.get(slug=slug)
    return render(requests, "pages/post.html", locals())


def login(requests):
    return render(requests, "pages/login.html")

from django.http import JsonResponse
def showArticleList(requests):
    article = Post.objects.all().values()
    article = list(article)
    return JsonResponse(article, safe=False)
