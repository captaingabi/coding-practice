#!/bin/python3

from twisted.internet import reactor
from twisted.internet.base import ReactorBase
from twisted.internet.defer import Deferred

from typing import cast


def my_callback_1(result):  # the result of initial call: "Start"
    print(f'1st callback input: {result}')
    return 1


def my_callback_2(result):  # the result of my_callback_1: 1
    print(f'2nd callback input: {result}')
    return result + 1


def my_callback_3(result):  # the result of my_callback_2: 2
    print(f'3rd callback input: {result}')


deferred: Deferred = Deferred()
cast(ReactorBase, reactor).callLater(0, deferred.callback, "Start")
deferred.addCallback(my_callback_1)
deferred.addCallback(my_callback_2)
deferred.addCallback(my_callback_3)

# You need to run reactor, otherwise nothing is printed of course
# Also it is worth to stop the reactor. It can be done with an
# "inline" function definition aka lambda function.
deferred.addBoth(lambda _: cast(ReactorBase, reactor).stop())
cast(ReactorBase, reactor).run()
