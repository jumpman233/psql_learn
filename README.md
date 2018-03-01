#  psql_learn
## Description
1. A program of helping learning python and database. In this project, you will stretch your SQL database skills. You will get practice interacting with a live database both from the command line and from your code.
2. The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. Here are the questions the reporting tool should answer.
3. Questions:
    1. What are the most popular three articles of all time?
    2. Who are the most popular article authors of all time?
    3. On which days did more than 1% of requests lead to errors?
## Requirements
1. If you are Udacity FSND student, You can run the program in **Virtual machine**.
    - Vagrant
    - VirtualBox
    - Udacity FSND VM file
2. If you want to run the code in **local environment**.
    - python(2.7)
    - PostgreSQL
    - psycopg2

## Start
1. Configure Environment
    - **If you are Udacity FSND student**. Follow the guide as [this link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0#) to install Udacity FSND-virtual machine
    - **If you want to run the code in local environment**.
        1. Using terminal command to create a new database called **news**.
            ```psql```
            ```create database news```
        2. Get sql data in [this link](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
        3. Use command to insert data
           ```psql -d news -f newsdata.sql ```
2.  Run command ```python main.py```.
3.  You got it!
