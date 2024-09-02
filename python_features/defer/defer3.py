#!/bin/python3

from twisted.internet import reactor
from twisted.internet.base import ReactorBase
from twisted.internet.defer import inlineCallbacks, Deferred  # returnValue
from twisted.internet.interfaces import IReactorTime
from twisted.internet.task import deferLater

from typing import cast


@inlineCallbacks
def my_callbacks(result):  # the result of initial call: "Start"

    # ----- Callback 1 start -----

    print(f'1st callback current result: {result}')
    # yielded values that aren't deferred objects come right back
    result = yield 1

    # ----- Callback 1 end -----

    # ----- Callback 2 start -----

    print(f"2nd callback current result: {result}")

    def add_one(x):
        print(f"    add_one: {x} => {x+1}")
        return x+1

    # Internal deferred passed between callbacks of outside deferred
    d1 = Deferred()
    reactor.callLater(3, d1.callback, add_one(result))

    # can add callbacks to internal deferred as well
    # e.g. calling add_one once more.
    # d.addCallback(add_one)

    # yielded deferred objects will pause the generator until resolved
    result = yield d1

    # ----- Callback 2 end -----

    # ----- Callback 3 start -----

    # the result of the deferred
    print(f"3rd callback current result: {result}")

    # Internal deferred passed between callbacks of outside deferred
    d2 = Deferred()
    # Resolution of this deferred will be an Exception.
    reactor.callLater(3, d2.errback, Exception(result+1))

    # ----- Callback 3 end -----

    # ----- Callback 4 start -----
    # (technically the "border" is on the "result = yield d" line itself)

    try:
        # yielded deferred objects will pause the generator until resolved
        result = yield d2
    except Exception as exception_result:
        # NOTE: result not updated, because the "yield d" throw an exception
        # prints "result: 2, exception_result: 3"
        print(f"4th callback current result: {result}, " +
              f"exception_result: {exception_result}")

    # ----- Callback 4 end -----

    # You can "return" real objects instead of
    # "yielding" deferred objects or values.

    # No more code after this point in the function are run as callbacks.

    # Older python: "return" is a syntax error in generators, and
    #               @inlineCallbacks decorated functions are generators.

    # Newer python: both return and returnValue work.

    # BUT:
    # yield "My real return value" does not work, because the reactor and
    # outside deferred object will think there are additional callback
    # after the yield, even with empty code, so the final return value
    # is "None", same as when you do not return anything in a normal function.

    # 1st way
    # returnValue("My real return value")

    # 2nd way
    return "My real return value"

    # 3rd way, this also works, but overhead!
    # There will be 1 additional callback block between yield and return
    # result = yield "My real return value" # 3rd way
    # return result

    # Does not work
    # There will be 1 additional callback block after the yield with empty code
    # yield  "My real return value"


# 1st way to call my_callbacks, and also print the return value
def report_result(result):
    print(f"End deferred report_result : {result}")


# outside deferred
deferred = deferLater(cast(IReactorTime, reactor), 0, my_callbacks, "Start")
# Final return value of my_callbacks can be passed to next callback to print
deferred.addCallback(report_result)

deferred.addBoth(lambda _: cast(ReactorBase, reactor).stop())
cast(ReactorBase, reactor).run()

# 2nd way to call my_callbacks
# reactor.callWhenRunning(my_callbacks, "Start")
# reactor.run()

# This does not work, because @inlineCallbacks and defer all part of the
# twisted python package, need to use reactor.
# from multiprocessing import Process
# p1 = Process(target=my_callbacks("Start"))
# p1.start()
# p1.join()
