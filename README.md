# 상세설명 추후 업데이트 예정



## DB_test.sql


데이터베이스를 생성 후 위도, 경도를 저장할 테이블을 만드는 코드





## database.sql


테이블 내의 좌표의 중복값을 제거해주는 코드, 

테이블 내에 저장되어 있는 좌표값을 소수점 2자리까지만 반올림하여 보여주는 코드






## random.coordinate.py

 
위도, 경도의 좌표값을 무작위로 생성하여 데이터베이스로 전송하는 코드
 

## DB 구현
> 밀리터리 데이터베이스 생성을 진행함. (최초 한 번 실행)
> ```mysql
> CREATE user "military"@"localhost" IDENTIFIED BY "1234";
> GRANT ALL PRIVILEGES ON military.* TO "military"@"localhost";
>
> CREATE DATABASE IF NOT EXISTS military;
> ```

> 목표물 위치 DB
> ```mysql
> drop table if exists coordinates;
> CREATE TABLE coordinates (
>    id INT AUTO_INCREMENT PRIMARY KEY,
>    latitude DECIMAL(9, 6),
>    longitude DECIMAL(9, 6)
> )comment ='The location of targets';
> ```

> 기체 위치 DB
> ```mysql
> DROP TABLE IF EXISTS location;
> CREATE TABLE location (
>     IS_GPS BOOL PRIMARY KEY,
>    latitude DECIMAL(9, 6),
>    longitude DECIMAL(9, 6)
>)comment ='current aircraft location';
>```