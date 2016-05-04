"""
file        :   util.py (core)
date        :   2016-05-03
description :   core utility tools and functions
"""

import datetime
import random
import re
import uuid

from django.db import connection


# get time in format I like
def get_timestamp():
    """
    method to generate timestamp for use in application

    :return timestamp:
    """

    dt = datetime.datetime.now()

    timestamp = dt.strftime("%Y-%m-%d %X")

    return timestamp


def gen_uid(length=10):
    """
    method to generate random uuid of varying length for application

    :param length: length of uid
    :return uid: formatted string
    """

    # TODO - find one that works in both v2.x/3.x...
    # python 3.x version
    uid = uuid.uuid4()

    tmp_uid = re.sub('-', '', str(uid))

    uid = ''.join(random.sample(list(tmp_uid), length))

    return uid


def find_recs_made(profile):
    """
    query database and determine number of recognitions made by given profile
    :param profile:
    :return: recs_made
    """

    c = connection.cursor()
    c.execute('SELECT COUNT(*) '
              'FROM board_card '
              'WHERE recognizer_id={0};'.format(profile.id))

    a = c.fetchall()
    b = [int(x[0]) for x in a][0]

    recs_made = b

    return recs_made


def find_recs_received(profile):
    """
    query database and determine number of recognitions received by given profile
    :param profile:
    :return: recs_received
    """

    c = connection.cursor()
    c.execute('SELECT COUNT(*) '
              'FROM board_card_recognitions '
              'WHERE profile_id={0};'.format(profile.id))

    a = c.fetchall()
    b = [int(x[0]) for x in a][0]

    recs_received = b

    return recs_received