# -*- coding: utf-8 -*-

'''
    Faros On-Air Addon
    Author Twilight0

        License summary below, for more details please read license.txt file

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from xbmc import executebuiltin, translatePath, getInfoLabel
from xbmcvfs import exists

ID = 'plugin.video.faros.on-air'

if 'CEMC' in getInfoLabel('System.FriendlyName'):

    executebuiltin('RunAddon({0})'.format(ID))

    if exists(
            translatePath('special://home/addons/{0}/addon.xml'.format(ID))
    ) and exists(
        translatePath('special://profile/keymaps/farosonair.xml')
    ):

        with open(translatePath('special://profile/keymaps/farosonair.xml'), 'r') as f:
            keymap_file = f.read()

        if 'home' not in keymap_file:
            with open(translatePath('special://profile/keymaps/farosonair.xml'), 'w') as f:
                f.write(keymap_file.replace('xbmc', 'home'))
