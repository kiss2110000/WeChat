from moment import *


def changePriceFromText(d):
    """
    重写该函数，可以修改信息的文本内容，将修改后的文本内容发布在自己的朋友圈中。
    """
    # 获取详情的文字描述
    text_word = d(resourceId=Element["详情文字"]).get_text(timeout=5)
    print(" -- 原始文字:{}".format(text_word))

    # 匹配 "💰125" 这种"钱袋+价格"的方式，并加价30元。
    def _replace(matched):
        value = int(matched.group('price'))
        return matched.group('flag') + str(value+30)
    text_word = re.sub("(?P<flag>💰)(?P<price>\d{1,3})", _replace, text_word)

    # 匹配 "P125" 这种"P+价格"的方式，并加价30元。
    def _replace(matched):
        value = int(matched.group('price'))
        return "💰" + str(value+30)
    text_word = re.sub("(?P<flag>P)(?P<price>\d{1,3})", _replace, text_word)

    # 匹配 "2201788105739145" 这种"取一串数字的后三位数作为价格"的方式。
    def _replace(matched):
        value = matched.group('price')[-3:]
        value = value[1:] if value[0] == "0" else value
        return "💰" + str(value)
    text_word = re.sub("(?P<price>\d{10,18})", _replace, text_word)

    print(" -- 替换文字:{}".format(text_word))
    return text_word


d = u2.connect()
d.freeze_rotation()

Element = version["7.0.3"]
forLoopElms(d, shoucangChangePrice)