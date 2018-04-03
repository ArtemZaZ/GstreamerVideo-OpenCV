# GstreamerVideo-OpenCV
Модуль-переходник Gstreamer(rtcp прием)->OpenCV
## Import
Чтобы импортировать данный модуль необходимо в файле программы ввести
```
import GstCV
```
## Связь
Т.к. видео передается через rtcp, необходимо указать ip(передающего устройства) и порты для связи
```
IP = '127.0.0.1'
RTP_RECV_PORT0 = 5000
RTCP_RECV_PORT0 = 5001
RTCP_SEND_PORT0 = 5005
```
## CVGstreamer 
Класс предоставляющий методы для работы с видеопотоком gstreamera, возможность выхватывать из потока
изображение и отправлять в OpenCV. В качастве параметров передаются ip, порты, какой нужен кодек(**'JPEG' или 'H264'**).                
Параметр **toAVS** определяет куда будет стримиться видео в autovideosink(**True**) или в appsink(**False**)
Если видео стримится в autovideosink, то оно отображается на экране через стандартный элемент gstreamer'a, переменная **cvImage** 
при этом равна **None**.
Если видео стримится в appsink, то его кадры записываются в переменную **cvImage** и должны быть отображены самостоятельно.

```
CVG=GstCV.CVGstreamer(IP, RTP_RECV_PORT0, RTCP_RECV_PORT0, RTCP_SEND_PORT0, codec='H264', toAVS=True)
```
## Методы
### video pipeline
Запуск видео
```
video.start()
```
Пауза
```
video.paused()
```
Остановка метода с освобождением ресурсов
```
video.stop()
```
Перевод потока видео в appsink
```
video.toAppSink()
```
Перевод потока видео в autovideosink
```
video.toAutoVideoSink()
```

## OpenCV
Изображение, полученное с Gstreamera и переведенное в CV хранится в переменной **cvImage** экземпляра класса CVGstreamer
```
CVG.cvImage
```
Если изображение еще не получено, оно равняется None
Пример работы с модулем в файле testcv3.py   
