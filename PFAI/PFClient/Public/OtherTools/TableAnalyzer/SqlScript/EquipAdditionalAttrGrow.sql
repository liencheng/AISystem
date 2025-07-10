--[This is a complex sql format Version:1.0]--
drop table if exists t_equip;
create table t_equip (Id integer, Identifier text, Level integer, ValueLevel integer);

insert into t_equip select e.Id, 
						   c.ClassID || '-' || c.SubClassID || '-' || c.ThirdClassID || '-' || c.Color || '-' || e.BaseAttrType1 || '-' || e.BaseAttrType2 || '-' || e.BaseAttrType3 || '-' || e.BaseAttrType4 || '-' || c.ProfessionRequire || '-' || c.SexReq || '-' || (case when e.SetId = -1 then 0 else 1 end) || '-' || e.ExAffixGroupID1 || '-' || e.ExAffixGroupID2,
						   c.MinLevelRequire,
						   e.ValueLevel
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
--准备好问题表
drop table if exists t_problem;
create table t_problem (Id integer, Identifier text, Level integer, ValueLevel integer, LevelDiff integer,
	AttrType1 integer,
	AttrType2 integer,
	AttrType3 integer,
	AttrType4 integer,
	AttrType5 integer,
	AttrType6 integer,
	AttrType7 integer,
	AttrType8 integer,
	AttrType9 integer,
	AttrType10 integer,
	AttrType11 integer,
	AttrType12 integer,
	AttrType13 integer,
	AttrType14 integer,
	AttrType15 integer,
	AttrType16 integer,
	AttrType17 integer,
	AttrType18 integer,
	AttrType19 integer,
	AttrType20 integer,
	AttrType21 integer,
	AttrType22 integer,
	AttrType23 integer,
	AttrType24 integer,
	AttrType25 integer,
	AttrType26 integer,
	AttrType27 integer,
	AttrType28 integer,
	AttrType29 integer,
	AttrType30 integer,
	AttrType31 integer,
	AttrType32 integer,
	AttrType33 integer,
	AttrType34 integer,
	AttrType35 integer,
	AttrType36 integer,
	AttrType37 integer,
	AttrType38 integer,
	AttrType39 integer,
	AttrType40 integer,
	AttrType41 integer,
	AttrType42 integer,
	AttrType43 integer,
	AttrType44 integer,
	AttrType45 integer,
	AttrType46 integer,
	AttrType47 integer,
	AttrType48 integer,
	AttrType49 integer,
	AttrType50 integer,
	AttrType51 integer,
	AttrType52 integer,
	AttrType53 integer,
	AttrType54 integer,
	AttrType55 integer,
	AttrType56 integer,
	AttrType57 integer,
	AttrType58 integer,
	AttrType59 integer,
	AttrType60 integer,
	AttrType61 integer,
	AttrType62 integer,
	AttrType63 integer,
	AttrType64 integer,
	AttrType65 integer,
	AttrType66 integer,
	AttrType67 integer,
	AttrType68 integer,
	AttrType69 integer,
	AttrType70 integer,
	AttrType71 integer,
	AttrType72 integer,
	AttrType73 integer,
	AttrType74 integer,
	AttrType75 integer,
	AttrType76 integer,
	AttrType77 integer,
	AttrType78 integer,
	AttrType79 integer,
	AttrType80 integer,
	AttrType81 integer,
	AttrType82 integer,
	AttrType83 integer,
	AttrType84 integer,
	AttrType85 integer,
	AttrType86 integer,
	AttrType87 integer,
	AttrType88 integer,
	AttrType89 integer,
	AttrType90 integer,
	AttrType91 integer,
	AttrType92 integer,
	AttrType93 integer,
	AttrType94 integer,
	AttrType95 integer,
	AttrType96 integer,
	AttrType97 integer,
	AttrType98 integer,
	AttrType99 integer,
	AttrType100 integer,
	AttrType101 integer,
	AttrType102 integer,
	AttrType103 integer,
	AttrType104 integer,
	AttrType105 integer,
	AttrType106 integer,
	AttrType107 integer,
	AttrType108 integer,
	AttrType109 integer,
	AttrType110 integer,
	AttrType111 integer,
	AttrType112 integer,
	AttrType113 integer,
	AttrType114 integer,
	AttrType115 integer,
	AttrType116 integer,
	AttrType117 integer,
	AttrType118 integer,
	AttrType119 integer,
	AttrType120 integer,
	AttrType121 integer,
	AttrType122 integer,
	AttrType123 integer,
	AttrType124 integer,
	AttrType125 integer,
	AttrType126 integer,
	AttrType127 integer,
	AttrType128 integer,
	AttrType129 integer,
	AttrType130 integer,
	AttrType131 integer,
	AttrType132 integer,
	AttrType133 integer,
	AttrType134 integer,
	AttrType135 integer,
	AttrType136 integer);
