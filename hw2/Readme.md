
# Лабораторная №2

### Описание
Проект состоит из pub, sub сервиса и очереди сообщений kafka(и зукипером к нему)
для sub/pub сервиса реализованы отдельные директории и dockerfil'ы

### Ответы на вопросы

1) Да, можно ограничить(начиная с версии 3.8):
   ```
   deploy:
     resources: #верхний предел
       limits:
         cpus: '0.50' # cpu
         memory: 500M # оперативка
       reservations: # гарантирует минимальное количество ресурсов
         cpus: '0.25'
         memory: 300M
   ```
2)  Пример:
   ```cmd
      docker-compose up service_name1 service_name2
   ```

3) Проверка на то, что сервис поднялся и работает можно сделать через **healthcheck**(пример в docker-compose)
