drop table if exists t_NotifyId1;
create table t_NotifyId1 (Id integer, NotifyId integer, StdDicId1 text);
insert into t_NotifyId1 (Id, NotifyId, StdDicId1) select r.Id, r.NotifyId, d.Content1 from RecursionDrop as r join DropNotify as d on r.NotifyId == d.Id;
insert into t_NotifyId1 (Id, NotifyId, StdDicId1) select r.Id, r.NotifyId, '无' from RecursionDrop as r where not exists(select * from t_NotifyId1 where r.Id == t_NotifyId1.Id);

drop table if exists t_NotifyIdCon1;
create table t_NotifyIdCon1 (Id integer, NotifyId integer, StdDicId1 text, Content1 text);
insert into t_NotifyIdCon1 (Id, NotifyId, StdDicId1, Content1) select n.Id, n.NotifyId, n.StdDicId1, s.StrDictionary from t_NotifyId1 as n join StrDictionary as s on n.StdDicId1 == '#{' || s.Id || '}';
insert into t_NotifyIdCon1 (Id, NotifyId, StdDicId1, Content1) select n.Id, n.NotifyId, '无' , '无' from t_NotifyId1 as n where not exists(select * from t_NotifyIdCon1 where n.Id == t_NotifyIdCon1.Id);

drop table if exists t_NotifyIdCon1Final;
create table t_NotifyIdCon1Final(Id integer, NotifyId integer, StdDicId1 text, Content1 text);
insert into t_NotifyIdCon1Final select * from t_NotifyIdCon1 order by t_NotifyIdCon1.Id;

drop table if exists t_NotifyId2;
create table t_NotifyId2 (Id integer, NotifyId integer, StdDicId2 text);
insert into t_NotifyId2 (Id, NotifyId, StdDicId2) select r.Id, r.NotifyId, d.Content2 from RecursionDrop as r join DropNotify as d on r.NotifyId == d.Id;
insert into t_NotifyId2 (Id, NotifyId, StdDicId2) select r.Id, r.NotifyId, '无' from RecursionDrop as r where not exists(select * from t_NotifyId2 where r.Id == t_NotifyId2.Id);

drop table if exists t_NotifyIdCon2;
create table t_NotifyIdCon2 (Id integer, NotifyId integer, StdDicId2 text, Content2 text);
insert into t_NotifyIdCon2 (Id, NotifyId, StdDicId2, Content2) select n.Id, n.NotifyId, n.StdDicId2, s.StrDictionary from t_NotifyId2 as n join StrDictionary as s on n.StdDicId2 == '#{' || s.Id || '}';
insert into t_NotifyIdCon2 (Id, NotifyId, StdDicId2, Content2) select n.Id, n.NotifyId, '无' , '无' from t_NotifyId2 as n where not exists(select * from t_NotifyIdCon2 where n.Id == t_NotifyIdCon2.Id);

drop table if exists t_NotifyIdCon2Final;
create table t_NotifyIdCon2Final(Id integer, NotifyId integer, StdDicId2 text, Content2 text);
insert into t_NotifyIdCon2Final select * from t_NotifyIdCon2 order by t_NotifyIdCon2.Id;

drop table if exists t_DropLuckyValue;
create table t_DropLuckyValue (Id integer, DropLuckyValueId integer, LuckyRatio real);
insert into t_DropLuckyValue (Id, DropLuckyValueId, LuckyRatio) select r.Id, r.DropLuckyValueId, d.LuckyRatio from RecursionDrop as r join DropLuckyValue as d on r.DropLuckyValueId == d.Id;
insert into t_DropLuckyValue (Id, DropLuckyValueId, LuckyRatio) select r.Id, r.DropLuckyValueId, 0 from RecursionDrop as r where not exists(select * from t_DropLuckyValue where r.Id == t_DropLuckyValue.Id);

drop table if exists t_DropLuckyValueFinal;
create table t_DropLuckyValueFinal(Id integer, DropLuckyValueId integer, LuckyRatio real);
insert into t_DropLuckyValueFinal select * from t_DropLuckyValue order by t_DropLuckyValue.Id;

