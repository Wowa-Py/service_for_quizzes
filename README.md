# service_for_quizzes
FastAPI web service: The service must implement a REST API that accepts POST requests with the contents of the form {"questions_num": integer}. 

# Tasks:

1. Using Docker (preferably docker-compose), deploy an image from any sensory DBMS (preferably PostgreSQL). Provide all the necessary scripts and configuration (docker/compose) files for deploying the DBMS, as well as instructions for connecting to it. It is necessary to ensure data safety when restarting the container (that is, use volumes to store DBMS files on the host machine.


2. Implement a simple web service in Python3 (using FastAPI or Flask, for example) that performs the following functions:

+ The service must implement a REST API that accepts an input POST request with content like {"questions_num": integer} ;

+ After receiving the request, the service, in turn, requests from the public API (Russian-language questions for quizzes) https://jservice.io/api/random?count=1 the number of questions specified in the received request.

+ Next, the received answers must be saved in the database from step 1, the storage location must contain at least the following information (names of columns and types that you can select yourself, and also add your own columns): 1. Question ID, 2. Question text, 3. Text of the answer, 4. - Date the question was created. If there is the same question in the database, additional requests must be made to the public API with quizzes until a unique question for the quiz is received.

+ The answer to the request under clause 2.a must be a saved question for the quiz. If enabled, it is an empty object.

3. The repository with the task must contain instructions for assembling a docker image with the service from step 2., configuring it and launching it. And also an example of a request to the POST API service.

4. It is advisable that if you use docker-compose, SqlAalchemy when executing the task, use the type annotatio

   

# Задачи:

1. С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL). Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД, а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера (то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.


2. Реализовать на Python3 простой веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:

+ В сервисе должно быть реализовано REST API, принимающее на вход POST запросы с содержимым вида {"questions_num": integer}  ;

+ После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.

+ Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.

+ Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

3. В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.

4. Желательно, если при выполнении задания вы будете использовать docker-compose, SqlAalchemy,  пользоваться аннотацией типов.
