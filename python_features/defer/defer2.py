#!/bin/python3

from twisted.internet import reactor
from twisted.internet.base import ReactorBase
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure

from typing import cast


def my_callback_1(result):  # the result of initial call: "Start"
    print(f'1st callback input: {result}')
    return 1


def my_callback_2(result):  # result of prev callback: 1
    print(f"2nd callback input: {result}")

    def add_one(x):
        print(f"    add_one: {x} => {x+1}")
        return x+1

    # Internal deferred passed between callbacks of outside deferred
    d1 = Deferred()

    # Resolution of this deferred will be 2
    reactor.callLater(3, d1.callback, add_one(result))

    # can add callbacks to internal deferred as well
    # e.g. calling add_one once more.
    # d.addCallback(add_one)

    return d1  # Deferred object, not real value!


def my_callback_3(result):  # result of the deferred d1: 2
    print(f"3rd callback input: {result}")

    # Internal deferred passed between callbacks of outside deferred
    d2 = Deferred()

    # Resolution of this deferred will be an Exception.
    reactor.callLater(3, d2.errback, Exception(result+1))

    return d2  # Deferred object, not real value!


def my_callback_4(result):  # result of the deferred d2: Failure(Exception(3))
    # defer wraps Exceptions into Failure class.
    # prints "result.type: <class 'Exception'>, result.value: 3"
    if isinstance(result, Failure):
        print(f"4th callback input: result.type: {result.type}, " +
              f"result.value: {result.value}")


deferred: Deferred = Deferred()  # outside deferred
cast(ReactorBase, reactor).callLater(0, deferred.callback, "Start")
deferred.addCallback(my_callback_1)
deferred.addCallback(my_callback_2)
deferred.addCallback(my_callback_3)

# Errback! Because d2 resolved to an Exception!
deferred.addErrback(my_callback_4)

deferred.addBoth(lambda _: cast(ReactorBase, reactor).stop())
cast(ReactorBase, reactor).run()
