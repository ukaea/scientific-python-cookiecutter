=========================
Guiding Design Principles
=========================

In this section we summarize some guiding principles for designing and
organizing scientific Python code. Before diving in, it should be noted that
none of these are anything close to "rules". They are ideas to keep in mind
when writing your code, so don't get too bogged down in making sure you have
satisfied each and every one. 

Moreover, the points below barely scratch the surface. Software design is much
more of an art than a science, and it is something that must be refined over
time with intentional practice. The RSE Team runs a "Software
Best Practices" Course that covers many of the topics here in a little more
detail. The content of `the course is available on GitLab
<https://git.ccfe.ac.uk/software-training/software-best-practices>`_ and you
can register for instructor-led sessions on U4BW.

Collaborate
-----------

Software developed by several people is preferable to software developed by
one. By adopting the conventions and tooling used by many other scientific
software projects, you are well on your way to making it easy for others to
contribute. Familiarity works in both directions: it will be easier for others
to understand and contribute to your project, and it will be easier for you to
use other popular open-source scientific software projects and modify them to
your purposes.

Talking through a design and the assumptions in it helps to clarify your
thinking.

Collaboration takes trust. It is OK to be "wrong"; it is part of the process
of making things better.

Having more than one person understanding every part of the code prevents
systematic risks for the project and keeps you from being tied to that code.

If you can bring together contributors with diverse scientific backgrounds, it
becomes easier to identify functionality that should be generalized for reuse
by different fields.

.. _refactor:

Don't Be Afraid to Refactor
---------------------------

No code is ever right the first (or second) time.

Refactoring the code once you understand the problem and the design trade-offs
more fully helps keep the code maintainable. Version control, tests, and
linting are your safety net, empowering you to make changes with confidence. A
nice resource for refactoring strategies is `Refactoring Guru
<https://refactoring.guru/refactoring>`_, and there was `a recent Coding
Discussion Group presentation on refactoring
<https://git.ccfe.ac.uk/software-training/Coding_Discussion_Group/-/blob/master/Meetings/2020_12_04-HBrooks-Code_refactoring/2020_12_04-HBrooks-Code_refactoring.pdf>`_.
Modern IDEs will have many builtin tools to assist with the implementation of
refactoring techniques.

Prefer "Wide" over "Deep"
-------------------------

It should be possible to reuse pieces of software in a way not anticipated by
the original author. That is, branching out from the initial use case should
enable unplanned functionality without a massive increase in complexity.

When building new things, work your way down to the lowest level, understand
that level, and then build back up. Try to imagine what else you would want to
do with the capability you are implementing for other research groups, for
related scientific applications, and next year.

Take the time to understand how things need to work at the bottom. It is better
to slowly deploy a robust extensible solution than to quickly deploy a brittle
narrow solution.

Writing *modular* code is your friend here. Don't write a monolithic procedural
script that goes through your particular analysis or use-case step-by-step.
This is not reusable. Instead, create functions for bits of code that you find
yourself reusing (see :ref:`advice below <small-functions>`) and group related
functions and classes into modules so that they can be used in other modules
and to avoid name clashing.

Keep I/O Separate
-----------------

One of the biggest impediments to reuse of scientific code is when I/O
code---assuming certain file locations, names, formats, or layouts---is
interspersed with scientific logic.

I/O-related functions should *only* perform I/O. For example, they should take
in a filepath and return a numpy array, or a dictionary of arrays and metadata.
The valuable scientific logic should be encoded in functions that take in
standard data types and return standard data types. This makes them easier to
test, maintain when data formats change, or reuse for unforeseen applications.

Duck Typing is a Good Idea
--------------------------

`Duck typing <https://en.wikipedia.org/wiki/Duck_typing>`_ treats objects based
on what they can *do*, not based on what type they *are*. "If it walks like a
duck and it quacks like a duck, then it must be a duck."

Consider this more concrete albeit contrived example. 

.. code-block:: python

   class Duck:
       def fly(self):
           print("Duck flying")

   class Goose:
       def fly(self):
           print("Goose flying")

   class Whale:
       def swim(self):
           print("Whale swimming")
   
   for animal in Duck(), Goose(), Whale():
       animal.fly()

In statically typed languages, this would not compile and run. But in Python
this code will run right up until the point that the ``fly()`` method is not
found on the ``Whale`` object. The for loop treats both ``Duck`` and ``Goose``
objects equally because they implement the ``fly()`` method. This is
*duck-typing*.

Python in general and scientific Python in particular leverage *interfaces* to
support interoperability and reuse. For example, it is possible to pass a
pandas DataFrame to the :func:`numpy.sum` function even though pandas was
created long after :func:`numpy.sum`. This is because :func:`numpy.sum` avoids
assuming it will be passed specific data types; it accepts any object that
provides the right methods (interfaces). Where possible, avoid ``isinstance``
checks in your code, and try to make your functions work on the broadest
possible range of input types.

"Stop Writing Classes"
----------------------

Not everything needs to be object-oriented. Object-oriented design frequently
does not add value in scientific computing.

