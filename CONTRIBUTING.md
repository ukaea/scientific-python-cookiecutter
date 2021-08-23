# Contributing to the Project

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways.

## Bugs in the Cookiecutter Template

If you find something wrong when using the cookiecutter, report these bugs at
https://github.com/ukaea/scientific-python-cookiecutter/issues.

If you are reporting a bug, please include:

* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.
* Tag it with the "bug" label.

## Submit Feedback

The best way to send feedback is to file an issue at
https://github.com/ukaea/scientific-python-cookiecutter/issues.

If you are proposing a feature (i.e. something that you think should be
included in the cookiecutter template and/or tutorial):

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

In keeping with the philosophy of this tutorial and template, the cookiecutter
should be kept fairly "lean" so as not to impose a steep learning curve on
researchers that use it. Therefore, new tools will be scrutinised closely to
see if they tip this balance.

## Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it. See how to raise a pull request below
to contribute your fix.

## Implement Features

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it. See how to raise a pull request below
to contribute your feature.

## Pull Requests

The general process for contributing content through pull requests is:

1. Fork this repository.
2. Create a branch for your additions or corrections.
3. Open a pull request from your branch to the main branch of this repository.

Ready to contribute? Here's how to get set up:

1. Fork the ukaea/scientific-python-cookiecutter repo on GitHub.

2. Clone your fork locally.

3. Install your local copy into a virtualenv, set up a dummy cookiecutter, and
   make the tutorial:
   ```bash
   cd scientific-python-cookiecutter
   python -m venv venv
   . venv/bin/activate
   pip install --upgrade -r requirements.txt
   ./run_cookiecutter_example.py 
   ./copy_user_content.sh 
   pip install -e example/
   make -C docs html
   ```
   View with your browser at `docs/build/html/index.html`

4. Create a branch for local development:

   ```bash
   git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

5. To modify the tutorial, edit the reStructuredText files under
   `docs/source/`. Then rebuild the tutorial with `make -C docs html` and check
   how your changes look. 

6. To modify the cookiecutter template, edit files in `{{
   cookiecutter.repo_name }}/`. To check how these changes impact the template,
   reissue the commands:
   ```bash
   ./run_cookiecutter_example.py 
   ./copy_user_content.sh 
   pip install -e example/
   ```

   Then, navigate into the `example/` directory and see if your expected change
   is there. Depending on your change, you might need to deactivate your
   current virtual environment and create one fresh in the `example/` directory
   to test the template there. 

   ```bash
   deactivate
   cd example
   python -m venv venv
   . venv/bin/activate
   pip install --upgrade -r requirements.txt
   pip install -r requirements-dev.txt # note the additional requirements file if you are adding something here
   pip install -e .
   make -C docs html # if you want to see what the docs for a new project will look like
   ```

   If you have an automated way of checking the project that has been created,
   that would be a welcome contribution to this project :)

6. Commit your changes and push your branch to GitHub:

   ```bash
   git add <file_list>
   git commit -m "Your detailed description of your changes."
   git push origin name-of-your-bugfix-or-feature
   ```

7. Submit a pull request through the GitHub website.


# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at

```
email bielsnohr (aka Matt):
matthew dot bluteau at ukaea dot uk 
```

All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available
at [https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

