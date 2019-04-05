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

LAUNCH_SPEECH_TEXT = "Welcome to Solar Edge, you can ask how much solar you " \
                     "generated today."

DAILY_ENERGY_TEXT = "Your solar system produced {kw} Kilowatt Hours {d} as " \
                    "reported by the Solar Edge Portal."

MONTHLY_ENERGY_TEXT = "Your solar system produced {kw} Kilowatt Hours this " \
                      "month as reported by the Solar Edge Portal."

NO_REPORTED_MONTHLY_ENERGY_TEXT = "Your solar system has not produced any " \
                                  "energy this month as reported by the " \
                                  "Solar Edge Portal"

LIFETIME_ENERGY_TEXT = "Your solar system produced {kw:.1f} Kilowatt Hours in its" \
                       " life, saving {t:.1f} trees, as much as {l:.1f} lightbulbs" \
                       " and {c:.1f} pounds of carbon dioxide."

NO_REPORTED_LIFETIME_ENERGY_TEXT = "Your solar system has not produced any " \
                                   "energy over its life as reported by the " \
                                   "Solar Edge Portal"

TODAY_ENERGY_TEXT = "Your solar system produced {kw} Kilowatt Hours and was " \
                    "producing {cp} Kilowatts the" \
                    " last time the Solar Edge inverter reported at {lr}."

NO_REPORTED_DAILY_ENERGY = "Your Solar Edge Portal does not have recorded " \
                           "values for {d}"

HELP_INTENT = "You can ask for Energy Production for Today."

TODAY = "today"
YESTERDAY = "yesterday"

GENERIC_DAY = "on {d}"
