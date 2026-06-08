SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '<' then l.value < r.value
        WHEN e.operator = '>' then l.value > r.value
        ELSE l.value = r.value
    END as value
FROM expressions e 
LEFT JOIN variables l
    on e.left_operand = l.name
LEFT JOIN variables r
    on e.right_operand = r.name