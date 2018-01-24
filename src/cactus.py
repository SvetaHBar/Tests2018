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
from datetime import date

class Cactus(object):

    def __init__(self, kind, watering):
        self._kind = kind
        self._watering = watering
        self._is_succulent = True
        self._is_plant_dry = True
        self._is_plant_humid = True

    def is_succulent(self):
        return self._is_succulent

    def need_to_water(self):
        watering_time = date(2018, 1, 20)
        localtime = time.localtime(time.time())
        print localtime
        delta_time = watering_time - localtime
        print delta_time
        if delta_time >= '7':
            return self._is_plant_humid
        else:
            return self._is_plant_dry

    def is_plant_dry(self):
        return self._is_plant_dry

    def is_plant_humid(self):
        return self._is_plant_humid



