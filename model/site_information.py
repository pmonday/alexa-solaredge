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
import solaredge.target_information as ti
import solaredge.constants as cn
import requests
import logging
import datetime


class SiteInformation:

    @property
    def timezone(self):
        if self._details is None:
            return None
        return self._details["details"]["location"]["timeZone"]

    @property
    def status(self):
        if self._details is None:
            return None
        return self._details["details"]["status"]

    @property
    def last_update_time(self):
        if self._overview is None:
            return None
        return datetime.datetime.strptime(
            self._overview["overview"]["lastUpdateTime"], cn.DATE_TIME_FORMAT)

    @property
    def current_power(self):
        if self._overview is None:
            return None
        return self._overview["overview"]["currentPower"]["power"]

    @property
    def last_day_data(self):
        if self._overview is None:
            return None
        return self._overview["overview"]["lastDayData"]["energy"]

    @property
    def last_month_data(self):
        if self._overview is None:
            return None
        return self._overview["overview"]["lastMonthData"]["energy"]

    @property
    def last_year_data(self):
        if self._overview is None:
            return None
        return self._overview["overview"]["lastYearData"]["energy"]

    @property
    def lifetime_data(self):
        if self._overview is None:
            return None
        return self._overview["overview"]["lifeTimeData"]["energy"]

    @property
    def overview(self):
        return self._overview

    @property
    def details(self):
        return self._details

    def __init__(self, s, a):
        """
        Initialize the site information object
        :param s: site id
        :param a: api key
        """
        self._overview = None
        self._details = None
        self._site_id = s
        self._api_key = a

    def refresh(self):
        s, self._details = self._get_json_from_remote(ti.SITE_DETAILS.format(
            target=ti.TARGET_SITE,
            site=self._site_id,
            key=self._api_key
        ))

        if s < 0:
            return s

        s, self._overview = self._get_json_from_remote(ti.SITE_OVERVIEW.format(
            target=ti.TARGET_SITE,
            site=self._site_id,
            key=self._api_key
        ))

        return s

    @staticmethod
    def _get_json_from_remote(target):
        """
        Do a more generic GET operation for compactness
        :param target: fully formed target information
        :return:
        """
        j = None
        r = requests.get(target)
        print(f'Getting information from: {target}')
        if r.status_code != 200:
            logging.warning(
                f'GET failed to {target}, status code {r.status_code}')
            return -1 * r.status_code, j

        j = r.json()

        return r.status_code, j
