Mes projets
###########

:summary: The github projects index for {{ g.get_user().name }} github account
:url: /projets
:slug: projets
:save_as: projets/index.html

Passionné par les logiciels libres. Je contribue à divers projets, j'ai contribué **{{ total_contribute }} heures** sur **{{ countrepos }}** projets.

-----------
Mes projets
-----------

{% for repo in owner %}
`{{ repo.name }} <{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{jsonfile[repo.name]['url']}}{% else %}{{ repo.url }}{% endif %}>`__ 
{{'-' * repo.name|length }}{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{'-' * jsonfile[repo.name]['url']|length }}{% else %}{{ '-' * repo.url|length }}{% endif %}{{'-' * repo.n|length }}-------

{% if jsonfile[repo.name] and jsonfile[repo.name]['hours'] %}a contribué **{{ jsonfile[repo.name]['hours']}} heures** {% endif %}{% if repo.watchers or repo.forks %}({% if repo.watchers > 0 %}{{ repo.watchers }} utilisateurs{% endif %}{% if repo.forks > 0 %}, {{ repo.forks }} forks{% endif %}){% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['travis']%}.. image:: https://travis-ci.org/{{ g.get_user().login }}/{{ repo.name }}.png?branch=master
   :target: https://travis-ci.org/{{ g.get_user().login }}/{{ repo.name }}
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['coveralls']%}.. image:: https://coveralls.io/repos/{{ g.get_user().login }}/{{ repo.name }}/badge.png
   :target: https://coveralls.io/r/{{ g.get_user().login }}/{{ repo.name }}
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['pypi']%}.. image:: https://pypip.in/v/{{ repo.name }}/badge.png
   :target: https://crate.io/packages/{{ repo.name }}/
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['pydownload']%}.. image:: https://pypip.in/d/{{ repo.name }}/badge.png
   :target: https://crate.io/packages/{{ repo.name }}/
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['description'] %}{{jsonfile[repo.name]['description']}}{% else %}{{ repo.description }}{% endif %}
{% endfor %}


-----------------
Mes contributions
-----------------

{% for repo in contrib %}
`{{ repo.name }} <{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{jsonfile[repo.name]['url']}}{% else %}{{ repo.url }}{% endif %}>`__ 
{{'-' * repo.name|length }}{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{'-' * jsonfile[repo.name]['url']|length }}{% else %}{{ '-' * repo.url|length }}{% endif %}{{'-' * repo.n|length }}-------

{% if jsonfile[repo.name] and jsonfile[repo.name]['hours'] %}a contribué **{{ jsonfile[repo.name]['hours']}} heures** {% endif %}{% if repo.parent.watchers or repo.parent.forks %}({% if repo.parent.watchers > 0 %}{{ repo.parent.watchers }} utilisateurs{% endif %}{% if repo.parent.forks > 0 %}, {{ repo.parent.forks }} forks{% endif %}){% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['travis']%}.. image:: https://travis-ci.org/{{ g.get_user().login }}/{{ repo.name }}.png?branch=master
   :target: https://travis-ci.org/{{ g.get_user().login }}/{{ repo.name }}
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['coveralls']%}.. image:: https://coveralls.io/repos/{{ g.get_user().login }}/{{ repo.name }}/badge.png
   :target: https://coveralls.io/r/{{ g.get_user().login }}/{{ repo.name }}
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['pypi']%}.. image:: https://pypip.in/v/{{ repo.name }}/badge.png
   :target: https://crate.io/packages/{{ repo.name }}/
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['pydownload']%}.. image:: https://pypip.in/d/{{ repo.name }}/badge.png
   :target: https://crate.io/packages/{{ repo.name }}/
{% endif %}

{% if jsonfile[repo.name] and jsonfile[repo.name]['description'] %}{{jsonfile[repo.name]['description']}}{% else %}{{ repo.description }}{% endif %}
{% endfor %}

-------------------------
Répartition des langages
-------------------------

**Répartition des langages:** {% for key, value in reposlanguages.items()[:10] %}{{ key|e }} ({{ value|e }}%){% if not loop.last %}, {% endif %}{% endfor %}

.. image:: https://chart.googleapis.com/chart?cht=p3&chs=600x180&chd=t:{% for key, value in reposlanguages.items()[:10] %}{{ value }}{% if not loop.last %},{% endif%}{% endfor %}&chl={% for key, value in reposlanguages.items()[:10] %}{{ key }}{% if not loop.last %}|{% endif%}{% endfor %}&chco=2669ad
    :alt: Languages graphs

Cette page a été générée avec le projet `github-summary`_

.. _github-summary: https://github.com/badele/github-summary

