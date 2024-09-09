from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        'page_title': my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count()
    }
    print("path", request.path)
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title 
    }
    html_ = """
        <!DOCTYPE html>
        <html>
            <body>
                <h1>{page_title}</h1>
            </body>
        </html>

    """.format(**my_context)
    return HttpResponse(html_)
