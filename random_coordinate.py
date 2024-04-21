import mysql.connector
import random

def generate_random_coordinates():
    # 무작위 위도 및 경도 생성
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    return latitude, longitude

def is_coordinate_duplicate(cursor, latitude, longitude):
    # 좌표값이 이미 데이터베이스에 존재하는지 확인
    select_query = "SELECT COUNT(*) FROM coordinates WHERE latitude = %s AND longitude = %s"
    cursor.execute(select_query, (latitude, longitude))
    result = cursor.fetchone()[0]
    return result > 0

def save_coordinates_to_mysql(num_coordinates):
    # MySQL 서버 연결 설정
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="0811",
        database="DB_test"
    )

    # 커서 생성
    cursor = conn.cursor()

    # 무작위 좌표값 생성 및 저장
    for _ in range(num_coordinates):
        while True:
            # 새로운 좌표값 생성
            latitude, longitude = generate_random_coordinates()
            
            # 좌표값이 이미 데이터베이스에 존재하는지 확인
            if not is_coordinate_duplicate(cursor, latitude, longitude):
                insert_query = "INSERT INTO coordinates (latitude, longitude) VALUES (%s, %s)"
                cursor.execute(insert_query, (latitude, longitude))
                print(f"좌표값 ({latitude}, {longitude})이(가) 삽입되었습니다.")
                break
            else:
                print(f"좌표값 ({latitude}, {longitude})이(가) 이미 데이터베이스에 존재합니다. 다시 생성합니다.")

    # 변경사항 저장 및 연결 종료
    conn.commit()
    cursor.close()
    conn.close()

# 원하는 좌표 수
num_coordinates = 5

# 좌표값을 MySQL 데이터베이스에 저장
save_coordinates_to_mysql(num_coordinates)