--准备好循环用到的表，循环里不能删表
drop table if exists t_equipMiddle;
create table t_equipMiddle(Id integer, Identifier text, Level integer, ValueLevel integer, LevelDiff integer);
drop table if exists t_middle;
create table t_middle(Id integer, Identifier text, Level integer, ValueLevel integer, LevelDiff integer,
	AttrType1 integer,
	AttrType2 integer,
	AttrType3 integer,
	AttrType4 integer,
	AttrType5 integer,
	AttrType6 integer,
	AttrType7 integer,
	AttrType8 integer,
	AttrType9 integer,
	AttrType10 integer,
	AttrType11 integer,
	AttrType12 integer,
	AttrType13 integer,
	AttrType14 integer,
	AttrType15 integer,
	AttrType16 integer,
	AttrType17 integer,
	AttrType18 integer,
	AttrType19 integer,
	AttrType20 integer,
	AttrType21 integer,
	AttrType22 integer,
	AttrType23 integer,
	AttrType24 integer,
	AttrType25 integer,
	AttrType26 integer,
	AttrType27 integer,
	AttrType28 integer,
	AttrType29 integer,
	AttrType30 integer,
	AttrType31 integer,
	AttrType32 integer,
	AttrType33 integer,
	AttrType34 integer,
	AttrType35 integer,
	AttrType36 integer,
	AttrType37 integer,
	AttrType38 integer,
	AttrType39 integer,
	AttrType40 integer,
	AttrType41 integer,
	AttrType42 integer,
	AttrType43 integer,
	AttrType44 integer,
	AttrType45 integer,
	AttrType46 integer,
	AttrType47 integer,
	AttrType48 integer,
	AttrType49 integer,
	AttrType50 integer,
	AttrType51 integer,
	AttrType52 integer,
	AttrType53 integer,
	AttrType54 integer,
	AttrType55 integer,
	AttrType56 integer,
	AttrType57 integer,
	AttrType58 integer,
	AttrType59 integer,
	AttrType60 integer,
	AttrType61 integer,
	AttrType62 integer,
	AttrType63 integer,
	AttrType64 integer,
	AttrType65 integer,
	AttrType66 integer,
	AttrType67 integer,
	AttrType68 integer,
	AttrType69 integer,
	AttrType70 integer,
	AttrType71 integer,
	AttrType72 integer,
	AttrType73 integer,
	AttrType74 integer,
	AttrType75 integer,
	AttrType76 integer,
	AttrType77 integer,
	AttrType78 integer,
	AttrType79 integer,
	AttrType80 integer,
	AttrType81 integer,
	AttrType82 integer,
	AttrType83 integer,
	AttrType84 integer,
	AttrType85 integer,
	AttrType86 integer,
	AttrType87 integer,
	AttrType88 integer,
	AttrType89 integer,
	AttrType90 integer,
	AttrType91 integer,
	AttrType92 integer,
	AttrType93 integer,
	AttrType94 integer,
	AttrType95 integer,
	AttrType96 integer,
	AttrType97 integer,
	AttrType98 integer,
	AttrType99 integer,
	AttrType100 integer,
	AttrType101 integer,
	AttrType102 integer,
	AttrType103 integer,
	AttrType104 integer,
	AttrType105 integer,
	AttrType106 integer,
	AttrType107 integer,
	AttrType108 integer,
	AttrType109 integer,
	AttrType110 integer,
	AttrType111 integer,
	AttrType112 integer,
	AttrType113 integer,
	AttrType114 integer,
	AttrType115 integer,
	AttrType116 integer,
	AttrType117 integer,
	AttrType118 integer,
	AttrType119 integer,
	AttrType120 integer,
	AttrType121 integer,
	AttrType122 integer,
	AttrType123 integer,
	AttrType124 integer,
	AttrType125 integer,
	AttrType126 integer,
	AttrType127 integer,
	AttrType128 integer,
	AttrType129 integer,
	AttrType130 integer,
	AttrType131 integer,
	AttrType132 integer,
	AttrType133 integer,
	AttrType134 integer,
	AttrType135 integer,
	AttrType136 integer);

