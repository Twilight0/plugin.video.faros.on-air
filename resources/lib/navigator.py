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

from base64 import b64decode
from tulip import control, directory, youtube, cache, cleantitle
from tulip.init import syshandle, sysaddon
from helpers import checkpoint, android_activity


class Indexer:

    def __init__(self):

        self.list = []; self.data = []
        self.main_youtube_id = 'UCfU04d4DbqpyotwfgxRS6EQ'
        self.main_playlist_id = 'UUfU04d4DbqpyotwfgxRS6EQ'
        self.yt_key = b64decode('QUl6YVN5QThrMU95TEdmMDNIQk5sMGJ5RDUxMWpyOWNGV28yR1I0')  # please do not copy this key
        self.live_url = 'http://master.cystreams.com:25461/live/faros/farostv/154.m3u8'

    def root(self):

        self.list = [
            {
                'title': control.lang(30001),
                'action': 'play',
                'isFolder': 'False',
                'url': self.live_url,
                'icon': 'live.jpg'
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
                'action': 'favourites',
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
                'title': control.lang(30012),
                'action': 'settings',
                'icon': 'settings.png',
            }
            ,
            {
                'title': control.lang(30018),
                'action': 'quit_kodi',
                'icon': 'quit.png',
            }
        ]

        for item in self.list:
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            refresh_cm = {'title': 30022, 'query': {'action': 'refresh'}}
            item.update({'cm': [cache_clear, refresh_cm]})

        control.set_view_mode('500')
        control.sleep(50)
        directory.add(self.list, content='videos')
        control.wait(1)
        checkpoint()

    def video_list(self):

        self.list = youtube.youtube(key=self.yt_key).videos(self.main_youtube_id)

        for item in self.list:
            item.update({'action': 'play', 'isFolder': 'False'})

        return self.list

    def yt_playlist(self, pid):

        self.list = youtube.youtube(key=self.yt_key).playlist(pid)

        for item in self.list:
            item.update({'action': 'play', 'isFolder': 'False'})

        return self.list

    def videos(self):

        self.list = cache.get(self.video_list, 3)

        if self.list is None:
            return

        for item in self.list:
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear]})

        if control.setting('force_view') == 'true':
            control.set_view_mode('50')
        directory.add(self.list)

    def playlist(self, url):

        self.list = cache.get(self.yt_playlist, 3, url)

        if self.list is None:
            return

        for item in self.list:
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear]})

        if control.setting('force_view') == 'true':
            control.set_view_mode('50')
        directory.add(self.list)

    def search(self):

        search_str = control.dialog.input(control.addonInfo('name'))
        search_str = cleantitle.strip_accents(search_str.decode('utf-8'))

        if not search_str:
            return

        self.list = self.video_list()
        self.list = [
            item for item in self.list if search_str.lower() in cleantitle.strip_accents(
                item['title'].decode('utf-8')
            ).lower()
        ]

        if not self.list:
            return

        for item in self.list:
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'action': 'play', 'isFolder': 'False', 'cm': [cache_clear]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        if control.setting('force_view') == 'true':
            control.set_view_mode('50')
        directory.add(self.list)

    def external_links(self):

        self.data = [
            {
                'title': control.lang(30030),
                'action': 'android_activity',
                'icon': control.addonInfo('icon'),
                'url': 'https://farosonair.com/'
            }
            ,
            {
                'title': control.lang(30028),
                'action': 'android_activity',
                'icon': 'facebook.png',
                'url': 'https://www.facebook.com/farosonair'
            }
            ,
            {
                'title': control.lang(30029),
                'action': 'android_activity',
                'icon': 'instagram.png',
                'url': 'https://www.instagram.com/farosonair16/'
            }
            ,
            {
                'title': control.lang(30026),
                'action': 'android_activity',
                'icon': 'twitter.png',
                'url': 'https://twitter.com/faros_on_air'
            }
            ,
            {
                'title': control.lang(30027),
                'action': 'android_activity',
                'icon': 'youtube_sub.png',
                'url': 'https://www.youtube.com/channel/UCfU04d4DbqpyotwfgxRS6EQ?sub_confirmation=1'
            }
        ]

        if control.setting('external_links') == 'false':

            links = [i['url'] for i in self.data]
            titles = [i['title'] for i in self.data]

            choice = control.selectDialog(titles)

            if choice >= 0:

                android_activity(links[choice])

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
