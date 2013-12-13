{{ g.get_user().name }}
{{'#' * g.get_user().name|length }}
:summary: The github projects index for {{ g.get_user().name }} github account
:save_as: index.html

.. image:: /static/bruno.jpg
    :alt: Ma photo
    :align: right

J'ai découvert l'informatique peut de temps après les années 80, c'est le début de l'informatique grand public, j'ai découvert linux vers 1994, dans la même période, 
j'ai également découvert ce que je pourrais appeler la meilleure invention de l'informatique: Internet. Depuis plus de 15 ans, j'ai acquis diverses compétences dans des 
domaines qui peuvent aller de l'ingienierie systeme à la programmation en passant pas le design. `Pour en savoir plus </cv>`__ 

Je suis également passionné par les logiciels libres. Jusqu'à présent j'ai contribué **{{ total_contribute }} heures** à divers projets libres.

Mes blogs
---------

- Le `blog jesuislibre`_ me permet de partager ma passion, il me sert également de bloc-note.
- Le `blog cendreo`_ est plus orienté professionnel, il est moins actif que le `blog jesuislibre`_.


Mes sites
---------

:jesuislibre: Ce site permet de faire sortir de l'ombre tous les développeurs qui conçoivent des projets dans le milieu du libre (communautaires, universitaires,etc..).
              `Plus d'info <http://www.jesuislibre.org>`__
:informemoi: Site d'agrégation des informations
             `Plus d'info <http://www.informemoi.com>`__
:cendreo: Site qui met à disposition mes compétences
          `Plus d'info <http://www.cendreo.com>`__

Mes contributions
-----------------
{% for repo in contrib %}
- `{{ repo.name }}`_ {% if clocktable[repo.name] %}a contribué **{{ clocktable[repo.name]}} heures** {% endif %}{% if repo.description %}/ {{ repo.description }}{% endif %}{% endfor %}


Mes projets
-----------
{% for repo in owner %}
- `{{ repo.name }}`_ {% if clocktable[repo.name] %}a contribué **{{ clocktable[repo.name]}} heures** {% endif %}{% if repo.watchers or repo.forks %}({% if repo.watchers > 0 %}{{ repo.watchers }} utilisateurs{% endif %}{% if repo.forks > 0 %}, {{ repo.forks }} forks{% endif %}){% endif %}{% if repo.description %}/ {{ repo.description }}{% endif %}{% endfor %}

**Répartition des languages:** {% for key, value in reposlanguages.iteritems() %}{{ key|e }} ({{ value|e }}%){% if not loop.last %}, {% endif %}{% endfor %}

Me contacter
------------

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
