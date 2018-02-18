***********
Import data
***********

This directory is used to provide data for models.

CSV's
=====

CSV's are intended to be imported with the importcsv command or Django admin
site.

importcsv
---------

.. code-block:: bash

   backend$ python manage.py importcsv data/app.model.csv

The file name must have the following format:

app.model.csv

The file must match the model scheme. You can use __codename for foreign
fields and __codenames for M2M fields. Using PK's is also allowed. codename
and pk fields are used as identifiers. Using PK's references and fields is
discouraged in most cases in favor of codename approach.

**Using codename field**

.. code-block::

   title   | codename | country__codename | categories__codenames | foreign_field | m2m_field
   Value 1 | ART1     | US                | GAMES,BOOKS           | 2             | 5,7
   Value 2 | ART2     | US                |                       | 5             | 3, 5
   Value 3 | ART3     | MX                | BOOKS, MUSIC          |               | 9

**Using pk field**

.. code-block::

   my_pk_field | name
   mypk        | Value 1

Records are updated based on the codename or pk fields. M2M fields are
completely updated, that is, data is added and removed. For example, if we
remove BOOKS from categories__codenames, it will be removed from the object.

Parler
""""""

Parler translation models must have "language_code" and "master__codename" or
"master" fields. Name of translation models end with "Translation".

world.countrytranslation.csv

.. code-block::

   language_code | master__codename | name
   es            | USA              | Estados Unidos

Other formats
-------------

See https://docs.djangoproject.com/en/dev/howto/initial-data/
