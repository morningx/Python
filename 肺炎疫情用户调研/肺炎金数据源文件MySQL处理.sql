# 20200126


# 1 调研数据集链接
# https://jinshuju.net/f/DqbKHF/r/jrMdw9/


# 2 webscaper浏览器插件爬取数据
# https://www.webscraper.io/cloud-scraper


# 3 Mysql导入数据库，改字段名及排列

use wuhanfeiyan_jinshuju;

select * from wuhanfeiyan;
desc wuhanfeiyan;
select count(id) from wuhanfeiyan;

SET SQL_SAFE_UPDATES = 0;

alter table wuhanfeiyan change column 序号 id varchar(100);
alter table wuhanfeiyan change column 您所在的位置 location varchar(100);

select * from wuhanfeiyan limit 3;

desc wuhanfeiyan;

# ALTER TABLE MODLFY 字段名1 数据类型 FIRST|AFTER 字段名2
# job  |age  |sex|education|time
# “字段名1”指的是修改位置的字段，“数据类型”指的是字段1的数据类型，
# “FIRST”为可选参数，指的是将字段1修改为表的第一个字段，
# “AFTER 字段名2”是将字段1插入到字段2的后面。
alter table wuhanfeiyan modify job varchar(500) after id;  
alter table wuhanfeiyan modify age varchar(100) after id;  
alter table wuhanfeiyan modify sex varchar(100) after id;  
alter table wuhanfeiyan modify education varchar(100) after id;  
alter table wuhanfeiyan modify time datetime FIRST;
