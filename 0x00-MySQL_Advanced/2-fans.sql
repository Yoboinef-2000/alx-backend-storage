-- This ranks country origins of bands, 
-- ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) AS Lfans
FROM bands
GROUP BY origin
ORDER BY Lfans DESC;