{% test negative_values(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} > 0
{% endtest %}

{% test negative_values_0(model, column_name) %}
    SELECT *
    FROM {{ model }}
    WHERE {{ column_name }} >= 0
{% endtest %}