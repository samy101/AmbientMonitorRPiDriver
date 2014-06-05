import time
from twisted.python import log

from smap.driver import SmapDriver
from smap.util import periodicSequentialCall

class AmbientDriver(SmapDriver):
    def setup(self, opts):
	tz = opts.get('Properties/Timezone', 'Asia/Kolkata')
        self.add_timeseries('/Temperature', 'C', data_type='double', timezone=tz)
        self.rate = int(opts.get('Rate', 30))
        self.set_metadata('/', {
                'Instrument/SamplingPeriod' : str(self.rate),
                })
        self.counter = int(opts.get('StartVal', 0))

    def start(self):
        periodicSequentialCall(self.read).start(self.rate)

    def read(self):
        # *Code Snippet from http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/*
        # Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before.
        tfile = open("/sys/bus/w1/devices/28-000004a51f07/w1_slave")
        # Read all of the text in the file.
        text = tfile.read()
        # Close the file now that the text has been read.
        tfile.close()
        # Split the text with new lines (\n) and select the second line.
        secondline = text.split("\n")[1]
        # Split the line into words, referring to the spaces, and select the 10th word (counting from 0).
        temperaturedata = secondline.split(" ")[9]
        # The first two characters are "t=", so get rid of those and convert the temperature from a string to a number.
        temperature = float(temperaturedata[2:])
        # Put the decimal point in the right place and display it.
        temperature = temperature / 1000
        # * *

        if temperature < 0:
        	return;

        self.add('/Temperature', time.time(), float(temperature))
	self.counter += 1
