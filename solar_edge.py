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

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard

import model.speech as speech
import model.daily_energy as de
import util.conversions as cnv
import util.keys as keys
import datetime
import conf.site as st
import model.speech_error as se
import pytz
import os
from model.site_information import SiteInformation

sb = SkillBuilder()


class LaunchRequestHandler(AbstractRequestHandler):
    # Handler for Skill Launch
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech_text = speech.LAUNCH_SPEECH_TEXT

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("SolarEdge Energy Monitoring", speech_text))\
            .set_should_end_session(
            False)
        return handler_input.response_builder.response


class TodayEnergyIntentHandler(AbstractRequestHandler):
    # Handler specifically for 'today', a simplification
    # that expands on information to tell you when data
    # was last uploaded
    def can_handle(self, handler_input):
        return is_intent_name("TodayEnergyIntent")(handler_input)

    def handle(self, handler_input):
        # Get the Site Information
        site_information = SiteInformation(os.environ['SITE_ID'],
                                           os.environ['API_KEY'])
        r = site_information.refresh()
        if r <= 0:
            speech_text = _process_error(r, "today")
            handler_input.response_builder.speak(speech_text).set_card(
                SimpleCard("SolarEdge Energy Production", speech_text)) \
                .set_should_end_session(
                True)
            return handler_input.response_builder.response

        print('Using site information for today\'s energy')
        watt_hours = site_information.last_day_data
        print(watt_hours)
        kilowatt_hours = cnv.wh_to_kwh(watt_hours)
        print(kilowatt_hours)
        current_power = cnv.wh_to_kwh(site_information.current_power)
        print(current_power)
        time_amz_fmt = cnv.datetime_to_english(
            site_information.last_update_time)
        print(time_amz_fmt)

        speech_text = speech.TODAY_ENERGY_TEXT.format(
            kw=kilowatt_hours,
            cp=current_power,
            lr=time_amz_fmt
        )

        print(speech_text)

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("SolarEdge Energy Production", speech_text))\
            .set_should_end_session(
            True)
        return handler_input.response_builder.response


class DailyEnergyIntentHandler(AbstractRequestHandler):
    # Handler for determining a day's energy output
    # This handles the DATE slot as long as it is
    # particular day
    def can_handle(self, handler_input):
        return is_intent_name("DailyEnergyIntent")(handler_input)

    def handle(self, handler_input):
        # Get the slots that may be available from the intent
        slots = handler_input.request_envelope.request.intent.slots
        day = None

        # Get the Site Information, this will likely be moved
        # somewhere more appropriate since we want to reuse it
        # once we have it, maybe in LaunchRequestHandler
        # site_information = SiteInformation(st.SITE_ID, st.API_KEY)
        site_information = SiteInformation(os.environ['SITE_ID'],
                                           os.environ['API_KEY'])
        r = site_information.refresh()
        if r <= 0:
            speech_text = _process_error(r, "today")
            handler_input.response_builder.speak(speech_text).set_card(
                SimpleCard("SolarEdge Energy Production", speech_text)) \
                .set_should_end_session(
                True)
            return handler_input.response_builder.response

        # Check if the day for energy use is in the slot
        print('Getting today information')
        today = datetime.datetime.now(pytz.timezone(
            site_information.timezone)).strftime(cnv.AMAZON_DAY_FORMAT)
        print('Today is {d}'.format(d=today))

        if keys.DAY_ENERGY_USE_SLOT in slots:
            day_as_string = slots[keys.DAY_ENERGY_USE_SLOT].value
            print(day_as_string)
            if day_as_string is not None:
                day = day_as_string

        print('Day to retrieve is {d}'.format(d=day))
        if day is None or (day == today):
            day = today
            print('Using site information for today\'s energy')
            watt_hours = site_information.last_day_data
        else:
            print('Getting watt hours from remote')
            watt_hours = de.energy_on_day(day, os.environ['SITE_ID'],
                                          os.environ['API_KEY'])

        # This should move to kilowatt hours and round to two decimal locations
        day_as_text = cnv.date_to_english(day)

        if watt_hours == -1:
            speech_text = speech.NO_REPORTED_DAILY_ENERGY.format(
                d=day_as_text
            )
        elif watt_hours >= 0:
            kilowatt_hours = cnv.wh_to_kwh(watt_hours)
            speech_text = speech.DAILY_ENERGY_TEXT.format(
                kw=kilowatt_hours,
                d=day_as_text
            )
        else:
            speech_text = _process_error(watt_hours, day_as_text)

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("SolarEdge Energy Production", speech_text))\
            .set_should_end_session(
            True)
        return handler_input.response_builder.response


class MonthEnergyIntentHandler(AbstractRequestHandler):
    # Handler for determining the month's energy output
    def can_handle(self, handler_input):
        return is_intent_name("MonthEnergyIntent")(handler_input)

    def handle(self, handler_input):
        # No slots

        # Get the Site Information, this contains the month information
        site_information = SiteInformation(os.environ['SITE_ID'],
                                           os.environ['API_KEY'])
        r = site_information.refresh()
        if r <= 0:
            speech_text = _process_error(r, "this month")
            handler_input.response_builder.speak(speech_text).set_card(
                SimpleCard("SolarEdge Energy Production", speech_text)) \
                .set_should_end_session(
                True)
            return handler_input.response_builder.response

        watt_hours = site_information.last_month_data

        if watt_hours == -1:
            speech_text = speech.NO_REPORTED_MONTHLY_ENERGY_TEXT
        elif watt_hours >= 0:
            kilowatt_hours = cnv.wh_to_kwh(watt_hours)
            speech_text = speech.MONTHLY_ENERGY_TEXT.format(
                kw=kilowatt_hours
            )
        else:
            speech_text = _process_error(watt_hours, " this month ")

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("SolarEdge Energy Production", speech_text))\
            .set_should_end_session(
            True)
        return handler_input.response_builder.response


def _process_error(error_code, day_as_text):
    """
    Process the error and return some acceptable error speech
    that can be used
    :param error_code:
    :param day_as_text:
    :return:
    """
    actual_error = -1 * error_code
    if actual_error in se.speech_error:
        speech_error_text = se.speech_error[actual_error]
    else:
        speech_error_text = se.speech_error[se.GENERIC_ERROR_TEXT]

    speech_text = speech_error_text.format(
        status=actual_error,
        site=st.SITE_ID,
        d=day_as_text
    )

    return speech_text


class HelpIntentHandler(AbstractRequestHandler):
    # Handler for Help Intent
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = speech.HELP_INTENT

        handler_input.response_builder.speak(speech_text).ask(
            speech_text).set_card(SimpleCard(
                "SolarEdge Energy", speech_text))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    # Single handler for Cancel and Stop Intent
    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speech_text = "Goodbye!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("SolarEdge Energy", speech_text))
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    # AMAZON.FallbackIntent is only available in en-US locale.
    # This handler will not be triggered except in that locale,
    # so it is safe to deploy on any locale
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = (
            "Solar Edge cannot help you with that.")
        reprompt = "Ask about today's energy production."
        handler_input.response_builder.speak(speech_text).ask(reprompt)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    # Handler for Session End
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    # Catch all exception handler, log exception and
    # respond with custom message
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        print("Encountered following exception: {}".format(exception))

        text = "Sorry, there was some problem. Please try again!!"
        handler_input.response_builder.speak(text).ask(text)

        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TodayEnergyIntentHandler())
sb.add_request_handler(DailyEnergyIntentHandler())
sb.add_request_handler(MonthEnergyIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
