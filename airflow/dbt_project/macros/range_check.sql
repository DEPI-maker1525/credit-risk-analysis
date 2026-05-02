{% test range_check(model, column_name, n1, n2) %}
    SELECT * 
    FROM {{ model }}
    WHERE {{ column_name }} < {{ n1 }} OR {{ column_name }} > {{ n2 }}
{% endtest %}