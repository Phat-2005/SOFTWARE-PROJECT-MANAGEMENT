CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);

INSERT INTO notes (content)
SELECT 'Lab 2 Compose is working'
WHERE NOT EXISTS (SELECT 1 FROM notes);
