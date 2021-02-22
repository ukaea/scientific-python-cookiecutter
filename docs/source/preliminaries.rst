===============
Getting Started
===============

In this section you will:

* Decide on a version control platform.
* Generate a scaffold for your new Python project.
* Upload it to the version control remote.
* Install your new Python project for development.

Then, in the next section, we will begin to move your scientific code into that
template.

You will need a Terminal (Windows calls it a "Command Prompt") and a plain text
editor. Any will do; we won't assume anything about the editor you are using.
If you are looking for a recommendation for beginners, the `Atom Editor
<https://atom.io/>`_ by GitHub is a good one. For minimalists, ``nano`` on
Linux or OSX and Notepad on Windows will get you up and running.

However, as you develop your programming skills, you will probably want to
correspondingly improve the tool you use to edit code. Most software developers
use something called an Integrated Development Environment (IDE). We have some
recommendations about good IDEs for Python here (TODO add link). If you are
more of an eccentric (read awesome), `Vim <https://www.vim.org/>`_ or 
`Emacs <https://www.gnu.org/software/emacs/>`_ are very customisable text
editors which are tuned for software development.

Reading the steps that follow, you might reasonably wonder, "Why isn't there
just an automated script for this?" We prefer to do this process manually so
that we are forced to think carefully about each step, notice when something
goes wrong, and debug if necessary. We recommend you do the same.

#. Decide where you are going to host your project and sign up if necessary.
   Please consult `the guidance here
   <http://intranet.ccfe.ac.uk/software/guides/gitlab.html>`_ for more
   information about your options. GitLab and GitHub are the recommended and
   most common. When in doubt, reach out to the RSE team.
      

#. Verify that you have Python 3.

   .. code-block:: bash
  
      python3 --version
  
   If necessary, install it by your method of choice: apt, Homebrew, conda,
   etc. Also ensure that you have ``pip`` (in apt, this is separate from the
   ``python3`` package and at the time of writing is called ``python3-pip``).


#. Verify that you have git installed.

   .. code-block:: bash
  
      git

   If necessary, install it by your method of choice (apt, Homebrew, conda, etc.).

#. Choose a name for your project.

   Ideal names are descriptive, succinct, and easy to Google. Think about who
   else might be interested in using or contributing to your project in the
   future, and choose a name that will help that person discover your project.
   There is no need to put "py" in the name; usually your user will already
   know that this is a Python project.

   Check that the name is not already taken by
   `searching for it on the Python Package Index (PyPI) <https://pypi.org/>`_.

#. Install cookiecutter.

   .. code-block:: bash

      python3 -m pip install --user --upgrade cookiecutter

   The ``--user`` flag installs this package in your user space rather than
   with the system site packages. :ref:`See the comment below about
   *environments*<environment>` for why this is important. However, a downside
   of using this flag is that the ``cookiecutter`` executable might not be
   placed in your path, in which case your shell won't be able to find it.
   There are a few solutions:

   #. The easiest option is to prepend the command to execute ``cookiecutter``
      with ``python3 -m``. The Python interpreter *will* be aware of the
      cookiecutter package in your user space, and so will have no trouble
      finding the executable.
   #. Find out where the cookiecutter executable has been installed and add
      that to your ``$PATH`` shell environment variable. This can be done with
      the following command from the terminal:

      .. code-block:: bash

         python3 -c 'import site; print(site.USER_BASE + "/bin")'
       
      Add that output to ``$PATH`` in your ``~/.bashrc`` file.
   #. If you are using conda, it is fine to install ``cookiecutter``
      in your base environment, or you can just go ahead and create an
      environment for this project :ref:`as detailed in the step below
      <environment>`, and then install cookiecutter in that.


