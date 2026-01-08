SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id

# 런타임 400 ms
ORDER BY id ASC;

# 런타임 413 ms
-- ORDER BY author_id ASC;