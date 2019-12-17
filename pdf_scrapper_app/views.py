# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import JsonResponse

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from . import serializers

# Create your views here.


class PdfFileView(viewsets.ModelViewSet):
    queryset = models.PdfFile.objects.all()
    serializer_class = serializers.PdfFileSerializer


class UrlLinkView(viewsets.ModelViewSet):
    model = models.UrlLink
    queryset = models.UrlLink.objects.all()
    serializer_class = serializers.UrlLinkSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ['document', ]


class GetAllLinksAndCountDocumentsView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, format=None):
        links = []
        all_links = models.UrlLink.objects.all()
        for i in all_links:
            links.append(str(i.link))
        documents_count = models.PdfFile.objects.all().filter(is_url_found=True).count()
        return JsonResponse({"Documents_count_that_contained_url": documents_count, "All_links": links}, safe=False)