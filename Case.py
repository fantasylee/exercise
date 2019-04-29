# -- coding: UTF-8 --
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
import csv
"""
常用的一些函数
"""
# xpath=open('xpath.csv')
# xpath_package=csv.DictReader(xpath)
def model_chose(num):
    if num=='1':#正常方式启动浏览器
        return webdriver.Chrome()
    elif num=='2':#不开浏览器直接运行，并发时能够节省跑脚本机器的资源
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        return webdriver.Chrome(options=option)
    elif num=='3':#以手机调试模式打开浏览器，H5
        mobile_emulation = {"deviceName": "Galaxy S5"}
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        return webdriver.Chrome(options=options)

def Execute_Js_Scroll_Top(driver):
    if driver.name == "chrome":  #获取浏览器名称
       js = "var q=document.body.scrollTop=0"
    else:
        js = "var q=document.documentElement.scrollTop=0"
    return driver.execute_script(js)
# 滚动底部
def Execute_Js_scroll_Foot(driver):
    if driver.name == "chrome":  #获取浏览器名称
        js = "var q=document.body.scrollTop=10000"
    else:
        js = "var q=document.documentElement.scrollTop=10000"
    return driver.execute_script(js)

def list_package(value):#常用的一些列表
        if value=='num':
            list=[num for num in range(0,10)]
        elif value=='EN_all':
            list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        elif value=='CN':
            list=["一","丁","七","万","丈","三","上","下","不","与","丐","丑","专","且","世","丘","丙","业","丛","东","丝","丢","两","严","丧","丨","个","丫","中","丰","串","临","丸","丹","为","主","丽","举",
    "么","义","之","乌","乍","乎","乏","乐","乒","乓","乔","乖","乘","乙","乜","九","乞","也","习","乡","书","买","乱","乳","乾","了","予","争","事","二","于","亏","云","互","亓","五","井","亘","亚","些",
    "亟","亡","亢","交","亥","亦","产","亨","亩","享","京","亭","亮","亲","亵","人","亿","什","仁","仃","仅","仆","仇","今","介","仍","从","仑","仓","仔","仕","他","仗","付","仙","仞","代","令","以","仪",
    "们","仰","仲","件","价","任","份","仿","企","伊","伍","伎","伏","伐","休","众","优","伙","会","伞","伟","传","伤","伥","伦","伪","伯","估","伴","伶","伸","伺","似","伽","但","位","低","住","佐","佑",
    "体","何","余","佛","作","佝","你","佣","佩","佬","佯","佳","佻","佼","使","侃","侄","侈","例","侍","侏","供","依","侠","侣","侥","侦","侧","侨","侩","侮","侯","侵","便","促","俄","俊","俎","俏","俐",
    "俑","俗","俘","保","俟","信","俨","俩","俭","修","俯","俱","俺","倌","倍","倏","倒","倔","候","倚","倜","借","倡","倦","倨","倩","倪","债","值","倾","偃","假","偌","偎","偏","偕","做","停","健","偶",
    "偷","偻","偿","傀","傅","傍","傥","储","催","傲","傻","像","僚","僧","僭","僵","僻","儆","儒","儡","儿","兀","允","元","兄","充","兆","先","光","克","免","兑","兔","党","兜","兢","入","全","八","公",
    "六","兮","兰","共","关","兴","兵","其","具","典","养","兼","兽","冀","内","冈","冉","册","再","冒","冕","冖","冗","写","军","农","冠","冢","冤","冥","冬","冯","冰","冲","决","况","冶","冷","冻","冼",
    "冽","净","凄","准","凉","凋","凌","减","凑","凛","凝","几","凡","凤","凭","凯","凰","凳","凶","凸","凹","出","击","函","凿","刀","刁","刃","分","切","刊","刎","刑","划","列","刘","则","刚","创","初",
    "删","判","刨","利","别","刮","到","制","刷","券","刹","刺","刻","刽","剁","剂","剃","削","前","剐","剑","剔","剖","剥","剧","剩","剪","副","割","剽","剿","劈","力","劝","办","功","加","务","劣","动",
    "助","努","劫","励","劲","劳","势","勃","勇","勉","勋","勒","勘","募","勤","勺","勾","勿","匀","包","匆","匈","匕","化","北","匙","匠","匡","匣","匪","匮","匹","区","医","匾","匿","十","千","升","午",
    "半","华","协","卑","卒","卓","单","卖","南","博","卜","卞","占","卡","卢","卤","卦","卧","卫","卯","印","危","即","却","卵","卷","卸","卿","厂","厄","厅","历","厉","压","厌","厕","厘","厚","原","厢",
    "厥","厦","厨","厮","去","县","参","又","叉","及","友","双","反","发","叔","取","受","变","叙","叛","叟","叠","口","古","句","另","叨","叩","只","叫","召","叭","叮","可","台","叱","史","右","叵","叶",
    "号","司","叹","叼","叽","吁","吃","各","吆","合","吉","吊","同","名","后","吏","吐","向","吓","吕","吗","吚","君","吝","吞","吟","吠","否","吧","吨","吩","含","听","吭","吮","启","吱","吴","吵","吸",
    "吹","吻","吼","吾","呀","呃","呆","呈","告","呐","呓","呕","呗","员","呛","呜","呢","周","呱","呲","味","呵","呶","呸","呻","呼","命","咀","咂","咄","咆","咋","和","咎","咐","咒","咔","咕","咖","咙",
    "咚","咛","咣","咤","咦","咧","咨","咪","咫","咬","咯","咱","咳","咸","咽","咿","哀","品","哄","哆","哇","哈","哉","响","哎","哏","哐","哑","哗","哟","哥","哦","哧","哨","哩","哪","哭","哮","哲","哺",
    "哼","哽","唁","唆","唇","唉","唏","唐","唔","唠","唤","唬","售","唯","唱","唳","唷","唾","啃","啄","商","啊","啐","啕","啜","啡","啤","啥","啦","啧","啪","啬","啰","啸","啻","啼","啾","喂","喃","善",
    "喇","喉","喊","喋","喏","喑","喘","喜","喝","喟","喧","喳","喷","喻","喽","嗅","嗑","嗒","嗓","嗔","嗜","嗝","嗡","嗤","嗦","嗯","嗲","嗵","嗷","嗽","嘀","嘈","嘉","嘎","嘘","嘛","嘟","嘣","嘤","嘭",
    "嘱","嘲","嘴","嘶","嘹","嘻","嘿","噎","噔","噗","噘","噙","噜","噤","器","噩","噪","噬","噱","噼","嚅","嚎","嚏","嚓","嚣","嚷","嚼","囊","囔","囘","囚","四","回","因","团","囤","园","囯","困","囱",
    "围","囹","固","国","图","圃","圄","圆","圈","圌","土","圣","在","圭","地","圳","场","圾","址","均","坊","坍","坎","坏","坐","坑","块","坚","坛","坝","坞","坟","坠","坡","坤","坦","坨","坪","坯","坳",
    "坷","垂","垃","垄","型","垒","垓","垢","垣","垦","垩","垫","垮","埃","埋","城","域","培","基","堀","堂","堆","堑","堕","堡","堤","堪","堵","塌","塑","塔","塘","塞","填","境","墅","墓","墙","增","墟",
    "墨","墩","壁","壑","壕","壤","士","壬","壮","声","壳","壶","壹","处","备","复","夏","夕","外","夙","多","夜","够","大","天","太","夫","夭","央","夯","失","头","夷","夸","夹","夺","奂","奄","奇","奈",
    "奉","奋","奏","契","奔","奕","奖","套","奚","奠","奢","奥","女","奴","奶","奸","她","好","如","妃","妄","妆","妇","妈","妊","妒","妓","妖","妙","妞","妣","妥","妨","妩","妮","妯","妹","妻","妾","姆",
    "始","姐","姑","姓","委","姗","姚","姜","姝","姣","姥","姨","姹","姻","姿","威","娃","娄","娆","娇","娉","娌","娑","娓","娘","娜","娟","娠","娥","娱","娴","娶","娼","婀","婆","婉","婊","婚","婢","婪",
    "婴","婶","婷","婿","媒","媚","媛","媲","媳","嫁","嫂","嫉","嫌","嫖","嫡","嫣","嫦","嫩","嬉","孀","子","孔","孕","字","存","孙","孜","孝","孟","孢","季","孤","学","孩","孪","孬","孰","孺","孽","宁",
    "它","宅","宇","守","安","宋","完","宏","宕","宗","官","宙","定","宛","宜","宝","实","宠","审","客","宣","室","宦","宪","宫","宰","害","宴","宵","家","容","宽","宾","宿","寂","寄","寅","密","寇","富",
    "寐","寒","寓","寝","寞","察","寡","寥","寨","寰","寸","对","寺","寻","导","寿","封","射","将","尊","小","少","尔","尖","尘","尚","尝","尤","尧","尬","就","尴","尸","尹","尺","尼","尽","尾","尿","局",
    "屁","层","居","屈","屉","届","屋","屎","屏","屐","屑","展","属","屠","屡","屣","履","山","屹","屿","岁","岂","岌","岐","岔","岖","岗","岚","岛","岩","岫","岭","岳","岸","岿","峋","峙","峡","峥","峦",
    "峨","峭","峰","峻","崇","崎","崔","崖","崛","崩","崭","崴","崽","嵋","嵘","嶙","巅","巍","川","州","巡","巢","工","左","巧","巨","巩","巫","差","己","已","巳","巴","巷","巾","币","市","布","帅","帆",
    "师","希","帐","帕","帖","帘","帚","帛","帜","帝","带","席","帮","帷","常","帼","帽","幄","幅","幌","幕","幡","幢","干","平","年","并","幸","幺","幻","幼","幽","广","庄","庆","庇","床","序","庐","库",
    "应","底","庖","店","庙","府","庞","废","庠","度","座","庭","庶","康","庸","廉","廊","廓","廖","延","廷","建","开","异","弃","弄","弈","弊","式","弓","引","弗","弘","弛","弟","张","弥","弦","弧","弩",
    "弭","弯","弱","弹","强","弼","彊","归","当","录","彗","形","彤","彦","彩","彪","彬","彭","彰","影","彷","役","彻","彼","往","征","径","待","徇","很","徊","律","徐","徒","得","徘","御","徨","循","微",
    "德","徽","心","必","忆","忌","忍","忏","忐","忑","忖","志","忘","忙","忠","忡","忤","忧","忪","快","念","忽","忾","忿","怀","态","怂","怅","怆","怎","怏","怒","怔","怕","怖","怜","思","怠","怡","急",
    "怦","性","怨","怪","怫","怯","怵","总","恁","恃","恋","恍","恏","恐","恒","恕","恙","恢","恤","恨","恩","恪","恫","恬","恭","息","恰","恳","恶","恹","恻","恼","恿","悄","悉","悍","悔","悖","悚","悟",
    "悠","患","悦","您","悬","悯","悱","悲","悴","悸","悻","悼","情","惆","惊","惋","惑","惕","惚","惜","惟","惠","惦","惧","惨","惩","惫","惬","惭","惮","惯","惰","想","惶","惹","惺","愁","愈","愉","愎",
    "意","愕","愚","感","愠","愣","愤","愧","愫","愿","慈","慌","慎","慑","慕","慢","慧","慨","慰","慵","慷","憋","憎","憔","憧","憨","憩","憬","憾","懂","懈","懊","懑","懒","懦","懵","戈","戊","戌","戍",
    "戎","戏","成","我","戒","或","战","戚","戛","戟","截","戳","戴","户","戾","房","所","扁","扇","扈","扉","手","才","扎","扑","扒","打","扔","托","扛","扣","执","扩","扪","扫","扬","扭","扮","扯","扰",
    "扳","扶","批","扼","找","承","技","抄","抉","把","抑","抒","抓","投","抖","抗","折","抚","抛","抠","抡","抢","护","报","抨","披","抬","抱","抵","抹","押","抽","抿","拂","担","拆","拇","拈","拉","拌",
    "拍","拎","拐","拒","拓","拔","拖","拗","拘","拙","招","拜","拟","拢","拣","拥","拦","拧","拨","择","括","拭","拯","拱","拳","拴","拷","拼","拽","拾","拿","持","挂","指","挈","按","挑","挖","挚","挛",
    "挞","挟","挠","挡","挣","挤","挥","挨","挪","挫","振","挲","挺","挽","捂","捅","捆","捉","捋","捍","捎","捏","捐","捕","捞","损","捡","换","捣","捧","捭","据","捱","捶","捷","捺","掀","掂","掇","授",
    "掉","掌","掏","掐","排","掖","掘","掠","探","掣","接","控","推","掩","措","掬","掰","掴","掷","掸","掺","揄","揉","揍","描","提","插","揖","握","揣","揩","揪","揭","援","揶","揽","搀","搁","搂","搅",
    "搏","搐","搓","搔","搜","搞","搡","搪","搬","搭","携","摁","摄","摆","摇","摊","摒","摔","摘","摞","摧","摩","摸","摹","摺","撂","撅","撇","撑","撒","撕","撞","撤","撩","撬","播","撮","撰","撷","撸",
    "撼","擀","擂","擅","操","擎","擒","擞","擦","攀","攒","攘","攥","支","收","攸","改","攻","放","政","故","效","敌","敏","救","敘","教","敛","敝","敞","敢","散","敦","敬","数","敲","整","敷","文","斋",
    "斌","斐","斑","斗","料","斜","斟","斡","斤","斥","斧","斩","断","斯","新","方","施","旁","旅","旋","旎","族","旖","旗","无","既","日","旦","旧","旨","早","旬","旭","旮","旯","旱","时","旷","旺","昂",
    "昆","昊","昌","明","昏","易","昔","昕","昙","星","映","春","昧","昨","昭","是","昱","昵","昼","显","晁","晃","晋","晌","晒","晓","晕","晖","晗","晚","晤","晦","晨","普","景","晰","晳","晴","晶","智",
    "晾","暂","暄","暇","暑","暖","暗","暧","暨","暮","暴","曙","曝","曦","曰","曲","曳","更","曹","曼","曾","替","最","月","有","朋","服","朔","朕","朗","望","朝","期","朦","木","未","末","本","术","朱",
    "朴","朵","机","朽","杀","杂","权","杆","李","杏","材","村","杖","杜","杞","束","杠","条","来","杨","杭","杯","杰","杳","杵","松","板","极","构","枉","析","枕","林","枙","枚","果","枝","枢","枣","枥",
    "枪","枫","枭","枯","枳","架","枷","枸","柄","柏","某","染","柔","柚","柜","柠","查","柬","柯","柱","柳","柴","柿","栅","标","栈","栉","栋","栏","树","栓","栖","栗","校","栩","株","样","核","根","格",
    "栽","桀","桂","桃","框","案","桌","桐","桑","桓","桔","档","桥","桧","桨","桩","桶","梁","梅","梆","梗","梢","梦","梧","梨","梭","梯","械","梳","检","棂","棉","棋","棍","棒","棕","棘","棚","棠","棣",
    "森","棰","棱","棵","棺","椅","植","椎","椒","椭","椽","楔","楗","楚","楞","楠","楷","楼","概","榄","榆","榔","榕","榜","榨","榭","榴","榷","榻","槁","槌","槐","槛","槟","槽","樊","模","横","樯","樱",
    "橄","橘","橙","橡","橹","檄","檐","檬","欠","次","欢","欣","欧","欲","欺","款","歇","歉","歌","止","正","此","步","武","歧","歪","歹","死","歼","殃","殄","殆","殉","殊","残","殒","殖","殚","殡","殴",
    "段","殷","殿","毁","毅","毋","母","每","毒","比","毕","毖","毗","毙","毛","毡","毫","毯","氏","民","氓","气","氛","氟","氢","氤","氧","氨","氪","氯","氰","氲","水","永","汀","汁","求","汇","汉","汐",
    "汗","汛","江","池","污","汤","汩","汪","汰","汲","汶","汹","汽","汾","沁","沂","沃","沆","沈","沉","沏","沐","沓","沙","沛","沟","没","沥","沦","沧","沪","沫","沮","沱","河","沸","油","治","沼","沽",
    "沾","沿","泄","泉","泊","泌","泓","法","泛","泞","泠","泡","波","泣","泥","注","泪","泯","泰","泱","泳","泵","泻","泼","泽","泾","洁","洋","洌","洒","洗","洛","洞","津","洪","洱","洲","活","洼","洽",
    "派","流","浃","浅","浆","浇","浊","测","济","浏","浑","浓","浙","浜","浦","浩","浪","浮","浴","海","浸","涂","消","涉","涌","涎","涓","涕","涛","涝","涟","涡","涣","润","涧","涨","涩","涮","涯","液",
    "涵","涸","涿","淀","淅","淆","淋","淌","淑","淖","淘","淙","淞","淡","淤","淫","淬","深","淳","混","淹","添","清","渊","渍","渎","渐","渔","渗","渠","渡","渣","渤","温","渭","港","渲","渴","游","渺",
    "湃","湍","湖","湘","湛","湮","湾","湿","溃","溅","溉","源","溘","溜","溢","溪","溯","溶","溺","滂","滇","滋","滑","滓","滔","滕","滚","滞","满","滤","滥","滨","滩","滴","漂","漆","漉","漏","漓","演",
    "漠","漩","漪","漫","漱","漾","潇","潘","潜","潦","潭","潮","潸","潺","澄","澈","澎","澜","澡","澳","澹","激","濒","濛","濡","瀑","瀚","瀛","瀣","灌","火","灭","灯","灰","灵","灶","灼","灾","灿","炉",
    "炊","炎","炒","炖","炙","炫","炬","炭","炮","炯","炳","炸","点","為","炼","炽","烁","烂","烈","烔","烕","烘","烙","烛","烟","烤","烦","烧","烨","烩","烫","热","烹","烽","焉","焊","焕","焖","焚","焦",
    "焰","然","煌","煎","煞","煤","煦","照","煮","煽","熄","熊","熏","熙","熟","熠","熨","熬","燃","燎","燕","燥","爆","爪","爬","爰","爱","爵","父","爷","爸","爹","爽","片","版","牌","牍","牒","牙","牛",
    "牟","牡","牢","牧","物","牲","牵","特","牺","犀","犁","犄","犊","犏","犒","犟","犬","犯","犰","状","犷","犹","狂","狄","狈","狍","狎","狐","狗","狙","狞","狠","狡","狩","独","狭","狮","狰","狱","狲",
    "狸","狼","猎","猕","猖","猛","猜","猝","猢","猥","猩","猪","猫","猬","献","猴","猾","猿","獗","獠","玄","率","玉","王","玑","玛","玩","玫","环","现","玲","玷","玻","珈","珊","珍","珑","珠","班","球",
    "琅","理","琉","琐","琢","琦","琳","琴","琵","琶","琼","瑕","瑜","瑞","瑟","瑰","瑶","瑾","璀","璃","璇","璋","璜","璞","璧","璨","瓜","瓢","瓣","瓦","瓮","瓴","瓶","瓷","甄","甘","甚","甜","生","甥",
    "用","甩","甫","甬","甭","田","由","甲","申","电","男","甸","画","畅","界","畏","畔","留","畜","略","番","畴","畸","畿","疆","疏","疑","疗","疙","疚","疤","疫","疮","疯","疲","疴","疵","疼","疾","病",
    "症","痉","痊","痒","痕","痘","痛","痞","痣","痪","痰","痴","痹","瘁","瘆","瘟","瘠","瘤","瘦","瘩","瘪","瘫","瘴","瘸","瘾","癌","癖","癞","癣","登","白","百","皂","的","皆","皇","皈","皎","皓","皙",
    "皮","皱","皿","盆","盈","益","盎","盏","盐","监","盒","盔","盖","盗","盘","盛","盟","目","盯","盲","直","相","盹","盼","盾","省","眈","眉","看","真","眠","眦","眨","眩","眯","眶","眷","眸","眺","眼",
    "着","睁","睐","睚","睛","睡","督","睦","睫","睬","睹","睽","睿","瞄","瞅","瞌","瞎","瞑","瞒","瞟","瞠","瞥","瞧","瞩","瞪","瞬","瞭","瞰","瞳","瞻","矍","矗","矛","矜","矢","矣","知","矩","矫","短",
    "矮","石","矿","码","砂","砌","砍","研","砖","砚","砝","砥","砭","砰","破","砸","砺","础","硊","硌","硕","硝","硫","硬","确","硼","碌","碍","碎","碑","碗","碘","碜","碟","碣","碧","碰","碱","碳","碴",
    "碾","磁","磅","磊","磋","磐","磕","磨","礴","示","礼","社","祁","祈","祖","祛","祝","神","祥","票","祭","祯","祷","祸","祼","禀","禁","禄","禅","福","禧","禹","离","禽","禾","秀","私","秃","秆","秉",
    "秋","种","科","秒","秘","租","秤","秦","秧","秩","积","称","移","秽","稀","程","稍","税","稔","稗","稚","稠","稳","稷","稻","稼","稽","稿","穆","穴","究","穷","穹","空","穿","突","窃","窄","窈","窍",
    "窑","窒","窕","窖","窗","窘","窜","窝","窟","窣","窥","窦","窸","窿","立","竖","站","竞","竟","章","竣","童","竦","竭","端","竹","竽","竿","笃","笋","笑","笔","笙","笛","笠","符","笨","第","笺","笼",
    "等","筋","筐","筑","筒","答","策","筛","筝","筠","筱","筷","筹","签","简","箍","箕","算","管","箩","箪","箭","箱","篇","篑","篓","篝","篡","篮","篱","簇","簌","簧","簪","簸","籁","籍","米","类","籽",
    "粉","粒","粕","粗","粘","粟","粤","粥","粪","粮","粱","粹","粼","粽","精","糊","糕","糖","糗","糙","糜","糟","糠","系","紊","素","索","紧","紫","累","絮","網","繁","纠","纡","红","纣","纤","约","级",
    "纨","纪","纫","纬","纭","纯","纰","纱","纲","纳","纵","纶","纷","纸","纹","纺","纽","线","练","组","绅","细","织","终","绉","绊","绌","绍","绎","经","绑","绒","结","绔","绕","绘","给","绚","络","绝",
    "绞","统","绢","绣","继","绩","绪","续","绮","绯","绰","绳","维","绵","绷","绸","绺","绻","综","绽","绿","缀","缄","缅","缆","缉","缎","缓","缔","缕","编","缘","缚","缛","缜","缝","缠","缤","缨","缩",
    "缪","缭","缰","缱","缴","缸","缺","罂","罄","罐","网","罔","罕","罗","罚","罡","罢","罩","罪","置","署","罹","羁","羊","羌","美","羔","羞","羡","群","羸","羹","羽","翁","翅","翌","翔","翕","翘","翟",
    "翠","翡","翩","翰","翱","翻","翼","耀","老","考","者","而","耍","耐","耕","耗","耘","耙","耳","耶","耸","耻","耽","耿","聂","聆","聊","聋","职","聒","联","聘","聚","聩","聪","肃","肆","肇","肉","肋",
    "肌","肓","肖","肘","肚","肝","肠","股","肢","肤","肥","肩","肪","肮","肯","育","肴","肺","肾","肿","胀","胁","胃","胄","胆","背","胎","胖","胚","胜","胞","胡","胤","胥","胧","胫","胯","胳","胴","胶",
    "胸","胺","能","脂","脆","脉","脊","脏","脐","脑","脖","脚","脯","脱","脸","脾","腆","腊","腋","腌","腐","腑","腔","腕","腚","腥","腮","腰","腴","腹","腻","腼","腾","腿","膀","膊","膏","膘","膛","膜",
    "膝","膨","膺","臀","臂","臃","臆","臊","臣","自","臭","至","致","臾","舅","舆","舌","舍","舐","舒","舔","舜","舞","舟","航","般","舰","舱","舵","船","艇","艘","良","艰","色","艳","艺","艾","节","芋",
    "芒","芙","芜","芝","芥","芦","芬","芭","芯","花","芳","芷","芸","芹","芽","苍","苏","苑","苔","苗","苛","苞","苟","若","苦","苯","英","苹","茁","茂","范","茄","茅","茉","茕","茗","茧","茨","茫","茬",
    "茵","茶","茸","茹","荀","荆","草","荏","荐","荒","荜","荞","荟","荡","荣","荤","荧","荫","药","荷","荼","莅","莉","莓","莘","莜","莞","莠","莫","莱","莲","获","莹","莺","莽","菁","菅","菊","菌","菜",
    "菠","菡","菩","菲","萃","萄","萋","萌","萍","萎","萏","萝","营","萦","萧","萨","萱","落","著","葛","葡","董","葩","葫","葬","葱","葵","葺","蒂","蒋","蒙","蒜","蒲","蒸","蒿","蓄","蓉","蓑","蓓","蓝",
    "蓦","蓬","蔑","蔓","蔗","蔚","蔡","蔫","蔬","蔷","蔺","蔼","蔽","蕉","蕊","蕙","蕨","蕴","蕻","蕾","薄","薇","薪","薯","藉","藏","藐","藓","藕","藤","藻","蘑","蘸","虎","虏","虐","虑","虚","虞","虫",
    "虱","虹","虽","虾","蚀","蚁","蚂","蚊","蚌","蚍","蚕","蚤","蚪","蚱","蛀","蛇","蛊","蛋","蛔","蛙","蛛","蛟","蛤","蛮","蛰","蛾","蜀","蜂","蜇","蜉","蜒","蜓","蜕","蜗","蜘","蜚","蜛","蜜","蜡","蜷",
    "蜻","蜿","蝇","蝉","蝌","蝎","蝗","蝴","蝶","螂","螃","融","螳","螺","蟀","蟆","蟋","蟑","蟹","蠕","蠢","血","衅","行","衍","衔","街","衙","衡","衢","衣","补","表","衩","衫","衬","衰","衷","衾","袁",
    "袄","袅","袋","袍","袒","袖","袜","袤","被","袭","袱","裁","裂","装","裆","裔","裕","裘","裙","裤","裨","裱","裳","裴","裸","裹","裾","褂","褐","褒","褓","褚","褛","褥","褪","褴","襁","襄","襟","西",
    "要","覃","覆","见","观","规","觅","视","览","觉","觊","觎","觑","角","解","觥","触","言","記","誉","誊","誓","說","警","讀","计","订","讣","认","讥","讧","讨","让","讪","训","议","讯","记","讲","讳",
    "讴","讶","讷","许","讹","论","讼","讽","设","访","诀","证","诃","评","诅","识","诈","诉","诊","诋","诌","词","译","试","诗","诙","诚","诛","话","诞","诟","诠","诡","询","诣","该","详","诧","诨","诩",
    "诫","诬","语","误","诱","诲","说","诵","请","诸","诺","读","诽","课","诿","谀","谁","调","谄","谅","谆","谈","谊","谋","谍","谎","谐","谑","谓","谗","谙","谛","谜","谡","谢","谣","谤","谦","谧","谨",
    "谩","谪","谬","谭","谱","谲","谴","谶","谷","豁","豆","豌","豙","豚","象","豢","豪","豫","豸","豹","豺","貂","貉","貌","贝","贞","负","贡","财","责","贤","败","账","货","质","贩","贪","贫","贬","购",
    "贯","贰","贱","贲","贴","贵","贷","贸","费","贺","贻","贼","贽","贾","贿","赁","赂","赃","资","赅","赈","赋","赌","赎","赏","赐","赔","赖","赘","赚","赛","赝","赞","赠","赡","赢","赣","赤","赦","赧",
    "赫","走","赴","赵","赶","起","趁","超","越","趋","趟","趣","足","趴","趾","跃","跄","跋","跌","跑","跚","跛","距","跟","跤","跨","跪","跬","路","跳","践","跷","跺","跻","踉","踊","踌","踏","踝","踞",
    "踢","踩","踪","踮","踱","踵","踹","踽","蹂","蹄","蹈","蹊","蹋","蹑","蹒","蹙","蹚","蹦","蹩","蹬","蹭","蹲","蹴","蹶","蹿","躁","躇","躏","身","躬","躯","躲","躺","车","轧","轨","轩","转","轮","软",
    "轰","轲","轴","轶","轻","轼","载","轿","较","辄","辅","辆","辈","辉","辍","辐","辑","输","辕","辖","辗","辘","辙","辛","辜","辞","辟","辣","辨","辩","辫","辰","辱","边","辽","达","迁","迂","迄","迅",
    "过","迈","迎","运","近","返","还","这","进","远","违","连","迟","迢","迥","迩","迪","迫","迭","述","迷","迸","迹","追","退","送","适","逃","逆","选","逊","逍","透","逐","逑","递","途","逗","通","逛",
    "逝","逞","速","造","逢","逮","逸","逻","逼","逾","遁","遂","遇","遍","遏","遐","遑","遒","道","遗","遛","遢","遣","遥","遭","遮","遵","避","邀","邃","邋","邓","邢","那","邦","邪","邮","邯","邰","邱",
    "邵","邹","邻","郁","郊","郎","郑","郜","郝","郞","部","郭","郸","都","鄂","鄙","鄣","酊","酌","配","酒","酗","酝","酡","酣","酥","酩","酬","酱","酵","酷","酸","酿","醇","醉","醋","醒","醚","醺","采",
    "释","里","重","野","量","金","釜","鉴","鎏","鑫","针","钉","钒","钓","钙","钛","钝","钞","钟","钢","钥","钦","钧","钩","钮","钱","钳","钵","钻","钾","铁","铃","铄","铅","铐","铛","铜","铠","铤","铩",
    "铭","铮","铲","银","铸","铺","链","铿","销","锁","锃","锄","锅","锈","锋","锌","锏","锐","锒","错","锚","锡","锢","锣","锤","锥","锦","锨","键","锯","锵","锹","锻","镀","镂","镇","镍","镖","镜","镣",
    "镯","镰","镳","镶","长","閱","门","闩","闪","闭","问","闯","闲","间","闷","闸","闹","闺","闻","闽","阀","阁","阂","阄","阅","阉","阎","阐","阑","阒","阔","阖","队","阱","防","阳","阴","阵","阶","阻",
    "阿","陀","附","际","陆","陇","陈","陋","陌","降","限","陕","陛","陡","院","除","陨","险","陪","陵","陶","陷","隅","隆","隋","随","隐","隔","隘","隙","障","隧","隶","隼","隽","难","雀","雁","雄","雅",
    "集","雇","雌","雍","雏","雕","雨","雪","雯","雳","零","雷","雹","雾","需","霁","霄","霆","震","霉","霍","霓","霖","霜","霞","露","霸","霹","青","靓","静","非","靠","靡","面","靥","革","靴","靶","鞅",
    "鞋","鞍","鞘","鞠","鞭","韦","韧","韩","韪","韬","韭","音","韵","韶","页","顶","顷","项","顺","须","顽","顾","顿","颁","颂","预","颅","领","颇","颈","颊","颐","频","颓","颔","颖","颗","题","颜","额",
    "颠","颤","颦","颧","风","飒","飘","飙","飞","食","餐","饥","饭","饮","饰","饱","饲","饴","饵","饶","饷","饺","饼","饽","饿","馁","馅","馆","馈","馊","馋","馒","首","香","馨","马","驭","驮","驯","驰",
    "驱","驳","驴","驶","驹","驻","驼","驾","驿","骂","骄","骅","骆","骇","骋","验","骑","骗","骚","骛","骜","骤","骥","骨","骸","骼","髅","髓","體","高","髦","髻","鬓","鬟","鬼","魁","魂","魄","魅","魇",
    "魉","魍","魏","魑","魔","鱼","鲁","鲂","鲜","鲟","鲠","鲤","鲨","鲫","鲲","鲸","鳄","鳅","鳌","鳐","鳖","鳞","鸟","鸡","鸣","鸥","鸦","鸨","鸩","鸭","鸯","鸳","鸵","鸽","鸾","鸿","鹂","鹃","鹅","鹉",
    "鹊","鹏","鹘","鹜","鹤","鹦","鹭","鹰","鹿","麋","麟","麦","麻","麾","黄","黎","黏","黑","黔","默","黛","黝","黠","黧","黩","黯","鼎","鼓","鼠","鼻","鼾","齐","齑","齿","龄","龇","龊","龌","龘","龙",
    "龟","乃","久",]
        elif value=='en':
            list=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        elif value=='EN':
            list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        elif value=='headers':
            list=[
                "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
                "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
                "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
                "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
                "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
                "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
                "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
                "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
                "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
                "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
                "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
                "UCWEB7.0.2.37/28/999",
                "NOKIA5700/ UCWEB7.0.2.37/28/999",
                "Openwave/ UCWEB7.0.2.37/28/999",
                "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
                # iPhone 6：
                "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

            ]

        return list


