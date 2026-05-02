{% macro get_mode(table_name, column_name) %}

(
    SELECT {{ column_name }}
    FROM {{ table_name }}
    GROUP BY {{ column_name }}
    ORDER BY COUNT(*) DESC
    LIMIT 1
)

{% endmacro %}