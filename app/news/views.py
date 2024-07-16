from django.shortcuts import render
from news import models
from news.utils import get_news


# Create your views here.
def index(request):
    category = request.GET.get("category", None)
    query = request.GET.get("query", None)

    context = {
                "news": get_news(category, query),
        "categories": models.Categories.objects.all()
    }

    if not context["news"]:
        if not category and not query:
            context["message"] = "Наразі новин немає"

        else:
            if category and not query:
                context["message"] = "У цій категорії немає новин"

            else:
                context["message"] = "За цим запитом не знайдено результатів"

    return render(request, "main/index.html", context)

def new(request, new_slug: str):
    context = {"new": models.News.objects.get(slug=new_slug)}
    return render(request, "main/new.html", context)

def info(request):
    context = {"information": models.Information.objects.all()}
    return render(request, "main/info.html", context)
