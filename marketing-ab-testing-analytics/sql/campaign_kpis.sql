SELECT variant,
       COUNT(*) FILTER (WHERE event='impression') impressions,
       COUNT(*) FILTER (WHERE event='click') clicks,
       COUNT(*) FILTER (WHERE event='purchase') purchases,
       SUM(spend) spend,
       SUM(revenue) revenue,
       SUM(revenue)/NULLIF(SUM(spend),0) roas
FROM campaign_events GROUP BY variant;

SELECT channel,
       COUNT(*) FILTER (WHERE event='purchase') purchases,
       SUM(spend) spend, SUM(revenue) revenue,
       SUM(revenue)/NULLIF(SUM(spend),0) roas
FROM campaign_events GROUP BY channel ORDER BY roas DESC;
