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
from http import HTTPStatus
import solaredge.target_information as ti
import logging


class EnvironmentalInformation:
    @property
    def trees(self):
        if self._env is None:
            return None
        return self._env["envBenefits"]["treesPlanted"]

    @property
    def lightbulbs(self):
        if self._env is None:
            return None
        return self._env["envBenefits"]["lightBulbs"]

    @property
    def co2(self):
        if self._env is None:
            return None
        return self._env["envBenefits"]["gasEmissionSaved"]["co2"]

    def __init__(self, s, a):
        """
        Initialize the environmental information
        :param s: site id
        :param a: api key
        """
        self._env = None
        self._site_id = s
        self._api_key = a

    def refresh(self):
        s, self._env = self._get_json_from_remote(self._site_id, self._api_key)
        return s

    @staticmethod
    def _get_json_from_remote(site_id, api_key):
        """
        Do a more generic GET operation for compactness
        :param target: fully formed target information
        :return:
        """
        target = ti.SITE_ENVIRONMENTAL_BENEFITS.format(
            target=ti.TARGET_SITE,
            site=site_id,
            key=api_key
        )

        r = requests.get(target)
        if r.status_code != 200:
            logging.warning(
                f'GET failed to {target}, status code {r.status_code}')
            return -1 * r.status_code, None

        return r.status_code, r.json()

