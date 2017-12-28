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

from resources.lib import action, url

if action is None:
    from resources.lib import navigator
    navigator.Main().root()

elif action == 'playlist':
    from resources.lib import navigator
    navigator.Main().playlist(url)

elif action == 'videos':
    from resources.lib import navigator
    navigator.Main().videos()

elif action == 'play':
    from resources.lib import player
    player.play(url)

elif action == 'settings':
    from tulip import control
    control.openSettings()

elif action == 'cache_clear':
    from tulip import cache
    cache.clear(withyes=False)

elif action == 'bookmarks':
    from resources.lib import navigator
    navigator.Main().bookmarks()

elif action == 'search':
    from resources.lib import navigator
    navigator.Main().search()

elif action == 'addBookmark':
    from tulip import bookmarks
    bookmarks.add(url)

elif action == 'deleteBookmark':
    from tulip import bookmarks
    bookmarks.delete(url)
