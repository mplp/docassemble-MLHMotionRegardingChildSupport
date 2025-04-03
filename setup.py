import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.MLHMotionRegardingChildSupport',
      version='1.0.3',
      description=('A motion to change or get child support in Michigan'),
      long_description='# docassemble.MLHMotionRegardingChildSupport\r\n\r\nA motion to change or get child support in Michigan\r\n\r\n## Authors:\r\n* Bryce Willey\r\n* Emily Kress Miller\r\n\r\n## Changelog:\r\n* 2/13/25   1.0.3 Behind-the-scenes court logic adjustment\r\n* 12/17/24  1.0.2 Update forms\r\n* 9/30/24   1.0.1 add user survey\r\n* 9/18/24   1.0.0 preparing to go live',
      long_description_content_type='text/markdown',
      author='Bryce Willey',
      author_email='ekressmiller@lsscm.org',
      license='The MIT License (MIT)',
      url='https://michiganlegalhelp.org/resources/family/do-it-yourself-motion-change-or-get-child-support',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/MLHMotionRegardingChildSupport/', package='docassemble.MLHMotionRegardingChildSupport'),
     )