--[LOOPTEMPLATE {0} 20]--
drop table if exists t_DropItem{0};
create table t_DropItem{0} (Id integer, DropType_{0} integer, ItemID_{0} integer, ItemName_{0} text, ItemLevel_{0}_Min integer, ItemLevel_{0}_Max integer, ItemDropRate_{0} real, Count_{0} integer);
insert into t_DropItem{0} (Id, DropType_{0}, ItemID_{0}, ItemName_{0}, ItemLevel_{0}_Min, ItemLevel_{0}_Max, ItemDropRate_{0}, Count_{0}) select r.Id, r.DropType_{0}, r.ItemID_{0}, c.Name, c.MinLevelRequire, c.MaxLevelRequire, r.ItemDropRate_{0}, r.Count_{0} from RecursionDrop as r join CommonItem as c on r.ItemID_{0} == c.Id and r.DropType_{0} == 1;
insert into t_DropItem{0} (Id, DropType_{0}, ItemID_{0}, ItemName_{0}, ItemLevel_{0}_Min, ItemLevel_{0}_Max, ItemDropRate_{0}, Count_{0}) select r.Id, r.DropType_{0}, r.ItemID_{0}, case when r.DropType_{0} == -1 then '无' when r.DropType_{0} == 1 then '没有此物品' when r.DropType_{0} == 2 then '掉落包' else '无' end, -1, -1, r.ItemDropRate_{0}, r.Count_{0} from RecursionDrop as r where not exists(select * from t_DropItem{0} where r.Id == t_DropItem{0}.Id);

drop table if exists t_DropItem{0}Final;
create table t_DropItem{0}Final (Id integer, DropType_{0} integer, ItemID_{0} integer, ItemName_{0} text, ItemLevel_{0}_Min integer, ItemLevel_{0}_Max integer, ItemDropRate_{0} real, Count_{0} integer);
insert into t_DropItem{0}Final select * from t_DropItem{0} order by t_DropItem{0}.Id;
--[LOOPTEMPLATE]--

drop table if exists t_RecursionDrop;
create table t_RecursionDrop(Id integer, NotifyId integer, StdDicId1 text, Content1 text, StdDicId2 text,Content2 text, DropLuckyValueId integer, LuckyRatio real,  
							DropType_1 integer, ItemID_1 integer, ItemName_1 text, ItemLevel_1_Min integer, ItemLevel_1_Max integer, ItemDropRate_1 real, Count_1 integer, 
							DropType_2 integer, ItemID_2 integer, ItemName_2 text, ItemLevel_2_Min integer, ItemLevel_2_Max integer, ItemDropRate_2 real, Count_2 integer, 
							DropType_3 integer, ItemID_3 integer, ItemName_3 text, ItemLevel_3_Min integer, ItemLevel_3_Max integer, ItemDropRate_3 real, Count_3 integer, 
							DropType_4 integer, ItemID_4 integer, ItemName_4 text, ItemLevel_4_Min integer, ItemLevel_4_Max integer, ItemDropRate_4 real, Count_4 integer, 
							DropType_5 integer, ItemID_5 integer, ItemName_5 text, ItemLevel_5_Min integer, ItemLevel_5_Max integer, ItemDropRate_5 real, Count_5 integer, 
							DropType_6 integer, ItemID_6 integer, ItemName_6 text, ItemLevel_6_Min integer, ItemLevel_6_Max integer, ItemDropRate_6 real, Count_6 integer, 
							DropType_7 integer, ItemID_7 integer, ItemName_7 text, ItemLevel_7_Min integer, ItemLevel_7_Max integer,ItemDropRate_7 real, Count_7 integer, 
							DropType_8 integer, ItemID_8 integer, ItemName_8 text, ItemLevel_8_Min integer, ItemLevel_8_Max integer, ItemDropRate_8 real, Count_8 integer, 
							DropType_9 integer, ItemID_9 integer, ItemName_9 text, ItemLevel_9_Min integer, ItemLevel_9_Max integer, ItemDropRate_9 real, Count_9 integer, 
							DropType_10 integer, ItemID_10 integer, ItemName_10 text, ItemLevel_10_Min integer, ItemLevel_10_Max integer, ItemDropRate_10 real, Count_10 integer, 
							DropType_11 integer, ItemID_11 integer, ItemName_11 text, ItemLevel_11_Min integer, ItemLevel_11_Max integer, ItemDropRate_11 real, Count_11 integer, 
							DropType_12 integer, ItemID_12 integer, ItemName_12 text, ItemLevel_12_Min integer, ItemLevel_12_Max integer, ItemDropRate_12 real, Count_12 integer, 
							DropType_13 integer, ItemID_13 integer, ItemName_13 text, ItemLevel_13_Min integer, ItemLevel_13_Max integer, ItemDropRate_13 real, Count_13 integer, 
							DropType_14 integer, ItemID_14 integer, ItemName_14 text, ItemLevel_14_Min integer, ItemLevel_14_Max integer, ItemDropRate_14 real, Count_14 integer, 
							DropType_15 integer, ItemID_15 integer, ItemName_15 text, ItemLevel_15_Min integer, ItemLevel_15_Max integer, ItemDropRate_15 real, Count_15 integer, 
							DropType_16 integer, ItemID_16 integer, ItemName_16 text, ItemLevel_16_Min integer, ItemLevel_16_Max integer, ItemDropRate_16 real, Count_16 integer, 
							DropType_17 integer, ItemID_17 integer, ItemName_17 text, ItemLevel_17_Min integer, ItemLevel_17_Max integer, ItemDropRate_17 real, Count_17 integer, 
							DropType_18 integer, ItemID_18 integer, ItemName_18 text, ItemLevel_18_Min integer, ItemLevel_18_Max integer, ItemDropRate_18 real, Count_18 integer, 
							DropType_19 integer, ItemID_19 integer, ItemName_19 text, ItemLevel_19_Min integer, ItemLevel_19_Max integer, ItemDropRate_19 real, Count_19 integer, 
							DropType_20 integer, ItemID_20 integer, ItemName_20 text, ItemLevel_20_Min integer, ItemLevel_20_Max integer, ItemDropRate_20 real, Count_20 integer);

