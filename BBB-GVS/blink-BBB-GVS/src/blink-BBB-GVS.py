import Adafruit_BBIO.GPIO as GPIO
import time

J8 = "P9_30"
J9 = "P9_27"
J10 = "P9_23"
J11_3 = "P9_24"
J11_4 = "P9_26"
J12_3 = "P9_21"
J12_4 = "P9_22"
J14 = "P9_15"
J15 = "P9_12"
J16_3 = "P9_13"
J16_4 = "P9_11"
J17 = "P8_26"
J18 = "P8_19"
J19 = "P8_18"
J20 = "P8_17"
J21 = "P8_16"
J22 = "P8_15"
J25 = "P8_13"
J26 = "P8_14"
J27 = "P8_11"
J28 = "P8_12"
J29 = "P8_9"
J30 = "P8_8"
J31 = "P8_7"
J32 = "P8_10"

D0 = "P9_30"
D16 = "P9_27"
D1 = "P9_23"
D17 = "P9_24"
D2 = "P9_26"
D18 = "P9_21"
D3 = "P9_22"
D19 = "P9_15"
D4 = "P9_12"
D20 = "P9_13"
D5 = "P9_11"
D21 = "P8_26"
D6 = "P8_19"
D22 = "P8_18"
D7 = "P8_17"
D23 = "P8_16"
D8 = "P8_15"
D24 = "P8_13"
D9 = "P8_14"
D25 = "P8_11"
D10 = "P8_12"
D26 = "P8_9"
D11 = "P8_8"
D27 = "P8_7"
D12 = "P8_10"

def blinkLEDHigh(channel):
	GPIO.output(channel, GPIO.HIGH)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.LOW)
	
def blinkLEDLow(channel):
	GPIO.output(channel, GPIO.LOW)
	time.sleep(0.25)
	GPIO.output(channel, GPIO.HIGH)
	
GPIO.setup(D0, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
GPIO.setup(D3, GPIO.OUT)
GPIO.setup(D4, GPIO.OUT)
GPIO.setup(D5, GPIO.OUT)
GPIO.setup(D6, GPIO.OUT)
GPIO.setup(D7, GPIO.OUT)
GPIO.setup(D8, GPIO.OUT)
GPIO.setup(D9, GPIO.OUT)
GPIO.setup(D10, GPIO.OUT)
GPIO.setup(D11, GPIO.OUT)
GPIO.setup(D12, GPIO.OUT)
GPIO.setup(D16, GPIO.OUT)
GPIO.setup(D17, GPIO.OUT)
GPIO.setup(D18, GPIO.OUT)
GPIO.setup(D19, GPIO.OUT)
GPIO.setup(D20, GPIO.OUT)
GPIO.setup(D21, GPIO.OUT)
GPIO.setup(D22, GPIO.OUT)
GPIO.setup(D23, GPIO.OUT)
GPIO.setup(D24, GPIO.OUT)
GPIO.setup(D25, GPIO.OUT)
GPIO.setup(D26, GPIO.OUT)
GPIO.setup(D27, GPIO.OUT)

while True:
	blinkLEDHigh(D0)
	blinkLEDHigh(D1)
	blinkLEDHigh(D2)
	blinkLEDHigh(D3)
	blinkLEDLow(D4)
	blinkLEDLow(D5)
	blinkLEDHigh(D6)
	blinkLEDHigh(D7)
	blinkLEDHigh(D8)
	blinkLEDHigh(D9)
	blinkLEDLow(D10)
	blinkLEDHigh(D11)
	blinkLEDHigh(D12)
	blinkLEDHigh(D27)
	blinkLEDHigh(D26)
	blinkLEDHigh(D25)
	blinkLEDHigh(D24)
	blinkLEDHigh(D23)
	blinkLEDHigh(D22)
	blinkLEDHigh(D21)
	blinkLEDHigh(D20)
	blinkLEDHigh(D19)
	blinkLEDHigh(D18)
	blinkLEDHigh(D17)
	blinkLEDHigh(D16)
