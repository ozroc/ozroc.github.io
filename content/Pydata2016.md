Title: Towards a full stack python monitoring+analytics framework
Slug: about-me
Date: 2016-04-09 16:15
Category: talks
Tags: python, monitoring, pydata, analytics
Author: Pablo Manuel García Corzo
picture: /images/pydata-logo-madrid-2016.png

Presentation for <a href="http://pydata.org/madrid2016/schedule/presentation/14/index.html">PyData Madrid 2016</a>: <a href="https://youtu.be/-iqzbahA23Q?list=PLGVZCDnMOq0o43_3tHLAblfdOWwFFg76T">**Towards a full stack python monitoring+analytics framework**</a>

Are traditional monitoring solutions ready for the software defined world (SDN/NFV) and the IoT? Analytics can’t be considered anymore as an extra but a must for diving in an ocean of data where threshold-based KPIs are not enough. We will attempt to identify lacks in current tools and design a full stack python monitoring+analytics framework capable to face the new challenges of today.

It’s quite probable that you already have a standard monitoring tool (such as Nagios) deployed in your production environment reading thousands of KPIs from your systems every minute.

As you may already suspect, there’s much more interesting information hidden in all that data than just plain threshold based alarms per kpi and you wish to exploit it in much more depth.

Furthermore, traditional monitoring solutions are not ready for the increasing flow of heterogeneous information coming from the software defined world (SDN/NFV) and the IoT, where isolated threshold based alarms are not enough and analytics are a must for redefining your KPIs.

In this talk, we will attempt to design a full stack python monitoring+analytics framework capable to face those new challenges. For such a purpose we will study several state of the art libraries and tools covering all the pieces involved in the framework:

* Agents and brokers for data acquisition (ncpa, dweepy, phant, paho, hbmqtt...)
* Data storage (gnocchi, Arctic, HDF5, RRD...)
* Analytics (numpy, pandas, scikit-learn...)
* Dashboard generation (Bokeh, plotly, matplotlib...)
* Alarm raising (mqttwarn, telegram bots...)


<div class="youtube" align="center">
<iframe width="800" height="500" src="https://www.youtube.com/embed/-iqzbahA23Q" frameborder="0"></iframe>
</div>


