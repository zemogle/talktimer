from setuptools import setup

setup(
    name='are_you_still_talking',
    version='0.3',
    packages=['session_chair'],
    install_requires=[
        'blink1',
        'Click',
        'pyusb==1.0.b1',
    ],
    entry_points='''
        [console_scripts]
        are_you_still_talking=session_chair:blink_timer
    ''',

classifiers=[

    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
],


)
