show tables;
select * from 고객;

select 고객번호, 담당자명 AS 이름, 마일리지*100 점수 FROM 고객
WHERE 도시 = '서울특별시' ORDER BY 담당자명 asc;

select 고객번호, 담당자명 AS 이름, 마일리지 점수 FROM 고객
where 도시 = '서울특별시' order by 마일리지 desc limit 3;

select 고객번호, 담당자명 AS 이름, 마일리지 점수 FROM 고객
WHERE 도시 = '서울특별시' limit 3 order by 마일리지 desc;

SELECT * FROM 고객;

SELECT 도시 FROM 고객;
SELECT DISTINCT 도시 FROM 고객;

SELECT 23 + 5 AS 더하기
	  ,23 - 5 AS 빼기
      ,23 * 5 AS 곱하기
      ,23 / 5 AS 실수나누기
      ,23 DIV 5 AS 정수나누기
      ,23 % 5 AS 나머지1
      ,23 MOD 5 AS 나머지2;
      
SELECT 23 >= 5
	  ,23 <= 5
      ,23 > 23
      ,23 < 23
      ,23 = 23
      ,23 != 23
      ,23 <> 23;
      
SELECT * FROM 고객;
WHERE 담당자직위 <> '대표 이사';

SELECT * FROM 고객;
WHERE 도시 = '부산광역시'
AND 마일리지 < 1000

SELECT DISTINCT 도시 FROM 고객;
SELECT * FROM 고객;
 
SELECT 고객번호 from 고객;
SELECT 담당자명 from 고객;
SELECT 마일리지 from 고객;
SELECT 도시 from 고객;

WHERE 도시 = '부산광역시'
UNION
SELECT 고객번호
	  ,담당자명
      ,마일리지
      ,도시
FROM 고객;
WHERE 마일리지 < 1000
ORDER BY 1;

SELECT *
FROM 고객;
WHERE 지역 IS NULL;

SELECT *
FROM 고객;
WHERE 지역 = ' ';


SELECT 고객번호 FROM 고객;
SELECT 담당자명 FROM 고객;
SELECT 담당자직위 FROM 고객;
WHERE 담당자직위 = '영업 과장'
OR 담당자직위 = '마케팅 과장';

SELECT *
FROM 고객
WHERE 도시 LIKE '%광역시'
AND (고객번호 LIKE '_C%' OR 고객번호 LIKE '__C%');

SELECT *
FROM 고객
WHERE 고객회사명 REGEXP '푸드';

SELECT CHAR_LENGTH('HELLO')
	  ,LENGTH('HELLO')
      ,CHAR_LENGTH('안녕')
      ,LENGTH('안녕');
      
SELECT CONCAT('DREAMS', 'COME', 'TRUE')
      ,CONCAT_WS('-', '2023', '01', '29')
      ,CONCAT_WS(' ', 도시, 주소) 주소 FROM 고객;
SELECT DISTINCT left(담당자명, 1) FROM 고객;
SELECT count(DISTINCT left(담당자명, 1)) FROM 고객;

SELECT count(*) FROM 고객;
      
SELECT LEFT('SQL 완전정복', 3)
      ,RIGHT('SQL 완전정복', 4)
      ,SUBSTR('SQL 완전정복', 2, 5)
      ,SUBSTR('SQL 완전정복', 2);
      
SELECT substring_index('서울시 동작구 흑석로', ' ', 2)
      ,substring_index('서울시 동작구 흑석로', ' ', -2);
      
SELECT LPAD('SQL', 10, '#')
      ,RPAD('SQL', 5, '*');
      
SELECT TRIM(BOTH 'abc' FROM 'abcSQLabcabc')
      ,TRIM(LEADING 'abc' FROM 'abcSQLabcabc')
      ,TRIM(TRAILING 'abc' FROM 'abcSQLabcabc');
      
SELECT REPLACE('010-1234-5678', '.', '-');

SELECT * FROM 고객;
SELECT replace(전화번호, ')', '-') FROM 고객

SELECT CEILING(123.56)
      ,FLOOR(123.56)
      ,ROUND(123.56);
      
SELECT ABS(-120)
      ,ABS(120)
      ,SIGN(-120)
      ,SIGN(120);
      
SELECT POWER(2, 3)
      ,SQRT(16)
      ,RAND()
      ,RAND(100)
      ,ROUND(RAND() * 100);