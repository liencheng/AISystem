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
drop table if exists t_cps;
create table t_cps (Id integer, LvMin integer, LvMax integer);
insert into t_cps select Drop1, 0, 4 from CopySceneDrop where Id = (select Id from t_param) and Drop1 != -1;
insert into t_cps select Drop2, 5, 9 from CopySceneDrop where Id = (select Id from t_param) and Drop2 != -1;
insert into t_cps select Drop3, 10, 14 from CopySceneDrop where Id = (select Id from t_param) and Drop3 != -1;
insert into t_cps select Drop4, 15, 19 from CopySceneDrop where Id = (select Id from t_param) and Drop4 != -1;
insert into t_cps select Drop5, 20, 24 from CopySceneDrop where Id = (select Id from t_param) and Drop5 != -1;
insert into t_cps select Drop6, 25, 29 from CopySceneDrop where Id = (select Id from t_param) and Drop6 != -1;
insert into t_cps select Drop7, 30, 34 from CopySceneDrop where Id = (select Id from t_param) and Drop7 != -1;
insert into t_cps select Drop8, 35, 39 from CopySceneDrop where Id = (select Id from t_param) and Drop8 != -1;
insert into t_cps select Drop9, 40, 44 from CopySceneDrop where Id = (select Id from t_param) and Drop9 != -1;
insert into t_cps select Drop10, 45, 49 from CopySceneDrop where Id = (select Id from t_param) and Drop10 != -1;
insert into t_cps select Drop11, 50, 54 from CopySceneDrop where Id = (select Id from t_param) and Drop11 != -1;
insert into t_cps select Drop12, 55, 59 from CopySceneDrop where Id = (select Id from t_param) and Drop12 != -1;
insert into t_cps select Drop13, 60, 64 from CopySceneDrop where Id = (select Id from t_param) and Drop13 != -1;
insert into t_cps select Drop14, 65, 69 from CopySceneDrop where Id = (select Id from t_param) and Drop14 != -1;
insert into t_cps select Drop15, 70, 74 from CopySceneDrop where Id = (select Id from t_param) and Drop15 != -1;
insert into t_cps select Drop16, 75, 79 from CopySceneDrop where Id = (select Id from t_param) and Drop16 != -1;
insert into t_cps select Drop17, 80, 84 from CopySceneDrop where Id = (select Id from t_param) and Drop17 != -1;
insert into t_cps select Drop18, 85, 89 from CopySceneDrop where Id = (select Id from t_param) and Drop18 != -1;
insert into t_cps select Drop19, 90, 94 from CopySceneDrop where Id = (select Id from t_param) and Drop19 != -1;
insert into t_cps select Drop20, 95, 99 from CopySceneDrop where Id = (select Id from t_param) and Drop20 != -1;
insert into t_cps select Drop21, 100, 104 from CopySceneDrop where Id = (select Id from t_param) and Drop21 != -1;
insert into t_cps select Drop22, 105, 109 from CopySceneDrop where Id = (select Id from t_param) and Drop22 != -1;
insert into t_cps select Drop23, 110, 114 from CopySceneDrop where Id = (select Id from t_param) and Drop23 != -1;
insert into t_cps select Drop24, 115, 119 from CopySceneDrop where Id = (select Id from t_param) and Drop24 != -1;
insert into t_cps select Drop25, 120, 124 from CopySceneDrop where Id = (select Id from t_param) and Drop25 != -1;
insert into t_cps select Drop26, 125, 129 from CopySceneDrop where Id = (select Id from t_param) and Drop26 != -1;
insert into t_cps select Drop27, 130, 134 from CopySceneDrop where Id = (select Id from t_param) and Drop27 != -1;
insert into t_cps select Drop28, 135, 139 from CopySceneDrop where Id = (select Id from t_param) and Drop28 != -1;
insert into t_cps select Drop29, 140, 144 from CopySceneDrop where Id = (select Id from t_param) and Drop29 != -1;
insert into t_cps select Drop30, 145, 149 from CopySceneDrop where Id = (select Id from t_param) and Drop30 != -1;
insert into t_cps select Drop31, 150, 154 from CopySceneDrop where Id = (select Id from t_param) and Drop31 != -1;
insert into t_cps select Drop32, 155, 159 from CopySceneDrop where Id = (select Id from t_param) and Drop32 != -1;
insert into t_cps select Drop33, 160, 164 from CopySceneDrop where Id = (select Id from t_param) and Drop33 != -1;
insert into t_cps select Drop34, 165, 169 from CopySceneDrop where Id = (select Id from t_param) and Drop34 != -1;
insert into t_cps select Drop35, 170, 174 from CopySceneDrop where Id = (select Id from t_param) and Drop35 != -1;
insert into t_cps select Drop36, 175, 179 from CopySceneDrop where Id = (select Id from t_param) and Drop36 != -1;
insert into t_cps select Drop37, 180, 184 from CopySceneDrop where Id = (select Id from t_param) and Drop37 != -1;
insert into t_cps select Drop38, 185, 189 from CopySceneDrop where Id = (select Id from t_param) and Drop38 != -1;
insert into t_cps select Drop39, 190, 194 from CopySceneDrop where Id = (select Id from t_param) and Drop39 != -1;
insert into t_cps select Drop40, 195, 199 from CopySceneDrop where Id = (select Id from t_param) and Drop40 != -1;
insert into t_cps select Drop41, 200, 204 from CopySceneDrop where Id = (select Id from t_param) and Drop41 != -1;
insert into t_cps select Drop42, 205, 209 from CopySceneDrop where Id = (select Id from t_param) and Drop42 != -1;
insert into t_cps select Drop43, 210, 214 from CopySceneDrop where Id = (select Id from t_param) and Drop43 != -1;
insert into t_cps select Drop44, 215, 219 from CopySceneDrop where Id = (select Id from t_param) and Drop44 != -1;
insert into t_cps select Drop45, 220, 224 from CopySceneDrop where Id = (select Id from t_param) and Drop45 != -1;
insert into t_cps select Drop46, 225, 229 from CopySceneDrop where Id = (select Id from t_param) and Drop46 != -1;
insert into t_cps select Drop47, 230, 234 from CopySceneDrop where Id = (select Id from t_param) and Drop47 != -1;
insert into t_cps select Drop48, 235, 239 from CopySceneDrop where Id = (select Id from t_param) and Drop48 != -1;
insert into t_cps select Drop49, 240, 244 from CopySceneDrop where Id = (select Id from t_param) and Drop49 != -1;
insert into t_cps select Drop50, 245, 249 from CopySceneDrop where Id = (select Id from t_param) and Drop50 != -1;
insert into t_cps select Drop51, 250, 254 from CopySceneDrop where Id = (select Id from t_param) and Drop51 != -1;
insert into t_cps select Drop52, 255, 259 from CopySceneDrop where Id = (select Id from t_param) and Drop52 != -1;
insert into t_cps select Drop53, 260, 264 from CopySceneDrop where Id = (select Id from t_param) and Drop53 != -1;
insert into t_cps select Drop54, 265, 269 from CopySceneDrop where Id = (select Id from t_param) and Drop54 != -1;
insert into t_cps select Drop55, 270, 274 from CopySceneDrop where Id = (select Id from t_param) and Drop55 != -1;
insert into t_cps select Drop56, 275, 279 from CopySceneDrop where Id = (select Id from t_param) and Drop56 != -1;
insert into t_cps select Drop57, 280, 284 from CopySceneDrop where Id = (select Id from t_param) and Drop57 != -1;
insert into t_cps select Drop58, 285, 289 from CopySceneDrop where Id = (select Id from t_param) and Drop58 != -1;
insert into t_cps select Drop59, 290, 294 from CopySceneDrop where Id = (select Id from t_param) and Drop59 != -1;
insert into t_cps select Drop60, 295, 299 from CopySceneDrop where Id = (select Id from t_param) and Drop60 != -1;
insert into t_cps select Drop61, 300, 304 from CopySceneDrop where Id = (select Id from t_param) and Drop61 != -1;
insert into t_cps select Drop62, 305, 309 from CopySceneDrop where Id = (select Id from t_param) and Drop62 != -1;
insert into t_cps select Drop63, 310, 314 from CopySceneDrop where Id = (select Id from t_param) and Drop63 != -1;
insert into t_cps select Drop64, 315, 319 from CopySceneDrop where Id = (select Id from t_param) and Drop64 != -1;
insert into t_cps select Drop65, 320, 324 from CopySceneDrop where Id = (select Id from t_param) and Drop65 != -1;
insert into t_cps select Drop66, 325, 329 from CopySceneDrop where Id = (select Id from t_param) and Drop66 != -1;
insert into t_cps select Drop67, 330, 334 from CopySceneDrop where Id = (select Id from t_param) and Drop67 != -1;
insert into t_cps select Drop68, 335, 339 from CopySceneDrop where Id = (select Id from t_param) and Drop68 != -1;
insert into t_cps select Drop69, 340, 344 from CopySceneDrop where Id = (select Id from t_param) and Drop69 != -1;
insert into t_cps select Drop70, 345, 349 from CopySceneDrop where Id = (select Id from t_param) and Drop70 != -1;
insert into t_cps select Drop71, 350, 354 from CopySceneDrop where Id = (select Id from t_param) and Drop71 != -1;
insert into t_cps select Drop72, 355, 359 from CopySceneDrop where Id = (select Id from t_param) and Drop72 != -1;
insert into t_cps select Drop73, 360, 364 from CopySceneDrop where Id = (select Id from t_param) and Drop73 != -1;
insert into t_cps select Drop74, 365, 369 from CopySceneDrop where Id = (select Id from t_param) and Drop74 != -1;
insert into t_cps select Drop75, 370, 374 from CopySceneDrop where Id = (select Id from t_param) and Drop75 != -1;
insert into t_cps select Drop76, 375, 379 from CopySceneDrop where Id = (select Id from t_param) and Drop76 != -1;
insert into t_cps select Drop77, 380, 384 from CopySceneDrop where Id = (select Id from t_param) and Drop77 != -1;
insert into t_cps select Drop78, 385, 389 from CopySceneDrop where Id = (select Id from t_param) and Drop78 != -1;
insert into t_cps select Drop79, 390, 394 from CopySceneDrop where Id = (select Id from t_param) and Drop79 != -1;
insert into t_cps select Drop80, 395, 399 from CopySceneDrop where Id = (select Id from t_param) and Drop80 != -1;
insert into t_cps select Drop81, 400, 404 from CopySceneDrop where Id = (select Id from t_param) and Drop81 != -1;
insert into t_cps select Drop82, 405, 409 from CopySceneDrop where Id = (select Id from t_param) and Drop82 != -1;
insert into t_cps select Drop83, 410, 414 from CopySceneDrop where Id = (select Id from t_param) and Drop83 != -1;
insert into t_cps select Drop84, 415, 419 from CopySceneDrop where Id = (select Id from t_param) and Drop84 != -1;
insert into t_cps select Drop85, 420, 424 from CopySceneDrop where Id = (select Id from t_param) and Drop85 != -1;
insert into t_cps select Drop86, 425, 429 from CopySceneDrop where Id = (select Id from t_param) and Drop86 != -1;
insert into t_cps select Drop87, 430, 434 from CopySceneDrop where Id = (select Id from t_param) and Drop87 != -1;
insert into t_cps select Drop88, 435, 439 from CopySceneDrop where Id = (select Id from t_param) and Drop88 != -1;
insert into t_cps select Drop89, 440, 444 from CopySceneDrop where Id = (select Id from t_param) and Drop89 != -1;
insert into t_cps select Drop90, 445, 449 from CopySceneDrop where Id = (select Id from t_param) and Drop90 != -1;
insert into t_cps select Drop91, 450, 454 from CopySceneDrop where Id = (select Id from t_param) and Drop91 != -1;
insert into t_cps select Drop92, 455, 459 from CopySceneDrop where Id = (select Id from t_param) and Drop92 != -1;
insert into t_cps select Drop93, 460, 464 from CopySceneDrop where Id = (select Id from t_param) and Drop93 != -1;
insert into t_cps select Drop94, 465, 469 from CopySceneDrop where Id = (select Id from t_param) and Drop94 != -1;
insert into t_cps select Drop95, 470, 474 from CopySceneDrop where Id = (select Id from t_param) and Drop95 != -1;
insert into t_cps select Drop96, 475, 479 from CopySceneDrop where Id = (select Id from t_param) and Drop96 != -1;
insert into t_cps select Drop97, 480, 484 from CopySceneDrop where Id = (select Id from t_param) and Drop97 != -1;
insert into t_cps select Drop98, 485, 489 from CopySceneDrop where Id = (select Id from t_param) and Drop98 != -1;
insert into t_cps select Drop99, 490, 494 from CopySceneDrop where Id = (select Id from t_param) and Drop99 != -1;
insert into t_cps select Drop100, 495, 499 from CopySceneDrop where Id = (select Id from t_param) and Drop100 != -1;
insert into t_cps select Drop101, 500, 504 from CopySceneDrop where Id = (select Id from t_param) and Drop101 != -1;
insert into t_cps select Drop102, 505, 509 from CopySceneDrop where Id = (select Id from t_param) and Drop102 != -1;
insert into t_cps select Drop103, 510, 514 from CopySceneDrop where Id = (select Id from t_param) and Drop103 != -1;
insert into t_cps select Drop104, 515, 519 from CopySceneDrop where Id = (select Id from t_param) and Drop104 != -1;
insert into t_cps select Drop105, 520, 524 from CopySceneDrop where Id = (select Id from t_param) and Drop105 != -1;
insert into t_cps select Drop106, 525, 529 from CopySceneDrop where Id = (select Id from t_param) and Drop106 != -1;
insert into t_cps select Drop107, 530, 534 from CopySceneDrop where Id = (select Id from t_param) and Drop107 != -1;
insert into t_cps select Drop108, 535, 539 from CopySceneDrop where Id = (select Id from t_param) and Drop108 != -1;
insert into t_cps select Drop109, 540, 544 from CopySceneDrop where Id = (select Id from t_param) and Drop109 != -1;
insert into t_cps select Drop110, 545, 549 from CopySceneDrop where Id = (select Id from t_param) and Drop110 != -1;
insert into t_cps select Drop111, 550, 554 from CopySceneDrop where Id = (select Id from t_param) and Drop111 != -1;
insert into t_cps select Drop112, 555, 559 from CopySceneDrop where Id = (select Id from t_param) and Drop112 != -1;
insert into t_cps select Drop113, 560, 564 from CopySceneDrop where Id = (select Id from t_param) and Drop113 != -1;
insert into t_cps select Drop114, 565, 569 from CopySceneDrop where Id = (select Id from t_param) and Drop114 != -1;
insert into t_cps select Drop115, 570, 574 from CopySceneDrop where Id = (select Id from t_param) and Drop115 != -1;
insert into t_cps select Drop116, 575, 579 from CopySceneDrop where Id = (select Id from t_param) and Drop116 != -1;
insert into t_cps select Drop117, 580, 584 from CopySceneDrop where Id = (select Id from t_param) and Drop117 != -1;
insert into t_cps select Drop118, 585, 589 from CopySceneDrop where Id = (select Id from t_param) and Drop118 != -1;
insert into t_cps select Drop119, 590, 594 from CopySceneDrop where Id = (select Id from t_param) and Drop119 != -1;
insert into t_cps select Drop120, 595, 599 from CopySceneDrop where Id = (select Id from t_param) and Drop120 != -1;

