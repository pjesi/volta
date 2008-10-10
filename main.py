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

"""Bootstrap for running a Django app under Google App Engine.

The site-specific code is all in other files: settings.py, urls.py,
models.py, views.py.  And in fact, only 'settings' is referenced here
directly -- everything else is controlled from there.

"""

import os
from django.conf import settings
from django.core.handlers import wsgi
from google.appengine.ext.webapp import util

settings._target = None
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.signals
import django.db
import django.dispatch.dispatcher

# Unregister the rollback event handler.
django.dispatch.dispatcher.disconnect(
    django.db._rollback_on_exception,  # pylint: disable-msg=W0212
    django.core.signals.got_request_exception)

def main():
  """Loads the django application."""
  application = wsgi.WSGIHandler()
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()
