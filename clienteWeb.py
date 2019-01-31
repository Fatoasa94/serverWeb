import pyfirmata
import urllib2
from threading import Timer
import time
import random

from pyfirmata import Arduino, util
board = Arduino('COM2')

it = util.Iterator (board)
it.start ()

A0 = board.get_pin('a:0:i')
val=A0.read()
print val

A1 = board.get_pin('a:1:i')
val1=A1.read()
print val1

def send_sensor(val):
        response = urllib2.urlopen('http://127.0.0.1:8080/?sensor='+str(val))
        #html = response.read()
        #print html

def send_sensor1(val1):
        response = urllib2.urlopen('http://127.0.0.1:8080/?sensor='+str(val1))
      
 
def _timer():
        
        val=A0.read()
        val1=A1.read()
        #print val
        print "sensor", '=', val
        print "sensor2", '=', val1
        
        send_sensor(val)
        send_sensor(val1)
        Timer(1, _timer, ()).start()
Timer(1, _timer, ()).start()

##        send_sensor(val1)
##        Timer(1, _timer, ()).start()
##Timer(1, _timer, ()).start()
