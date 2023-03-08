from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader



# Create your views here.

class TempClass:
    x = 5



def hello(request):
    temp = TempClass()
    lst = ['alpha', 'beta']
    h = 'George'
    is_athenticated = False
    context = {'name': 'Django', 'age': 10, 'first_list': lst, 'temp_object': temp, 'user': h
               , "is_athenticated": is_athenticated}
    return render(request, 'app/hello.html', context)

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
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3"
        # return HttpResponse(return_html)
        context = {'job_title': job_title[id], 'job_description': job_description[id]}
        return render(request, 'app/job_1.html', context)
    except:
        return HttpResponseNotFound("Item not found!")