insert into t_RecursionDrop (Id, NotifyId, StdDicId1, Content1, StdDicId2, Content2, DropLuckyValueId, LuckyRatio, 
                            DropType_1, ItemID_1, ItemName_1, ItemLevel_1_Min, ItemLevel_1_Max, ItemDropRate_1, Count_1, 
							DropType_2, ItemID_2, ItemName_2, ItemLevel_2_Min, ItemLevel_2_Max, ItemDropRate_2, Count_2, 
							DropType_3, ItemID_3, ItemName_3, ItemLevel_3_Min, ItemLevel_3_Max, ItemDropRate_3, Count_3, 
							DropType_4, ItemID_4, ItemName_4, ItemLevel_4_Min, ItemLevel_4_Max, ItemDropRate_4, Count_4, 
							DropType_5, ItemID_5, ItemName_5, ItemLevel_5_Min, ItemLevel_5_Max, ItemDropRate_5, Count_5, 
							DropType_6, ItemID_6, ItemName_6, ItemLevel_6_Min, ItemLevel_6_Max, ItemDropRate_6, Count_6, 
							DropType_7, ItemID_7, ItemName_7, ItemLevel_7_Min, ItemLevel_7_Max, ItemDropRate_7, Count_7, 
							DropType_8, ItemID_8, ItemName_8, ItemLevel_8_Min, ItemLevel_8_Max, ItemDropRate_8, Count_8, 
							DropType_9, ItemID_9, ItemName_9, ItemLevel_9_Min, ItemLevel_9_Max, ItemDropRate_9, Count_9, 
							DropType_10, ItemID_10, ItemName_10, ItemLevel_10_Min, ItemLevel_10_Max, ItemDropRate_10, Count_10, 
							DropType_11, ItemID_11, ItemName_11, ItemLevel_11_Min, ItemLevel_11_Max, ItemDropRate_11, Count_11, 
							DropType_12, ItemID_12, ItemName_12, ItemLevel_12_Min, ItemLevel_12_Max, ItemDropRate_12, Count_12, 
							DropType_13, ItemID_13, ItemName_13, ItemLevel_13_Min, ItemLevel_13_Max, ItemDropRate_13, Count_13, 
							DropType_14, ItemID_14, ItemName_14, ItemLevel_14_Min, ItemLevel_14_Max, ItemDropRate_14, Count_14, 
							DropType_15, ItemID_15, ItemName_15, ItemLevel_15_Min, ItemLevel_15_Max, ItemDropRate_15, Count_15, 
							DropType_16, ItemID_16, ItemName_16, ItemLevel_16_Min, ItemLevel_16_Max, ItemDropRate_16, Count_16, 
							DropType_17, ItemID_17, ItemName_17, ItemLevel_17_Min, ItemLevel_17_Max, ItemDropRate_17, Count_17, 
							DropType_18, ItemID_18, ItemName_18, ItemLevel_18_Min, ItemLevel_18_Max, ItemDropRate_18, Count_18, 
							DropType_19, ItemID_19, ItemName_19, ItemLevel_19_Min, ItemLevel_19_Max, ItemDropRate_19, Count_19, 
							DropType_20, ItemID_20, ItemName_20, ItemLevel_20_Min, ItemLevel_20_Max, ItemDropRate_20, Count_20) 
