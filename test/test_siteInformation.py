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
from model.site_information import SiteInformation
import conf.site as si


class TestSiteInformation(TestCase):

    def setUp(self):
        self.goodSiteInformation = SiteInformation(si.SITE_ID, si.API_KEY)

    def tearDown(self):
        pass

    def test_timezone(self):
        r = self.goodSiteInformation.refresh()
        self.assertGreaterEqual(r, 0, "Unexpected refresh result: {r}"
                                .format(r=r))
        self.assertIsNotNone(self.goodSiteInformation.details)
        self.assertEqual("America/Denver", self.goodSiteInformation.timezone,
                         "Unexpected TimeZone ({tz})".format(
                             tz=self.goodSiteInformation.timezone))

    def test_overview(self):
        r = self.goodSiteInformation.refresh()
        self.assertGreaterEqual(r, 0, "Unexpected refresh result: {r}"
                                .format(r=r))
        self.assertIsNotNone(self.goodSiteInformation.overview)
        self.assertTrue("overview" in self.goodSiteInformation.overview)

    def test_details(self):
        r = self.goodSiteInformation.refresh()
        self.assertGreaterEqual(r, 0, "Unexpected refresh result: {r}"
                                .format(r=r))
        self.assertIsNotNone(self.goodSiteInformation.details)
        self.assertTrue("details" in self.goodSiteInformation.details)

    def test_refresh(self):
        r = self.goodSiteInformation.refresh()
        self.assertGreaterEqual(r, 0, "Unexpected refresh result: {r}"
                                .format(r=r))

    def test_lastupdate(self):
        r = self.goodSiteInformation.refresh()
        print(self.goodSiteInformation.overview)
        print(self.goodSiteInformation.last_update_time)
        self.assertIsNotNone(self.goodSiteInformation.last_update_time)
