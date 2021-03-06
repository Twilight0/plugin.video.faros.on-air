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

import json
from base64 import b64decode
from zlib import decompress
from tulip import control, directory, cache, cleantitle, bookmarks, youtube
from tulip.init import syshandle, sysaddon
from tulip.compat import iteritems, py3_dec
from resources.lib.helpers import checkpoint, get_weather_bool

method_cache = cache.FunctionCache().cache_method

class Indexer:

    def __init__(self):

        self.list = []; self.data = []
        self.main_youtube_id = 'UCfU04d4DbqpyotwfgxRS6EQ'
        self.main_playlist_id = 'UUfU04d4DbqpyotwfgxRS6EQ'
        self.scramble = (
            'eJwVy80KgjAAAOBXkZ1TdCrTbmIhogVhYHUR24Yzl1ubP1n07uH9+75AU6zoALYGaNLkUJ6YyXEWeTebDZdsHqGHwcYAtWyrji4ri9JPXS'
            'yxSooS7eTcPsg9z0O2XI/v86vak1HESPBgXS1ZA7Rtzw2RGyAfmRPjyPFdSBWRsCGOpoSzafJF1wVKt8SqpdRWI0TD6aipwqIfaD9YWDzB'
            '7w/HIjj4'
        )
        self.live_url = 'https://s1.cystream.net/live/faros1/playlist.m3u8'
        self.live_url_2 = 'https://s1.cystream.net/live/faros2/playlist.m3u8'
        self.radio_url = 'http://176.31.183.51:8300'
        self.key = json.loads(decompress(py3_dec(b64decode(self.scramble))))['api_key']

    def root(self):

        self.list = [
            {
                'title': control.lang(30001),
                'action': 'live',
                'icon': 'live.jpg'
            }
            ,
            {
                'title': control.lang(30036),
                'action': 'play',
                'isFolder': 'False',
                'url': self.radio_url,
                'icon': 'radio.png',
                'fanart': control.join(control.addonPath, 'resources', 'media', 'bgradio.jpg')
            }
            ,
            {
                'title': control.lang(30002),
                'action': 'videos',
                'icon': 'youtube.png'
            }
            ,
            {
                'title': control.lang(30003),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdtUFNDIHozh_EpVSUYwCVuI',
                'icon': 'newspapers.png'
            }
            ,
            {
                'title': control.lang(30004),
                'action': 'playlist',
                'url': 'PL0cttCfQzkduInQQt3nCEKYValRROk1AV',
                'icon': 'users.png'
            }
            ,
            {
                'title': control.lang(30005),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdskGTTd3pLvUVKmlK8UyK3J',
                'icon': 'diet.png'
            }
            ,
            {
                'title': control.lang(30006),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdve608IsDG2jHqQ2AwAB4rm',
                'icon': 'sports.png'
            }
            ,
            {
                'title': control.lang(30007),
                'action': 'playlist',
                'url': 'PL0cttCfQzkduVZzwQZyAXOgkL_2CRCBlC',
                'icon': 'culture.png'
            }
            ,
            {
                'title': control.lang(30008),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdsgy5MDvGyl_Qsw7bKKq7V9',
                'icon': 'events.png'
            }
            ,
            {
                'title': control.lang(30009),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdvjJGEFQsNvQSOXaFA6jFde',
                'icon': 'world.png'
            }
            ,
            {
                'title': control.lang(30010),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdtnlBmYgZM75dVPbN3V6YsP',
                'icon': 'doctor.png'
            }
            ,
            {
                'title': control.lang(30013),
                'action': 'favourites' if 'CEMC' in control.infoLabel('System.FriendlyName') else 'bookmarks',
                'icon': 'favourites.png'
            }
            ,
            {
                'title': control.lang(30017),
                'action': 'search',
                'icon': 'search.png'
            }
            ,
            {
                'title': control.lang(30025),
                'action': 'weather',
                'icon': 'weather.png'
            }
            ,
            {
                'title': control.lang(30032),
                'action': 'external_links',
                'icon': 'external.png'
            }
            ,
            {
                'title': control.lang(30037),
                'action': 'presentation',
                'icon': control.addonInfo('icon'),
                'isFolder': 'False', 'isPlayable': 'False'
            }
            ,
            {
                'title': control.lang(30012),
                'action': 'settings',
                'icon': 'settings.png',
                'isFolder': 'False', 'isPlayable': 'False'
            }
            ,
            {
                'title': control.lang(30018),
                'action': 'quit_kodi',
                'icon': 'quit.png',
                'isFolder': 'False', 'isPlayable': 'False'
            }
        ]

        if control.setting('show_exit_button') == 'false':
            self.list = [d for d in self.list if d.get('action') != 'quit_kodi']

        if not get_weather_bool()[0] and not get_weather_bool()[1]:
            self.list = [d for d in self.list if d.get('action') != 'weather']

        for item in self.list:

            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            refresh_cm = {'title': 30022, 'query': {'action': 'refresh'}}
            item.update({'cm': [cache_clear, refresh_cm]})

        control.set_view_mode('500')
        control.sleep(50)
        directory.add(self.list, content='videos')
        control.wait(1)
        checkpoint()

    def live(self):

        self.list = [
            {
                'title': control.lang(30039),
                'action': 'play',
                'isFolder': 'False',
                'url': self.live_url,
                'icon': 'live.jpg'
            }
            ,
            {
                'title': control.lang(30040),
                'action': 'play',
                'isFolder': 'False',
                'url': self.live_url_2,
                'icon': 'live.jpg'
            }
        ]

        directory.add(self.list)

    def bookmarks(self):

        self.list = bookmarks.get()

        if not self.list:
            na = [{'title': 30016, 'action': None, 'icon': 'open-box.png'}]
            directory.add(na)
            return

        for item in self.list:
            bookmark = dict((k, v) for k, v in iteritems(item) if not k == 'next')
            bookmark['delbookmark'] = item['url']
            item.update({'cm': [{'title': 30014, 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    @method_cache(30)
    def yt_videos(self):

        return youtube.youtube(key=self.key).videos(self.main_youtube_id, limit=10)

    @method_cache(60)
    def yt_playlist(self, pid):

        self.list = youtube.youtube(key=self.key).playlist(pid, limit=10)

        for item in self.list:
            item.update({'action': 'play', 'isFolder': 'False'})

        return self.list

    def video_list(self):

        self.list = self.yt_videos()

        if not self.list:
            return

        for item in self.list:
            item.update({'action': 'play', 'isFolder': 'False', 'title': cleantitle.replaceHTMLCodes(item['title'])})

        return self.list

    def videos(self):

        self.list = self.video_list()

        if self.list is None:
            return

        for item in self.list:
            item['title'] = cleantitle.replaceHTMLCodes(item['title'])
            bookmark = dict((k, v) for k, v in iteritems(item) if not k == 'next')
            bookmark['bookmark'] = item['url']
            bm_cm = {'title': 30011, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear, bm_cm]})

        directory.add(self.list)

    def playlist(self, url):

        self.list = self.yt_playlist(url)

        if self.list is None:
            return

        for item in self.list:
            item['title'] = cleantitle.replaceHTMLCodes(item['title'])
            bookmark = dict((k, v) for k, v in iteritems(item) if not k == 'next')
            bookmark['bookmark'] = item['url']
            bm_cm = {'title': 30011, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear, bm_cm]})

        directory.add(self.list)

    def search(self):

        search_str = control.dialog.input(control.addonInfo('name'))
        search_str = cleantitle.strip_accents(search_str.decode('utf-8'))

        if not search_str:
            return

        self.list = self.video_list()
        try:
            self.list = [
                item for item in self.list if search_str.lower() in cleantitle.strip_accents(
                    item['title'].decode('utf-8')
                ).lower()
            ]
        except Exception:
            self.list = [
                item for item in self.list if search_str.lower() in cleantitle.strip_accents(
                    item['title']
                ).lower()
            ]

        if not self.list:
            return

        for item in self.list:
            item['title'] = cleantitle.replaceHTMLCodes(item['title'])
            bookmark = dict((k, v) for k, v in iteritems(item) if not k == 'next')
            bookmark['bookmark'] = item['url']
            bm_cm = {'title': 30011, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear, bm_cm]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        if control.setting('force_view') == 'true':
            control.set_view_mode('50')
        directory.add(self.list)

    def external_links(self):

        self.data = [
            {
                'title': control.lang(30030),
                'icon': control.addonInfo('icon'),
                'url': 'https://farosonair.com/'
            }
            ,
            {
                'title': control.lang(30031),
                'icon': control.addonInfo('icon'),
                'url': 'https://farosonair.com/category/farosnews/'
            }
            ,
            {
                'title': control.lang(30028),
                'icon': 'facebook.png',
                'url': 'https://www.facebook.com/farosonair'
            }
            ,
            {
                'title': control.lang(30029),
                'icon': 'instagram.png',
                'url': 'https://www.instagram.com/farosonair16/'
            }
            ,
            {
                'title': control.lang(30026),
                'icon': 'twitter.png',
                'url': 'https://twitter.com/faros_on_air'
            }
            ,
            {
                'title': control.lang(30027),
                'icon': 'youtube_sub.png',
                'url': 'https://www.youtube.com/channel/UCfU04d4DbqpyotwfgxRS6EQ?sub_confirmation=1'
            }
        ]

        for i in self.data:
            i.update({'action': 'open_website'})

        if control.setting('external_action') == 'false':

            links = [i['url'] for i in self.data]
            titles = [i['title'] for i in self.data]

            choice = control.selectDialog(titles)

            if choice >= 0:
                if control.condVisibility('System.Platform.Android'):
                    from resources.lib.helpers import android_activity
                    android_activity(links[choice])
                else:
                    import webbrowser
                    webbrowser.open(links[choice])

            else:

                pass

        else:

            for i in self.data:

                if i['icon'] != control.addonInfo('icon'):
                    image = control.join(control.addonPath, 'resources', 'media', i['icon'])
                else:
                    image = control.addonInfo('icon')

                li = control.item(label=i['title'])
                li.setArt({'poster': image, 'thumb': image, 'fanart': control.addonInfo('fanart')})
                li.setInfo('video', {'title': i['title']})
                url = '{0}?action={1}&url={2}'.format(sysaddon, i['action'], i['url'])
                self.list.append((url, li, False))

            control.addItems(syshandle, self.list)
            control.directory(syshandle)
