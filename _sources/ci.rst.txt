=============================
Continous Integration Testing
=============================

In this section you will:

* Understand the benefits Continuous Integration.
* Configure GitLab CI or Travis-CI, "continuous integration" services, to
  operate on your repository.

What is CI for?
---------------

If "Continuous Integration" (CI) is new to you, we refer you to
`this excellent Software Carpentry tutorial <https://katyhuff.github.io/python-testing/08-ci/>`_
on the subject. To summarize, CI speeds development by checking out your code on
a fresh, clean server, installing your software, running the tests, and
reporting the results. This helps you ensure that your code will work on your
colleague's computer---that it doesn't accidentally depend on some local detail
of your machine. It also creates a clear, public record of whether the tests
passed or failed, so if things are accidentally broken (say, while you are on
vacation) you can trace when the breaking change occurred.

GitLab CI configuration
---------------------------------------------
The UKAEA GitLab has its own CI servers with their own distinct configuration. An example
of such a configuration file is included in the cookiecutter template. 

.. literalinclude:: .example-gitlab-ci.yml

Using GitLab CI
---------------------------------------------
The config file, ``.gitlab-ci.yml``, included in the cookiecutter template will be 
automatically recognised and used to configure the CI service.
Alternatively if a different configuration for the CI is needed then one can be set 
up by deleting the existing config and using the ``Set up CI/CD`` button on your 
repository homepage. For convenience there are also many templates that can be chosen. 
If a non-template-based configuration file is needed then a step-by-step guide for 
`writing a .gitlab-ci.yml file <https://git.ccfe.ac.uk/help/user/project/pages/getting_started_part_four.md>`_
is available.

Travis-CI Configuration
-----------------------

If instead you are using GitHub, the cookiecutter template also has generated a
configuration file for Travis-CI, which is one of several CI services that are
free for public open-source projects.

.. literalinclude:: example_travis.yml

You can customize this to your liking. For example, if you are migrating a
large amount of existing code that is not compliant with PEP8, you may want to
remove the line that does ``flake8`` style-checking.

Activate Travis-CI for Your GitHub Repository
---------------------------------------------

#. Go to https://travis-ci.org and sign in with your GitHub account.
#. You will be prompted to authorize Travis-CI to access your GitHub account.
   Authorize it.
#. You will be redirected to https://travis-ci.org/profile, which shows a list
   of your GitHub repositories. If necessary, click the "Sync Account" button
   to refresh that list.
#. Find your new repository in the list. Click the on/off switch next to its
   name activate Travis-CI on that repository.
#. Click the repository name, which will direct you to the list of *builds* at
   ``https://travis-ci.org/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/builds``. The
   list will currently be empty. You'll see construction cones.
#. The next time you open a pull request or push a new commit to the master
   branch, Travis-CI will kick off a new build, and that list will update.

.. note::

    If this repository belongs to a GitHub *organization* (e.g.
    http://github.com/NSLS-II) as opposed to a personal user account
    (e.g. http://github.com/danielballan) you should follow Steps 3-5
    above for the organization's profile at
    ``https://travis-ci.org/profile/YOUR_GITHUB_ORGANIZATION``. It does no
    harm to *also* activate Travis-CI for your personal fork at
    ``https://travis-ci.org/profile``, but it's more important to activate it for
    the upstream fork associated with the organization.

Code Coverage
---------------------------------------------
The example GitLab CI configuration file, ``.gitlab-ci.yml`` runs a number 
of commands in the ``tests`` stage concerning code coverage. The 
`coverage <https://coverage.readthedocs.io/en/coverage-5.5/#quick-start>`_ 
package is one of the packages pre-populated in ``requirements-dev.txt``. This
can generate a report of the coverage of the tests that are run, as in what
percentage of lines of code are executed when the tests are run. If this is a
low percentage then there may be bugs hiding in the code which cannot be
identified as the tests do not cover the lines where they may be hiding. 

GitLab CI has the ability to parse the reports from ``coverage`` and
produce an overall test coverage badge (see the "Settings > CI > General"
section to find it) as well as test coverage visualisation for merge requests.
Both of these features have already been set up in the ``.gitlab-ci.yml`` file
with the cookie-cutter. 

.. note::

    Test coverage visualisation is a bit hacky at the moment. Don't be
    surprised if it doesn't show up or stops working.

Alternatively, GitHub does not come with test coverage reporting out of the
box, and you must use the 
`codecov <https://github.com/codecov/codecov-python>`_
package instead. The Travis-CI file uses a bash script to upload the coverage
report, but you will need to sign up to codecov in order to use this. You can
use your GitHub account to sign up to codecov.
