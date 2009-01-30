#!/usr/bin/python2.5
#
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Middleware classes for Django."""

import logging

from django import http
from google.appengine.api import users

import models
import utility


class AddUserToRequestMiddleware(object):
  # pylint: disable-msg=R0903
  """Adds a user data to each request.

  Add a user object, a profile object, and a user_is_admin flag to each
  request.  If the user is not logged in, redirect them.

  """

  def process_request(self, request):
    # pylint: disable-msg=R0201
    """Method defined by Django to handle processing requests.

    Args:
      request: the http request to process

    Returns:
      None
    """
    user = users.GetCurrentUser()
    #if not user:
      #return http.HttpResponseRedirect(users.create_login_url(request.path))
    if user:
        request.user = user
        request.user_is_admin = users.is_current_user_admin()
        profile = models.UserProfile.load(user.email())
        if not profile:
          if request.user_is_admin:
            profile = models.UserProfile(email=user.email(), is_superuser=True)
            profile.put()
            logging.info('Created profile for admin %s' % profile.email)
          #else:
            #return utility.forbidden(request)
        request.profile = profile
    else:
        request.profile = None
        request.user = None
    return None
