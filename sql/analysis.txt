Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.46 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> USE student_performance;
Database changed
mysql> SHOW TABLES;
+-------------------------------+
| Tables_in_student_performance |
+-------------------------------+
| student_performance           |
+-------------------------------+
1 row in set (0.00 sec)

mysql> DESCRIBE student_performance;
+----------------------------+-------------+------+-----+---------+-------+
| Field                      | Type        | Null | Key | Default | Extra |
+----------------------------+-------------+------+-----+---------+-------+
| Hours_Studied              | int         | YES  |     | NULL    |       |
| Attendance                 | int         | YES  |     | NULL    |       |
| Parental_Involvement       | varchar(20) | YES  |     | NULL    |       |
| Access_to_Resources        | varchar(20) | YES  |     | NULL    |       |
| Extracurricular_Activities | varchar(10) | YES  |     | NULL    |       |
| Sleep_Hours                | int         | YES  |     | NULL    |       |
| Previous_Scores            | int         | YES  |     | NULL    |       |
| Motivation_Level           | varchar(20) | YES  |     | NULL    |       |
| Internet_Access            | varchar(10) | YES  |     | NULL    |       |
| Tutoring_Sessions          | int         | YES  |     | NULL    |       |
| Family_Income              | varchar(20) | YES  |     | NULL    |       |
| Teacher_Quality            | varchar(20) | YES  |     | NULL    |       |
| School_Type                | varchar(20) | YES  |     | NULL    |       |
| Peer_Influence             | varchar(20) | YES  |     | NULL    |       |
| Physical_Activity          | int         | YES  |     | NULL    |       |
| Learning_Disabilities      | varchar(10) | YES  |     | NULL    |       |
| Parental_Education_Level   | varchar(30) | YES  |     | NULL    |       |
| Distance_from_Home         | varchar(20) | YES  |     | NULL    |       |
| Gender                     | varchar(10) | YES  |     | NULL    |       |
| Exam_Score                 | int         | YES  |     | NULL    |       |
+----------------------------+-------------+------+-----+---------+-------+
20 rows in set (0.00 sec)

mysql> SELECT COUNT(*) AS Total_Students FROM student_performance;
+----------------+
| Total_Students |
+----------------+
|           6607 |
+----------------+
1 row in set (0.00 sec)

mysql> SELECT * FROM student_performance LIMIT 10;
+---------------+------------+----------------------+---------------------+----------------------------+-------------+-----------------+------------------+-----------------+-------------------+---------------+-----------------+-------------+----------------+-------------------+-----------------------+--------------------------+--------------------+--------+------------+
| Hours_Studied | Attendance | Parental_Involvement | Access_to_Resources | Extracurricular_Activities | Sleep_Hours | Previous_Scores | Motivation_Level | Internet_Access | Tutoring_Sessions | Family_Income | Teacher_Quality | School_Type | Peer_Influence | Physical_Activity | Learning_Disabilities | Parental_Education_Level | Distance_from_Home | Gender | Exam_Score |
+---------------+------------+----------------------+---------------------+----------------------------+-------------+-----------------+------------------+-----------------+-------------------+---------------+-----------------+-------------+----------------+-------------------+-----------------------+--------------------------+--------------------+--------+------------+
|            23 |         84 | Low                  | High                | No                         |           7 |              73 | Low              | Yes             |                 0 | Low           | Medium          | Public      | Positive       |                 3 | No                    | High School              | Near               | Male   |         67 |
|            19 |         64 | Low                  | Medium              | No                         |           8 |              59 | Low              | Yes             |                 2 | Medium        | Medium          | Public      | Negative       |                 4 | No                    | College                  | Moderate           | Female |         61 |
|            24 |         98 | Medium               | Medium              | Yes                        |           7 |              91 | Medium           | Yes             |                 2 | Medium        | Medium          | Public      | Neutral        |                 4 | No                    | Postgraduate             | Near               | Male   |         74 |
|            29 |         89 | Low                  | Medium              | Yes                        |           8 |              98 | Medium           | Yes             |                 1 | Medium        | Medium          | Public      | Negative       |                 4 | No                    | High School              | Moderate           | Male   |         71 |
|            19 |         92 | Medium               | Medium              | Yes                        |           6 |              65 | Medium           | Yes             |                 3 | Medium        | High            | Public      | Neutral        |                 4 | No                    | College                  | Near               | Female |         70 |
|            19 |         88 | Medium               | Medium              | Yes                        |           8 |              89 | Medium           | Yes             |                 3 | Medium        | Medium          | Public      | Positive       |                 3 | No                    | Postgraduate             | Near               | Male   |         71 |
|            29 |         84 | Medium               | Low                 | Yes                        |           7 |              68 | Low              | Yes             |                 1 | Low           | Medium          | Private     | Neutral        |                 2 | No                    | High School              | Moderate           | Male   |         67 |
|            25 |         78 | Low                  | High                | Yes                        |           6 |              50 | Medium           | Yes             |                 1 | High          | High            | Public      | Negative       |                 2 | No                    | High School              | Far                | Male   |         66 |
|            17 |         94 | Medium               | High                | No                         |           6 |              80 | High             | Yes             |                 0 | Medium        | Low             | Private     | Neutral        |                 1 | No                    | College                  | Near               | Male   |         69 |
|            23 |         98 | Medium               | Medium              | Yes                        |           8 |              71 | Medium           | Yes             |                 0 | High          | High            | Public      | Positive       |                 5 | No                    | High School              | Moderate           | Male   |         72 |
+---------------+------------+----------------------+---------------------+----------------------------+-------------+-----------------+------------------+-----------------+-------------------+---------------+-----------------+-------------+----------------+-------------------+-----------------------+--------------------------+--------------------+--------+------------+
10 rows in set (0.00 sec)

