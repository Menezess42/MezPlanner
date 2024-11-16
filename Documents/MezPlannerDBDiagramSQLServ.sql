CREATE TABLE [users] (
  [usr_id] integer PRIMARY KEY,
  [name] nvarchar(255) NOT NULL,
  [email] nvarchar(255) NOT NULL,
  [password] nvarchar(255) NOT NULL,
  [birthday] date NOT NULL,
  [createdat] datetime NOT NULL
)
GO

CREATE TABLE [tasks] (
  [tsk_id] integer PRIMARY KEY,
  [usr_id] integer NOT NULL,
  [name] nvarchar(255) NOT NULL,
  [description] nvarchar(255) NOT NULL,
  [color] nvarchar(255) NOT NULL,
  [tempalte] bool NOT NULL,
  [weekdays] integer(7) NOT NULL
)
GO

CREATE TABLE [task_times] (
  [tsktime_id] integer PRIMARY KEY,
  [tsk_id] integer NOT NULL,
  [startime] time NOT NULL,
  [endtime] time NOT NULL
)
GO

CREATE TABLE [intervals] (
  [intvl_id] integer PRIMARY KEY,
  [usr_id] integer NOT NULL,
  [type] enum(df,sd,cd) NOT NULL,
  [weekdays] integer(7) NOT NULL,
  [valid_startdate] date NOT NULL,
  [valid_enddate] date NOT NULL
)
GO

CREATE TABLE [stocks] (
  [stok_id] integer PRIMARY KEY,
  [symbol] nvarchar(255) NOT NULL,
  [name] nvarchar(255) NOT NULL,
  [current_price] nvarchar(255) NOT NULL
)
GO

CREATE TABLE [wallets] (
  [walet_id] integer PRIMARY KEY,
  [usr_id] integer NOT NULL,
  [name] varcar NOT NULL,
  [current_value] float NOT NULL,
  [highest_value] float NOT NULL,
  [highest_value_day] date NOT NULL,
  [stock_value] float NOT NULL,
  [own_money_value] float NOT NULL,
  [credit] flaot NOT NULL
)
GO

CREATE TABLE [ownMoney] (
  [own_id] integer PRIMARY KEY,
  [walet_id] integer NOT NULL,
  [invested_value] float NOT NULL,
  [invested_date] Datetime NOT NULL,
  [is_started_value] bool
)
GO

CREATE TABLE [transactions] (
  [trans_id] integer PRIMARY KEY,
  [walet_id] integer NOT NULL,
  [stok_id] integer NOT NULL,
  [qtde] integer NOT NULL,
  [price] float NOT NULL,
  [trans_date] datetime NOT NULL,
  [total_value] float NOT NULL,
  [type] bool NOT NULL
)
GO

ALTER TABLE [tasks] ADD FOREIGN KEY ([usr_id]) REFERENCES [users] ([usr_id])
GO

ALTER TABLE [task_times] ADD FOREIGN KEY ([tsk_id]) REFERENCES [tasks] ([tsk_id])
GO

ALTER TABLE [intervals] ADD FOREIGN KEY ([usr_id]) REFERENCES [users] ([usr_id])
GO

ALTER TABLE [wallets] ADD FOREIGN KEY ([usr_id]) REFERENCES [users] ([usr_id])
GO

ALTER TABLE [transactions] ADD FOREIGN KEY ([walet_id]) REFERENCES [wallets] ([walet_id])
GO

ALTER TABLE [transactions] ADD FOREIGN KEY ([stok_id]) REFERENCES [stocks] ([stok_id])
GO

ALTER TABLE [ownMoney] ADD FOREIGN KEY ([walet_id]) REFERENCES [wallets] ([walet_id])
GO
