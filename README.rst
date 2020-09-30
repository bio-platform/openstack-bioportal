Bioportal backend
=================

Backend of Bioportal, web application created to offer frontend a
connection to openstack cloud via REST API. This backend runs at
`link`_. On the server side, it’s running in Docker container. The
Dockerfile is not provided here yet.

Requirements
------------

-  Python 3
-  Nginx
-  `python requirements`_

Usage
-----

::

   sudo sh start.sh

Documentation
-------------

`here`_

Contributing
------------

1.Fork `openstack`_

2.Create your feature branch (``git checkout -b my-new-feature``)

3.Commit your changes (``git commit -am 'Add some feature'``)

4.Push to the branch (``git push origin my-new-feature``)

5.Create a new Pull Request

.. _link: http://bio-portal.metacentrum.cz/
.. _python requirements: https://github.com/andrejcermak/openstack/blob/master/requirements.txt
.. _here: https://bio-platform.github.io/openstack-bioportal/
.. _openstack: %60https://github.com/andrejcermak/openstack/fork%60
