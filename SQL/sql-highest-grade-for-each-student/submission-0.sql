WITH
    student_ranks as (
        SELECT
            student_id,
            exam_id,
            score,
            RANK() OVER(PARTITION BY student_id ORDER BY score desc, exam_id asc) as ranks
        FROM exam_results
    )

SELECT 
    student_id,
    exam_id,
    score
from student_ranks
where ranks = 1