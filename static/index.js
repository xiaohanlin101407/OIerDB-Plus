function process(string) {
    var json_ = JSON.parse(string);
    var contest = { 'NOI2004': 0, 'NOI2005': 1, 'NOI2006': 2, 'NOI2007': 3, 'NOI2008': 4, 'NOIP2008提高': 5, 'NOI2009': 6, 'NOIP2009提高': 7, 'CTSC2010': 8, 'APIO2010': 9, 'NOI2010': 10, 'NOI2010D类': 11, 'IOI2010': 12, 'NOIP2010提高': 13, 'CTSC2011': 14, 'APIO2011': 15, 'NOI2011': 16, 'NOI2011D类': 17, 'IOI2011': 18, 'NOIP2011提高': 19, 'CTSC2012': 20, 'APIO2012': 21, 'NOI2012': 22, 'NOI2012D类': 23, 'IOI2012': 24, 'NOIP2012提高': 25, 'CTSC2013': 26, 'APIO2013': 27, 'NOI2013': 28, 'NOI2013D类': 29, 'IOI2013': 30, 'NOIP2013提高': 31, 'NOIP2013普及': 32, 'CTSC2014': 33, 'APIO2014': 34, 'NOI2014': 35, 'NOI2014D类': 36, 'IOI2014': 37, 'NOIP2014提高': 38, 'NOIP2014普及': 39, 'WC2015': 40, 'CTSC2015': 41, 'APIO2015': 42, 'NOI2015': 43, 'NOI2015D类': 44, 'IOI2015': 45, 'NOIP2015提高': 46, 'NOIP2015普及': 47, 'WC2016': 48, 'CTSC2016': 49, 'APIO2016': 50, 'NOI2016': 51, 'NOI2016D类': 52, 'IOI2016': 53, 'NOIP2016提高': 54, 'NOIP2016普及': 55, 'WC2017': 56, 'CTSC2017': 57, 'APIO2017': 58, 'NOI2017': 59, 'NOI2017D类': 60, 'IOI2017': 61, 'NOIP2017提高': 62, 'NOIP2017普及': 63, 'WC2018': 64, 'CTSC2018': 65, 'APIO2018': 66, 'NOI2018': 67, 'NOI2018D类': 68, 'IOI2018': 69, 'NOIP2018提高': 70, 'NOIP2018普及': 71, 'WC2019': 72, 'CTS2019': 73, 'APIO2019': 74, 'NOI2019': 75, 'NOI2019D类': 76, 'IOI2019': 77, 'CSP2019提高': 78, 'CSP2019入门': 79, 'WC2020': 80, 'APIO2020': 81, 'NOI2020': 82, 'NOI2020D类': 83, 'IOI2020': 84, 'CSP2020提高': 85, 'CSP2020入门': 86, 'NOIP2020': 87, 'WC2021': 88, 'APIO2021': 89, 'IOI2021': 90, 'NOI2021': 91, 'NOI2021D类': 92, 'CSP2021提高': 93, 'CSP2021入门': 94, 'NOIP2021': 95, 'WC2022': 96, 'NGOI2022': 97, 'APIO2022': 98, 'APIO2022线上': 99, 'IOI2022': 100, 'NOI2022': 101, 'NOI2022D类': 102, 'CSP2022提高': 103, 'CSP2022入门': 104, 'NOIP2022': 105, 'WC2023': 106, '春季测试2023': 107, 'NGOI2023': 108, 'APIO2023': 109, 'APIO2023线上': 110 };
    if ("contest" in json_) {
        var value = json_["contest"];
        if (typeof value == "string") {
            if(!(value in contest)) {
                alert(`"${value}" is not a valid contest name.`);
                throw new Error(`"${value}" is not a valid contest name.`);
            }
            json_["contest"] = contest[value];
        }
    }
    var level = { '金牌': 0, '银牌': 1, '铜牌': 2, '一等奖': 3, '二等奖': 4, '三等奖': 5, '国际金牌': 6, '国际银牌': 7, '国际铜牌': 8, '前5%': 9, '前15%': 10, '前25%': 11 };
    if ("level" in json_) {
        var value = json_["level"];
        if (typeof value == "string") {
            if(!(value in level)) {
                alert(`"${value}" is not a valid level name.`);
                throw new Error(`"${value}" is not a valid level name.`);
            }
            json_["level"] = level[value];
        }
    }
    var Province = { '安徽': 0, '北京': 1, '福建': 2, '甘肃': 3, '广东': 4, '广西': 5, '贵州': 6, '海南': 7, '河北': 8, '河南': 9, '黑龙江': 10, '湖北': 11, '湖南': 12, '吉林': 13, '江苏': 14, '江西': 15, '辽宁': 16, '内蒙古': 17, '山东': 18, '山西': 19, '陕西': 20, '上海': 21, '四川': 22, '天津': 23, '新疆': 24, '浙江': 25, '重庆': 26, '宁夏': 27, '云南': 28, '澳门': 29, '香港': 30, '青海': 31, '西藏': 32, '台湾': 33 };
    if ("Province" in json_) {
        var value = json_["Province"];
        if (typeof value == "string") {
            if(!(value in Province)) {
                alert(`"${value}" is not a valid Province name.`);
                throw new Error(`"${value}" is not a valid Province name.`);
            }
            json_["Province"] = Province[value];
        }
    }
    return JSON.stringify(json_);
}