mysql> SELECT ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score FROM student_performance;
+--------------------+
| Average_Exam_Score |
+--------------------+
|              67.24 |
+--------------------+
1 row in set (0.01 sec)

mysql> SELECT Motivation_Level, COUNT(*) AS Student_Count, ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score FROM student_performance GROUP BY Motivation_Level ORDER BY Average_Exam_Score DESC;
+------------------+---------------+--------------------+
| Motivation_Level | Student_Count | Average_Exam_Score |
+------------------+---------------+--------------------+
| High             |          1319 |              67.70 |
| Medium           |          3351 |              67.33 |
| Low              |          1937 |              66.75 |
+------------------+---------------+--------------------+
3 rows in set (0.01 sec)

mysql> SELECT Parental_Involvement, COUNT(*) AS Student_Count, ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score FROM student_performance GROUP BY Parental_Involvement ORDER BY Average_Exam_Score DESC;
+----------------------+---------------+--------------------+
| Parental_Involvement | Student_Count | Average_Exam_Score |
+----------------------+---------------+--------------------+
| High                 |          1908 |              68.09 |
| Medium               |          3362 |              67.10 |
| Low                  |          1337 |              66.36 |
+----------------------+---------------+--------------------+
3 rows in set (0.01 sec)

mysql> SELECT    Access_to_Resources,    COUNT(*) AS Student_Count,    ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score FROM student_performance GROUP BY Access_to_Resources ORDER BY Average_Exam_Score DESC;
+---------------------+---------------+--------------------+
| Access_to_Resources | Student_Count | Average_Exam_Score |
+---------------------+---------------+--------------------+
| High                |          1975 |              68.09 |
| Medium              |          3319 |              67.13 |
| Low                 |          1313 |              66.20 |
+---------------------+---------------+--------------------+
3 rows in set (0.01 sec)

mysql> SELECT    Teacher_Quality,    COUNT(*) AS Student_Count,    ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score FROM student_performance GROUP BY Teacher_Quality ORDER BY Average_Exam_Score DESC;
+-----------------+---------------+--------------------+
| Teacher_Quality | Student_Count | Average_Exam_Score |
+-----------------+---------------+--------------------+
| High            |          1947 |              67.68 |
| Medium          |          4003 |              67.10 |
| Low             |           657 |              66.75 |
+-----------------+---------------+--------------------+
3 rows in set (0.01 sec)

mysql> SELECT
    ->     CASE
    ->         WHEN Attendance < 70 THEN 'Low Attendance'
    ->         WHEN Attendance < 85 THEN 'Moderate Attendance'
    ->         ELSE 'High Attendance'
    ->     END AS Attendance_Category,
    ->     COUNT(*) AS Student_Count,
    ->     ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score
    -> FROM student_performance
    -> GROUP BY Attendance_Category
    -> ORDER BY Average_Exam_Score DESC;
+---------------------+---------------+--------------------+
| Attendance_Category | Student_Count | Average_Exam_Score |
+---------------------+---------------+--------------------+
| High Attendance     |          2511 |              69.69 |
| Moderate Attendance |          2523 |              66.68 |
| Low Attendance      |          1573 |              64.21 |
+---------------------+---------------+--------------------+
3 rows in set (0.01 sec)

