gPodder Online via Dokku
==============================

mygpo is the website and webservice powering gpodder.net.

This is a fork that can be deployed via Dokku for a personal version of the service.

Dokku setup
-----

In this repository:

```
git remote add dokku dokku@my-dokku-host.com:gpodder
```

On the dokku host:

```
dokku apps:create gpodder
dokku plugin:install https://github.com/dokku/dokku-postgres.git
dokku plugin:install https://github.com/dokku/dokku-redis.git redis
dokku postgres:create gpodder
dokku postgres:link gpodder gpodder
dokku redis:create gpodder
dokku redis:link gpodder gpodder
dokku config:set gpodder SECRET_KEY=my-secret-key
dokku config:set gpodder DEFAULT_BASE_URL=https://my-gpodder-site.com
dokku config:set gpodder BROKER_URL=$(dokku config:get gpodder REDIS_URL)
dokku storage:mount gpodder /var/log/gpodder-gunicorn:/var/log/gunicorn
dokku storage:mount gpodder /var/lib/dokku/data/storage/gpodder/staticfiles:/app/staticfiles
```

In this repository:

```
git push dokku master
```

On the dokku host:

```
dokku domains:set gpodder my-gpodder-site.com
dokku domains:report gpodder
dokku run gpodder python manage.py migrate
dokku run gpodder python manage.py createsuperuser
dokku config:set gpodder DOKKU_LETSENCRYPT_EMAIL=me@my-email.com
dokku letsencrypt gpodder
dokku ps:scale gpodder web=1 beat=1 celery=1
```

Either set [SMTP settings](https://docs.djangoproject.com/en/3.1/topics/email/) or if you don't need public registration, log them to console:

```
dokku config:set gpodder EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
```

License
-------
mygpo is licensed under the GNU Affero General Public License Version 3. See file [COPYING](COPYING) for details.


Feedback
--------

There might be more convenient or efficient ways to set some of this up in Dokku. If you have improvements, please suggest them!

Additional Info
----
Please see the [official project repository](https://github.com/gpodder/mygpo) for more information on the code, to report non-Dokku issues, etc.
