drop table if exists t_equip;
create table t_equip (Id integer, Identifier text, Level integer, BaseAttrType1 integer, BaseAttrType2 integer, BaseAttrType3 integer, BaseAttrType4 integer,
					  BaseAttrValueMin1 integer, BaseAttrValueMin2 integer, BaseAttrValueMin3 integer, BaseAttrValueMin4 integer,
					  BaseAttrValueMax1 integer, BaseAttrValueMax2 integer, BaseAttrValueMax3 integer, BaseAttrValueMax4 integer);

insert into t_equip select e.Id, 
						   c.ClassID || '-' || c.SubClassID || '-' || c.ThirdClassID || '-' || c.Color || '-' || e.BaseAttrType1 || '-' || e.BaseAttrType2 || '-' || e.BaseAttrType3 || '-' || e.BaseAttrType4 || '-' || c.ProfessionRequire || '-' || c.SexReq || '-' || (case when e.SetId = -1 then 0 else 1 end) || '-' || e.ExAffixGroupID1 || '-' || e.ExAffixGroupID2,
						   c.MinLevelRequire,
						   e.BaseAttrType1, e.BaseAttrType2, e.BaseAttrType3, e.BaseAttrType4,
						   e.BaseAttrValueMin1, e.BaseAttrValueMin2, e.BaseAttrValueMin3, e.BaseAttrValueMin4,
						   e.BaseAttrValueMax1, e.BaseAttrValueMax2, e.BaseAttrValueMax3, e.BaseAttrValueMax4
				    from EquipAttr as e join CommonItem as c 
				    on 
				    	e.Id = c.Id and
				    	instr(c.Name, '废弃') <= 0 and instr(c.Name, '未投') <= 0 and instr(c.Name, '不投') <= 0 and instr(c.Desc, '展示') <= 0 and
				    	((c.MinLevelRequire >= (select LvMinLow from t_param) and c.MinLevelRequire <= (select LvMinHigh from t_param)) or
				    	(c.MinLevelRequire >= (select LvMaxLow from t_param) and c.MinLevelRequire <= (select LvMaxHigh from t_param)));

--以特征ID为key做遍历
drop table if exists t_iter;
create table t_iter (Id text);
insert into t_iter select distinct Identifier from t_equip;

--准备好循环用到的表，循环里不能删表
drop table if exists t_equip_cache;
create table t_equip_cache(Id integer, Identifier text, Level integer, LevelAttr integer,
	BaseAttrType1 integer, BaseAttrType2 integer, BaseAttrType3 integer, BaseAttrType4 integer,
	BaseAttrValueMin1 integer, BaseAttrValueMin2 integer, BaseAttrValueMin3 integer, BaseAttrValueMin4 integer,
	BaseAttrValueMax1 integer, BaseAttrValueMax2 integer, BaseAttrValueMax3 integer, BaseAttrValueMax4 integer);

drop table if exists t_equip_cache_copy;
create table t_equip_cache_copy(Id integer, Identifier text, Level integer, LevelAttr integer,
	BaseAttrType1 integer, BaseAttrType2 integer, BaseAttrType3 integer, BaseAttrType4 integer,
	BaseAttrValueMin1 integer, BaseAttrValueMin2 integer, BaseAttrValueMin3 integer, BaseAttrValueMin4 integer,
	BaseAttrValueMax1 integer, BaseAttrValueMax2 integer, BaseAttrValueMax3 integer, BaseAttrValueMax4 integer);

drop table if exists t_limit;
create table t_limit (LevelMin integer, LevelMax integer);

drop table if exists t_problem;
create table t_problem(Id integer, Identifier text, Level integer, LevelAttr integer,
	BaseAttrType1 integer, BaseAttrType2 integer, BaseAttrType3 integer, BaseAttrType4 integer,
	BaseAttrValueMin1 integer, BaseAttrValueMin2 integer, BaseAttrValueMin3 integer, BaseAttrValueMin4 integer,
	BaseAttrValueMax1 integer, BaseAttrValueMax2 integer, BaseAttrValueMax3 integer, BaseAttrValueMax4 integer);

drop table if exists t_Identifier;
create table t_Identifier(Identifier text);

--[LOOPTABLE t_iter]--
--找到该特征ID下的所有装备，计算一下对应的成长率
delete from t_equip_cache;
insert into t_equip_cache select Id, Identifier, Level, 0,
	BaseAttrType1, BaseAttrType2, BaseAttrType3, BaseAttrType4,
	BaseAttrValueMin1, BaseAttrValueMin2, BaseAttrValueMin3, BaseAttrValueMin4,
	BaseAttrValueMax1, BaseAttrValueMax2, BaseAttrValueMax3, BaseAttrValueMax4
from t_equip where Identifier = (select Id from t_iteration_param);

