from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pdf_file', views.PdfFileView)
router.register(r'url_link', views.UrlLinkView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get_all_links_and_count_doc/', views.GetAllLinksAndCountDocumentsView.as_view())
]