.. epigraph::

   It is better to have 100 functions operate on one data structure than 10
   functions on 10 data structures.

   -- From ACM's SIGPLAN publication, (September, 1982), Article "Epigrams in
   Programming", by Alan J. Perlis of Yale University.

It is often tempting to invent special objects for a use case or workflow ---
an ``Image`` object or a ``DiffractionAnalysis`` object. This approach has
proven again and again to be difficult to extend and maintain. It is better to
prefer standard, simple data structures like Python dictionaries and numpy
arrays and use simple functions to operate on them.

A popular talk, "Stop Writing Classes," which you can
`watch on YouTube <https://www.youtube.com/watch?v=o9pEzgHorH0&t=193s>`_,
illustrates how some situations that *seem* to lend themselves to
object-oriented programming are much more simply handled using plain, built-in
data structures and functions.

As another example, the widely-used scikit-image library initially experimented
with using an ``Image`` class, but ultimately decided that it was better to use
plain old numpy arrays. All scientific Python libraries understand numpy
arrays, but they don't understand custom classes, so it is better to pass
application-specific metadata *alongside* a standard array than to try to
encapsulate all of that information in a new, bespoke object.

Permissiveness Isn't Always Convenient
--------------------------------------

Overly permissive code can lead to very confusing bugs. If you need a flexible
user-facing interface that tries to "do the right thing" by guessing what the
users wants, separate it into two layers: a thin "friendly" layer on top of a
"cranky" layer that takes in only exactly what it needs and does the actual
work. The cranky layer should be easy to test; it should be constrained about
what it accepts and what it returns. This layered design makes it possible to
write *many* friendly layers with different opinions and different defaults.

Exceptions should just be raised: don't catch them and print. Exceptions are a
tool for being clear about what the code needs and letting the caller decide
what to do about it. *Application* code (e.g. GUIs) should catch and handle
errors to avoid crashing, but *library* code should generally raise errors
unless it is sure how the user or the caller wants to handle them.

Write Useful Error Messages
---------------------------

Be specific. Include what the wrong value was, what was wrong with it, and
perhaps how it might be fixed. For example, if the code fails to locate a file
it needs, it should say what it was looking for and where it looked.

Write for Readability
---------------------

Unless you are writing a script that you plan to delete tomorrow or next week,
your code will probably be read many more times than it is written. And today's
"temporary solution" often becomes tomorrow's critical code. Therefore,
optimize for clarity over brevity, using descriptive and consistent names.

Complexity is Always Conserved
------------------------------

Complexity is always conserved and is strictly greater than the system the code
is modeling. Attempts to hide complexity from the user frequently backfire.

For example, it is often tempting to hide certain reused keywords in a
function, shortening this:

.. code-block:: python

    get_image(filename, normalize=True, beginning=0, end=None):
        ...

into this:

.. code-block:: python

    def get_image(filename, options={}):
        ...

Although the interface appears to have been simplified through hidden keyword
arguments, now the user needs to remember what the ``options`` are or dig
through documentation to better understand how to use them.

Because new science occurs when old ideas are reapplied or extended in
unforeseen ways, scientific code should not bury its complexity or overly
optimize for a specific use case. It should expose what complexity there is
straightforwardly.

.. note::

    Even better, you should consider using "keyword-only" arguments, introduced
    in Python 3, which require the user to pass an argument by keyword rather
    than position.

    .. code-block:: python

        get_image(filename, *, normalize=True, beginning=0, end=None):
            ...

    Every argument after the ``*`` is keyword-only. Therefore, the usage
    ``get_image('thing.png', False)`` will not be allowed; the caller must
    explicitly type ``get_image('thing.png', normalize=False)``. The latter is
    easier to read, and it enables the author to insert additional parameters
    without breaking backward compatibility.

.. _small-functions:

Similarly, it can be tempting to write one function that performs multiple
steps and has many options instead of multiple functions that do a single step
and have few options. The advantages of "many small functions" reveal
themselves in time:

* Small functions are easier to explain and document because their behavior is
  well-scoped.
* Small functions can be tested individually, and it is easy to see which paths
  have and have not yet been tested.
* It is easier to compose a function with other functions and reuse it in an
  unanticipated way if its behavior is well-defined and tightly scoped. This is
  `the UNIX philosophy <https://en.wikipedia.org/wiki/Unix_philosophy>`_:
  "Do one thing and do it well."
* The number of possible interactions between arguments goes up with the number
  of arguments, which makes the function difficult to reason about and test. In
  particular, arguments whose meaning depends on other arguments should be
  avoided.

Functions should return the same kind of thing no matter what their arguments,
particularly their optional arguments.  Violating "return type stability" puts
a burden on the function's caller, which now must understand the internal
details of the function to know what type to expect for any given input. That
makes the function harder to document, test, and use.  Python does not enforce
return type stability, but we should try for it anyway.  If you have a function
that returns different types of things depending on its inputs, that is a sign
that it should be :ref:`refactored <refactor>` into multiple functions.

Python is incredibly flexible. It accommodates many possible design choices.
By exercising some restraint and consistency with the scientific Python
ecosystem, Python can be used to build scientific tools that last and grow well
over time.
