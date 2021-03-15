gPodder Online via Dokku
==============================

mygpo is the website and webservice powering gpodder.net.

This is a fork that can be deployed via Dokku for a personal version of the service.

Dokku setup
-----

1. git remote add dokku dokku@my-dokku-host.com:gpodder
1. dokku apps:create gpodder
1. dokku plugin:install https://github.com/dokku/dokku-postgres.git
1. dokku plugin:install https://github.com/dokku/dokku-redis.git redis
1. dokku postgres:create gpodder
1. dokku postgres:link gpodder gpodder
1. dokku redis:create gpodder
1. dokku redis:link gpodder gpodder
1. dokku config:set gpodder SECRET_KEY=my-secret-key
1. dokku config:set gpodder DEFAULT_BASE_URL=https://my-gpodder-site.com
1. dokku config:set gpodder BROKER_URL=$(dokku config:get gpodder REDIS_URL)
1. dokku storage:mount gpodder /var/log/gpodder-gunicorn:/var/log/gunicorn
1. dokku storage:mount gpodder /var/lib/dokku/data/storage/gpodder/staticfiles:/app/staticfiles
1. git push dokku master
1. dokku domains:set gpodder my-gpodder-site.com
1. dokku domains:report gpodder
1. dokku run gpodder python manage.py migrate
1. dokku run gpodder python manage.py createsuperuser
1. dokku config:set gpodder DOKKU_LETSENCRYPT_EMAIL=me@my-email.com
1. Either set [SMTP settings](https://docs.djangoproject.com/en/3.1/topics/email/) or if you don't need public registration, log them to console: dokku config:set gpodder EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
1. dokku letsencrypt gpodder
1. dokku ps:scale gpodder web=1 beat=1 celery=1


License
-------
mygpo is licensed under the GNU Affero General Public License Version 3. See file [COPYING](COPYING) for details.


Additional Info
----
Please see the [official project repository](https://github.com/gpodder/mygpo) for more information on the code, to report non-Dokku issues, etc.
