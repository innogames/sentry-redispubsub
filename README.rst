sentry-redispubsub
=============

An extension for Sentry to send error metrics to a Redis pub/sub message queue.

Details
-------

The queue will get pushed a json payload with the following fields

project -> Project slug

logger -> Used logger

level -> Error level

msg -> Group message

times_seen -> Number of times seen

last_seen -> Unixtimestamp xxxxxxxx.0  #Please remove the trailing .0

first_seen -> Unixtimestamp xxxxxxxx.0 #Please remove the trailing .0

url -> Absolut url

checksum -> Checksum of group


Install
-------

Install the package with ``pip``::

    pip install sentry-redispubsub


Configuration
-------------

Go to your project's configuration page (Projects -> [Project]) and select the
"RedisPubSub" tab. Enter the Redis host, port, db number, channel name for metrics:

.. image:: https://github.com/innogames/sentry-redispubsub/raw/master/docs/images/options.png


After installing and configuring, make sure to restart sentry-worker for the
changes to take into effect.
