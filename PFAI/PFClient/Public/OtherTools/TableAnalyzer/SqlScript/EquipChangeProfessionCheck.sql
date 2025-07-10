drop table if exists t_result;
create table t_result (Id text);

insert into t_result select (Id || '存在漏配职业') from EquipAttr 
	where (
	ChangePro_0 = -1 or 
	ChangePro_1 = -1 or
	ChangePro_2 = -1 or
	ChangePro_3 = -1 or
	ChangePro_4 = -1 or
	ChangePro_5 = -1 or
	ChangePro_6 = -1 or
	ChangePro_7 = -1 or
	ChangePro_8 = -1 or
	ChangePro_9 = -1 or
	ChangePro_10 = -1
	) and (not(
	ChangePro_0 = -1 and
	ChangePro_1 = -1 and
	ChangePro_2 = -1 and
	ChangePro_3 = -1 and
	ChangePro_4 = -1 and
	ChangePro_5 = -1 and
	ChangePro_6 = -1 and
	ChangePro_7 = -1 and
	ChangePro_8 = -1 and
	ChangePro_9 = -1 and
	ChangePro_10 = -1
	));

drop table if exists t_task;
create table t_task (
	Id1 integer, 
	Pro1 integer, 
	Level1 integer,
	Color1 integer,
	Class1 text,
	Id2 integer
);

insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 0  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_0  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_0  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 1  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_1  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_1  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 2  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_2  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_2  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 3  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_3  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_3  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 4  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_4  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_4  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 5  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_5  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_5  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 6  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_6  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_6  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 7  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_7  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_7  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 8  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_8  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_8  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 9  end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_9  from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_9  != -1;
insert into t_task select e.Id, (case when c.ProfessionRequire = -1 then -1 else 10 end), c.MinLevelRequire, c.Color, c.TipsClassDesc, e.ChangePro_10 from EquipAttr as e join CommonItem as c on e.Id = c.Id and e.ChangePro_10 != -1;

drop table if exists t_middle;
create table t_middle (
	Id1 integer, 
	Pro1 integer, 
	Level1 integer,
	Color1 integer,
	Class1 text,
	Id2 integer, 
	Pro2 integer, 
	Level2 integer,
	Color2 integer,
	Class2 text
	);

insert into t_middle select t.Id1, t.Pro1, t.Level1, t.Color1, t.Class1, t.Id2, c.ProfessionRequire, c.MinLevelRequire, c.Color, c.TipsClassDesc from t_task as t join CommonItem as c on t.Id2 = c.Id;

insert into t_result select (Id1 || '转职后职业不一致，转职后ID' || Id2) from t_middle where Pro1 != Pro2;
insert into t_result select (Id1 || '转职后等级不一致，转职后ID' || Id2) from t_middle where Level1 != Level2;
insert into t_result select (Id1 || '转职后品阶不一致，转职后ID' || Id2) from t_middle where Color1 != Color2;
insert into t_result select (Id1 || '转职后类型不一致，转职后ID' || Id2) from t_middle where Class1 != Class2;

--drop table if exists t_result;
--create table t_result as select * from t_middle;