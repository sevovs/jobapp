from django.urls import path

from app.views import job_1, job_list

# Create your patterns for the application.


urlpatterns = [
    #path("", hello),
    path("", job_list, name='jobs_home'),
    path("job/<int:id>", job_1, name='jobs_detail'),
]
