# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment(object):


    # cisco iosxr documentation fragment
    DOCUMENTATION = r'''
options:
  comment:
    description:
    - Allows a commit description to be specified to be included when the configuration
      is committed.  If the configuration is not changed or committed, this argument
      is ignored.
    type: str
    default: configured by iosxr_config
  label:
    description:
    - Allows a commit label to be specified to be included when the configuration
      is committed. A valid label must begin with an alphabet and not exceed 30 characters,
      only alphabets, digits, hyphens and underscores are allowed. If the configuration
      is not changed or committed, this argument is ignored.
    type: str
  exclusive:
    description:
    - Enters into exclusive configuration mode that locks out all users from committing
      configuration changes until the exclusive session ends.
    type: bool
    default: false
  disable_default_comment:
    description:
    - disable default comment when set to True.
    type: bool
    default: false
  disable_default_prompts:
    description:
    - disable default prompts and answers when set to True.
    type: bool
    default: false
'''
