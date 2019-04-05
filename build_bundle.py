#!/usr/bin/env python
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
import os
import zipfile

EXCLUDE = set(['.git', '.idea', '.gitignore'])


def zip_dir(path, handle):
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        for file in files:
            handle.write(os.path.join(root, file))


if __name__ == '__main__':
    zip_handle = zipfile.ZipFile('../solar_edge.zip', 'w', zipfile.ZIP_DEFLATED)
    zip_dir('./', zip_handle)
    zip_handle.close()