/* MariaDB에서 새로운 데이터베이스와 계정 생성하기
	: 오라클에서는 계정만 생성하면 되짐나 MySQL(MariaDB)에서는
	새로운 DB와 User를 동시에 생성한 후 권한설정을 해야한다. */
	
# 아래 작업은 root 계정으로 접속한 후 실행해야 함

# 새로운 데이터베이스 생성
CREATE DATABASE sample_db;
# 새로운 사용자 계정 생성(로컬에서만 접속할 수 있게 설정)
CREATE USER 'sample_user'@'localhost' IDENTIFIED BY '1234';
# sample_db를 사용할 수 있는 모든 권한을 sample_user에게 부여
GRANT ALL PRIVILEGES ON sample_db.* TO 'sample_user'@'localhost';
# 이 명령을 통해 위에서 설정한 사항을 MariaDB에 적용
FLUSH PRIVILEGES;

/* 블럭단위 주석은 Java와 동일하게 작성 */

# 라인단위 주석은 #

/* F9 : 현재 문서의 전체 쿼리문을 실행한다.
	Ctrl + F9 : 블럭으로 지정한 쿼리만 실행한다.
		만약 쿼리문의 절반 정도만 선택하면 에러가 발생한다.
	Ctrl + Shift + F9 : 현재 쿼리를 실행한다. 단, 마지막에 기술한
		세미콜론 안으로 커서를 옮긴 후 실행해야 한다. */


# 여기부터는 sample_user 계정으로 접속한 후 작성

/* 테이블 생성하기
	제약조건
		PRIMARY KEY : 기본키 지정. null 값이나 중복값을 가질 수 없는 컬럼으로 지정됨.
		AUTO_INCREMENT : 자동증가 컬럼으로 지정. 1씩 증가하는 순차적인 정수값이
			자동으로 입력됨. 오라클의 시퀀스와 유사함.
		UNSIGNED : 정수형 컬럼으로 지정하는 경우 음수는 사용하지 않고 양수의
			범위만 사용. 이때 양의 범위가 2배로 늘어남. */

# 1. 숫자형으로만 테이블 생성
CREATE TABLE tb_int (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	num1 TINYINT UNSIGNED NOT NULL,
	num2 smallint NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT,
	sample_db
	fnum1 FLOAT(10, 5) NOT NULL,
	fnum2 DOUBLE(20, 10) 
);
DESC tb_int;

/* 레코드 입력하기
	형식1 : 일련번호 idx 컬럼은 insert문에서 생략하고 작성한다.
		자동증가 컬럼으로 지정되었으므로 순차적인 번호가 자동으로 부여된다.
		즉, 자동증가 컬럼은 insert문에서 생략하는 것이 기본이다. */
INSERT INTO tb_int (num1, num2, num3, num4, fnum1, fnum2)
	VALUES (123, 12345, 1234567, 1234567890, 12345.12345, 1234567890.1234567890);

/* 형식2 : insert문 작성시 컬럼을 명시하지 않으면 전체 컬럼에 대해
		입력값을 기술해야 하므로 실행시 오류가 발생할 수 있어 권장하지 않는다. */
INSERT INTO tb_int
	VALUES (2, 123, 12345, 1234567, 1234567890, 12345.12345, 1234567890.1234567890);

SELECT * FROM tb_int;

# ---------------------------------------------------------------------- #

/* current_timestamp : 날짜형식으로 지정된 컬럼에 디폴트값으로 현재시각을 입력할
		때 사용한다.
	NOW() : 날짜형식으로 지정된 컬럼에 현재시각을 입력한다.
		초 단위까지의 시간이 입력된다. 오라클의 sysdate와 동일한 역할을 한다. */

# 2. 날짜형으로 구성된 테이블
CREATE TABLE tb_date (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT current_timestamp
);
DESC tb_date;

INSERT INTO tb_date (DATE1, DATE2) VALUES ('2023-02-25', NOW());
INSERT INTO tb_date (DATE1) VALUES ('2023-02-27');

SELECT * FROM tb_date;

# ---------------------------------------------------------------------- #

CREATE TABLE tb_string (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str2 text
);
DESC tb_string;

INSERT INTO tb_string (str1, str2) VALUES ('난 짧은글3', '난 엄청 긴글3');

SELECT * FROM tb_string;

# ---------------------------------------------------------------------- #

/* enum : 여러 항목 중 1개만 선택할 수 있는 타입.
		radio와 유사하다.
	set : 여러 항목 중 2개 이상을 선택할 수 있는 타입.
		checkbox와 유사함. */

# 4. 특수형
CREATE TABLE tb_spec (
	idx INT AUTO_INCREMENT,
	
	spec1 ENUM('M', 'W', 'T'),
	spec2 SET('A', 'B', 'C', 'D'),
	# 아웃 라인 방식으로 컬럼을 먼저 생성한 후 별도로 기본키를 지정함
	PRIMARY KEY (idx)
);

INSERT INTO tb_spec (spec1, spec2) VALUES ('W', 'A,B,C');

INSERT INTO tb_spec (spec1, spec2) VALUES ('X', 'A, B, C'); # spec1 에러
INSERT INTO tb_spec (spec1, spec2) VALUES ('M', 'X, B, C'); # spec2 에러

/* spec1 컬럼은 not null로 지정하지 않았으므로 null을 허용하는 컬럼으로 정의된다.
	따라서 값을 입력하지 않아도 된다. */
INSERT INTO tb_spec (spec2) VALUES ('B,C,D');

SELECT * FROM tb_spec;

# ---------------------------------------------------------------------- #

# 파이썬 실습을 위한 테이블 생성
CREATE TABLE board (
	num INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(100) NOT NULL,
	content TEXT NOT NULL, # 내용 : 긴 텍스트
	id VARCHAR(30) NOT NULL,
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP, # 작성일. 현재시각을 디폴트
	visitcount MEDIUMINT NOT NULL DEFAULT 0,
	PRIMARY KEY (num)
);

# 더미 데이터 입력. 일련번호 컬럼은 쿼리문에서 생략한 상태로 작성
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목1', '내용1입니다', 'korea', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목2', '내용2입니다', 'korea', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목3', '내용3입니다', 'korea', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목4', '내용4입니다', 'korea', NOW(), 0);
INSERT INTO board (title, content, id, postdate, visitcount)
	VALUES ('제목5', '내용5입니다', 'korea', NOW(), 0);

SELECT * FROM board;

CREATE TABLE phonebooks (
	idx INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(10) NOT NULL,
	phoneNum INT UNSIGNED NOT NULL,
	address VARCHAR(20) NOT null
);

DROP TABLE phonebooks;