--[LOOPTABLE t_iter]--
--找到该特征ID下的所有装备，计算一下对应的成长率
delete from t_equipMiddle;
insert into t_equipMiddle select Id, Identifier, Level, ValueLevel, 0 from t_equip where Identifier = (select Id from t_iteration_param);
update t_equipMiddle set LevelDiff = (select count(distinct t_equip.Level) from t_equip where t_equip.Identifier = t_equipMiddle.Identifier and t_equip.Level > t_equipMiddle.Level);

delete from t_middle;
insert into t_middle select e.Id, e.Identifier, e.Level, e.ValueLevel, e.LevelDiff,
	v.AttrType1 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 0),
	v.AttrType2 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 1),
	v.AttrType3 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 2),
	v.AttrType4 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 3),
	v.AttrType5 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 4),
	v.AttrType6 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 5),
	v.AttrType7 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 6),
	v.AttrType8 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 7),
	v.AttrType9 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 8),
	v.AttrType10 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 9),
	v.AttrType11 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 10),
	v.AttrType12 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 11),
	v.AttrType13 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 12),
	v.AttrType14 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 13),
	v.AttrType15 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 14),
	v.AttrType16 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 15),
	v.AttrType17 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 16),
	v.AttrType18 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 17),
	v.AttrType19 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 18),
	v.AttrType20 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 19),
	v.AttrType21 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 20),
	v.AttrType22 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 21),
	v.AttrType23 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 22),
	v.AttrType24 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 23),
	v.AttrType25 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 24),
	v.AttrType26 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 25),
	v.AttrType27 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 26),
	v.AttrType28 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 27),
	v.AttrType29 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 28),
	v.AttrType30 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 29),
	v.AttrType31 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 30),
	v.AttrType32 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 31),
	v.AttrType33 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 32),
	v.AttrType34 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 33),
	v.AttrType35 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 34),
	v.AttrType36 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 35),
	v.AttrType37 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 36),
	v.AttrType38 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 37),
	v.AttrType39 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 38),
	v.AttrType40 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 39),
	v.AttrType41 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 40),
	v.AttrType42 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 41),
	v.AttrType43 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 42),
	v.AttrType44 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 43),
	v.AttrType45 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 44),
	v.AttrType46 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 45),
	v.AttrType47 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 46),
	v.AttrType48 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 47),
	v.AttrType49 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 48),
	v.AttrType50 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 49),
	v.AttrType51 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 50),
	v.AttrType52 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 51),
	v.AttrType53 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 52),
	v.AttrType54 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 53),
	v.AttrType55 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 54),
	v.AttrType56 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 55),
	v.AttrType57 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 56),
	v.AttrType58 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 57),
	v.AttrType59 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 58),
	v.AttrType60 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 59),
	v.AttrType61 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 60),
	v.AttrType62 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 61),
	v.AttrType63 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 62),
	v.AttrType64 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 63),
	v.AttrType65 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 64),
	v.AttrType66 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 65),
	v.AttrType67 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 66),
	v.AttrType68 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 67),
	v.AttrType69 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 68),
	v.AttrType70 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 69),
	v.AttrType71 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 70),
	v.AttrType72 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 71),
	v.AttrType73 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 72),
	v.AttrType74 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 73),
	v.AttrType75 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 74),
	v.AttrType76 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 75),
	v.AttrType77 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 76),
	v.AttrType78 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 77),
	v.AttrType79 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 78),
	v.AttrType80 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 79),
	v.AttrType81 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 80),
	v.AttrType82 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 81),
	v.AttrType83 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 82),
	v.AttrType84 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 83),
	v.AttrType85 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 84),
	v.AttrType86 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 85),
	v.AttrType87 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 86),
	v.AttrType88 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 87),
	v.AttrType89 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 88),
	v.AttrType90 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 89),
	v.AttrType91 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 90),
	v.AttrType92 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 91),
	v.AttrType93 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 92),
	v.AttrType94 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 93),
	v.AttrType95 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 94),
	v.AttrType96 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 95),
	v.AttrType97 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 96),
	v.AttrType98 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 97),
	v.AttrType99 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 98),
	v.AttrType100 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 99),
	v.AttrType101 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 100),
	v.AttrType102 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 101),
	v.AttrType103 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 102),
	v.AttrType104 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 103),
	v.AttrType105 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 104),
	v.AttrType106 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 105),
	v.AttrType107 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 106),
	v.AttrType108 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 107),
	v.AttrType109 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 108),
	v.AttrType110 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 109),
	v.AttrType111 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 110),
	v.AttrType112 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 111),
	v.AttrType113 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 112),
	v.AttrType114 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 113),
	v.AttrType115 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 114),
	v.AttrType116 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 115),
	v.AttrType117 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 116),
	v.AttrType118 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 117),
	v.AttrType119 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 118),
	v.AttrType120 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 119),
	v.AttrType121 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 120),
	v.AttrType122 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 121),
	v.AttrType123 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 122),
	v.AttrType124 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 123),
	v.AttrType125 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 124),
	v.AttrType126 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 125),
	v.AttrType127 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 126),
	v.AttrType128 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 127),
	v.AttrType129 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 128),
	v.AttrType130 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 129),
	v.AttrType131 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 130),
	v.AttrType132 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 131),
	v.AttrType133 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 132),
	v.AttrType134 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 133),
	v.AttrType135 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 134),
	v.AttrType136 * (select exp(ln(GrowRate) * e.LevelDiff) from Preset_AttrGrow where Preset_AttrGrow.Id = 135)
	from t_equipMiddle as e join EquipAttrValue as v on e.ValueLevel = v.Id;

