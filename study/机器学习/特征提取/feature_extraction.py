from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import jieba


def dict_extraction():
    """
    字典特征提取
    sklearn.feature_extraction.DictVectorizer(sparse=True,…)
        DictVectorizer.fit_transform(X)
            X:字典或者包含字典的迭代器返回值
            返回sparse矩阵
        DictVectorizer.get_feature_names() 返回类别名称
    """
    data = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]
    # 1、实例化一个转换器类 sparse可以更节省内存的显示数据
    transfer = DictVectorizer(sparse=True)
    # 2、调用fit_transform
    transform_data = transfer.fit_transform(data)
    print("特征名字是：\n", transfer.get_feature_names())
    print("返回的结果：\n", transform_data)


def english_text_extraction():
    """
        英文文本特征提取
        sklearn.feature_extraction.text.CountVectorizer(stop_words=[])
        单个字符和标点符号不进行统计
        返回词频矩阵
          CountVectorizer.fit_transform(X)
           X:文本或者包含文本字符串的可迭代对象
           返回值:返回sparse矩阵
           CountVectorizer.get_feature_names() 返回值:单词列表
        sklearn.feature_extraction.text.TfidfVectorizer
    :return:
    """
    data = ["life is short,i like like python",
            "life is too long,i dislike python"]
    # 1、实例化一个转换器类
    transfer = CountVectorizer()# 注意,与DictVectorizer不同，没有sparse这个参数
    # 2、调用fit_transform
    data = transfer.fit_transform(data)
    #利用toarray()进行sparse矩阵转换array数组
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names())

def cut_word(text):
    """
    对中文进行分词
    "我爱北京天安门"————>"我 爱 北京 天安门"
    :param text:
    :return: text
    """
    # 用结巴对中文字符串进行分词
    text = " ".join(list(jieba.cut(text)))

    return text

def chinese_text_extraction():
    """
    在中文进行特征抽取之前 需要先进行分词（jieba）
    :return: None
    """
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 将原始数据转换成分好词的形式
    text_list = []
    for sent in data:
        text_list.append(cut_word(sent))
    # print(text_list)

    # 1、实例化一个转换器类
    transfer = CountVectorizer()
    # 2、调用fit_transform
    data = transfer.fit_transform(text_list)
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names())

def tf_idf_text_extraction():
    """
    TF-IDF的主要思想是：如果某个词或短语在一篇文章中出现的概率高，并且在其他文章中很少出现，则认为此词或者短语具有很好的类别区分能力，适合用来分类。
    TF-IDF作用：用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
    tf---词频
    idf---逆向文档频率
    """
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]
    # 将原始数据转换成分好词的形式
    text_list = []
    for sent in data:
        text_list.append(cut_word(sent))
    # 1、实例化一个转换器类
    transfer = TfidfVectorizer()
    # 2、调用fit_transform
    data = transfer.fit_transform(text_list)
    print("文本特征抽取的结果：\n", data.toarray())
    print("返回特征名字：\n", transfer.get_feature_names())





if __name__ == "__main__":
    # dict_extraction()
    # english_text_extraction()
    # chinese_text_extraction()
    tf_idf_text_extraction()