select nic1f.Id, nic1f.NotifyId, nic1f.StdDicId1, nic1f.Content1, nic2f.StdDicId2, nic2f.Content2, dlvf.DropLuckyValueId, dlvf.LuckyRatio,  
		dif1.DropType_1, dif1.ItemID_1, dif1.ItemName_1, dif1.ItemLevel_1_Min, dif1.ItemLevel_1_Max, dif1.ItemDropRate_1, dif1.Count_1, 
		dif2.DropType_2, dif2.ItemID_2, dif2.ItemName_2, dif2.ItemLevel_2_Min, dif2.ItemLevel_2_Max, dif2.ItemDropRate_2, dif2.Count_2, 
		dif3.DropType_3, dif3.ItemID_3, dif3.ItemName_3, dif3.ItemLevel_3_Min, dif3.ItemLevel_3_Max, dif3.ItemDropRate_3, dif3.Count_3, 
		dif4.DropType_4, dif4.ItemID_4, dif4.ItemName_4, dif4.ItemLevel_4_Min, dif4.ItemLevel_4_Max, dif4.ItemDropRate_4, dif4.Count_4, 
		dif5.DropType_5, dif5.ItemID_5, dif5.ItemName_5, dif5.ItemLevel_5_Min, dif5.ItemLevel_5_Max, dif5.ItemDropRate_5, dif5.Count_5, 
		dif6.DropType_6, dif6.ItemID_6, dif6.ItemName_6, dif6.ItemLevel_6_Min, dif6.ItemLevel_6_Max, dif6.ItemDropRate_6, dif6.Count_6, 
		dif7.DropType_7, dif7.ItemID_7, dif7.ItemName_7, dif7.ItemLevel_7_Min, dif7.ItemLevel_7_Max, dif7.ItemDropRate_7, dif7.Count_7, 
		dif8.DropType_8, dif8.ItemID_8, dif8.ItemName_8, dif8.ItemLevel_8_Min, dif8.ItemLevel_8_Max, dif8.ItemDropRate_8, dif8.Count_8, 
		dif9.DropType_9, dif9.ItemID_9, dif9.ItemName_9, dif9.ItemLevel_9_Min, dif9.ItemLevel_9_Max, dif9.ItemDropRate_9, dif9.Count_9, 
		dif10.DropType_10, dif10.ItemID_10, dif10.ItemName_10, dif10.ItemLevel_10_Min, dif10.ItemLevel_10_Max, dif10.ItemDropRate_10, dif10.Count_10, 
		dif11.DropType_11, dif11.ItemID_11, dif11.ItemName_11, dif11.ItemLevel_11_Min, dif11.ItemLevel_11_Max, dif11.ItemDropRate_11, dif11.Count_11, 
		dif12.DropType_12, dif12.ItemID_12, dif12.ItemName_12, dif12.ItemLevel_12_Min, dif12.ItemLevel_12_Max, dif12.ItemDropRate_12, dif12.Count_12, 
		dif13.DropType_13, dif13.ItemID_13, dif13.ItemName_13, dif13.ItemLevel_13_Min, dif13.ItemLevel_13_Max, dif13.ItemDropRate_13, dif13.Count_13, 
		dif14.DropType_14, dif14.ItemID_14, dif14.ItemName_14, dif14.ItemLevel_14_Min, dif14.ItemLevel_14_Max, dif14.ItemDropRate_14, dif14.Count_14, 
		dif15.DropType_15, dif15.ItemID_15, dif15.ItemName_15, dif15.ItemLevel_15_Min, dif15.ItemLevel_15_Max, dif15.ItemDropRate_15, dif15.Count_15, 
		dif16.DropType_16, dif16.ItemID_16, dif16.ItemName_16, dif16.ItemLevel_16_Min, dif16.ItemLevel_16_Max, dif16.ItemDropRate_16, dif16.Count_16, 
		dif17.DropType_17, dif17.ItemID_17, dif17.ItemName_17, dif17.ItemLevel_17_Min, dif17.ItemLevel_17_Max, dif17.ItemDropRate_17, dif17.Count_17, 
		dif18.DropType_18, dif18.ItemID_18, dif18.ItemName_18, dif18.ItemLevel_18_Min, dif18.ItemLevel_18_Max, dif18.ItemDropRate_18, dif18.Count_18, 
		dif19.DropType_19, dif19.ItemID_19, dif19.ItemName_19, dif19.ItemLevel_19_Min, dif19.ItemLevel_19_Max, dif19.ItemDropRate_19, dif19.Count_19, 
		dif20.DropType_20, dif20.ItemID_20, dif20.ItemName_20, dif20.ItemLevel_20_Min, dif20.ItemLevel_20_Max, dif20.ItemDropRate_20, dif20.Count_20 
