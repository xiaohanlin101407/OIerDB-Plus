## OIer DB++
你是否因为无法根据一些信息来查询一位 OIer 的真实姓名而苦恼？你是否面对着很多获奖记录只能手动查询？你是否因为查询条件 OIerDB 不支持而苦恼？OIerDB++ 可以解决你的问题！它支持很多种查询，包您满意！  

### OIerDB Plus Lang
查询的一种方式是采用 OIerDB Plus Lang 来指定各种字段。对于每一个字段，形如
```
Table:
    xxxxxx
```
其中，第一行指定的是字段名，接下来若干行，描述你的查询条件。查询条件应当以若干个空白字符作为起始，否则会被解析为字段名称。例如，接下来几段都是合法的：
```
Table:
 xxxx
```
```
Table:
  xxxxx
   xxxxx
```
```
Table:
    xxx
     xxxxxxx   
```
但接下来的不是合法查询：
```
Table:
xxx
xxx
```

OIerDB Plus Lang 接受的字段名有：Records, initial, name, gender, enroll_middle, CCF Level。  
#### Records 字段
Records 字段用来指定获奖记录。接受多行，每行一个获奖记录，用 JSON 格式来表达。合法的 JSON 键值对仅包括以下描述的几个：

- contest: 一个整数，代表比赛编号。
- uid: 一个整数，代表 OIer 的 OIerDB uid。
- school: 一个整数，代表学校编号。
- score: 一个**字符串**，代表获得的分数。
- rank: 一个整数，代表排名。
- Province: 一个整数，代表省份。
- level: 一个整数，代表获奖等级。

Records 字段可以反复声明，OIerDB Lang 将会把所有提及的记录都作为合法的查询条件。

#### initial 字段
initial 字段用来指定姓名缩写。initial 字段仅能接受一行一个字符串，否则将会报错。  
initial 字段的参数应为一个仅包含英文字母的字符串。其大小写不敏感。

#### name 字段
name 字段用来指定姓名。name 字段仅能接受一行一个字符串，否则将会报错。  
name 字段的参数应为一个仅包含汉字的字符串。

#### gender 字段
gender 字段用来指定性别。gender 字段仅能接受一行一个整数，否则将会报错。  
gender 字段的值应在 $\{-1, 0, 1\}$，其中 $1$ 代表男性， $-1$ 代表女性， $0$ 代表性别未知。可能是因为获奖记录中未记录过其性别，或性别记录有误，或该选手是跨性别者，或其他情况，OIerDB Plus 不能很好的处理这种情况，如果想修改的请利用 GitHub Issue 向 **OIerDB 而不是 OIerDB Plus** 请求修改。

#### enroll_middle 字段
enroll_middle 字段用来指定一个人的初中入学年级。enroll_middle 字段仅能接受一行一个整数，否则将会报错。  
enroll_middle 字段的参数应为一个合理的整数。因为各地学制不一定完全相同，所以这一项的计算可能会出错。

#### CCF_level 字段
CCF_level 字段用来指定姓名缩写。CCF_level 字段仅能接受一行一个整数，否则将会报错。  
initial 字段的参数应为一个合理的整数。目前 CCF_level 应满足 $0\le x\le 10$。