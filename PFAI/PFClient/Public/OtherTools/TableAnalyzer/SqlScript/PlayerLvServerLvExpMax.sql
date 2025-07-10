drop table if exists t_levelupcopy;
create table t_levelupcopy as select * from LevelUp;
alter table t_levelupcopy add column RealOpenDay integer;
update t_levelupcopy set RealOpenDay = (select julianday(NowDate) - julianday(ServerOpenDate) from t_param);
alter table t_levelupcopy add column UseNewTable integer;
update t_levelupcopy set UseNewTable = (select julianday(ServerOpenDate) - julianday('2019-07-09') from t_param);

alter table t_levelupcopy add column OpenDayDiff integer;
update t_levelupcopy set OpenDayDiff = (case when UseNewTable >= 0 then RealOpenDay - FixServerOpenDay2 else RealOpenDay - FixServerOpenDay end);
update t_levelupcopy set OpenDayDiff = (case when OpenDayDiff > 0 then OpenDayDiff else 0 end);

alter table t_levelupcopy add column ExpAdd number;
update t_levelupcopy set ExpAdd = (case when UseNewTable >= 0 then (select ExpParam from ServerOpenDay2 where Id = OpenDayDiff) else (select ExpParam from ServerOpenDay where Id = OpenDayDiff) end);

drop table if exists t_result;
create table t_result (PlayerLevel integer, ServerLevel integer, ExpMax integer);
insert into t_result select Id, 
	(case when UseNewTable >= 0 
		then (select SeverLevel from ServerOpenDay2 where Id = RealOpenDay) 
		else (select SeverLevel from ServerOpenDay where Id = RealOpenDay) 
	end), 
	(ExpAdd + 1.0) * DailyExpMax
from t_levelupcopy;