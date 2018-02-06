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

import cactus
import time
from datetime import date

def test_cactus_default_state():
    Haworthiopsis_fasciata = cactus.Cactus("Haworthiopsis_fasciata")
    assert Haworthiopsis_fasciata.is_succulent()

def test_if_need_to_water_by_default():
    Haworthiopsis_fasciata = cactus.Cactus("Haworthiopsis_fasciata")
    assert Haworthiopsis_fasciata.need_to_water()

def test_if_cactus_no_needed_water():
    Haworthiopsis_fasciata = cactus.Cactus("Haworthiopsis_fasciata")
    Haworthiopsis_fasciata.watering()
    assert not Haworthiopsis_fasciata.need_to_water()

def test_is_need_large_potter():# first move the cactus to large potter and check if cactus not need the large potter = True
    Haworthiopsis_fasciata = cactus.Cactus("Haworthiopsis_fasciata")
    Haworthiopsis_fasciata.move_to_large_potter()
    assert not Haworthiopsis_fasciata.is_need_large_potter()

def test_is_need_large_potter():# check if cactus need the large potter = True
    Haworthiopsis_fasciata = cactus.Cactus("Haworthiopsis_fasciata")
    assert Haworthiopsis_fasciata.is_need_large_potter()

def test_is_need_sun():
    Peyote = cactus.Cactus("Peyote")
    assert Peyote.is_need_sun

def test_is_need_shadow():
    Peyote = cactus.Cactus("Peyote")
    Peyote.move_to_shadow()
    assert not Peyote._is_need_sun










