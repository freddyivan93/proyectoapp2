from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from escuela import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    url(r'^snippets/$', views.MateriaList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.MateriaDetail.as_view()),
    url(r'^snippets/profesor/$', views.ProfesorList.as_view()),
    url(r'^snippets/profesor/(?P<pk>[0-9]+)/$', views.ProfesorDetail.as_view()),
   

]

urlpatterns = format_suffix_patterns(urlpatterns)
