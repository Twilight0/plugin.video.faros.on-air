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
from tulip import control, directory, youtube, cache, bookmarks, cleantitle


class Main:

    def __init__(self):

        self.list = []; self.data = []
        self.live_url = 'http://master.cystreams.com:25461/live/faros/farostv/154.m3u8'
        self.main_youtube_id = 'UCfU04d4DbqpyotwfgxRS6EQ'
        self.main_playlist_id = 'UUfU04d4DbqpyotwfgxRS6EQ'
        self.yt_key = b64decode('QUl6YVN5QThrMU95TEdmMDNIQk5sMGJ5RDUxMWpyOWNGV28yR1I0')  # please do not copy this key

    def root(self):

        self.list = [
            {
                'title': control.lang(30001),
                'action': 'play',
                'url': self.live_url,
                'icon': 'live.jpg',
                'isFolder': 'False',
            }
            ,
            {
                'title': control.lang(30002),
                'action': 'videos',
                'icon': 'youtube.png',
            }
            ,
            {
                'title': control.lang(30003),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdtUFNDIHozh_EpVSUYwCVuI',
                'icon': 'newspapers.png',
            }
            ,
            {
                'title': control.lang(30004),
                'action': 'playlist',
                'url': 'PL0cttCfQzkduInQQt3nCEKYValRROk1AV',
                'icon': 'users.png',
            }
            ,
            {
                'title': control.lang(30005),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdskGTTd3pLvUVKmlK8UyK3J',
                'icon': 'diet.png',
            }
            ,
            {
                'title': control.lang(30006),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdve608IsDG2jHqQ2AwAB4rm',
                'icon': 'sports.png',
            }
            ,
            {
                'title': control.lang(30007),
                'action': 'playlist',
                'url': 'PL0cttCfQzkduVZzwQZyAXOgkL_2CRCBlC',
                'icon': 'culture.png',
            }
            ,
            {
                'title': control.lang(30008),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdsgy5MDvGyl_Qsw7bKKq7V9',
                'icon': 'events.png',
            }
            ,
            {
                'title': control.lang(30009),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdvjJGEFQsNvQSOXaFA6jFde',
                'icon': 'world.png',
            }
            ,
            {
                'title': control.lang(30010),
                'action': 'playlist',
                'url': 'PL0cttCfQzkdtnlBmYgZM75dVPbN3V6YsP',
                'icon': 'doctor.png',
            }
            ,
            {
                'title': control.lang(30013),
                'action': 'bookmarks',
                'icon': 'bookmarks.png',
            }
            ,
            {
                'title': control.lang(30017),
                'action': 'search',
                'icon': 'search.png',
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

        directory.add(self.list)

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
            bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
            bookmark['bookmark'] = item['url']
            bm_cm = {'title': 30011, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear, bm_cm]})

        directory.add(self.list)

    def playlist(self, url):

        self.list = cache.get(self.yt_playlist, 3, url)

        if self.list is None:
            return

        for item in self.list:
            bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
            bookmark['bookmark'] = item['url']
            bm_cm = {'title': 30011, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear, bm_cm]})

        directory.add(self.list)

    def bookmarks(self):

        self.list = bookmarks.get()

        if not self.list:
            na = [{'title': 30016, 'action': None, 'icon': 'open-box.png'}]
            directory.add(na)
            return

        for item in self.list:
            bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
            bookmark['delbookmark'] = item['url']
            item.update({'cm': [{'title': 30014, 'query': {'action': 'deleteBookmark', 'url': json.dumps(bookmark)}}]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)

    def search(self):

        search_str = control.dialog.input(control.addonInfo('name'))
        search_str = cleantitle.strip_accents(search_str.decode('utf-8'))

        self.list = self.video_list()
        self.list = [
            item for item in self.list if search_str.lower() in cleantitle.strip_accents(
                item['title'].decode('utf-8')
            ).lower()
        ]

        if not self.list:
            return

        for item in self.list:
            item.update({'action': 'play', 'isFolder': 'False'})

        for item in self.list:
            bookmark = dict((k, v) for k, v in item.iteritems() if not k == 'next')
            bookmark['bookmark'] = item['url']
            bm_cm = {'title': 30011, 'query': {'action': 'addBookmark', 'url': json.dumps(bookmark)}}
            cache_clear = {'title': 30015, 'query': {'action': 'cache_clear'}}
            item.update({'cm': [cache_clear, bm_cm]})

        self.list = sorted(self.list, key=lambda k: k['title'].lower())

        directory.add(self.list)
