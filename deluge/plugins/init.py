#
# init.py
#
# Copyright (C) 2007 Andrew Resch <andrewresch@gmail.com>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA    02110-1301, USA.
#

"""
This base class is used in plugin's __init__ for the plugin entry points.
"""
from deluge.log import LOG as log

class PluginInitBase(object):
    _plugin_cls = None
    def __init__(self, plugin_name):
        self.plugin = self._plugin_cls(plugin_name)

    def enable(self):
        try:
            self.plugin.enable()
        except Exception, e:
            log.error("Unable to enable plugin!")
            log.exception(e)

    def disable(self):
        try:
            self.plugin.disable()
        except Exception, e:
            log.error("Unable to disable plugin!")
            log.exception(e)
