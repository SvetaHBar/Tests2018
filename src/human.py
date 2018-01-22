#
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
from __future__ import print_function

import time
import datetime
import fixtures
import pytest


class HumanCreator(object):
    def __init__(self, age, name):
        self._age = age
        self._name = name

    def create_human(self):
        new_human = Human(self._age, self._name)
        return new_human


class Family(object):
    def __init__(self,name,num_of_person):
        self._name = name
        self._num_of_person = num_of_person
        self._is_in_vacation = False
        self._is_a_wake = True
        self._is_new_apartment = False
        if num_of_person >= 5:
            self._is_new_apartment = True

    def is_vacation(self):
        return self._is_in_vacation

    def go_to_vacation(self):
        self._is_in_vacation = True

    def is_a_wake(self):
        return self.is_a_wake()

    def a_waked_up(self):
        self._is_a_wake = True

    def is_new_apartment(self):
        return self._is_new_apartment

    def move_to_new_apartments(self):
        self._is_new_apartment = True

class Human(object):
    def __init__(self, age, name):
        self._age = age
        self._name = name
        self._is_sleeping = False
        self._is_eating = False
        self._is_playing = True
        self._is_crying = False
        self._is_working = False
        self._is_a_brake = False
        self._is_go_home = False
        self._is_birth_date = 0
        self._is_a_member_in_childgarden = False
        self._is_dead = False

    def is_sleeping(self):
        return self._is_sleeping

    def go_to_sleep(self):
        self._is_sleeping = True

    def is_eating(self):
        self._is_eating

    def go_to_eat(self):
        self._is_eating = True

    def wake_up(self):
        self._is_sleeping = False

    def is_playing(self):
        return self._is_playing

    def stop_to_play(self):
        self._is_playing = False

    def go_to_play(self):
        self._is_playing = True

    def is_crying(self):
        return self._is_crying

    def start_to_cry(self):
        self._is_crying = True

    def is_working(self):
        return self._is_working

    def go_to_work(self):
        self._is_working = True

    def is_dead(self):
        return self._is_dead

    def kill(self):
        self._is_dead = True



    def go_home(self):
        self._is_go_home = True

    def is_go_home(self):
        return self._is_go_home

    def take_a_brake(self):
        self._is_a_brake = True

    def is_a_brake(self):
        return self._is_a_brake

    def going_to_childgarden(self):
        return self._age >= 3 and self._age < 7

    def go_to_childgarden(self):
        return self._is_a_member_in_childgarden


