#!/usr/bin/env python3
import pexpect

p = pexpect.spawn('cookiecutter .')

p.expect('full_name .*')
p.sendline('UKAEA')

p.expect('email .*')
p.sendline('rse@o365.ukaea.uk')

p.expect('vcs_domain .*')
p.sendline('git.ccfe.ac.uk')

p.expect('vcs_username .*')
p.sendline('soft-eng-group')

p.expect('project_name .*')
p.sendline('Example')

p.expect('package_dist_name .*')
p.sendline('')

p.expect('package_dir_name .*')
p.sendline('')

p.expect('repo_name .*')
p.sendline('')

p.expect('project_short_description .*')
p.sendline('')

p.expect('year .*')
p.sendline('')

p.expect('Select minimum_supported_python_version.*')
p.sendline('')

# Runs until the cookiecutter is done; then exits.
p.wait()
