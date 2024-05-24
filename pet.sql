CREATE TABLE petapi_comment (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES petapi_post(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
    text VARCHAR(200),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO petapi_comment (id, post_id, user_id, text, timestamp)
VALUES (1, 1, 1, 'This is a sample comment 1.', '2024-05-18T12:00:00Z');

CREATE TABLE petapi_like (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES petapi_post(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_like UNIQUE (post_id, user_id)
);

INSERT INTO petapi_like (id, post_id, user_id, timestamp)
VALUES (1, 1, 1, '2024-05-18T12:00:00Z');


DROP TABLE IF EXISTS petapi_postlikes;
DROP TABLE IF EXISTS petapi_comment;



ALTER TABLE petapi_comment
ADD COLUMN post_id INTEGER REFERENCES petapi_post(id) ON DELETE CASCADE;


ALTER TABLE petapi_post
ADD COLUMN comment_id INTEGER REFERENCES petapi_comment(id) ON DELETE CASCADE;


ALTER TABLE petapi_like
ADD COLUMN post_id INTEGER REFERENCES petapi_post(id) ON DELETE CASCADE;


CREATE TABLE petapi_post_comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES petapi_post(id) ON DELETE CASCADE,
    comment_id INTEGER REFERENCES petapi_comment(id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS petapi_post_comments;

INSERT INTO petapi_comment (id, post_id, user_id, text, timestamp)
VALUES
    (1, 1, 1, 'This is a sample comment 1.', '2024-05-18T12:00:00Z');

INSERT INTO petapi_post_comments (id,post_id, comment_id)
VALUES
    (1, 1, 1);


UPDATE petapi_post
SET comment_id = (
    CASE
        WHEN id = 1 THEN 1 
       
    END
)
WHERE id IN (1); 


CREATE TABLE petapi_post_likes (
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES petapi_post(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES auth_user(id) ON DELETE CASCADE,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_postlike UNIQUE (post_id, user_id)
);

INSERT INTO petapi_post_likes (id, post_id, user_id, timestamp)
VALUES (1, 1, 1, '2024-05-18T12:00:00Z');


ALTER TABLE petapi_post
ADD COLUMN like_id INTEGER REFERENCES petapi_like(id) ON DELETE CASCADE;


DROP TABLE IF EXISTS petapi_postlikes;

UPDATE petapi_post
SET like_id = (
    CASE
        WHEN id = 1 THEN 1 
       
    END
)
WHERE id IN (1); 
