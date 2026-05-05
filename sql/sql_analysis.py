-- Top performing ads
SELECT ad_id, ctr
FROM ctr_metrics
ORDER BY ctr DESC;

-- Low CTR ads
SELECT ad_id, ctr
FROM ctr_metrics
WHERE ctr < 0.2;

-- Total impressions vs clicks
SELECT SUM(impressions), SUM(clicks)
FROM ctr_metrics;
