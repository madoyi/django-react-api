from django.urls import path
from django.views.generic import TemplateDetailView

app_name = 'blog'

urlpatterns =[
    path('', TemplateView.as_view(template_name="blog/index.html")),
]