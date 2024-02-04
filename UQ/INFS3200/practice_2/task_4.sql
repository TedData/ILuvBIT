/*Task 4*/

SELECT c.class_short_description AS class, p.department_long_descript AS dept, t.calendar_quarter_long_de AS qtr, ROUND(s.sales) AS sales FROM PRODUCT_STANDARD_VIEW p, SALES_CUBE_VIEW s, CHANNEL_SALES_CHANNEL_VIEW c, TIME_CALENDAR_VIEW t, GEOGRAPHY_REGIONAL_VIEW g WHERE (c.DIM_KEY = s.CHANNEL AND g.DIM_KEY = s.GEOGRAPHY AND p.dim_key = s.product AND t.DIM_KEY = s.TIME AND c.LEVEL_NAME = 'CLASS' AND p.LEVEL_NAME = 'DEPARTMENT' AND s.geography = 'ALL_REGIONS' AND t.LEVEL_NAME = 'CALENDAR_QUARTER' AND t.CALENDAR_YEAR = 'CY2009') ORDER BY class, dept, qtr;
