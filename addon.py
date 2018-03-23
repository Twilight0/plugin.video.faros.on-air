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
    navigator.Indexer().root()

elif action == 'playlist':
    from resources.lib import navigator
    navigator.Indexer().playlist(url)

elif action == 'videos':
    from resources.lib import navigator
    navigator.Indexer().videos()

elif action == 'play':
    from resources.lib import player
    player.play(url)

elif action == 'settings':
    from tulip import control
    control.openSettings()

elif action == 'cache_clear':
    from resources.lib import helpers
    helpers.cache_clear()

elif action == 'search':
    from resources.lib import navigator
    navigator.Indexer().search()

elif action == 'external_links':
    from resources.lib import navigator
    navigator.Indexer().external_links()

elif action == 'quit_kodi':
    from resources.lib import helpers
    helpers.quit_kodi()

elif action == 'lang_choice':
    from resources.lib import helpers
    helpers.lang_choice()

elif action == 'refresh':
    from resources.lib import helpers
    helpers.refresh()

elif action == 'check_updates':
    from resources.lib import helpers
    helpers.check_updates()

elif action == 'android_activity':
    from resources.lib import helpers
    helpers.android_activity(url)

elif action == 'weather':
    from resources.lib import helpers
    helpers.weather()

elif action == 'presentation':
    from resources.lib import helpers
    helpers.presentation()

elif action == 'favourites':
    from tulip import control
    control.execute('ActivateWindow(favourites,return)')

elif action == 'bookmarks':
    from resources.lib import navigator
    navigator.Indexer().bookmarks()

elif action == 'addBookmark':
    from tulip import bookmarks
    bookmarks.add(url)

elif action == 'deleteBookmark':
    from tulip import bookmarks
    bookmarks.delete(url)
