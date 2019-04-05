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

GENERIC_ERROR_TEXT = 999

speech_error = {
    403: "The Solar Edge portal responded unexpectedly with a status of "
         "{status}, you may not have access to site {site} on {d}.",
    999: "An unknown error occurred with {status} against site {site} for {d}."
}