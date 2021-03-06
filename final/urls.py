from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from finalapp.api.resources import UserResource, EmployerResource, WorkerResource, CategoryResource, TagResource, \
    JobPostResource, JobResource, WorkerReviewResource, EmployerReviewResource

admin.autodiscover()

v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(EmployerResource())
v1_api.register(WorkerResource())
v1_api.register(CategoryResource())
v1_api.register(TagResource())
v1_api.register(JobPostResource())
v1_api.register(JobResource())
v1_api.register(WorkerReviewResource())
v1_api.register(EmployerReviewResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'finalapp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    # url('', include('social.apps.django_app.urls', namespace='social')),

    # url(r'^signup-email/', 'finalapp.views.signup_email'),
    # url(r'^email-sent/', 'finalapp.views.validation_sent'),
    # url(r'^login/$', 'finalapp.views.home'),
    # url(r'^logout/$', 'finalapp.views.logout'),
    # url(r'^done/$', 'finalapp.views.done', name='done'),
    # url(r'^email/$', 'finalapp.views.require_email', name='require_email'),
    # url(r'', include('social.apps.django_app.urls', namespace='social'))
)

