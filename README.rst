sentry-redispubsub
=============

An extension for Sentry to send errors metrics to a Redis pub/sub message queue.

Install
-------

Install the package with ``pip``::

    pip install sentry-redispubsub


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
"RedisPubSub" tab. Enter the Redis host, port and prefix for metrics: @todo: Add additional help

.. image:: https://github.com/innogames/sentry-redispubsub/raw/master/docs/images/options.png


After installing and configuring, make sure to restart sentry-worker for the
changes to take into effect.
