User Manual
###########

The Summit project provides a simple mathematical evaluation tool in the
form of a class named :class:`~summit.node.SummitNode`.

Operations
**********
Using this object and standard integer or float literals, you can perform the
following operations.

    * (+) Addition
    * (-) Subtraction
    * (*) Multiplication
    * (/) Division

Now, knowing the operations possible, you probably want to know how to actually
use these. First, we need to know what we can perform these operations against.

Operands (Children)
*******************
:class:`~summit.node.SummitNode` requires a *minimum* of *two* operands to be
provided. This is so you can fulfill both "sides" of the simple operations
listed in the `Operations` section. All four operations require a minimum of
two operands and as such, so does :class:`~summit.node.SummitNode`.

Now, what are valid operands ?

    * :class:`~summit.node.SummitNode` : You can model more complex
        expressions by nesting multiple :class:`~summit.node.SummitNode`
        instances.
    * :class:`int`: Standard Python integers
    * :class:`float`: Standard Python float values



Simple Example
**************

To learn how to use this project, it's best to work with practical examples.
The following will be a very simple example to get your feet wet, there will
be more in depth examples later.

Lets start with a simple script;

.. code-block:: python

    from summit import SummitNode

    root = SummitNode('+', [1, 1])
    print(root.value)
    # will print '6'

The above script is 3 lines of code, simple right? Now to the explanation!

The import at the top is basic Python, if you are not familiar, please use
your search engine of choice and look for "Dive into Python" before starting.

Next, a new SummitNode is instantiated with the addition operator '+' and two
integer values that we want summed within a list.

.. code-block:: python

    root = SummitNode('+', [1, 1])

Why a list ? Well, we need to
allow two or more elements to be operated on, and this is a straightforward
method of representing that!

The SummitNode will automatically evaluate the expression upon
instantiation. Upon successful evaluation, the result can be retrieved
from the `value` attribute.

.. code-block:: python

    print(root.value)
    # will print '6'

Now, for something more complex!

Advanced Example
****************

Given the following code, the SummitNode will allow you to evaluate more
complex mathematical formulae.

.. code-block:: python
    :linenos:

    from summit import SummitNode

    node1 = SummitNode('+', [1, 2]) # 2
    node2 = SummitNode('-', [10, 2]) # 8
    node3 = SummitNode('*', [2, 2 ,2]) # 8
    node4 = SummitNode('/', [node2, 2] # 4
    node5 = SummitNode('*', [node4, node3]) # 32

In the example above, the ability to mix integers (or floats) and SummitNodes
can be used to build parts of a larger expression.

Of course, in the above examples you have only been shown two operands being
provided to SummitNode, however, this is not a limitation, you can have many
more operands, the only limitation is you must have *at least* two operands.