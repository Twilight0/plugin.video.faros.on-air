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

from tulip import control, cache


def quit_kodi():

    control.execute('Quit')


def lang_choice():

    english = '{"jsonrpc":"2.0", "method": "Settings.SetSettingValue", "params": {"setting": "locale.language", "value": "resource.language.en_gb"}, "id": 1}'
    greek = '{"jsonrpc":"2.0", "method": "Settings.SetSettingValue", "params": {"setting": "locale.language", "value": "resource.language.el_gr"}, "id": 1}'

    selections = [control.lang(30020), control.lang(30021)]

    dialog = control.selectDialog(selections)

    if dialog == 0:
        control.jsonrpc(english)
    elif dialog == 1:
        control.jsonrpc(greek)
    else:
        control.execute('Dialog.Close(all)')


def refresh():

    control.execute('Container.Refresh')


def cache_clear():

    cache.clear(withyes=False)
    control.infoDialog(control.lang(30402))


def weather():

    control.execute('ActivateWindow(weather,return)')


def check_updates():

    control.execute('UpdateAddonRepos')
    control.okDialog(heading=control.addonInfo('name'), line1=control.lang(30402))


def checkpoint():

    if control.setting('first_time') == 'true':
        control.okDialog(heading=control.addonInfo('name'), line1=control.lang(30024))
        control.setSetting('first_time', 'false')
    else:
        pass
