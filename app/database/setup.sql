CREATE TABLE IF NOT EXISTS "films" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "swapi_id" TEXT NOT NULL,
  "user_id" TEXT NOT NULL,
  CONSTRAINT "user" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "swapi_user" UNIQUE ("swapi_id" ASC, "user_id" ASC) ON CONFLICT FAIL
);
CREATE TABLE IF NOT EXISTS "people" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "swapi_id" TEXT NOT NULL,
  "user_id" TEXT NOT NULL,
  CONSTRAINT "user" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "swapi_user" UNIQUE ("swapi_id" ASC, "user_id" ASC) ON CONFLICT FAIL
);
CREATE TABLE IF NOT EXISTS "planets" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "swapi_id" TEXT NOT NULL,
  "user_id" TEXT NOT NULL,
  CONSTRAINT "user" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "swapi_user" UNIQUE ("swapi_id" ASC, "user_id" ASC) ON CONFLICT FAIL
);
CREATE TABLE IF NOT EXISTS "species" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "swapi_id" TEXT NOT NULL,
  "user_id" TEXT NOT NULL,
  CONSTRAINT "user" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "swapi_user" UNIQUE ("swapi_id" ASC, "user_id" ASC) ON CONFLICT FAIL
);
CREATE TABLE IF NOT EXISTS "sqlite_sequence" (
  "name",
  "seq"
);
CREATE TABLE IF NOT EXISTS "starships" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "swapi_id" TEXT NOT NULL,
  "user_id" TEXT NOT NULL,
  CONSTRAINT "user" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "swapi_user" UNIQUE ("swapi_id" ASC, "user_id" ASC) ON CONFLICT FAIL
);
CREATE TABLE IF NOT EXISTS "users" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "username" TEXT NOT NULL,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "username" UNIQUE ("username" ASC) ON CONFLICT FAIL
);
CREATE TABLE IF NOT EXISTS "vehicles" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "created" TEXT NOT NULL,
  "modified" TEXT NOT NULL,
  "swapi_id" TEXT NOT NULL,
  "user_id" TEXT NOT NULL,
  CONSTRAINT "user" FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT "id" UNIQUE ("id" ASC) ON CONFLICT FAIL,
  CONSTRAINT "swapi_user" UNIQUE ("swapi_id" ASC, "user_id" ASC) ON CONFLICT FAIL
);
CREATE UNIQUE INDEX IF NOT EXISTS "films_id"
ON "films" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "films_user"
ON "films" (
  "user_id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "people_id"
ON "people" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "people_user"
ON "people" (
  "user_id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "planet_user"
ON "planets" (
  "user_id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "planets_id"
ON "planets" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "species_id"
ON "species" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "species_user"
ON "species" (
  "user_id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "starships_id"
ON "starships" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "starships_user"
ON "starships" (
  "user_id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "user_id"
ON "users" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "user_username"
ON "users" (
  "username" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "vehicles_id"
ON "vehicles" (
  "id" ASC
);
CREATE UNIQUE INDEX IF NOT EXISTS "veicles_user"
ON "vehicles" (
  "user_id" ASC
);
PRAGMA foreign_keys = ON;