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

import human
import fixtures
import pytest
from human import Human



@pytest.fixture
#fixture for module -once in the beggining and teardown in the end
def create_family():
    family = human.Family("Haas\n",5)
    yield family
    family.go_to_vacation()
    print('\nteardown_module()')


@pytest.fixture
#fixture for function for each test
def create_new_named_human():
    tom = human.Human("20", "Tom")
    #return tom
    yield tom   #like a return tom , just not existing from function (after return function ended), after yield pass to next step (kill in our case)S
    tom.kill()  #teardown - for every test


@pytest.fixture
def config_file():
    with open("my_family.txt",'w')as f:
        f.write("Haas\n")
        f.write("5\n")
    with open("my_family.txt", "r") as my_config_file:
        yield my_config_file.readlines()   #RETURN LIST


def test_family_wake_up_in_the_morning(create_family):
    assert not create_family.a_waked_up()


def test_data_in_config_file(config_file):
    expected_res = ["Haas\n" , "5\n"]
    assert expected_res == config_file


def test_family_move_to_new_apartments(config_file):
    family = human.Family(config_file[0], int(config_file[1]))
    assert family.is_new_apartment()


def test_human_default_values(create_new_named_human):
    #tom = human.Human("20", "Tom") #object
    assert not create_new_named_human.is_sleeping()
    assert not create_new_named_human.is_eating()
    assert create_new_named_human.is_playing()
    assert not create_new_named_human.is_crying()
    assert not create_new_named_human.is_working()


def test_human_go_to_sleep(create_new_named_human):
    #tom = human.Human("20", "Tom")
    create_new_named_human.go_to_sleep()
    assert create_new_named_human.is_sleeping()


def test_human_is_waking_up(create_new_named_human):
    #tom = human.Human("20", "Tom")
    create_new_named_human.go_to_sleep()
    create_new_named_human.wake_up()
    assert not create_new_named_human.is_sleeping()


def test_human_go_to_eat(create_new_named_human):
    #jerry = human.Human("20", "Jerry")
    create_new_named_human.go_to_eat()
    assert not create_new_named_human.go_to_eat()


def test_human_start_to_play(create_new_named_human):
    #jerry = human.Human("20", "Jerry")
    create_new_named_human.stop_to_play()
    create_new_named_human.go_to_play()
    assert create_new_named_human.is_playing()


def test_human_go_to_cry(create_new_named_human):
    #jerry = human.Human("20", "Jerry")
    create_new_named_human.start_to_cry()
    assert create_new_named_human.is_crying()

def test_human_go_to_work(create_new_named_human):
    #dori = human.Human("40", "Dori")
    create_new_named_human.go_to_work()
    assert create_new_named_human.is_working() == True


def test_human_take_a_brake(create_new_named_human):
    #dori = human.Human("40", "Dori")
    create_new_named_human.go_to_work()
    create_new_named_human.take_a_brake()
    assert create_new_named_human.is_a_brake()


def test_human_have_not_brake(create_new_named_human):
    #dori = human.Human("40", "Dori")
    create_new_named_human.go_to_work()
    assert not create_new_named_human.is_a_brake()


def test_human_go_home(create_new_named_human):
    #dori = human.Human("40", "Dori")
    create_new_named_human.go_to_work()
    create_new_named_human.go_home()
    assert create_new_named_human.is_go_home()

#TODO : to check why tests alwayes passed
def test_human_go_home_1():
    dori = human.Human("40", "Dori")
    dori.go_to_work()
    dori.go_home()
    assert dori.is_working()

def test_human_go_to_childgarden():
    dorit = human.Human(5, "Dori")
    dorit.go_to_childgarden()
    dorit.going_to_childgarden()
    assert dorit.going_to_childgarden()

#TODO: fix for test below and add aditional tests
# add test when user go to pensia after age =67
# add test when user go to school /child garden /military/university


'''
def setup_module(module):
    print('\nsetup_module()') # module per set of tests , happen only once in the start of the run

def teardown_module(module): #happen once, after all tests in module will be run
    print ('teardownn_module')

def setup_function(function):  # setup_function will run for every tests in module
    print('\nsetup_function()')

def teardown_function(function):
    print('\nteardown_function()')


def test_1():
    print('- test_1()')

def test_2():
    print('- test_2()')



# TEST for fixures



class TestClass:
    @classmethod
    def setup_class(cls):
        print('\nsetup_class()')

    @classmethod
    def teardown_class(cls):
        print('teardown_class()')

    def setup_method(self, method):
        print('\nsetup_method()')

    def teardown_method(self, method):
        print('\nteardown_method()')

    def test_3(self):
        print('- test_3()')

    def test_4(self):
        print('- test_4()')  '''
