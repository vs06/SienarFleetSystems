#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
   url(r'^compare/', login_required(views.ShipsList.as_view()), name='compare'),
]