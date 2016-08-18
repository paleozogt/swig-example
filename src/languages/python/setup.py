from setuptools import setup, dist


class BinaryDistribution(dist.Distribution):
    def is_pure(self):
        return False
    def has_ext_modules(self):
        return True

setup(
    name='@PYTHON_PACKAGE@',
    version='@VERSION@',
    author='Foobar, Inc',
    packages=['@PYTHON_PACKAGE@'],
    distclass=BinaryDistribution,
    include_package_data=True
)
