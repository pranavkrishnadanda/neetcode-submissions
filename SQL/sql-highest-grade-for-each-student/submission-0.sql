select distinct on (e.student_id) student_id,e.exam_id,e.score

from exam_results e

order by student_id,score desc,exam_id