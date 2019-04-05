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
"""
This is target information for SolarEdge
"""

TARGET_SITE = "https://monitoringapi.solaredge.com"

"""
This API gives energy use for any single day
"""
SITE_ENERGY_DAY = "{target}/site/{site}/energy?timeUnit=DAY&startDate=" \
                  "{day}&endDate={day}&api_key={key}"

"""
This is used to get the energy total for a period of time (like the last 30 
days, etc...)
"""
SITE_TIME_FRAME_ENERGY = "{target}/site/{site}/timeFrameEnergy?timeUnit=" \
                         "{unit}&startDate={start}&endDate={end}&api_key={key}"

"""
List the environmental benefits of a site
"""
SITE_ENVIRONMENTAL_BENEFITS = "{target}/site/{site}/envBenefits?" \
                              "systemUnits=Imperial&api_key={key}"

"""
Get details of an individual site, this will likely have the
timezone as well, etc...
"""
SITE_DETAILS = "{target}/site/{site}/details?api_key={key}"

"""
Get overview of an individual site, this can give you a day total, month
total, etc...
"""
SITE_OVERVIEW = "{target}/site/{site}/overview?api_key={key}"
