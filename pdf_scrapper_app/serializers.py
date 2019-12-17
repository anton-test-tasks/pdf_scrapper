from rest_framework import serializers
from . import models


class PdfFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PdfFile
        fields = ('url', 'id', 'file', 'file_name', 'links_count', 'is_url_found', 'timestamp')


class UrlLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UrlLink
        fields = ('url', 'id', 'link', 'is_alive', 'document', 'timestamp')
