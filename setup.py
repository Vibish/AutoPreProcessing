from setuptools import setup

setup(name='AutoPreProcessing',
      version='1.0.0',
      description='Pre Process the data by doing various exploratory data analysis and Statistical Test',
      url='https://github.com/bhagatsajan0073/AutoPreProcessing',
      author=['Kunjithapatham Sivakumar','Sajan Kumar'],
      author_email=["bhagat.sajan0073@gmail.com"],
      license='MIT',
      packages=['AutoPreProcessing'],
      install_requires=[
          'pandas',
          'numpy',
          'Jinja2',
          'scipy',
          'seaborn',
          'matplotlib',
          'statsmodels',
          'sklearn'
      ],
      include_package_data=True,
      zip_safe=False)
