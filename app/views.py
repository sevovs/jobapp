from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader



# Create your views here.

def hello(request):
    template = loader.get_template('hello.html')
    context = {}
    return HttpResponse(template.render(context, request))

job_title = [
    "First Job",
    "Second Job",
    "Third Job",
    "Fourth Job",
]

job_description = [
    "First Job description",
    "Second Job description",
    "Third Job description",
    "Fourth Job description",
]

#def hello(request):
#    return HttpResponse("<h1>Hello Amigos!</h1>")

def job_list(request):
    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = (reverse('jobs_detail', args=(job_id,)))
        list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)


def job_1(request, id):
    try:
        if int(id) == 0:
            return redirect(reverse('jobs_home'))
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Item not found!")

