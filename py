python3 -c "
import serial, time
try:
    s = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    s.write(b'\r\nAT+KSTRING=0,3\r\n')
    time.sleep(0.5)
    print('Yanıt:', s.read_all().decode(errors='ignore'))
    s.close()
except Exception as e:
    print('Hata:', e)
"
