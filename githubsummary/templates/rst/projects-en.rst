My projets
-----------
:summary: The github projects index for {{ g.get_user().name }} github account
:url: /projets
:slug: projets
:save_as: projets/index.html

I Love the Opensource software, i contribute Free software projets, i have contributed **{{ total_contribute }} hours** from  **{{ countrepos }}** projects.

-----------
My projects
-----------

{% for repo in owner %}
`{{ repo.name }} <{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{jsonfile[repo.name]['url']}}{% else %}{{ repo.url }}{% endif %}>`__ 
{{'-' * repo.name|length }}{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{'-' * jsonfile[repo.name]['url']|length }}{% else %}{{ '-' * repo.url|length }}{% endif %}{{'-' * repo.n|length }}-------

{% if jsonfile[repo.name] and jsonfile[repo.name]['hours'] %}a contribué **{{ jsonfile[repo.name]['hours']}} hours** {% endif %}{% if repo.watchers or repo.forks %}({% if repo.watchers > 0 %}{{ repo.watchers }} utilisateurs{% endif %}{% if repo.forks > 0 %}, {{ repo.forks }} forks{% endif %}){% endif %}

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


--------------
My contributes
--------------

{% for repo in contrib %}
`{{ repo.name }} <{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{jsonfile[repo.name]['url']}}{% else %}{{ repo.url }}{% endif %}>`__ 
{{'-' * repo.name|length }}{% if jsonfile[repo.name] and jsonfile[repo.name]['url']%}{{'-' * jsonfile[repo.name]['url']|length }}{% else %}{{ '-' * repo.url|length }}{% endif %}{{'-' * repo.n|length }}-------

{% if jsonfile[repo.name] and jsonfile[repo.name]['hours'] %}a contribué **{{ jsonfile[repo.name]['hours']}} hours** {% endif %}{% if repo.watchers or repo.forks %}({% if repo.watchers > 0 %}{{ repo.watchers }} utilisateurs{% endif %}{% if repo.forks > 0 %}, {{ repo.forks }} forks{% endif %}){% endif %}

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


This page is generated with `github-summary`_ project

.. _github-summary: https://github.com/badele/github-summary