#. Generate a new Python project using our cookiecutter template.

   .. code-block:: bash
   
      cookiecutter https://github.com/NSLS-II/scientific-python-cookiecutter


   You will see the following the prompts. The default suggestion is given in
   square brackets.

   For the last question, ``minimum_supported_python_version``, we recommend
   supporting back to Python 3.6 unless you have a need for newer Python
   features.

   .. code-block:: bash

      full_name [Name or Organization]: Brookhaven National Lab
      email []: dallan@bnl.gov
      github_username []: danielballan
      project_name [Your Project Name]: Example
      package_dist_name [example]:
      package_dir_name [example]:
      repo_name [example]:
      project_short_description [Python package for doing science.]: Example package for docs.
      year [2018]:
      Select minimum_supported_python_version:
      1 - Python 3.6
      2 - Python 3.7
      3 - Python 3.8
      Choose from 1, 2, 3 [1]:

   This generates a new directory, ``example`` in this case, with all the
   "scaffolding" of a working Python project.

   .. code-block:: bash

      $ ls example/
      AUTHORS.rst        MANIFEST.in     example                 setup.cfg
      CONTRIBUTING.rst   README.rst      requirements-dev.txt    setup.py
      LICENSE            docs            requirements.txt        versioneer.py

   .. note::

      Cookiecutter prompted us for several variations of *name*.
      If are you wondering what differentiates all these names, here's a primer, 
      and make sure to pay attention to the punctuation allowed for each:

      * ``project_name`` -- Human-friendly title. Case sensitive. Spaces allowed.
      * ``package_dist_name`` -- The name to use when you ``pip install ___``.
        Dashes and underscores are allowed. Dashes are conventional. Case
        insensitive.
      * ``package_dir_name`` --- The name to use when you ``import ___`` in Python.
        **Underscores are the only punctuation allowed.** Conventionally
        lowercase.
      * ``repo_name`` --- The name of the GitHub repository. This will be the
        name of the new directory on your filesystem.

#. Take a moment to see what we have. (Some systems treat files whose name
   begins with ``.`` as "hidden files", not shown by default. Use the ``ls -a``
   command in the Terminal to show them.)

   .. The following code-block output was generated using `tree -a example/`.

   .. code-block:: text

      example/
      ├── .flake8
      ├── .gitattributes
      ├── .gitignore
      ├── .travis.yml
      ├── AUTHORS.rst
      ├── CONTRIBUTING.rst
      ├── LICENSE
      ├── MANIFEST.in
      ├── README.rst
      ├── docs
      │   ├── Makefile
      │   ├── build
      │   ├── make.bat
      │   └── source
      │       ├── _static
      │       │   └── .placeholder
      │       ├── _templates
      │       ├── conf.py
      │       ├── index.rst
      │       ├── installation.rst
      │       ├── release-history.rst
      │       └── usage.rst
      ├── example
      │   ├── __init__.py
      │   ├── _version.py
      │   └── tests
      │       └── test_examples.py
      ├── requirements-dev.txt
      ├── requirements.txt
      ├── setup.cfg
      ├── setup.py
      └── versioneer.py

   In this top ``example/`` directory, we have files specifying metadata about
   the Python package (e.g. ``LICENSE``) and configuration files related to
   tools we will cover in later sections. We are mostly concerned with the
   ``example/example/`` subdirectory, which is the Python package itself. This
   is where we'll put the scientific code. But first, we should get a proper
   development environment and version-control our project using git.

#. Change directories into your new project.

   .. code-block:: bash

      cd example

   We are now in the top-level ``example/`` directory---not ``example/example``!


#.  .. _environment:
    
    Create an *environment*, a sandboxed area for installing
    software that is separate from the system defaults. This is not essential,
    but it is strongly encouraged. It ensures that your project and its software
    dependencies will not interfere with other Python software on your system.
    On Linux-based systems, the system Python installation has some pretty core
    functionality, so if you bugger that up, your whole OS can be affected.
    **You have been warned!!!*** There are several tools for creating virtual
    environments.  But the simplest is Python's built-in ``venv`` (short for
    "virtual environments"), illustrated here.

    Do this once:

    .. code-block:: bash

       python3 -m venv my-env

    The term ``my-env`` can be anything. It names the new environment. A
    typical choice is ``env`` or ``venv``, possibly with a ``.`` prepended if
    you want the directory invisible by default from the terminal. In our
    experience, it is best to make this directory as visible as possible to
    remind yourself that the project requires you to initiate the virtual
    environment. You will want to add the name of the environment directory to
    `.gitignore` if it is different from the defaults just suggested.

    Do this every time you open up a new Terminal / Command Prompt to work on
    your project:

    .. code-block:: bash

       . my-env/bin/activate

    .. note::

       If you are a conda user, you may prefer a conda environment:

       .. code-block:: bash

          conda create -n my-env python=3.7
          conda activate my-env   # repeat everytime you come back to project

#. Make the directory a git repository.

   .. code-block:: bash

      $ git init
      Initialized empty Git repository in (...)