insert into t_problem select Id, Identifier, Level, ValueLevel, LevelDiff,
	max(AttrType1) - min(AttrType1),
	max(AttrType2) - min(AttrType2),
	max(AttrType3) - min(AttrType3),
	max(AttrType4) - min(AttrType4),
	max(AttrType5) - min(AttrType5),
	max(AttrType6) - min(AttrType6),
	max(AttrType7) - min(AttrType7),
	max(AttrType8) - min(AttrType8),
	max(AttrType9) - min(AttrType9),
	max(AttrType10) - min(AttrType10),
	max(AttrType11) - min(AttrType11),
	max(AttrType12) - min(AttrType12),
	max(AttrType13) - min(AttrType13),
	max(AttrType14) - min(AttrType14),
	max(AttrType15) - min(AttrType15),
	max(AttrType16) - min(AttrType16),
	max(AttrType17) - min(AttrType17),
	max(AttrType18) - min(AttrType18),
	max(AttrType19) - min(AttrType19),
	max(AttrType20) - min(AttrType20),
	max(AttrType21) - min(AttrType21),
	max(AttrType22) - min(AttrType22),
	max(AttrType23) - min(AttrType23),
	max(AttrType24) - min(AttrType24),
	max(AttrType25) - min(AttrType25),
	max(AttrType26) - min(AttrType26),
	max(AttrType27) - min(AttrType27),
	max(AttrType28) - min(AttrType28),
	max(AttrType29) - min(AttrType29),
	max(AttrType30) - min(AttrType30),
	max(AttrType31) - min(AttrType31),
	max(AttrType32) - min(AttrType32),
	max(AttrType33) - min(AttrType33),
	max(AttrType34) - min(AttrType34),
	max(AttrType35) - min(AttrType35),
	max(AttrType36) - min(AttrType36),
	max(AttrType37) - min(AttrType37),
	max(AttrType38) - min(AttrType38),
	max(AttrType39) - min(AttrType39),
	max(AttrType40) - min(AttrType40),
	max(AttrType41) - min(AttrType41),
	max(AttrType42) - min(AttrType42),
	max(AttrType43) - min(AttrType43),
	max(AttrType44) - min(AttrType44),
	max(AttrType45) - min(AttrType45),
	max(AttrType46) - min(AttrType46),
	max(AttrType47) - min(AttrType47),
	max(AttrType48) - min(AttrType48),
	max(AttrType49) - min(AttrType49),
	max(AttrType50) - min(AttrType50),
	max(AttrType51) - min(AttrType51),
	max(AttrType52) - min(AttrType52),
	max(AttrType53) - min(AttrType53),
	max(AttrType54) - min(AttrType54),
	max(AttrType55) - min(AttrType55),
	max(AttrType56) - min(AttrType56),
	max(AttrType57) - min(AttrType57),
	max(AttrType58) - min(AttrType58),
	max(AttrType59) - min(AttrType59),
	max(AttrType60) - min(AttrType60),
	max(AttrType61) - min(AttrType61),
	max(AttrType62) - min(AttrType62),
	max(AttrType63) - min(AttrType63),
	max(AttrType64) - min(AttrType64),
	max(AttrType65) - min(AttrType65),
	max(AttrType66) - min(AttrType66),
	max(AttrType67) - min(AttrType67),
	max(AttrType68) - min(AttrType68),
	max(AttrType69) - min(AttrType69),
	max(AttrType70) - min(AttrType70),
	max(AttrType71) - min(AttrType71),
	max(AttrType72) - min(AttrType72),
	max(AttrType73) - min(AttrType73),
	max(AttrType74) - min(AttrType74),
	max(AttrType75) - min(AttrType75),
	max(AttrType76) - min(AttrType76),
	max(AttrType77) - min(AttrType77),
	max(AttrType78) - min(AttrType78),
	max(AttrType79) - min(AttrType79),
	max(AttrType80) - min(AttrType80),
	max(AttrType81) - min(AttrType81),
	max(AttrType82) - min(AttrType82),
	max(AttrType83) - min(AttrType83),
	max(AttrType84) - min(AttrType84),
	max(AttrType85) - min(AttrType85),
	max(AttrType86) - min(AttrType86),
	max(AttrType87) - min(AttrType87),
	max(AttrType88) - min(AttrType88),
	max(AttrType89) - min(AttrType89),
	max(AttrType90) - min(AttrType90),
	max(AttrType91) - min(AttrType91),
	max(AttrType92) - min(AttrType92),
	max(AttrType93) - min(AttrType93),
	max(AttrType94) - min(AttrType94),
	max(AttrType95) - min(AttrType95),
	max(AttrType96) - min(AttrType96),
	max(AttrType97) - min(AttrType97),
	max(AttrType98) - min(AttrType98),
	max(AttrType99) - min(AttrType99),
	max(AttrType100) - min(AttrType100),
	max(AttrType101) - min(AttrType101),
	max(AttrType102) - min(AttrType102),
	max(AttrType103) - min(AttrType103),
	max(AttrType104) - min(AttrType104),
	max(AttrType105) - min(AttrType105),
	max(AttrType106) - min(AttrType106),
	max(AttrType107) - min(AttrType107),
	max(AttrType108) - min(AttrType108),
	max(AttrType109) - min(AttrType109),
	max(AttrType110) - min(AttrType110),
	max(AttrType111) - min(AttrType111),
	max(AttrType112) - min(AttrType112),
	max(AttrType113) - min(AttrType113),
	max(AttrType114) - min(AttrType114),
	max(AttrType115) - min(AttrType115),
	max(AttrType116) - min(AttrType116),
	max(AttrType117) - min(AttrType117),
	max(AttrType118) - min(AttrType118),
	max(AttrType119) - min(AttrType119),
	max(AttrType120) - min(AttrType120),
	max(AttrType121) - min(AttrType121),
	max(AttrType122) - min(AttrType122),
	max(AttrType123) - min(AttrType123),
	max(AttrType124) - min(AttrType124),
	max(AttrType125) - min(AttrType125),
	max(AttrType126) - min(AttrType126),
	max(AttrType127) - min(AttrType127),
	max(AttrType128) - min(AttrType128),
	max(AttrType129) - min(AttrType129),
	max(AttrType130) - min(AttrType130),
	max(AttrType131) - min(AttrType131),
	max(AttrType132) - min(AttrType132),
	max(AttrType133) - min(AttrType133),
	max(AttrType134) - min(AttrType134),
	max(AttrType135) - min(AttrType135),
	max(AttrType136) - min(AttrType136)
	from t_middle;

