drop table if exists t_equip;
create table t_equip (Id integer, Prof integer, Class1 integer, Class2 integer, Class3 integer, Class4 integer);

insert into t_equip select e.Id, 
						   (select AttrClass from Preset_ProfessionConfig where Id = c.ProfessionRequire),
						   (select AttrClass from PlayerCombatValue where Id = e.BaseAttrType1), 
						   (select AttrClass from PlayerCombatValue where Id = e.BaseAttrType2), 
						   (select AttrClass from PlayerCombatValue where Id = e.BaseAttrType3), 
						   (select AttrClass from PlayerCombatValue where Id = e.BaseAttrType4)
				    from EquipAttr as e join CommonItem as c on e.Id = c.Id;

drop table if exists t_middle;
create table t_middle as select * from t_equip 
	where (Prof is not null and Prof != -1) and (
	(Class1 is not null and Class1 != -1 and Class1 != Prof) or
	(Class2 is not null and Class2 != -1 and Class2 != Prof) or
	(Class3 is not null and Class3 != -1 and Class3 != Prof) or
	(Class4 is not null and Class4 != -1 and Class4 != Prof));

drop table if exists t_result;
create table t_result (Id integer, Prof text, Name text, Attr1 text, Attr2 text, Attr3 text, Attr4 text);
insert into t_result select e.Id, 
	(select Desc from Preset_ProfessionConfig where Id = c.ProfessionRequire), 
	c.Name, 
	(select Desc from PlayerCombatValue where Id = e.BaseAttrType1),
	(select Desc from PlayerCombatValue where Id = e.BaseAttrType2),
	(select Desc from PlayerCombatValue where Id = e.BaseAttrType3),
	(select Desc from PlayerCombatValue where Id = e.BaseAttrType4)
	from EquipAttr as e join CommonItem as c on e.Id = c.Id where e.Id in (select Id from t_middle);

drop table if exists t_equip;
create table t_equip (Id integer, Identifier text, AttrGroup1 integer, AttrGroup2 integer);
insert into t_equip select e.Id, 
						   c.ClassID || '-' || c.SubClassID || '-' || c.ThirdClassID || '-' || c.Color || '-' || e.BaseAttrType1 || '-' || e.BaseAttrType2 || '-' || e.BaseAttrType3 || '-' || e.BaseAttrType4 || '-' || c.ProfessionRequire || '-' || c.SexReq || '-' || (case when e.SetId = -1 then 0 else 1 end),
						   e.ExAffixGroupID1, e.ExAffixGroupID2
				    from EquipAttr as e join CommonItem as c 
				    on 
				    	e.Id = c.Id and instr(c.Name, '废弃') <= 0 and instr(c.Name, '未投') <= 0 and instr(c.Name, '不投') <= 0 and instr(c.Desc, '展示') <= 0 and instr(c.Desc, '不使用') <= 0 and instr(c.Desc, '物理') <= 0 and instr(c.Desc, '法术') <= 0  and instr(c.Desc, '玉玦') <= 0  and instr(c.Desc, '星盘') <= 0 and instr(c.Desc, '分解物') <= 0 and c.MinLevelRequire >= 100;

drop table if exists t_ref;
create table t_ref (Identifier integer, AttrDiff1 integer, AttrDiff2 integer);
insert into t_ref select Identifier, count(distinct AttrGroup1), count(distinct AttrGroup2) from t_equip group by Identifier;

drop table if exists t_middle;
create table t_middle (Id integer, Identifier text, AttrType1 integer, AttrType2 integer, AttrDiff1 integer, AttrDiff2 integer);
insert into t_middle select e.Id, e.Identifier, e.AttrGroup1, e.AttrGroup2, r.AttrDiff1, r.AttrDiff2 from t_equip as e join t_ref as r on e.Identifier = r.Identifier and (r.AttrDiff1 > 1 or r.AttrDiff2 > 1);
insert into t_result select m.Id,
							(select Desc from Preset_ProfessionConfig where Id = c.ProfessionRequire), 
							c.Name,
							m.Identifier,
							(case when m.AttrDiff1 > 1 then 'ExAffixGroupID1 配置不一致，为' || m.AttrType1 else '' end),
							(case when m.AttrDiff2 > 1 then 'ExAffixGroupID2 配置不一致，为' || m.AttrType2 else '' end),
							'这条是：！附加属性职业检查！'
					 from t_middle as m join CommonItem as c on m.Id = c.Id;