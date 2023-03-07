Usage
=====

.. _installation:

Installation
------------

To use Determined, first install it using pip:

.. code-block:: console

   (.venv) $ pip install determined

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``determined.get_random_ingredients()`` function:

.. autofunction:: determined.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`determined.get_random_ingredients`
will raise an exception.

.. autoexception:: determined.InvalidKindError

For example:

>>> import determined
>>> determined.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

