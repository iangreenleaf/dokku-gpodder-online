gPodder Online via Dokku
==============================

mygpo is the website and webservice powering gpodder.net.

This fork is deployed via Dokku for a personal version of the service.

Setup
-----

1. git remote add dokku dokku@dokku.youngram.com:gpodder
2. dokku apps:create gpodder
3. dokku plugin:install https://github.com/dokku/dokku-postgres.git
4. dokku postgres:create gpodder
5. dokku postgres:link gpodder gpodder
6. dokku config:set gpodder SECRET_KEY=my-secret-key
7. dokku storage:mount gpodder /var/log/gpodder-gunicorn:/var/log/gunicorn
8. git push dokku master
9. dokku domains:set gpodder podcasts.youngram.com
10. dokku domains:report gpodder
11. dokku run gpodder python manage.py migrate
12. dokku run gpodder python manage.py createsuperuser
13. dokku config:set --no-restart gpodder DOKKU_LETSENCRYPT_EMAIL=ian@iangreenleaf.com
14. dokku letsencrypt gpodder


License
-------
mygpo is licensed under the GNU Affero General Public License Version 3. See file [COPYING](COPYING) for details.


Installation
------------
See the [installation instructions](https://gpoddernet.readthedocs.io/en/latest/dev/installation.html) for details.


Bugs
----
Please report bugs in the [GitHub issue tracker](https://github.com/gpodder/mygpo/issues).


Contributing
------------
gpodder.net is an open source project and your contributions are wanted and appreciated.  To get started please see the [developer documentation](https://gpoddernet.readthedocs.io/en/latest/dev/index.html).

Slack
------------
Join our Slack channel: [gpodder-net.slack.com](https://gpodder-net.slack.com/)

[Invitation link](https://join.slack.com/t/gpodder-net/shared_invite/zt-aaiagl5i-uZeqVR8w1Yf_G~9rhktRfw)

Mailing List
------------
gpodder.org related issues are discussed on the [gPodder Mailing List](https://gpodder.github.io/docs/mailing-list.html).


Documentation
-------------
Documentation, especially for the API, is stored in the [**doc** folder](https://github.com/gpodder/mygpo/tree/master/doc) and can be read on [ReadTheDocs](https://gpoddernet.readthedocs.io/en/latest/index.html).


Name (Why mygpo?)
------------------
mygpo is a short version of "my.gpodder.org" which was the old [domain] name of gpodder.net and has been used as the project name since then.