from t_NotifyIdCon1Final as nic1f 
join t_NotifyIdCon2Final as nic2f on nic1f.Id == nic2f.Id  
join t_DropLuckyValueFinal as dlvf on nic1f.Id == dlvf.Id 
join t_DropItem1Final as dif1 on nic1f.Id == dif1.Id 
join t_DropItem2Final as dif2 on nic1f.Id == dif2.Id 
join t_DropItem3Final as dif3 on nic1f.Id == dif3.Id 
join t_DropItem4Final as dif4 on nic1f.Id == dif4.Id 
join t_DropItem5Final as dif5 on nic1f.Id == dif5.Id 
join t_DropItem6Final as dif6 on nic1f.Id == dif6.Id 
join t_DropItem7Final as dif7 on nic1f.Id == dif7.Id 
join t_DropItem8Final as dif8 on nic1f.Id == dif8.Id 
join t_DropItem9Final as dif9 on nic1f.Id == dif9.Id 
join t_DropItem10Final as dif10 on nic1f.Id == dif10.Id 
join t_DropItem11Final as dif11 on nic1f.Id == dif11.Id 
join t_DropItem12Final as dif12 on nic1f.Id == dif12.Id 
join t_DropItem13Final as dif13 on nic1f.Id == dif13.Id 
join t_DropItem14Final as dif14 on nic1f.Id == dif14.Id 
join t_DropItem15Final as dif15 on nic1f.Id == dif15.Id 
join t_DropItem16Final as dif16 on nic1f.Id == dif16.Id 
join t_DropItem17Final as dif17 on nic1f.Id == dif17.Id 
join t_DropItem18Final as dif18 on nic1f.Id == dif18.Id 
join t_DropItem19Final as dif19 on nic1f.Id == dif19.Id 
join t_DropItem20Final as dif20 on nic1f.Id == dif20.Id;

