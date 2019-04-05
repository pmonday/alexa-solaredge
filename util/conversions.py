# -*- coding: utf-8 -*-
# Copyright 2019, Paul B. Monday
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime
import pytz
import model.speech as sp

AMAZON_DAY_FORMAT = "%Y-%m-%d"
SPEAKABLE_DAY_FORMAT = "%A %B %d, %Y"
SPEAKABLE_DATETIME_FORMAT = "%A %B %d, %Y at %I:%M %p"


def wh_to_kwh(wh):
    """
    Convert watt hours to kilowatt hours and round to two decimal places
    :param wh: integer or decimal value
    :return: two decimal spot kilowatt hours
    """
    kw = float("{0:.2f}".format(wh / 1000.00))
    return kw


def date_to_english(d, tz="America/Denver"):
    today = datetime.datetime.now(pytz.timezone(tz))\
        .strftime(AMAZON_DAY_FORMAT)
    difference = days_between(today, d)
    if difference == datetime.timedelta(days=0):
        return sp.TODAY
    elif difference == datetime.timedelta(days=1):
        return sp.YESTERDAY

    return datetime.datetime.strptime(d, AMAZON_DAY_FORMAT)\
        .strftime(SPEAKABLE_DAY_FORMAT)


def datetime_to_english(d, tz="America/Denver"):
    return d.strftime(SPEAKABLE_DATETIME_FORMAT)


def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, AMAZON_DAY_FORMAT)
    d2 = datetime.datetime.strptime(d2, AMAZON_DAY_FORMAT)
    return abs(d1 - d2)
