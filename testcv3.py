import GstCV
import cv2
import time
import threading

# IP = '192.168.42.14'
IP = '127.0.0.1'
RTP_RECV_PORT0 = 5000
RTCP_RECV_PORT0 = 5001
RTCP_SEND_PORT0 = 5005

CVG = GstCV.CVGstreamer(IP, RTP_RECV_PORT0, RTCP_RECV_PORT0, RTCP_SEND_PORT0, codec="JPEG", toAVS=True)

print("I started")
CVG.start()


def th():  # в отдельном потоке запускаем вывод изображения через openCV
    while True:
        if CVG.cvImage is not None:
            cv2.cvtColor(CVG.cvImage, cv2.COLOR_BGR2RGB)
            cv2.imshow("appsink image arr", CVG.cvImage)
            cv2.waitKey(1)
        else:
            time.sleep(1)


t = threading.Thread(target=th)
t.start()

time.sleep(10)
print("I go to AppSink!")
CVG.toAppSink()