drop table if exists t_result;
create table t_result (Id integer, NotifyId integer, StdDicId1 text, Content1 text, StdDicId2 text, Content2 text, DropLuckyValueId integer, LuckyRatio real,  
						ItemID_1 integer, ItemName_1 text, ItemLevel_1_Min integer, ItemLevel_1_Max integer, ItemDropRate_1 real, Count_1 integer, 
						ItemID_2 integer, ItemName_2 text, ItemLevel_2_Min integer, ItemLevel_2_Max integer, ItemDropRate_2 real, Count_2 integer, 
						ItemID_3 integer, ItemName_3 text, ItemLevel_3_Min integer, ItemLevel_3_Max integer, ItemDropRate_3 real, Count_3 integer, 
						ItemID_4 integer, ItemName_4 text, ItemLevel_4_Min integer, ItemLevel_4_Max integer, ItemDropRate_4 real, Count_4 integer, 
						ItemID_5 integer, ItemName_5 text, ItemLevel_5_Min integer, ItemLevel_5_Max integer, ItemDropRate_5 real, Count_5 integer, 
						ItemID_6 integer, ItemName_6 text, ItemLevel_6_Min integer, ItemLevel_6_Max integer, ItemDropRate_6 real, Count_6 integer, 
						ItemID_7 integer, ItemName_7 text, ItemLevel_7_Min integer, ItemLevel_7_Max integer, ItemDropRate_7 real, Count_7 integer, 
						ItemID_8 integer, ItemName_8 text, ItemLevel_8_Min integer, ItemLevel_8_Max integer, ItemDropRate_8 real, Count_8 integer, 
						ItemID_9 integer, ItemName_9 text, ItemLevel_9_Min integer, ItemLevel_9_Max integer, ItemDropRate_9 real, Count_9 integer, 
						ItemID_10 integer, ItemName_10 text, ItemLevel_10_Min integer, ItemLevel_10_Max integer, ItemDropRate_10 real, Count_10 integer, 
						ItemID_11 integer, ItemName_11 text, ItemLevel_11_Min integer, ItemLevel_11_Max integer, ItemDropRate_11 real, Count_11 integer, 
						ItemID_12 integer, ItemName_12 text, ItemLevel_12_Min integer, ItemLevel_12_Max integer, ItemDropRate_12 real, Count_12 integer, 
						ItemID_13 integer, ItemName_13 text, ItemLevel_13_Min integer, ItemLevel_13_Max integer, ItemDropRate_13 real, Count_13 integer, 
						ItemID_14 integer, ItemName_14 text, ItemLevel_14_Min integer, ItemLevel_14_Max integer, ItemDropRate_14 real, Count_14 integer, 
						ItemID_15 integer, ItemName_15 text, ItemLevel_15_Min integer, ItemLevel_15_Max integer, ItemDropRate_15 real, Count_15 integer, 
						ItemID_16 integer, ItemName_16 text, ItemLevel_16_Min integer, ItemLevel_16_Max integer, ItemDropRate_16 real, Count_16 integer, 
						ItemID_17 integer, ItemName_17 text, ItemLevel_17_Min integer, ItemLevel_17_Max integer, ItemDropRate_17 real, Count_17 integer, 
						ItemID_18 integer, ItemName_18 text, ItemLevel_18_Min integer, ItemLevel_18_Max integer, ItemDropRate_18 real, Count_18 integer, 
						ItemID_19 integer, ItemName_19 text, ItemLevel_19_Min integer, ItemLevel_19_Max integer, ItemDropRate_19 real, Count_19 integer, 
						ItemID_20 integer, ItemName_20 text, ItemLevel_20_Min integer, ItemLevel_20_Max integer, ItemDropRate_20 real, Count_20 integer);
