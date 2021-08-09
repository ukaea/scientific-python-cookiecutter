============================
Converting Existing Projects
============================

This tutorial assumes that you are starting your Python project from a very
early stage: either a completely fresh project with no source written yet, or a
collection of Python source files with not much else. However, it is a possible
scenario that you have been drawn to this tutorial because it provides an
appealing project layout, and you want to convert an existing project to use it.
It is impossible to provide a generic step-by-step guide to convert any project
to use this structure because the details depend too much on the existing setup
and maturity of the project. In lieu of that, we provide some helpful tips for
solutions to likely challenges you will face during conversion.

Assess Project Maturity
-----------------------

The strategies for converting projects loosely fall into two categories.

1. Pick'n'Mix: retain your existing project structure and fill in the gaps with
   features from the tutorial/cookiecutter, pulling over the relevant configurations from the cookiecutter template.
2. Full conversion: completely ditch your existing project structure in favour
   of the cookiecutter scaffolding, bringing over any necessary existing files
   in the process.

Again, there is no hard and fast way to determine which you should use, but a
heuristic for guidance is to consider whether your project contains at least 50%
of tools and configurations recommended by this tutorial. The side menu should
provide an adequate checklist of topics. If you are well above the 50%
threshold, then the Pick'n'Mix is probably for you, while if you are below it,
then a full conversion probably won't be too painful and will yield benefits.

Pick'n'Mix
----------

Start by instigating a "dummy" version of the cookiecutter like in
:doc:`preliminaries`. Although you won't be directly using the scaffolding that
is generated, it is still valuable to fill out the cookiecutter with information
that fits your project as closely as possible. This will help minimise
configuration when transposing elements back to your project.  

Then, briefly skim through the tutorial to find the components that your project
is missing or that you feel could be improved. Follow those sections of the
tutorial, and try to reproduce the results in your project. This will
undoubtedly require pulling over files from the "dummy" cookiecutter scaffolding
you just generated. In some cases, it won't be obvious from the tutorial which
files or tools you need, so forensic investigation with a trusted search engine
will be required. For example, to set up ``versioneer`` it will be easiest to
consult `the GitHub page
<https://github.com/python-versioneer/python-versioneer>`_ and follow the
instructions there, rather than trying to pull each of the files from the
cookiecutter.

It is also likely you will pose the question: should I stick with what I already
have or use what is in this tutorial? This tutorial can't answer that for you.
The recommendations we make are based on what we deem to be "good practice" in
most cases. However, the criteria for your project might require you to use
different tools, and that is absolutely fine, as long as you are clear what your
criteria are and that the alternate tools fulfill them.
