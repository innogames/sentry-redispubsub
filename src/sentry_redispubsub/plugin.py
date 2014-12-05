# coding: utf-8
"""
sentry_redispubsub.plugin
"""

from sentry.plugins import Plugin

import sentry_redispubsub
from sentry_redispubsub.forms import RedisPubSubOptionsForm

import json
import redis
from time import mktime


class RedisPubSubPlugin(Plugin):
    """
    Sentry plugin to send errors stats to a Redis pub/sub message queue.
    """
    author = 'Anthony Boah'
    author_url = 'https://github.com/innogames/sentry-redispubsub'
    version = sentry_redispubsub.VERSION
    description = 'Send errors stats to a Redis pub/sub message queue.'
    slug = 'redispubsub'
    title = 'Redis Pub/Sub'
    conf_key = slug
    conf_title = title
    resource_links = [
        ('Source', 'https://github.com/innogames/sentry-redispubsub'),
        ('Bug Tracker', 'https://github.com/innogames/sentry-redispubsub/issues'),
        ('README', 'https://github.com/innogames/sentry-redispubsub/blob/master/README.rst'),
    ]
    project_conf_form = RedisPubSubOptionsForm

    def is_configured(self, project, **kwargs):
        """
        Check if plugin is configured.
        """
        params = self.get_option
        return bool(params('host', project) and params('port', project) and params('channel_name', project))

    def post_process(self, group, event, is_new, is_sample, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        host = self.get_option('host', group.project)
        port = self.get_option('port', group.project)
        db = self.get_option('db', group.project)
        channel_name = self.get_option('channel_name', group.project)

        metric = {}
        metric['project'] = group.project.slug
        metric['logger'] = group.logger
        metric['level'] = group.get_level_display()
        metric['msg'] = group.message
        metric['times_seen'] = group.times_seen
        metric['last_seen'] = mktime(group.last_seen.utctimetuple())
        metric['first_seen'] = mktime(group.first_seen.utctimetuple())
        metric['url'] = group.get_absolute_url()
        metric['checksum'] = group.checksum

        client = redis.StrictRedis(host, port, db)
        client.publish(channel_name, json.dumps(metric, sort_keys=False))