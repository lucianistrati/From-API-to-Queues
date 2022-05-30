FROM ubuntu:20.04.2

# START FAST API APP
CMD python main.py

# START POSTGRESQL TABLE POPULATION
CMD python table_script.py

# START RabbitMQ
CMD python broker_script.py

# START  Redis service
CMD python backend_script.py