mysql> SELECT    Internet_Access,    COUNT(*) AS Student_Count,    ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score FROM student_performance GROUP BY Internet_Access ORDER BY Average_Exam_Score DESC;
+-----------------+---------------+--------------------+
| Internet_Access | Student_Count | Average_Exam_Score |
+-----------------+---------------+--------------------+
| Yes             |          6108 |              67.29 |
| No              |           499 |              66.53 |
+-----------------+---------------+--------------------+
2 rows in set (0.01 sec)

mysql> SELECT
    ->     School_Type,
    ->     COUNT(*) AS Student_Count,
    ->     ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score
    -> FROM student_performance
    -> GROUP BY School_Type
    -> ORDER BY Average_Exam_Score DESC;
+-------------+---------------+--------------------+
| School_Type | Student_Count | Average_Exam_Score |
+-------------+---------------+--------------------+
| Private     |          2009 |              67.29 |
| Public      |          4598 |              67.21 |
+-------------+---------------+--------------------+
2 rows in set (0.01 sec)

mysql> SELECT
    ->     Tutoring_Sessions,
    ->     COUNT(*) AS Student_Count,
    ->     ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score
    -> FROM student_performance
    -> GROUP BY Tutoring_Sessions
    -> ORDER BY Tutoring_Sessions;
+-------------------+---------------+--------------------+
| Tutoring_Sessions | Student_Count | Average_Exam_Score |
+-------------------+---------------+--------------------+
|                 0 |          1513 |              66.49 |
|                 1 |          2179 |              66.98 |
|                 2 |          1649 |              67.57 |
|                 3 |           836 |              67.89 |
|                 4 |           301 |              68.23 |
|                 5 |           103 |              69.06 |
|                 6 |            18 |              71.67 |
|                 7 |             7 |              69.86 |
|                 8 |             1 |              69.00 |
+-------------------+---------------+--------------------+
9 rows in set (0.01 sec)

mysql> SELECT
    ->     Hours_Studied,
    ->     COUNT(*) AS Student_Count,
    ->     ROUND(AVG(Exam_Score), 2) AS Average_Exam_Score
    -> FROM student_performance
    -> GROUP BY Hours_Studied
    -> ORDER BY Hours_Studied;
+---------------+---------------+--------------------+
| Hours_Studied | Student_Count | Average_Exam_Score |
+---------------+---------------+--------------------+
|             1 |             3 |              71.00 |
|             2 |             6 |              63.00 |
|             3 |            12 |              61.33 |
|             4 |            17 |              61.65 |
|             5 |            21 |              62.86 |
|             6 |            17 |              63.47 |
|             7 |            51 |              64.35 |
|             8 |            58 |              64.16 |
|             9 |            86 |              64.16 |
|            10 |            94 |              64.39 |
|            11 |           146 |              64.98 |
|            12 |           192 |              64.77 |
|            13 |           218 |              64.72 |
|            14 |           269 |              65.58 |
|            15 |           315 |              65.59 |
|            16 |           351 |              66.18 |
|            17 |           381 |              66.33 |
|            18 |           401 |              67.04 |
|            19 |           441 |              66.96 |
|            20 |           465 |              66.95 |
|            21 |           431 |              67.68 |
|            22 |           402 |              67.48 |
|            23 |           411 |              68.18 |
|            24 |           357 |              68.19 |
|            25 |           289 |              68.85 |
|            26 |           263 |              68.67 |
|            27 |           229 |              69.46 |
|            28 |           171 |              69.61 |
|            29 |           134 |              70.28 |
|            30 |           123 |              70.62 |
|            31 |            77 |              70.69 |
|            32 |            54 |              70.94 |
|            33 |            40 |              70.03 |
|            34 |            29 |              70.72 |
|            35 |            20 |              71.80 |
|            36 |            11 |              71.18 |
|            37 |             6 |              73.33 |
|            38 |             7 |              72.71 |
|            39 |             7 |              74.71 |
|            43 |             1 |              78.00 |
|            44 |             1 |              71.00 |
+---------------+---------------+--------------------+
41 rows in set (0.01 sec)

mysql> SELECT COUNT(*) AS High_Performing_Students FROM student_performance WHERE Exam_Score >= 80;
+--------------------------+
| High_Performing_Students |
+--------------------------+
|                       48 |
+--------------------------+
1 row in set (0.01 sec)

mysql> SELECT COUNT(*) AS High_Attendance_High_Performance FROM student_performance WHERE Attendance >= 85  AND Exam_Score >= 80;
+----------------------------------+
| High_Attendance_High_Performance |
+----------------------------------+
|                               17 |
+----------------------------------+
1 row in set (0.01 sec)

mysql>