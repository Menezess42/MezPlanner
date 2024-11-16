CREATE TABLE "users" (
  "usr_id" integer PRIMARY KEY,
  "name" varchar NOT NULL,
  "email" varchar NOT NULL,
  "password" varchar NOT NULL,
  "birthday" date NOT NULL,
  "createdat" datetime NOT NULL
);

CREATE TABLE "tasks" (
  "tsk_id" integer PRIMARY KEY,
  "usr_id" integer NOT NULL,
  "name" varchar NOT NULL,
  "description" varchar NOT NULL,
  "color" varchar NOT NULL,
  "tempalte" bool NOT NULL,
  "weekdays" integer(7) NOT NULL
);

CREATE TABLE "task_times" (
  "tsktime_id" integer PRIMARY KEY,
  "tsk_id" integer NOT NULL,
  "startime" time NOT NULL,
  "endtime" time NOT NULL
);

CREATE TABLE "intervals" (
  "intvl_id" integer PRIMARY KEY,
  "usr_id" integer NOT NULL,
  "type" enum(df,sd,cd) NOT NULL,
  "weekdays" integer(7) NOT NULL,
  "valid_startdate" date NOT NULL,
  "valid_enddate" date NOT NULL
);

CREATE TABLE "stocks" (
  "stok_id" integer PRIMARY KEY,
  "symbol" varchar NOT NULL,
  "name" varchar NOT NULL,
  "current_price" varchar NOT NULL
);

CREATE TABLE "wallets" (
  "walet_id" integer PRIMARY KEY,
  "usr_id" integer NOT NULL,
  "name" varcar NOT NULL,
  "current_value" float NOT NULL,
  "highest_value" float NOT NULL,
  "highest_value_day" date NOT NULL,
  "stock_value" float NOT NULL,
  "own_money_value" float NOT NULL,
  "credit" flaot NOT NULL
);

CREATE TABLE "ownMoney" (
  "own_id" integer PRIMARY KEY,
  "walet_id" integer NOT NULL,
  "invested_value" float NOT NULL,
  "invested_date" Datetime NOT NULL,
  "is_started_value" bool
);

CREATE TABLE "transactions" (
  "trans_id" integer PRIMARY KEY,
  "walet_id" integer NOT NULL,
  "stok_id" integer NOT NULL,
  "qtde" integer NOT NULL,
  "price" float NOT NULL,
  "trans_date" datetime NOT NULL,
  "total_value" float NOT NULL,
  "type" bool NOT NULL
);

ALTER TABLE "tasks" ADD FOREIGN KEY ("usr_id") REFERENCES "users" ("usr_id");

ALTER TABLE "task_times" ADD FOREIGN KEY ("tsk_id") REFERENCES "tasks" ("tsk_id");

ALTER TABLE "intervals" ADD FOREIGN KEY ("usr_id") REFERENCES "users" ("usr_id");

ALTER TABLE "wallets" ADD FOREIGN KEY ("usr_id") REFERENCES "users" ("usr_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("walet_id") REFERENCES "wallets" ("walet_id");

ALTER TABLE "transactions" ADD FOREIGN KEY ("stok_id") REFERENCES "stocks" ("stok_id");

ALTER TABLE "ownMoney" ADD FOREIGN KEY ("walet_id") REFERENCES "wallets" ("walet_id");