insert into t_result (Id, NotifyId, StdDicId1, Content1, StdDicId2, Content2, DropLuckyValueId, LuckyRatio, 
						ItemID_1, ItemName_1, ItemLevel_1_Min, ItemLevel_1_Max, ItemDropRate_1, Count_1, 
						ItemID_2, ItemName_2, ItemLevel_2_Min, ItemLevel_2_Max, ItemDropRate_2, Count_2, 
						ItemID_3, ItemName_3, ItemLevel_3_Min, ItemLevel_3_Max, ItemDropRate_3, Count_3, 
						ItemID_4, ItemName_4, ItemLevel_4_Min, ItemLevel_4_Max, ItemDropRate_4, Count_4, 
						ItemID_5, ItemName_5, ItemLevel_5_Min, ItemLevel_5_Max, ItemDropRate_5, Count_5, 
						ItemID_6, ItemName_6, ItemLevel_6_Min, ItemLevel_6_Max, ItemDropRate_6, Count_6, 
						ItemID_7, ItemName_7, ItemLevel_7_Min, ItemLevel_7_Max, ItemDropRate_7, Count_7, 
						ItemID_8, ItemName_8, ItemLevel_8_Min, ItemLevel_8_Max, ItemDropRate_8, Count_8, 
						ItemID_9, ItemName_9, ItemLevel_9_Min, ItemLevel_9_Max, ItemDropRate_9, Count_9, 
						ItemID_10, ItemName_10, ItemLevel_10_Min, ItemLevel_10_Max, ItemDropRate_10, Count_10, 
						ItemID_11, ItemName_11, ItemLevel_11_Min, ItemLevel_11_Max, ItemDropRate_11, Count_11, 
						ItemID_12, ItemName_12, ItemLevel_12_Min, ItemLevel_12_Max, ItemDropRate_12, Count_12, 
						ItemID_13, ItemName_13, ItemLevel_13_Min, ItemLevel_13_Max, ItemDropRate_13, Count_13, 
						ItemID_14, ItemName_14, ItemLevel_14_Min, ItemLevel_14_Max, ItemDropRate_14, Count_14, 
						ItemID_15, ItemName_15, ItemLevel_15_Min, ItemLevel_15_Max, ItemDropRate_15, Count_15, 
						ItemID_16, ItemName_16, ItemLevel_16_Min, ItemLevel_16_Max, ItemDropRate_16, Count_16, 
						ItemID_17, ItemName_17, ItemLevel_17_Min, ItemLevel_17_Max, ItemDropRate_17, Count_17, 
						ItemID_18, ItemName_18, ItemLevel_18_Min, ItemLevel_18_Max, ItemDropRate_18, Count_18, 
						ItemID_19, ItemName_19, ItemLevel_19_Min, ItemLevel_19_Max, ItemDropRate_19, Count_19, 
						ItemID_20, ItemName_20, ItemLevel_20_Min, ItemLevel_20_Max, ItemDropRate_20, Count_20) 
						select r.Id, r.NotifyId, r.StdDicId1, r.Content1, r.StdDicId2, r.Content2, r.DropLuckyValueId, r.LuckyRatio,  
						r.ItemID_1, r.ItemName_1, r.ItemLevel_1_Min, r.ItemLevel_1_Max, r.ItemDropRate_1, r.Count_1, 
						r.ItemID_2, r.ItemName_2, r.ItemLevel_2_Min, r.ItemLevel_2_Max, r.ItemDropRate_2, r.Count_2, 
						r.ItemID_3, r.ItemName_3, r.ItemLevel_3_Min, r.ItemLevel_3_Max, r.ItemDropRate_3, r.Count_3, 
						r.ItemID_4, r.ItemName_4, r.ItemLevel_4_Min, r.ItemLevel_4_Max, r.ItemDropRate_4, r.Count_4, 
						r.ItemID_5, r.ItemName_5, r.ItemLevel_5_Min, r.ItemLevel_5_Max, r.ItemDropRate_5, r.Count_5, 
						r.ItemID_6, r.ItemName_6, r.ItemLevel_6_Min, r.ItemLevel_6_Max, r.ItemDropRate_6, r.Count_6, 
						r.ItemID_7, r.ItemName_7, r.ItemLevel_7_Min, r.ItemLevel_7_Max, r.ItemDropRate_7, r.Count_7, 
						r.ItemID_8, r.ItemName_8, r.ItemLevel_8_Min, r.ItemLevel_8_Max, r.ItemDropRate_8, r.Count_8, 
						r.ItemID_9, r.ItemName_9, r.ItemLevel_9_Min, r.ItemLevel_9_Max, r.ItemDropRate_9, r.Count_9, 
						r.ItemID_10, r.ItemName_10, r.ItemLevel_10_Min, r.ItemLevel_10_Max, r.ItemDropRate_10, r.Count_10, 
						r.ItemID_11, r.ItemName_11, r.ItemLevel_11_Min, r.ItemLevel_11_Max, r.ItemDropRate_11, r.Count_11, 
						r.ItemID_12, r.ItemName_12, r.ItemLevel_12_Min, r.ItemLevel_12_Max, r.ItemDropRate_12, r.Count_12, 
						r.ItemID_13, r.ItemName_13, r.ItemLevel_13_Min, r.ItemLevel_13_Max, r.ItemDropRate_13, r.Count_13, 
						r.ItemID_14, r.ItemName_14, r.ItemLevel_14_Min, r.ItemLevel_14_Max, r.ItemDropRate_14, r.Count_14, 
						r.ItemID_15, r.ItemName_15, r.ItemLevel_15_Min, r.ItemLevel_15_Max, r.ItemDropRate_15, r.Count_15, 
						r.ItemID_16, r.ItemName_16, r.ItemLevel_16_Min, r.ItemLevel_16_Max, r.ItemDropRate_16, r.Count_16, 
						r.ItemID_17, r.ItemName_17, r.ItemLevel_17_Min, r.ItemLevel_17_Max, r.ItemDropRate_17, r.Count_17, 
						r.ItemID_18, r.ItemName_18, r.ItemLevel_18_Min, r.ItemLevel_18_Max, r.ItemDropRate_18, r.Count_18, 
						r.ItemID_19, r.ItemName_19, r.ItemLevel_19_Min, r.ItemLevel_19_Max, r.ItemDropRate_19, r.Count_19, 
						r.ItemID_20, r.ItemName_20, r.ItemLevel_20_Min, r.ItemLevel_20_Max, r.ItemDropRate_20, r.Count_20  
						from t_RecursionDrop as r join t_param as p on p.Id == r.Id;