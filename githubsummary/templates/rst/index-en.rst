{{ g.get_user().name }}
{{'#' * g.get_user().name|length }}
:summary: The github projects index for {{ g.get_user().name }} github account
:save_as: index.html

.. image:: {{ g.get_user().avatar_url }}
    :alt: My photo
    :align: right

I discovered computers can after 80 years, this is the beginning of mainstream computing, I found linux to 1994 in the same period, I also discovered that I could call the best invention of computers, the Internet.

Self-taught, I learned various technology to guide me to the managements systems and networks. 15 years of experience in IT with broad and deep skill. Which can range Developpement to design IT infrastructure.

My strength, being constantly listen technologies evolutions and use a technologies will be apport a simplicity and max performances. 

I also love the Opensource Software, in the last time, i have contributed **{{ total_contribute }} hours**.

My blogs
---------

- `blog jesuislibre`_ my hobby blog.
- `blog cendreo`_ my professional blog


My sites
---------

:jesuislibre: The website for promote the french opensource software.
              `More informations <http://www.jesuislibre.org>`__
:informemoi: Agregation news
             `More informations <http://www.informemoi.com>`__
:cendreo: Share my skill
          `More informations <http://www.cendreo.com>`__

My contributions
-----------------
{% for repo in contrib %}
- `{{ repo.name }}`_ {% if jsonfile[repo.name] and jsonfile[repo.name]['hours'] %}contribute **{{ jsonfile[repo.name]['hours']}} hours** {% endif %}{% if repo.description %}/ {{ repo.description }}{% endif %}{% endfor %}

My projects
-----------
{% for repo in owner %}
- `{{ repo.name }}`_ {% if jsonfile[repo.name] and jsonfile[repo.name]['hours'] %}contribute **{{ jsonfile[repo.name]['hours']}} hours** {% endif %}{% if repo.watchers or repo.forks %}({% if repo.watchers > 0 %}{{ repo.watchers }} users{% endif %}{% if repo.forks > 0 %}, {{ repo.forks }} forks{% endif %}){% endif %}{% if repo.description %}/ {{ repo.description }}{% endif %}{% endfor %}

**Languages repartitions:** {% for key, value in reposlanguages.iteritems() %}{{ key|e }} ({{ value|e }}%){% if not loop.last %}, {% endif %}{% endfor %}

This page is generated with `github-summary`_ project

Contact me
----------

:Email: bruno.adele@jesuislibre.org
:Twitter: https://twitter.com/jesuislibre
:Google+: https://plus.google.com/100723270029692582967
:Facebook: https://www.facebook.com/bruno.adele
:Linuxfr: http://linuxfr.org/users/b_adele
:Github: https://github.com/badele
:Flickr: http://www.flickr.com/photos/b_adele/
:Lastfm: http://www.lastfm.fr/user/b_adele
:Stackoverflow: http://stackoverflow.com/users/2015612/bruno-adele



{% for repo in owner %}.. _{{ repo.name|lower }}: https://github.com/{{ g.get_user().login }}/{{ repo.name|lower }}
{% endfor %}

{% for repo in contrib %}.. _{{ repo.name|lower }}: https://github.com/{{ g.get_user().login }}/{{ repo.name|lower }}
{% endfor %}

.. _blog jesuislibre: http://blog.jesuislibre.org
.. _blog cendreo: http://blog.cendreo.com
.. _github-summary: https://github.com/badele/github-summary
