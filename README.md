# Repositorio de la sección 18 del curso Universidad Python

## 1. Instalar dependencias
`pip install flask flask-migrate flask-sqlalchemy flask-wtf pymysql python-dotenv`

## 2. Renomambrar el archivo .env.template por .env y completar con los datos de MySQL y secret key

`DB_USER=`

`DB_PASSWORD=`

`DB_HOST=localhost`

`DB_PORT=3306`

`DB_NAME=flask_academy_db`

`SECRET_KEY= `

## 3. En MySQL Workbench crear la base de datos con 
`CREATE DATABASE IF NOT EXISTS flask_academy_db;` y `SHOW DATABASES;` para ver si se creo correctamente

## 4. Iniciar la bd y crear la tabla
Ejecutar los comandos en la raiz del proyecto: `flask db init` y
`flask db migrate -m "Crear tabla curso"`

## 5. Actualizar la bd
`flask db upgrade`

## 6. Datos de prueba (opcional)
En Workbench: 

`USE flask_academy_db;`

`INSERT INTO curso (nombre, instructor, duracion)`

`VALUES
    ('Python desde cero', 'Juan Pérez', 20.00),
    ('Flask para principiantes', 'María López', 15.50),
    ('MySQL y bases de datos', 'Carlos Gómez', 12.00);`


    
