python3 -c "
import serial
import time

try:
    s = serial.Serial('/dev/ttyACM0', 115200, timeout=2)
    time.sleep(0.5)
    s.write(b'\r\nAT\r\n')
    time.sleep(1)
    res1 = s.read_all()
    print('AT Yanıtı:', res1)

    s.write(b'AT+KSTRING=0,3\r\n')
    time.sleep(1)
    res2 = s.read_all()
    print('FRP Komut Yanıtı:', res2)
    s.close()
except Exception as e:
    print('Hata:', e)
"
