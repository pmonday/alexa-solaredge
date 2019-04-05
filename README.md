README
------
This is an Alexa Skill designed to give you information about
your [SolarEdge](https://www.solaredge.com/us/products/pv-monitoring#)
system installed at your home. To use this, you must have a SolarEdge
Inverter and have a monitoring account that you access via
the [SolarEdge Monitoring Portal](https://monitoring.solaredge.com/solaredge-web/p/login).

It is licensed under the [Apache 2.0 License](./LICENSE.txt)

What it does:
* Reports today's, yesterday's, or a specific day's energy output
* Reports the current month's energy output

What it does not do:
* I don't have a site set up to register your account at and use
single-sign on so you have to deploy the skill on your own (this is
my next priority after getting this open-sourced)
* I am hoping to add additional summaries, they are relatively easy
to add in, just takes time
* Some branding that I would like to do for the SolarEdge folks for
people that have viewable Alexa devices
* English-only

With all of those caveats, I use the skill a lot, almost daily
since I built it in September-ish timeframe.

Please see the additional information about:
* [Building](BUILD.md) - contains information on customizing and
packaging, I hope this evolves so I keep it separate for now
* [Deployment](DEPLOY.md) - contains information on getting it out
on Amazon Lambda and Alexa for you to access



