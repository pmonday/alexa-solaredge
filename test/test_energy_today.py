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
from unittest import TestCase
import model.daily_energy as de
import datetime
import util.conversions as cnv
import conf.site as st


class TestEnergy_today(TestCase):
    """

    """
    def test_energy_today(self):
        r = de.energy_today(st.SITE_ID, st.API_KEY)
        print("Energy today is {wh} watt hours".format(wh=r))
        self.assertGreaterEqual(r, 0, "unexpected value")

    def test_energy_on_today(self):
        day = datetime.datetime.now().strftime(cnv.AMAZON_DAY_FORMAT)
        r = de.energy_on_day(day, st.SITE_ID, st.API_KEY)
        print("Energy on today is {wh} watt hours".format(wh=r))
        self.assertGreaterEqual(r, 0, "unexpected value {v}".format(v=r))

    def test_energy_on_today_bad_site_good_api_key(self):
        bad_site = "10009990"
        day = datetime.datetime.now().strftime(cnv.AMAZON_DAY_FORMAT)
        r = de.energy_on_day(day, bad_site, st.API_KEY)
        self.assertEqual(r, -403, "unexpected value {v}".format(v=r))

    def test_energy_on_today_bad_api_key(self):
        bad_api_key = "10009990"
        day = datetime.datetime.now().strftime(cnv.AMAZON_DAY_FORMAT)
        r = de.energy_on_day(day, st.SITE_ID, bad_api_key)
        self.assertEqual(r, -403, "unexpected value {v}".format(v=r))
