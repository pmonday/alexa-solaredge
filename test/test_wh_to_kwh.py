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
import util.conversions as c


class TestWh_to_kwh(TestCase):
    """
    Test simple conversion
    """
    def test_wh_to_kwh(self):
        w = 1000
        k = c.wh_to_kwh(w)
        self.assertEqual(k, 1, "kilowatt ({k}), watt ({w})".format(k=k, w=w))

    """
    Test decimal truncation
    """
    def test_wh_to_kwh_2decimal(self):
        w = 1150
        k = c.wh_to_kwh(w)
        self.assertEqual(k, 1.15, "kilowatt ({k}), watt ({w})".format(k=k, w=w))

    """
    Test decimal truncation
    """
    def test_wh_to_kwh_2decimal3(self):
        w = 1154
        k = c.wh_to_kwh(w)
        self.assertEqual(k, 1.15, "kilowatt ({k}), watt ({w})".format(k=k, w=w))