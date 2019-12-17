# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import validators
import datetime
import requests
# from django.utils import timezone

import pdfx
# Create your models here.


class PdfFile(models.Model):
    file = models.FileField(default='media/default_document.pdf',
                            upload_to='media', null=False, blank=False,
                            validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],
                                                                          message='Invalid file extension')],
                            error_messages={'blank': 'Blank pdf file field not allowed',
                                            'null': 'Null pdf file field not allowed'})
    file_name = models.CharField(max_length=200, null=True, blank=True)
    links_count = models.IntegerField(default=0, null=True, blank=True)
    is_url_found = models.BooleanField(default=False, blank=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return str(self.file_name) + ' ' + str(self.timestamp)

    def save(self, *args, **kwargs):
        super(PdfFile, self).save(*args, **kwargs)
        # print(self.file.url)
        pdf_file = pdfx.PDFx(self.file.path)
        l_count = pdf_file.get_references_count()
        if l_count > 0:
            PdfFile.objects.filter(id=self.id).update(links_count=l_count)
            PdfFile.objects.filter(id=self.id).update(is_url_found=True)
        links_in_dict = pdf_file.get_references_as_dict()
        for link in links_in_dict['url']:
            link_status = False
            try:
                response = requests.get(link.encode("utf-8"))
                if str(response) == '<Response [200]>':
                    link_status = True
            except:
                link_status = False
            u_link = UrlLink(link=link.encode("utf-8"), is_alive=link_status, document=self)
            u_link.save()


class UrlLink(models.Model):
    link = models.URLField(null=False, blank=False)
    is_alive = models.BooleanField(default=False, null=False, blank=False)
    document = models.ForeignKey(PdfFile, null=False, blank=False)
    timestamp = models.DateTimeField(default=datetime.datetime.now(), null=False, blank=False)

    def __str__(self):
        return str(self.link) + ' ' + str(self.timestamp)
