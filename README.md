# Are you still talking?

When I'm chairing a session at .Astronomy 8 or some other conference, I don't want to have to look at my watch. I want to just set a timer and the onus is on the speaker.

Use a [blink(1) light](https://blink1.thingm.com/) to control your speakers when you are chairing a session.

You will need a blink(1) light and python. Is that too much to ask? (maybe)

## Installation instructions
The blink(1) library is only Python 3 compatible and PyUSB 1.0.0 release version has a bug in it. My advice to use a virtualenv with this. You set it up as follows

Using [Anaconda](http://anaconda.io)
```
conda create -n blink python=3.4
source activate blink
```
Using `virtualenv`
```
virtualenv -p python3 env/blink
source env/blink/bin/activate
```
Then you can download this package and install with:
```
pip install talktimer-master/ # or whatever the directory name is that contains these files
```

## Usage instructions
After the package is installed you will have a command line script on your system path, which you can access from anywhere. If you installed with a virtual environment then you'll need to activate this first.

Example usage is:
```
are_you_still_talking --total 60 --warning 10 --seconds
```
- Total = total talk time
- Warning = Time before the end when the warning will compatible
- Seconds [optional] = When the numbers refer to seconds. If you leave this off, the numbers are in minutes.

## Troubleshooting
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

### 3. Access Denied
If you get the following:
```
usb.core.USBError: [Error 13] Access denied (insufficient permissions)
```
this is because you are using a Mac and `libusb1` has a bug in it (since 2011). In the requirements I make sure you get `pyusb`. Unfortunately `libusb1` gets installed by the `blink1` library and it seems these are in conflict.

Just uninstall `libusb1` and you should be fine:
```
pip uninstall libusb1
```
