# Are you still talking?

When I'm chairing a session at .Astronomy 8 or some other conferece, I don't want to have to look at my watch. I want to just set a timer and the onus is on the speaker.

Use a [blink(1) light](https://blink1.thingm.com/) to control your speakers when you are chairing a session.

You will need a blink(1) light and python. Is that too much to ask? (maybe)

## Installation instructions
The blink(1) library is only Python 3 compatible and PyUSB 1.0.0 release version has a bug in it. My advice to use a virtualenv with this. You set it up as follows

Using [Anaconda](http://anaconda.io)
```
conda create -n blink python=3.4
source blink
```
Using `virtualenv`
```
virtualenv -p python3 env/blink
source env/blink/bin/activate
```
Then you can download this package and install with:
```
pip install blink_chair/
```

## FAQs
### 1. Blink1 module not found
If you get the following error:
```
ImportError: No module named 'blink1'
```
you probably installed the normal `python setup.py install` route. This doesn't install Blink1 properly.

### 2. No 'backend'
If you get the following error:
```
ValueError: No backend available
```
you have the wrong version of PyUSB. The released version `1.0.0` has a bug in it. You need to use version `1.0.b1`. To do that, do the following:
```
pip uninstall pyusb
pip install pyusb==1.0.b1
```
