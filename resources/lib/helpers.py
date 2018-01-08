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
from tulip.client import parseDOM


def get_weather_bool():

    try:

        guisettings_xml = control.transPath('special://profile/guisettings.xml')
        with open(guisettings_xml) as f: gui_xml = f.read()
        addon_used = parseDOM(gui_xml, 'addon')[0]
        addon_bool = True if addon_used == 'weather.yahoo' else False
    
        yahoo_settings_xml = control.transPath('special://profile/addon_data/weather.yahoo/settings.xml')
        with open(yahoo_settings_xml) as f: yahoo_xml = f.read()
        city = parseDOM(yahoo_xml, 'setting', attrs={'id': 'Location1'})[0]
        city_bool = True if 'Paphos' in city else False

        return addon_bool, city_bool

    except:

        bools = False, False
        return bools


def quit_kodi():

    control.execute('Quit')


def set_a_setting(setting, value):

    json_cmd = {
        "jsonrpc": "2.0", "method": "Settings.SetSettingValue", "params": {"setting": setting, "value": value}, "id": 1
    }

    control.json_rpc(json_cmd)


def lang_choice():

    def set_other_options():

        set_a_setting('locale.longdateformat', 'regional')
        set_a_setting('locale.shortdateformat', 'regional')
        set_a_setting('locale.speedunit', 'regional')
        set_a_setting('locale.temperatureunit', 'regional')
        set_a_setting('locale.timeformat', 'regional')
        # set_a_setting('locale.timezone', 'default')
        # set_a_setting('locale.timezonecountry', 'default')
        set_a_setting('locale.use24hourclock', 'regional')

    selections = [control.lang(30020), control.lang(30021)]

    dialog = control.selectDialog(selections)

    if dialog == 0:
        set_a_setting('locale.language', 'resource.language.en_gb')
        set_other_options()
    elif dialog == 1:
        set_a_setting('locale.language', 'resource.language.el_gr')
        set_other_options()
    else:
        control.execute('Dialog.Close(all)')

    control.sleep(100)
    refresh()


def weather_set_up():

    addon_settings = '''<settings>
    <setting id="Location1" value="Paphos (CY)" />
    <setting id="Location1id" value="841589" />
    <setting id="Location2" value="" />
    <setting id="Location2id" value="" />
    <setting id="Location3" value="" />
    <setting id="Location3id" value="" />
    <setting id="Location4" value="" />
    <setting id="Location4id" value="" />
    <setting id="Location5" value="" />
    <setting id="Location5id" value="" />
</settings>
'''

    location = control.transPath('special://profile/addon_data/weather.yahoo')
    if not control.exists(location):
        control.makeFile(location)

    with open(control.join(location, 'settings.xml'), mode='w') as f:
        f.write(addon_settings)

    set_a_setting('weather.addon', 'weather.yahoo')
    control.execute('Weather.Refresh')


def key_map_setup():

    if control.exists(control.transPath('special://home/addons/plugin.video.faros.on-air.standalone/addon.xml')):
        script_location = 'special://home/addons/plugin.video.faros.on-air.standalone/resources/lib/key_nav.py'
    else:
        script_location = 'special://xbmc/addons/plugin.video.faros.on-air.standalone/resources/lib/key_nav.py'

    xml = '''<keymap>
    <global>
        <keyboard>
            <key id="browser_back">RunScript({0})</key>
            <key id="61448">RunScript({0})</key>
            <key id="backspace">RunScript({0})</key>
            <key id="browser_home">noop</key>
            <key id="homepage">noop</key>
            <key id="escape">noop</key>
            <key id="61467">noop</key>
        </keyboard>
    </global>
</keymap> 
    '''.format(script_location)

    location = control.transPath('special://profile/keymaps/')

    if not control.exists(location):
        control.makeFile(location)

    with open(control.join(location, 'farosonair.xml'), mode='w') as f:
        f.write(xml)

    control.execute('Action(reloadkeymaps)')


def youtube_set_up():

    _id_ = '498788153161-pe356urhr0uu2m98od6f72k0vvcdsij0.apps.googleusercontent.com'
    key = 'AIzaSyA8k1OyLGf03HBNl0byD511jr9cFWo2GR4'
    secret = 'e6RBIFCVh1Fm-IX87PVJjgUu'

    control.addon('plugin.video.youtube').setSetting('youtube.api.enable', 'true')
    control.addon('plugin.video.youtube').setSetting('youtube.api.id', _id_)
    control.addon('plugin.video.youtube').setSetting('youtube.api.key', key)
    control.addon('plugin.video.youtube').setSetting('youtube.api.secret', secret)
    control.addon('plugin.video.youtube').setSetting('kodion.setup_wizard', 'false')
    control.addon('plugin.video.youtube').setSetting('youtube.language', 'el')
    control.addon('plugin.video.youtube').setSetting('youtube.region', 'GR')


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

    if control.setting('first_time') == 'true' and 'CEMC' in control.infoLabel('System.FriendlyName'):

        control.setSetting('first_time', 'false')
        set_a_setting('locale.keyboardlayouts', ['English QWERTY', 'Greek QWERTY'])
        weather_set_up()
        youtube_set_up()
        key_map_setup()
        lang_choice()
        control.okDialog(heading=control.addonInfo('name'), line1=control.lang(30024))

    else:

        pass


def android_activity(url):

    if control.setting('browser') == 'Opera Mobile':
        browser = 'com.opera.browser'
    elif control.setting('browser') == 'Opera Mini':
        browser = 'com.opera.mini.native'
    elif control.setting('browser') == 'Firefox':
        browser = 'org.mozilla.firefox'
    elif control.setting('browser') == 'UC Browser':
        browser = 'com.UCMobile.intl'
    else:
        browser = 'com.android.chrome'

    control.execute('StartAndroidActivity("{0}","android.intent.action.VIEW","","{1}")'.format(browser, url))
