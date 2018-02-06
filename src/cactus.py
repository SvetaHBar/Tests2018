# Copyright 2018 Sveta Haas.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#
import time
import datetime

class Cactus(object):

    def __init__(self, kind):
        self._kind = kind
        self._is_succulent = True
        self._is_plant_dry = True
        self._is_plant_humid = False
        self._is_watering_time = 0
        self._is_potter = 0
        self._is_need_sun = True


    def is_succulent(self):
        return self._is_succulent

    def watering(self):
        self._is_watering_time = time.time()
        print self._is_watering_time

    def need_to_water(self):
        current_time = time.time()
        print current_time
        delta_time = current_time - self._is_watering_time
      # more optimated way to write "if" :if delta_time <= 7777: return False else : return True
        return delta_time > 7777

    def is_need_large_potter(self):
        current_potter = time.time()
        delta_potter = current_potter - self._is_potter
        #if passed more than X time from the biginning move to large potter
        return delta_potter >= 88888

    def move_to_large_potter(self):
        self._is_potter = time.time() # current time

    def is_need_sun(self):
        return self._is_need_sun

    def move_to_shadow(self):#if cactus should not be on the sun , move them to shadow
        self._is_need_sun = False

