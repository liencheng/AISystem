drop table if exists t_dropcopy;
create table t_dropcopy as select * from RecursionDrop;
alter table t_dropcopy add column ratesum;

--预处理一下掉落表
update t_dropcopy set ItemDropRate_1  = (case when ItemMax >= 1  then ItemDropRate_1  else 0 end);
update t_dropcopy set ItemDropRate_2  = (case when ItemMax >= 2  then ItemDropRate_2  else 0 end);
update t_dropcopy set ItemDropRate_3  = (case when ItemMax >= 3  then ItemDropRate_3  else 0 end);
update t_dropcopy set ItemDropRate_4  = (case when ItemMax >= 4  then ItemDropRate_4  else 0 end);
update t_dropcopy set ItemDropRate_5  = (case when ItemMax >= 5  then ItemDropRate_5  else 0 end);
update t_dropcopy set ItemDropRate_6  = (case when ItemMax >= 6  then ItemDropRate_6  else 0 end);
update t_dropcopy set ItemDropRate_7  = (case when ItemMax >= 7  then ItemDropRate_7  else 0 end);
update t_dropcopy set ItemDropRate_8  = (case when ItemMax >= 8  then ItemDropRate_8  else 0 end);
update t_dropcopy set ItemDropRate_9  = (case when ItemMax >= 9  then ItemDropRate_9  else 0 end);
update t_dropcopy set ItemDropRate_10 = (case when ItemMax >= 10 then ItemDropRate_10 else 0 end);
update t_dropcopy set ItemDropRate_11 = (case when ItemMax >= 11 then ItemDropRate_11 else 0 end);
update t_dropcopy set ItemDropRate_12 = (case when ItemMax >= 12 then ItemDropRate_12 else 0 end);
update t_dropcopy set ItemDropRate_13 = (case when ItemMax >= 13 then ItemDropRate_13 else 0 end);
update t_dropcopy set ItemDropRate_14 = (case when ItemMax >= 14 then ItemDropRate_14 else 0 end);
update t_dropcopy set ItemDropRate_15 = (case when ItemMax >= 15 then ItemDropRate_15 else 0 end);
update t_dropcopy set ItemDropRate_16 = (case when ItemMax >= 16 then ItemDropRate_16 else 0 end);
update t_dropcopy set ItemDropRate_17 = (case when ItemMax >= 17 then ItemDropRate_17 else 0 end);
update t_dropcopy set ItemDropRate_18 = (case when ItemMax >= 18 then ItemDropRate_18 else 0 end);
update t_dropcopy set ItemDropRate_19 = (case when ItemMax >= 19 then ItemDropRate_19 else 0 end);
update t_dropcopy set ItemDropRate_20 = (case when ItemMax >= 20 then ItemDropRate_20 else 0 end);
update t_dropcopy set ratesum = 
    (case when Type = 2 then 
	    ItemDropRate_1  + 
		ItemDropRate_2  + 
		ItemDropRate_3  + 
		ItemDropRate_4  + 
		ItemDropRate_5  + 
		ItemDropRate_6  + 
		ItemDropRate_7  + 
		ItemDropRate_8  + 
		ItemDropRate_9  + 
		ItemDropRate_10 + 
		ItemDropRate_11 + 
		ItemDropRate_12 + 
		ItemDropRate_13 + 
		ItemDropRate_14 + 
		ItemDropRate_15 + 
		ItemDropRate_16 + 
		ItemDropRate_17 + 
		ItemDropRate_18 + 
		ItemDropRate_19 + 
		ItemDropRate_20 
	else 1 
	end);

--将参数表里的数据填入到任务表
drop table if exists t_task;
create table t_task (Id integer, rate real);
insert into t_task (Id) select * from t_param;
update t_task set rate = 1.0;

drop table if exists t_tasktmp;
create table t_tasktmp (Id integer, rate real);

--准备好中间表
drop table if exists t_middle;
create table t_middle (Id integer, description text, count integer, rate real);

--第一遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle (Id, count, rate) select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task (Id, rate) select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task (Id, rate) select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task (Id, rate) select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task (Id, rate) select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task (Id, rate) select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task (Id, rate) select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task (Id, rate) select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task (Id, rate) select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task (Id, rate) select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task (Id, rate) select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task (Id, rate) select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task (Id, rate) select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task (Id, rate) select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task (Id, rate) select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task (Id, rate) select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task (Id, rate) select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task (Id, rate) select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task (Id, rate) select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task (Id, rate) select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task (Id, rate) select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第二遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle (Id, count, rate) select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task (Id, rate) select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task (Id, rate) select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task (Id, rate) select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task (Id, rate) select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task (Id, rate) select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task (Id, rate) select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task (Id, rate) select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task (Id, rate) select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task (Id, rate) select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task (Id, rate) select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task (Id, rate) select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task (Id, rate) select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task (Id, rate) select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task (Id, rate) select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task (Id, rate) select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task (Id, rate) select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task (Id, rate) select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task (Id, rate) select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task (Id, rate) select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task (Id, rate) select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第三遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle (Id, count, rate) select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task (Id, rate) select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task (Id, rate) select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task (Id, rate) select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task (Id, rate) select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task (Id, rate) select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task (Id, rate) select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task (Id, rate) select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task (Id, rate) select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task (Id, rate) select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task (Id, rate) select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task (Id, rate) select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task (Id, rate) select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task (Id, rate) select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task (Id, rate) select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task (Id, rate) select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task (Id, rate) select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task (Id, rate) select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task (Id, rate) select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task (Id, rate) select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task (Id, rate) select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第四遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle (Id, count, rate) select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task (Id, rate) select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task (Id, rate) select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task (Id, rate) select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task (Id, rate) select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task (Id, rate) select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task (Id, rate) select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task (Id, rate) select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task (Id, rate) select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task (Id, rate) select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task (Id, rate) select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task (Id, rate) select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task (Id, rate) select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task (Id, rate) select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task (Id, rate) select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task (Id, rate) select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task (Id, rate) select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task (Id, rate) select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task (Id, rate) select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task (Id, rate) select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task (Id, rate) select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第五遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle (Id, count, rate) select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle (Id, count, rate) select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle (Id, count, rate) select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task (Id, rate) select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task (Id, rate) select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task (Id, rate) select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task (Id, rate) select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task (Id, rate) select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task (Id, rate) select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task (Id, rate) select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task (Id, rate) select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task (Id, rate) select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task (Id, rate) select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task (Id, rate) select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task (Id, rate) select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task (Id, rate) select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task (Id, rate) select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task (Id, rate) select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task (Id, rate) select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task (Id, rate) select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task (Id, rate) select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task (Id, rate) select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task (Id, rate) select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--准备好结果表
drop table if exists t_result;
create table t_result (Id integer, description text, count integer, rate real);
insert into t_result select m.Id, c.Desc, m.count, m.rate from t_middle as m  join CommonItem as c on m.Id = c.Id