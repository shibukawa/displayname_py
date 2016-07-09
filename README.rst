displayname for Python
========================

It gets user name for display ("First Family") from operating system.

It is a FullName on Windows, RealName on macOS.

This is a multi-platform and a pure Python library.

.. code:: python

   import displayname

   print(displayname.get())
   # "First Family" instead of "first.family"

This module is pure python module.

API
-----

* ``imagesize.get(filepath)``

  Returns image size(width, height).

Current Status
----------------

.. list-table::
   :header-rows: 1

   - * OS
     * Status
   - * macOS
     * OK
   - * Windows
     * not tested
   - * Other
     * Fallback to login name(``getpass.getuser()``)

License
----------

MIT License
