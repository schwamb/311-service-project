DROP TABLE data_311

CREATE TABLE data_311 (
    "SR_NUMBER" VARCHAR PRIMARY KEY,
    "SR_TYPE" VARCHAR,
    "STATUS" VARCHAR,
    "CREATED_DATE" DATE,
    "CLOSED_DATE" DATE,
    "WARD" INT,
    "CREATED_MONTH" INT,
    "CREATED_DAY_OF_WEEK" INT,
    "CREATED_HOUR" INT,
    "DUPLICATE" VARCHAR,
    "LEGACY_RECORD" VARCHAR,
    "TIME_TO_COMPLETION (Days)" Float
);
