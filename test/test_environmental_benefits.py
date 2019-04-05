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
import model.environmental_benefits as eb
import conf.site as st


class TestTotal_trees_planted(TestCase):
    """

    """
    def test_energy_today(self):
        r = eb.total_trees_planted(st.SITE_ID, st.API_KEY)
        self.assertGreaterEqual(r, 0, "unexpected value")
