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
import requests
import solaredge.target_information as ti
import solaredge.constants as cn
import datetime
import logging


def energy_today(site_id, api_key):
    """
    Retrieve the total power generated today (regardless of what
    time it is)
    :return: the number of wH generated today (decimal)
    """
    t = datetime.datetime.now().strftime(cn.DATE_FORMAT)
    return energy_on_day(t, site_id, api_key)


def energy_on_day(d, site_id, api_key):
    """
    Retrieve the total power generated today (regardless of what
    time it is)
    :return: the number of wH generated today (decimal)
    """
    u = ti.SITE_ENERGY_DAY.format(
            target=ti.TARGET_SITE,
            site=site_id,
            key=api_key,
            day=d)

    print(u)

    r = requests.get(u)

    if r.status_code != 200:
        logging.warning("GET failed, status code {sc}".format(sc=r.status_code))
        return -1 * r.status_code

    d = r.json()

    print(d)

    wh = d["energy"]["values"][0]["value"]

    # THe api can return "None" if information is not gathered yet on this day
    if wh is None:
        wh = -1

    return wh
