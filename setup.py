from setuptools import setup

setup(
    name='are_you_still_talking',
    version='0.1',
    packages=['session_chair'],
    install_requires=[
        'Click',
        'pyusb==1.0.b1',
        'blink1'
    ],
    entry_points='''
        [console_scripts]
        are_you_still_talking=session_chair:blink_timer
    ''',
)
