SELECT X, Y, Z,
    CASE
        WHEN X < Y + Z AND Y < X + Z AND Z < X + Y THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle