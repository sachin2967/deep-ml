-- your query

SELECT date_trunc('month', review_date) as month, product_id, round(avg(stars),2) as avg_stars
from reviews
group by date_trunc('month', review_date), product_id;


