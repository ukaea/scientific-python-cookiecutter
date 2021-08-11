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

Full Conversion
---------------

There are a variety of steps to consider for a full conversion, and they depend
on the degree of existing infrastructure in your project. Follow those that are
applicable to your situation.

Version control
^^^^^^^^^^^^^^^

If the project that you are converting is already under version control, then
you will want to retain the history of the source files you have been working
on. If you use a version control system other than ``git``, you will need to
decide if you want to keep using that system (likely less hassle, but then the
release process in this tutorial won't work) or migrate to using ``git`` like
this tutorial advises (more hassle as you will need to figure out a conversion
step to make your repository a ``git`` repository).

If you use git already, this is a bit easier, but there are still many pitfalls,
so use these steps as a guide:

#. Create a "dummy" cookiecutter directory outside of the directory that your
   existing project is in (e.g. put it next to your project's directory). 

   .. code-block:: bash

      cd directory_next_to_project
      cookiecutter scientific-python-cookiecutter # this should be cached from before
   
   And then fill out the prompts as if it were for your current project, using
   the instructions from :doc:`preliminaries`.  Even though you will not be
   directly using this directory for your project, it is helpful to fill out the
   cookiecutter prompts accurately so that you can drop in any relevant
   configuration files from the cookiecutter with little or no modification.

#. Change into the cookiecutter-generated directory and initiate a ``git`` repo.

   .. code-block:: bash

      cd cookie_cutter_generated_directory
      git init
      git branch -m main
      git add .
      git commit -m "Scientific Python cookiecutter scaffolding"
   
#. Move back to your original project repository and add the cookiecutter one as
   a remote:

   .. code-block:: bash

      cd /path/to/original_project_directory
      git remote add -m main cookiecutter /absolute/or/relative/path/to/cookie_cutter_generated_directory
      git fetch cookiecutter

#. Merge in the cookiecutter structure to your project.

   .. code-block:: bash

      # make sure you are on an appropriate branch, probably not main/master
      git checkout -b project-structure-update
      git merge --allow-unrelated-histories cookiecutter/main 
   
   Depending on your project setup, there might be file conflicts. You will need
   to manually go through the files that git has identified, and resolve those
   conflicts. This is somewhat tedious, but less error-prone and no more tedious
   than copying over files from the cookiecutter manually with ``cp``.

#. Move your source files into the correct location if they are not already
   there. Again, how easy this is will depend on how you have structured you
   project up to this point. Regardless, you should use the ``git mv`` command.

   .. code-block:: bash

      git mv source1.py source2.py package_dir_name/

#. To get the full history of a file that has moved, be aware that you will need
   to pass the ``--follow`` command to ``git log``

   .. code-block:: bash

      git log --follow  file_that_has_moved.py
