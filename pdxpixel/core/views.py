"""
file        :   views.py
date        :   2016-0330
module      :   common.views
classes     :
description :   views used by entire site, eg, error pages
"""

from django.shortcuts import render_to_response
from django.template import RequestContext


def custom_bad_request(request):

    response = render_to_response('error/400.html', context_instance=RequestContext(request))

    response.status_code = 400

    return response


def custom_permission_denied(request):

    response = render_to_response('error/403.html', context_instance=RequestContext(request))

    response.status_code = 403

    return response


def custom_page_not_found(request):

    response = render_to_response('error/404.html', context_instance=RequestContext(request))

    response.status_code = 404

    return response


def custom_server_error(request):

    response = render_to_response('error/500.html', context_instance=RequestContext(request))

    response.status_code = 500

    return response


def custom_bad_gateway(request):

    response = render_to_response('error/502.html', context_instance=RequestContext(request))

    response.status_code = 502

    return response
