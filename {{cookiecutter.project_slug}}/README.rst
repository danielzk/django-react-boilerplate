{% for _ in cookiecutter.project_name %}*{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}*{% endfor %}

{{ cookiecutter.project_description }}

Getting Started
===============

Prerequisites
-------------

* Python >= 3.5.0
* Node >= 6.5.0
* Postgres >= 9.3

Installing
----------

1. Create the database and the virtual environment.
2. Create an .env file and set variables. Examples can be found in
   :code:`.env.example`.
3. Install Node dependencies:

   .. code-block:: bash

      frontend$ npm install

4. Start Node script for build and watch files:

   .. code-block:: bash

      frontend$ npm start

5. Install Python dependencies:

   .. code-block:: bash

      backend$ pip install -r requirements/dev.txt

6. Run migrations:

   .. code-block:: bash

      backend$ python manage.py migrate

7. Start the server:

   .. code-block:: bash

      backend$ python manage.py runserver

The site will be available on <http://127.0.0.1:8000>.

**Note**

Add the :code:`backend/apps` directory to the PYTHONPATH so your editor/IDE
recognizes it. This is not required to run the site since this is done in
:code:`backend/project/settings/base.py`.

Deploy
======

TODO

Tests
=====

Django
------

.. code-block:: bash

  backend$ make tests
  backend$ make wip-tests
  backend$ make review-tests

JS
--

.. code-block:: bash

  frontend$ npm test
  frontend$ npm run review-tests

Authors
=======

* **{{ cookiecutter.author_name }}**