drop table if exists t_task;
create table t_task (Id integer, rate real, profession integer, LvMin integer, LvMax integer, origin integer);
insert into t_task select d.CommonDropIndex1 , 1, (case when d.IsCommonDropClass = 0 then -1 else 0  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex1  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex2 , 1, (case when d.IsCommonDropClass = 0 then -1 else 1  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex2  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex3 , 1, (case when d.IsCommonDropClass = 0 then -1 else 2  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex3  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex4 , 1, (case when d.IsCommonDropClass = 0 then -1 else 3  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex4  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex5 , 1, (case when d.IsCommonDropClass = 0 then -1 else 4  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex5  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex6 , 1, (case when d.IsCommonDropClass = 0 then -1 else 5  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex6  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex7 , 1, (case when d.IsCommonDropClass = 0 then -1 else 6  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex7  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex8 , 1, (case when d.IsCommonDropClass = 0 then -1 else 7  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex8  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex9 , 1, (case when d.IsCommonDropClass = 0 then -1 else 8  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex9  != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex10, 1, (case when d.IsCommonDropClass = 0 then -1 else 9  end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex10 != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);
insert into t_task select d.CommonDropIndex11, 1, (case when d.IsCommonDropClass = 0 then -1 else 10 end), c.LvMin, c.LvMax, c.Id from t_cps as c join DropList as d on d.CommonDropIndex11 != -1 and c.Id = d.Id and c.LvMin >= (select LvMin from t_param) and c.LvMax <= (select LvMax from t_param);

drop table if exists t_tasktmp;
create table t_tasktmp (Id integer, rate real, profession integer, LvMin integer, LvMax integer, origin integer);

--准备好中间表
drop table if exists t_middle;
create table t_middle (Id integer, count integer, rate real, profession integer, LvMin integer, LvMax integer, origin integer);

--第一遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第二遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第三遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第四遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--第五遍
delete from t_tasktmp;
insert into t_tasktmp select * from t_task;
delete from t_task;
insert into t_middle select r.ItemID_1  , r.Count_1  , (r.ItemDropRate_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 1 and r.ItemDropRate_1  > 0;
insert into t_middle select r.ItemID_2  , r.Count_2  , (r.ItemDropRate_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 1 and r.ItemDropRate_2  > 0;
insert into t_middle select r.ItemID_3  , r.Count_3  , (r.ItemDropRate_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 1 and r.ItemDropRate_3  > 0;
insert into t_middle select r.ItemID_4  , r.Count_4  , (r.ItemDropRate_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 1 and r.ItemDropRate_4  > 0;
insert into t_middle select r.ItemID_5  , r.Count_5  , (r.ItemDropRate_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 1 and r.ItemDropRate_5  > 0;
insert into t_middle select r.ItemID_6  , r.Count_6  , (r.ItemDropRate_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 1 and r.ItemDropRate_6  > 0;
insert into t_middle select r.ItemID_7  , r.Count_7  , (r.ItemDropRate_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 1 and r.ItemDropRate_7  > 0;
insert into t_middle select r.ItemID_8  , r.Count_8  , (r.ItemDropRate_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 1 and r.ItemDropRate_8  > 0;
insert into t_middle select r.ItemID_9  , r.Count_9  , (r.ItemDropRate_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 1 and r.ItemDropRate_9  > 0;
insert into t_middle select r.ItemID_10 , r.Count_10 , (r.ItemDropRate_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 1 and r.ItemDropRate_10 > 0;
insert into t_middle select r.ItemID_11 , r.Count_11 , (r.ItemDropRate_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 1 and r.ItemDropRate_11 > 0;
insert into t_middle select r.ItemID_12 , r.Count_12 , (r.ItemDropRate_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 1 and r.ItemDropRate_12 > 0;
insert into t_middle select r.ItemID_13 , r.Count_13 , (r.ItemDropRate_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 1 and r.ItemDropRate_13 > 0;
insert into t_middle select r.ItemID_14 , r.Count_14 , (r.ItemDropRate_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 1 and r.ItemDropRate_14 > 0;
insert into t_middle select r.ItemID_15 , r.Count_15 , (r.ItemDropRate_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 1 and r.ItemDropRate_15 > 0;
insert into t_middle select r.ItemID_16 , r.Count_16 , (r.ItemDropRate_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 1 and r.ItemDropRate_16 > 0;
insert into t_middle select r.ItemID_17 , r.Count_17 , (r.ItemDropRate_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 1 and r.ItemDropRate_17 > 0;
insert into t_middle select r.ItemID_18 , r.Count_18 , (r.ItemDropRate_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 1 and r.ItemDropRate_18 > 0;
insert into t_middle select r.ItemID_19 , r.Count_19 , (r.ItemDropRate_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 1 and r.ItemDropRate_19 > 0;
insert into t_middle select r.ItemID_20 , r.Count_20 , (r.ItemDropRate_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 1 and r.ItemDropRate_20 > 0;

insert into t_task select r.ItemID_1 , (r.ItemDropRate_1   * r.Count_1   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_1  = 2 and r.ItemDropRate_1  > 0;
insert into t_task select r.ItemID_2 , (r.ItemDropRate_2   * r.Count_2   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_2  = 2 and r.ItemDropRate_2  > 0;
insert into t_task select r.ItemID_3 , (r.ItemDropRate_3   * r.Count_3   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_3  = 2 and r.ItemDropRate_3  > 0;
insert into t_task select r.ItemID_4 , (r.ItemDropRate_4   * r.Count_4   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_4  = 2 and r.ItemDropRate_4  > 0;
insert into t_task select r.ItemID_5 , (r.ItemDropRate_5   * r.Count_5   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_5  = 2 and r.ItemDropRate_5  > 0;
insert into t_task select r.ItemID_6 , (r.ItemDropRate_6   * r.Count_6   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_6  = 2 and r.ItemDropRate_6  > 0;
insert into t_task select r.ItemID_7 , (r.ItemDropRate_7   * r.Count_7   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_7  = 2 and r.ItemDropRate_7  > 0;
insert into t_task select r.ItemID_8 , (r.ItemDropRate_8   * r.Count_8   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_8  = 2 and r.ItemDropRate_8  > 0;
insert into t_task select r.ItemID_9 , (r.ItemDropRate_9   * r.Count_9   / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_9  = 2 and r.ItemDropRate_9  > 0;
insert into t_task select r.ItemID_10, (r.ItemDropRate_10  * r.Count_10  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_10 = 2 and r.ItemDropRate_10 > 0;
insert into t_task select r.ItemID_11, (r.ItemDropRate_11  * r.Count_11  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_11 = 2 and r.ItemDropRate_11 > 0;
insert into t_task select r.ItemID_12, (r.ItemDropRate_12  * r.Count_12  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_12 = 2 and r.ItemDropRate_12 > 0;
insert into t_task select r.ItemID_13, (r.ItemDropRate_13  * r.Count_13  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_13 = 2 and r.ItemDropRate_13 > 0;
insert into t_task select r.ItemID_14, (r.ItemDropRate_14  * r.Count_14  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_14 = 2 and r.ItemDropRate_14 > 0;
insert into t_task select r.ItemID_15, (r.ItemDropRate_15  * r.Count_15  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_15 = 2 and r.ItemDropRate_15 > 0;
insert into t_task select r.ItemID_16, (r.ItemDropRate_16  * r.Count_16  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_16 = 2 and r.ItemDropRate_16 > 0;
insert into t_task select r.ItemID_17, (r.ItemDropRate_17  * r.Count_17  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_17 = 2 and r.ItemDropRate_17 > 0;
insert into t_task select r.ItemID_18, (r.ItemDropRate_18  * r.Count_18  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_18 = 2 and r.ItemDropRate_18 > 0;
insert into t_task select r.ItemID_19, (r.ItemDropRate_19  * r.Count_19  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_19 = 2 and r.ItemDropRate_19 > 0;
insert into t_task select r.ItemID_20, (r.ItemDropRate_20  * r.Count_20  / r.ratesum) * l.rate, l.profession, l.LvMin, l.LvMax, l.origin from t_tasktmp as l  join t_dropcopy as r on l.Id = r.Id and r.DropType_20 = 2 and r.ItemDropRate_20 > 0;

--准备好结果表
drop table if exists t_result;
create table t_result (Id integer, description text, name text, count integer, rate real, profession integer, LvMin integer, LvMax integer, origin integer, sortOrder integer);
insert into t_result select m.Id, c.Desc, c.Name, m.count, m.rate, m.profession, m.LvMin, m.LvMax, m.origin, m.LvMin * 100 + m.profession from t_middle as m  join CommonItem as c on m.Id = c.Id