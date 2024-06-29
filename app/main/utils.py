"""Утиліти"""


from django.contrib.postgres.search import SearchVector, SearchHeadline
from main.models import News


def get_news(category_slug: str = None, query: str = None):
    """Повертає список новин за обраною категорією та запросом"""
    result = News.objects.all()

    if category_slug:
        result = result.filter(category__slug=category_slug)

    if query:
        result = result.annotate(search=SearchVector("title", "text")).filter(search=query)
        result = result.annotate(
            titleline=SearchHeadline(
                "title",
                query,
                start_sel="<span style=\"color: rgb(255, 255, 0)\">",
                stop_sel="</span>"
            )
        )
        result = result.annotate(
            textline=SearchHeadline(
                "text",
                query,
                start_sel="<b><span style=\"color: rgb(255, 255, 0)\">",
                stop_sel="</span></b>"
            )
        )

    return result
