from setuptools import setup, find_packages

setup(name='simplisafe-ss3',
      version='0.1',
      description='Wrapper for the SimpliSafe SS3 API.',
      url='https://github.com/rottmanj/simplisafe-ss3',
      author='Jeremy Rottman',
      license='Apache License 2.0',
      install_requires=['requests>=2.18.4', 'requests-oauthlib>=0.8.0'],
      test_suite='tests',
      packages=find_packages(exclude=["dist", "*.test", "*.test.*", "test.*", "test"]),
      zip_safe=True)