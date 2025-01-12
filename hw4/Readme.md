#### ДЗ4
Проект состоит из/включает все требования:
- 5 Deployment(kafka, zookeeper, akhq, producer, consumer)
- 2 кастомных образа
- Deployment producer.yaml содержит в себе контейнер и инит-контейнер
- 2 Deployment содержит Volume(kafka-pv и logs-pv)
- Использование ConfigMap
- 3 Service(akhq-service, kafka-service, zookeeper-service)
- добавлены Liveness и Readiness проба в Deployment akhq.yaml
- используется почти в каждом файле

### Запуск проекта
```bash
minikube start
```
Каждый файл представляет цельное приложение со всеми нужными для него манифестами
Создано 2 namespace:
1. Очередь сообщений(kafka)
```bash
kubectl apply -f ./manifests/kafka.yaml
```
UI интерфейс для kafka
```bash
kubectl apply -f ./manifests/akhq.yaml
```
2. Продюсер и сабскрайбер
Билдим образ:
```bash
docker build -t app_init_consumer:latest -f ./old_system/Dockerfile_consumer ./old_system
docker build -t app_init_producer:latest -f ./old_system/Dockerfile_producer ./old_system
```
Пуллим образ в миникуб
```bash
minikube image load app_init_consumer:latest
minikube image load app_init_producer:latest
```
Запускаем сервисы
```bash
kubectl apply -f ./manifests/producer.yaml
kubectl apply -f ./manifests/consumer.yaml
```
### Скриншоты работы:
запуск миникуба
![img.png](old_system/images/img.png)
Запускам очередь сообщений(kafka)
![img.png](img_1.png)
Запускам UI интерфейс для kafka
![img.png](img.png)
Билдим образы:
![img_2.png](img_2.png)
![img_3.png](img_3.png)
Пуллим образ в миникуб
![img_4.png](img_4.png)
![img_5.png](img_5.png)
Запускаем сервисы
![img_6.png](img_6.png)
![img_7.png](img_7.png)
### Результаты
namespace default(с инит контейнером)
![img_8.png](img_8.png)
namespace kafka
![img_9.png](img_9.png)
Можем стянуть с миникуба данные с volume
![img_10.png](img_10.png)
![img_11.png](img_11.png)
p.s minikube mount не работает на arm системе(много гуглил, подошло только через docker cp)