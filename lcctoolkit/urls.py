import lcctoolkit.views as project_views
import lcctoolkit.mainapp.views as views

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings


rest_framework_urls = [
    url(r'question-category/(?P<category_pk>\d+)/$',
        views.QuestionViewSet.as_view()),
    url(r'classification/$', views.ClassificationViewSet.as_view()),
    url(r'answers/$', views.AnswerList.as_view(), name='answers_list_create'),
    url(r'answers/(?P<pk>[0-9]+)/$', views.AnswerDetail.as_view(), name='answers_get_update')
]

OTHER_URLS = (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

handler500 = 'lcctoolkit.views.handler500'

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login.as_view()),
    url(r'^logout/', views.Logout.as_view()),

    url(r'^crashme$', project_views.crashme, name='crashme'),

    url(r'^legislation/add/$', views.LegislationAdd.as_view()),
    url(r'^legislation/edit/.*$', views.LegislationEditView.as_view()),
    url(r'^legislation/add/articles.*$',
        views.AddArticles.as_view(), name="add_articles"),
    url(r'^legislation/$', views.LegislationExplorer.as_view(), name="legislation"),
    url(r'^legislation/(?P<legislation_pk>\d+)$',
        views.LegislationView.as_view(), name="legislation_details"),
    url(r'^legislation/pages.*$', views.LegislationPagesView.as_view()),
    url(r'^legislation/articles/edit.*$', views.EditArticles.as_view()),
    url(r'^legislation/articles.*$', views.ArticlesList.as_view()),
    url(r'^$', views.Index.as_view()),
    url(r'^api/', include(rest_framework_urls, namespace='api')),
] + OTHER_URLS
