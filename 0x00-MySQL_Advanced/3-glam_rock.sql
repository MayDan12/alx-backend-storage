-- this lists all bands with Glam rock as their main style,
-- ranked by their longevity.
-- SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
SELECT band_name,
       YEAR('2022-01-01') - CAST(SUBSTRING_INDEX(formed, '-', 1) AS UNSIGNED) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
    