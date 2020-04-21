from distutils.core import setup
setup(
  name = 'decoyarg',
  packages = ['decoyarg'], 
  version = '0.1',  
  license='MIT', 
  description = 'a small library that wraps argparse to map arguments to decorated functions',
  author = 'nilput',                  
  author_email = 'nilputs@gmail.com',   
  url = 'https://github.com/nilput/decoyarg/',  
  download_url = 'MISSING', 
  keywords = ['argparse', 'arguments', 'cli'],
  install_requires=[        
          'argparse',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',     
    'Intended Audience :: Developers',    
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Environment :: Console',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
