python3 -c "
import serial
import time

s = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
s.reset_input_buffer()
s.reset_output_buffer()

s.write(b'\r\nAT\r\n')
time.sleep(0.5)
print('1. Yanıt:', s.read_all())

s.write(b'AT+KSTRING=0,3\r\n')
time.sleep(1)
print('2. Yanıt:', s.read_all())
s.close()
"
