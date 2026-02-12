SELECT genre, count
FROM netflix_analytics.genre_distribution
ORDER BY count DESC
LIMIT 10;
