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
from datetime import date, timedelta
import datetime
import util.conversions as cnv
import model.speech as sp
import pytz


class TestDate_to_english(TestCase):

    def test_date_to_english_today(self):
        today = datetime.datetime.now(pytz.timezone('America/Denver'))\
            .strftime(cnv.AMAZON_DAY_FORMAT)
        today_speech = cnv.date_to_english(today)
        self.assertEqual(sp.TODAY, today_speech, "result is incorrect {m}"
                         .format(m=today_speech))

    def test_date_to_english_yesterday(self):
        yesterday = (date.today() - timedelta(1))\
            .strftime(cnv.AMAZON_DAY_FORMAT)
        yesterday_speech = cnv.date_to_english(yesterday)
        self.assertEqual(sp.YESTERDAY, yesterday_speech,
                         "result is incorrect {m}"
                         .format(m=yesterday_speech))

    def test_difference_today(self):
        today = datetime.datetime.now().strftime(cnv.AMAZON_DAY_FORMAT)
        self.assertEqual(datetime.timedelta(days=0), cnv.days_between(today, today))

    def test_datetime_to_english_yesterday(self):
        now = datetime.datetime.now()
        eng = cnv.datetime_to_english(now)
        print(eng)
        self.assertIsNotNone(eng)