update t_equip_cache set LevelAttr = (select max(Level) from Preset_AttrGrow where Preset_AttrGrow.Id = t_equip_cache.BaseAttrType1 and Preset_AttrGrow.Level <= t_equip_cache.Level);
delete from t_limit;
insert into t_limit select min(LevelAttr), max(LevelAttr) from t_equip_cache;
update t_equip_cache set BaseAttrValueMin1 = BaseAttrValueMin1 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType1 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));
update t_equip_cache set BaseAttrValueMax1 = BaseAttrValueMax1 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType1 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));

update t_equip_cache set LevelAttr = (select max(Level) from Preset_AttrGrow where Preset_AttrGrow.Id = t_equip_cache.BaseAttrType2 and Preset_AttrGrow.Level <= t_equip_cache.Level);
delete from t_limit;
insert into t_limit select min(LevelAttr), max(LevelAttr) from t_equip_cache;
update t_equip_cache set BaseAttrValueMin2 = BaseAttrValueMin2 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType2 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));
update t_equip_cache set BaseAttrValueMax2 = BaseAttrValueMax2 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType2 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));

update t_equip_cache set LevelAttr = (select max(Level) from Preset_AttrGrow where Preset_AttrGrow.Id = t_equip_cache.BaseAttrType3 and Preset_AttrGrow.Level <= t_equip_cache.Level);
delete from t_limit;
insert into t_limit select min(LevelAttr), max(LevelAttr) from t_equip_cache;
update t_equip_cache set BaseAttrValueMin3 = BaseAttrValueMin3 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType3 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));
update t_equip_cache set BaseAttrValueMax3 = BaseAttrValueMax3 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType3 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));

update t_equip_cache set LevelAttr = (select max(Level) from Preset_AttrGrow where Preset_AttrGrow.Id = t_equip_cache.BaseAttrType4 and Preset_AttrGrow.Level <= t_equip_cache.Level);
delete from t_limit;
insert into t_limit select min(LevelAttr), max(LevelAttr) from t_equip_cache;
update t_equip_cache set BaseAttrValueMin4 = BaseAttrValueMin4 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType4 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));
update t_equip_cache set BaseAttrValueMax4 = BaseAttrValueMax4 * (select exp(sum(ln(GrowRate))) from Preset_AttrGrow where Preset_AttrGrow.Id = BaseAttrType4 and Preset_AttrGrow.Level >= t_equip_cache.LevelAttr and Preset_AttrGrow.Level <= (select LevelMax from t_limit));

insert into t_problem select Id, Identifier, Level, LevelAttr, BaseAttrType1, BaseAttrType2, BaseAttrType3, BaseAttrType4,
	max(BaseAttrValueMin1) - min(BaseAttrValueMin1),
	max(BaseAttrValueMin2) - min(BaseAttrValueMin2),
	max(BaseAttrValueMin3) - min(BaseAttrValueMin3),
	max(BaseAttrValueMin4) - min(BaseAttrValueMin4),
	max(BaseAttrValueMax1) - min(BaseAttrValueMax1),
	max(BaseAttrValueMax2) - min(BaseAttrValueMax2),
	max(BaseAttrValueMax3) - min(BaseAttrValueMax3),
	max(BaseAttrValueMax4) - min(BaseAttrValueMax4)
	from t_equip_cache;

insert into t_equip_cache_copy select * from t_equip_cache;

--[LOOPTABLE]--

insert into t_Identifier select Identifier from t_problem where
	(BaseAttrValueMin1 > (select DiffFilter from t_param)) or
	(BaseAttrValueMin2 > (select DiffFilter from t_param)) or
	(BaseAttrValueMin3 > (select DiffFilter from t_param)) or
	(BaseAttrValueMin4 > (select DiffFilter from t_param)) or
	(BaseAttrValueMax1 > (select DiffFilter from t_param)) or
	(BaseAttrValueMax2 > (select DiffFilter from t_param)) or
	(BaseAttrValueMax3 > (select DiffFilter from t_param)) or
	(BaseAttrValueMax4 > (select DiffFilter from t_param));

drop table if exists t_result;
create table t_result as select e.Id, (select Name from CommonItem where CommonItem.Id = e.Id), e.Identifier, e.Level,
	e.BaseAttrType1, e.BaseAttrType2, e.BaseAttrType3, e.BaseAttrType4,
	e.BaseAttrValueMin1, e.BaseAttrValueMin2, e.BaseAttrValueMin3, e.BaseAttrValueMin4,
	e.BaseAttrValueMax1, e.BaseAttrValueMax2, e.BaseAttrValueMax3, e.BaseAttrValueMax4
from t_equip_cache_copy as e join t_Identifier as p on e.Identifier = p.Identifier;