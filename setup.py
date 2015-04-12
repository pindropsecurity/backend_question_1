from setuptools import setup, find_packages


version = '1.0.0'

setup(name='summit',
      version=version,
      description="A node based math utility",
      long_description="""A node based math utility, and by node, it does not mean Node.js. A node in this case\
        represents a single element within a mathematical expression and houses children thereof.\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Greg Gullett',
      author_email='ggullett@ecsquest.com',
      url='',
      license='',
      packages=find_packages(exclude=['test']),
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      """,
      )
