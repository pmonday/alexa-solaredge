BUILD
------
This file contains information about what to do once you have
the core files downloaded from github. I don't mind feedback on 
this, here are the obvious locations for improvement:

* Reorganization - Use a venv environment instead of flat structure

## Setup Environment

To set up this project:
* clone the repository to a directory: `git clone <repo> solar`
* install the dependencies
  * `cd solar` (or whatever directory you cloned the repository into) 
  * `pip install pytz -t .`
  * `pip install requests -t .`
  * `pip install ask-sdk -t .`

* modify the configuration file
  * open `conf/site.py`
  * set API_KEY and SITE_ID to the values obtained in the previous section
 
Do *not* check your API Key and Site ID into the git project
by accident after your site.py file is modified.

## Package
From *within* the solar edge skill directory (we need a flat directory
with the skill at the root) call the following:
`./build_bundle.py`

It will create a package `solar_edge.zip` in the parent directory.

Modify the `build_bundle.py` program as necessary, but avoid pushing
it back unless your update is amazing and you've updated the above
instructions.
