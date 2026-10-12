-- rank.sql
DROP VIEW IF EXISTS rank;

CREATE VIEW rank AS
SELECT
    class_name,
    SUM(score)            AS total_score,
    COUNT(*)              AS contest_count,
    ROUND(AVG(score), 4)  AS avg_score,
    RANK() OVER (ORDER BY SUM(score) DESC) AS rank
FROM Score_table
GROUP BY class_name;