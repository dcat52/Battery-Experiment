import serial
import time
import sys

def main():
	print "entered main"
	# open serial device
	ser = serial.Serial('/dev/ttyACM0', 9600)
	print "connected to serial"

	print "beginning data collection"
	while True:
		try:
			#print "reading from serial..."
			val=ser.readline().rstrip()
			#print "val:",val
		
			t = time.time()			
			data = "%s, %s\n" % (val,t)
			print data
			with open('./data_battery.txt', 'a') as f:
				f.write(data)

		except KeyboardInterrupt:
			print "print user exiting"
			sys.exit()
		except:
			print "attempting to reconnect"
			ser = serial.Serial('/dev/ttyACM0',9600)
			pass

if __name__=="__main__":
	main()
