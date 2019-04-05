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
import conf.site as site
import datetime


def total_trees_planted(site_id, api_key):
    """
    Retrieve the total number of trees planted
    :return: the number of trees planted equivalence
    """
    r = requests.get(
        ti.SITE_ENVIRONMENTAL_BENEFITS.format(
            target=ti.TARGET_SITE,
            site=site_id,
            key=api_key
        )
    )

    d = r.json()
    return d["envBenefits"]["treesPlanted"]
