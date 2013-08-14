Example tx_people Project
=========================
This provides an example project for ``tx_people``.


Usage
-----
Create your virtualenv, then run:

::

    pip install -r requirements.txt

Next, install the various gems.

::

    bundle install

Finally, start up the demo server using Foreman.

::

    bundle exec foreman start


Testing
-------
Once you've installed the various requirements, you can run the tests for
``tx_people`` by running ``manage.py`` like this:

::

    python manage.py test app