#. Make the first "commit". If we break anything in later steps, we can always
   roll back to this clean initial state.

   .. code-block:: bash

      $ git add .
      $ git commit -m "Initial commit."
   
   .. note::

      If the author credentials for this repository will differ from your
      globally configured settings in git, then you should set them locally to
      what you want before committing:

      .. code-block:: bash

         git config --local user.name USERNAME_FOR_VCS
         git config --local user.email EMAIL_FOR_VCS

#. Create a new repository on `GitLab <https://git.ccfe.ac.uk/projects/new>`_
   or `GitHub <https://github.com/new>`_,
   naming it with the ``repo_name`` from your cookiecutter input above and
   selecting the appropriate group or organisation that should own it.

   .. important::

      Do **not** check "Initialize this repository with a README".

#. Configure your local repository to know about the remote repository...

   .. code-block:: bash

      $ git remote add origin git@git.ccfe.ac.uk/GITLAB_USER_OR_ORG_NAME/YOUR_REPOSITORY_NAME.

   ... and upload the code.

   .. code-block:: bash

      $ git push -u origin master
      Counting objects: 42, done.
      Delta compression using up to 4 threads.
      Compressing objects: 100% (40/40), done.
      Writing objects: 100% (42/42), 29.63 KiB | 0 bytes/s, done.
      Total 42 (delta 4), reused 0 (delta 0)
      remote: Resolving deltas: 100% (4/4), done.
      To git.ccfe.ac.uk:GITLAB_USER_OR_ORG_NAME/YOUR_REPO_NAME.git
       * [new branch]      master -> master
         Branch master set up to track remote branch master from origin.

   .. note::

      There has been a movement within software development away from using
      ``master`` as the name for the primary/default branch of a git repository
      because of the connection to the master/slave dynamic. There has been a
      lot of debate around this, and you can get a sense of it from `this
      source
      <https://mail.gnome.org/archives/desktop-devel-list/2019-May/msg00066.html>`_
      and `this one
      <https://twitter.com/mislav/status/1270388510684598272>`_. Whatever
      conclusions you reach, it is pretty easy to change to a different default 
      branch name *before you first push to the remote*:

      .. code-block:: bash

         $ git branch -M main
         $ git push -u origin main

   .. note::

      If this repository is to belong to an *organization* (e.g.
      http://github.com/ukaea) as opposed to a personal user account
      (e.g. http://github.com/bielsnohr) it is conventional to name the
      organization remote ``upstream`` instead of ``origin``.

      .. code-block:: bash

          $ git remote add upstream https://github.com/ORGANIZATION_NAME/YOUR_REPOSITORY_NAME.
          $ git push -u upstream master
          Counting objects: 42, done.
          Delta compression using up to 4 threads.
          Compressing objects: 100% (40/40), done.
          Writing objects: 100% (42/42), 29.63 KiB | 0 bytes/s, done.
          Total 42 (delta 4), reused 0 (delta 0)
          remote: Resolving deltas: 100% (4/4), done.
          To github.com:ORGANIZATION_NAME/YOUR_REPO_NAME.git
           * [new branch]      master -> master
             Branch master set up to track remote branch master from upstream.

      and, separately, add your personal fork as ``origin``.

      .. code-block:: bash

          $ git remote add origin https://github.com/YOUR_GITHUB_USER_NAME/YOUR_REPOSITORY_NAME.

#. Now let's install your project for development.

   .. code-block:: python

      python3 -m pip install -e .

   .. note::

      The ``-e`` stands for "editable". It uses simlinks to link to the actual
      files in your repository (rather than copying them, which is what plain
      ``pip install .`` would do) so that you do not need to re-install the
      package for an edit to take effect.

      This is similar to the behavior of ``python setup.py develop``. If you
      have seen that before, we recommend always using ``pip install -e .``
      instead because it avoids certain pitfalls.

#. Finally, verify that we can import it.

   .. code-block:: bash

      python3

   .. code-block:: python

      >>> import your_package_name

#. Looking ahead, we'll also need the "development requirements" for our
   package. These are third-party Python packages that aren't necessary to
   *use* our package, but are necessary to *develop* it (run tests, build the
   documentation). The cookiecutter template has listed some defaults in
   ``requirements-dev.txt``. Install them now.

  .. code-block:: bash

     python3 -m pip install --upgrade -r requirements-dev.txt

Now we have a working but empty Python project. In the next section, we'll
start moving your scientific code into the project.