--[LOOPTABLE]--
delete from t_problem where 
	AttrType1 <= (select DiffFilter from t_param) and
	AttrType2 <= (select DiffFilter from t_param) and
	AttrType3 <= (select DiffFilter from t_param) and
	AttrType4 <= (select DiffFilter from t_param) and
	AttrType5 <= (select DiffFilter from t_param) and
	AttrType6 <= (select DiffFilter from t_param) and
	AttrType7 <= (select DiffFilter from t_param) and
	AttrType8 <= (select DiffFilter from t_param) and
	AttrType9 <= (select DiffFilter from t_param) and
	AttrType10 <= (select DiffFilter from t_param) and
	AttrType11 <= (select DiffFilter from t_param) and
	AttrType12 <= (select DiffFilter from t_param) and
	AttrType13 <= (select DiffFilter from t_param) and
	AttrType14 <= (select DiffFilter from t_param) and
	AttrType15 <= (select DiffFilter from t_param) and
	AttrType16 <= (select DiffFilter from t_param) and
	AttrType17 <= (select DiffFilter from t_param) and
	AttrType18 <= (select DiffFilter from t_param) and
	AttrType19 <= (select DiffFilter from t_param) and
	AttrType20 <= (select DiffFilter from t_param) and
	AttrType21 <= (select DiffFilter from t_param) and
	AttrType22 <= (select DiffFilter from t_param) and
	AttrType23 <= (select DiffFilter from t_param) and
	AttrType24 <= (select DiffFilter from t_param) and
	AttrType25 <= (select DiffFilter from t_param) and
	AttrType26 <= (select DiffFilter from t_param) and
	AttrType27 <= (select DiffFilter from t_param) and
	AttrType28 <= (select DiffFilter from t_param) and
	AttrType29 <= (select DiffFilter from t_param) and
	AttrType30 <= (select DiffFilter from t_param) and
	AttrType31 <= (select DiffFilter from t_param) and
	AttrType32 <= (select DiffFilter from t_param) and
	AttrType33 <= (select DiffFilter from t_param) and
	AttrType34 <= (select DiffFilter from t_param) and
	AttrType35 <= (select DiffFilter from t_param) and
	AttrType36 <= (select DiffFilter from t_param) and
	AttrType37 <= (select DiffFilter from t_param) and
	AttrType38 <= (select DiffFilter from t_param) and
	AttrType39 <= (select DiffFilter from t_param) and
	AttrType40 <= (select DiffFilter from t_param) and
	AttrType41 <= (select DiffFilter from t_param) and
	AttrType42 <= (select DiffFilter from t_param) and
	AttrType43 <= (select DiffFilter from t_param) and
	AttrType44 <= (select DiffFilter from t_param) and
	AttrType45 <= (select DiffFilter from t_param) and
	AttrType46 <= (select DiffFilter from t_param) and
	AttrType47 <= (select DiffFilter from t_param) and
	AttrType48 <= (select DiffFilter from t_param) and
	AttrType49 <= (select DiffFilter from t_param) and
	AttrType50 <= (select DiffFilter from t_param) and
	AttrType51 <= (select DiffFilter from t_param) and
	AttrType52 <= (select DiffFilter from t_param) and
	AttrType53 <= (select DiffFilter from t_param) and
	AttrType54 <= (select DiffFilter from t_param) and
	AttrType55 <= (select DiffFilter from t_param) and
	AttrType56 <= (select DiffFilter from t_param) and
	AttrType57 <= (select DiffFilter from t_param) and
	AttrType58 <= (select DiffFilter from t_param) and
	AttrType59 <= (select DiffFilter from t_param) and
	AttrType60 <= (select DiffFilter from t_param) and
	AttrType61 <= (select DiffFilter from t_param) and
	AttrType62 <= (select DiffFilter from t_param) and
	AttrType63 <= (select DiffFilter from t_param) and
	AttrType64 <= (select DiffFilter from t_param) and
	AttrType65 <= (select DiffFilter from t_param) and
	AttrType66 <= (select DiffFilter from t_param) and
	AttrType67 <= (select DiffFilter from t_param) and
	AttrType68 <= (select DiffFilter from t_param) and
	AttrType69 <= (select DiffFilter from t_param) and
	AttrType70 <= (select DiffFilter from t_param) and
	AttrType71 <= (select DiffFilter from t_param) and
	AttrType72 <= (select DiffFilter from t_param) and
	AttrType73 <= (select DiffFilter from t_param) and
	AttrType74 <= (select DiffFilter from t_param) and
	AttrType75 <= (select DiffFilter from t_param) and
	AttrType76 <= (select DiffFilter from t_param) and
	AttrType77 <= (select DiffFilter from t_param) and
	AttrType78 <= (select DiffFilter from t_param) and
	AttrType79 <= (select DiffFilter from t_param) and
	AttrType80 <= (select DiffFilter from t_param) and
	AttrType81 <= (select DiffFilter from t_param) and
	AttrType82 <= (select DiffFilter from t_param) and
	AttrType83 <= (select DiffFilter from t_param) and
	AttrType84 <= (select DiffFilter from t_param) and
	AttrType85 <= (select DiffFilter from t_param) and
	AttrType86 <= (select DiffFilter from t_param) and
	AttrType87 <= (select DiffFilter from t_param) and
	AttrType88 <= (select DiffFilter from t_param) and
	AttrType89 <= (select DiffFilter from t_param) and
	AttrType90 <= (select DiffFilter from t_param) and
	AttrType91 <= (select DiffFilter from t_param) and
	AttrType92 <= (select DiffFilter from t_param) and
	AttrType93 <= (select DiffFilter from t_param) and
	AttrType94 <= (select DiffFilter from t_param) and
	AttrType95 <= (select DiffFilter from t_param) and
	AttrType96 <= (select DiffFilter from t_param) and
	AttrType97 <= (select DiffFilter from t_param) and
	AttrType98 <= (select DiffFilter from t_param) and
	AttrType99 <= (select DiffFilter from t_param) and
	AttrType100 <= (select DiffFilter from t_param) and
	AttrType101 <= (select DiffFilter from t_param) and
	AttrType102 <= (select DiffFilter from t_param) and
	AttrType103 <= (select DiffFilter from t_param) and
	AttrType104 <= (select DiffFilter from t_param) and
	AttrType105 <= (select DiffFilter from t_param) and
	AttrType106 <= (select DiffFilter from t_param) and
	AttrType107 <= (select DiffFilter from t_param) and
	AttrType108 <= (select DiffFilter from t_param) and
	AttrType109 <= (select DiffFilter from t_param) and
	AttrType110 <= (select DiffFilter from t_param) and
	AttrType111 <= (select DiffFilter from t_param) and
	AttrType112 <= (select DiffFilter from t_param) and
	AttrType113 <= (select DiffFilter from t_param) and
	AttrType114 <= (select DiffFilter from t_param) and
	AttrType115 <= (select DiffFilter from t_param) and
	AttrType116 <= (select DiffFilter from t_param) and
	AttrType117 <= (select DiffFilter from t_param) and
	AttrType118 <= (select DiffFilter from t_param) and
	AttrType119 <= (select DiffFilter from t_param) and
	AttrType120 <= (select DiffFilter from t_param) and
	AttrType121 <= (select DiffFilter from t_param) and
	AttrType122 <= (select DiffFilter from t_param) and
	AttrType123 <= (select DiffFilter from t_param) and
	AttrType124 <= (select DiffFilter from t_param) and
	AttrType125 <= (select DiffFilter from t_param) and
	AttrType126 <= (select DiffFilter from t_param) and
	AttrType127 <= (select DiffFilter from t_param) and
	AttrType128 <= (select DiffFilter from t_param) and
	AttrType129 <= (select DiffFilter from t_param) and
	AttrType130 <= (select DiffFilter from t_param) and
	AttrType131 <= (select DiffFilter from t_param) and
	AttrType132 <= (select DiffFilter from t_param) and
	AttrType133 <= (select DiffFilter from t_param) and
	AttrType134 <= (select DiffFilter from t_param) and
	AttrType135 <= (select DiffFilter from t_param) and
	AttrType136 <= (select DiffFilter from t_param);

