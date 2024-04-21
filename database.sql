USE db_test;

-- 중복된 좌표값을 식별하여 삭제
DELETE c1
FROM coordinates c1
JOIN coordinates c2 ON c1.latitude = c2.latitude AND c1.longitude = c2.longitude
WHERE c1.id > c2.id;

-- 좌표값과 함께 id도 표시
SELECT id, ROUND(latitude, 2) AS latitude, ROUND(longitude, 2) AS longitude
FROM coordinates;

