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

"""Forms referenced by the views."""

from django import newforms as forms
from google.appengine.ext.db import djangoforms
import models
import validators


class PageEditForm(djangoforms.ModelForm):
  """Form used by editors to create or modify a page."""

  _text_attrs = dict(size=55, maxlength=80)
  title = forms.CharField(
      widget=forms.TextInput(attrs=_text_attrs))
  name = forms.CharField(
      widget=forms.TextInput(attrs=_text_attrs))

  def __init__(self, *args, **kwargs):
    # pylint: disable-msg=W0142
    super(PageEditForm, self).__init__(*args, **kwargs)
    self.fields.keyOrder = self.Meta.fields  #This line should be unnecessary

  class Meta(object):
    # pylint: disable-msg=R0903
    """Django instruction to link form to Page model."""
    fields = ['title', 'name']
    model = models.Page

  def clean_name(self):
    """Django validator to ensure the page name can be part of a URL."""
    name = self.clean_data['name']
    validators.is_valid_page_name(name)
    return name


class GroupEditForm(djangoforms.ModelForm):
  """Form used by editors to modify a user group."""

  class Meta(object):
    # pylint: disable-msg=R0903
    """Django instruction to link the form to UserGroup model."""
    model = models.UserGroup
    exclude = ['users']


class UserEditForm(djangoforms.ModelForm):
  """Form used by editors to modify a user profile."""

  #TODO(bogosian): when checkbox is empty the form POST is empty without this
  hidden_dummy = forms.Field(widget=forms.HiddenInput(attrs={'value': 'dummy'}))

  class Meta(object):
    # pylint: disable-msg=R0903
    """Django instruction to link the form to UserProfile model."""
    model = models.UserProfile
    exclude = ['email']