drop table if exists t_result;
create table t_result as select e.Id, (select Name from CommonItem where Id = e.Id), e.Identifier, e.Level, e.ValueLevel,
	p.AttrType1,
	p.AttrType2,
	p.AttrType3,
	p.AttrType4,
	p.AttrType5,
	p.AttrType6,
	p.AttrType7,
	p.AttrType8,
	p.AttrType9,
	p.AttrType10,
	p.AttrType11,
	p.AttrType12,
	p.AttrType13,
	p.AttrType14,
	p.AttrType15,
	p.AttrType16,
	p.AttrType17,
	p.AttrType18,
	p.AttrType19,
	p.AttrType20,
	p.AttrType21,
	p.AttrType22,
	p.AttrType23,
	p.AttrType24,
	p.AttrType25,
	p.AttrType26,
	p.AttrType27,
	p.AttrType28,
	p.AttrType29,
	p.AttrType30,
	p.AttrType31,
	p.AttrType32,
	p.AttrType33,
	p.AttrType34,
	p.AttrType35,
	p.AttrType36,
	p.AttrType37,
	p.AttrType38,
	p.AttrType39,
	p.AttrType40,
	p.AttrType41,
	p.AttrType42,
	p.AttrType43,
	p.AttrType44,
	p.AttrType45,
	p.AttrType46,
	p.AttrType47,
	p.AttrType48,
	p.AttrType49,
	p.AttrType50,
	p.AttrType51,
	p.AttrType52,
	p.AttrType53,
	p.AttrType54,
	p.AttrType55,
	p.AttrType56,
	p.AttrType57,
	p.AttrType58,
	p.AttrType59,
	p.AttrType60,
	p.AttrType61,
	p.AttrType62,
	p.AttrType63,
	p.AttrType64,
	p.AttrType65,
	p.AttrType66,
	p.AttrType67,
	p.AttrType68,
	p.AttrType69,
	p.AttrType70,
	p.AttrType71,
	p.AttrType72,
	p.AttrType73,
	p.AttrType74,
	p.AttrType75,
	p.AttrType76,
	p.AttrType77,
	p.AttrType78,
	p.AttrType79,
	p.AttrType80,
	p.AttrType81,
	p.AttrType82,
	p.AttrType83,
	p.AttrType84,
	p.AttrType85,
	p.AttrType86,
	p.AttrType87,
	p.AttrType88,
	p.AttrType89,
	p.AttrType90,
	p.AttrType91,
	p.AttrType92,
	p.AttrType93,
	p.AttrType94,
	p.AttrType95,
	p.AttrType96,
	p.AttrType97,
	p.AttrType98,
	p.AttrType99,
	p.AttrType100,
	p.AttrType101,
	p.AttrType102,
	p.AttrType103,
	p.AttrType104,
	p.AttrType105,
	p.AttrType106,
	p.AttrType107,
	p.AttrType108,
	p.AttrType109,
	p.AttrType110,
	p.AttrType111,
	p.AttrType112,
	p.AttrType113,
	p.AttrType114,
	p.AttrType115,
	p.AttrType116,
	p.AttrType117,
	p.AttrType118,
	p.AttrType119,
	p.AttrType120,
	p.AttrType121,
	p.AttrType122,
	p.AttrType123,
	p.AttrType124,
	p.AttrType125,
	p.AttrType126,
	p.AttrType127,
	p.AttrType128,
	p.AttrType129,
	p.AttrType130,
	p.AttrType131,
	p.AttrType132,
	p.AttrType133,
	p.AttrType134,
	p.AttrType135,
	p.AttrType136
	from t_equip as e join t_problem as p on e.Identifier = p.Identifier;