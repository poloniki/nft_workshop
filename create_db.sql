BEGIN;

CREATE TABLE workshop (
    name text NOT NULL,
    twitter text NOT NULL,
    thezos text NOT NULL,
    cuisine text NOT NULL,
    teia text NOT NULL
);

alter table workshop
    owner to postgres;

COMMIT;