def suijishu(y,x=0,z=1):
    """
    在x到y之间随机产生z个数
    """
    fanwei=[num for num in range(x,y+1)]
    haha=random.sample(fanwei,z)
    return haha
def Phoneunmber_suiji():
    Phonenumber='1'
    secend=str(suijishu(9,3)[0])
    Phonenumber+=secend
    three_to_11=suijishu(9,z=9)
    for i in three_to_11:
        Phonenumber+=str(i)
    return Phonenumber

def true_name_suiji():
    name=''
    num=suijishu(4,2,1)
    # print num
    list=list_package('CN')
    words_package=random.sample(list,num[0])
    for i in words_package:
        name+=i
    return name
def user_suiji():
    user=''
    weishu=random.randint(5,11)
    first_wordp=list_package('EN_all')
    first_word=random.sample(first_wordp,1)
    user+=first_word[0]
    pack=first_wordp+list_package('num')+['_']
    username=random.sample(pack,weishu)
    for i in username:
        user+=str(i)
    return user
def QQnumber_suiji():
    number=''
    list1=[num for num in range(1,10)]
    firstnum=random.sample(list1,1)
    number+=str(firstnum[0])
    weishu=random.randint(4,9)
    list2=[num for num in range(0,10)]
    number_package=random.sample(list2,weishu)
    for i in number_package:
        number+=str(i)
    return number
def wx_suiji():
    wx=''
    first_word_list=list_package("EN_all")
    first_word=random.sample(first_word_list,1)
    wx+=first_word[0]
    another_word_list=list_package('num')+list_package('EN_all')
    weishu=suijishu(19,5,1)
    another_word=random.sample(another_word_list,weishu[0])
    for another in another_word:
        wx+=str(another)
    return wx
#

def switch_to_new_window(driver):#跳到最新开的窗口
    handles = driver.window_handles
    driver.switch_to_window(handles[-1])

def get_char(num,what_char='x'):
    now = int(time.time())     # 1533952277
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    str_255=otherStyleTime.center(num,what_char)
    return str_255



if __name__ == '__main__':
    d=model_chose('1')
    wait=WebDriverWait(d, 2)
    send = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
    )




