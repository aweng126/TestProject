
def deduplicate_data(file):
    """
    读取原始数据文件进行去重操作，返回一个包含不重复元素的
    :param file:  存储初始数据的文件名
    :return:  所有的不重复的数据，格式为list
    """
    s = set()
    with open(file, 'r') as f:
        sentence = ""
        for line in f:
            if line.strip() != "" and "沙雕" not in line:
                sentence = sentence + line
            else:
                s.add(sentence)
                sentence = ""
    return list(s)


def create_data_file(dlist, nfile):
    with open(nfile, 'w') as f:
        for item in dlist:
            f.write(item + '\r\n')


def begin_process():
    data_list = deduplicate_data("data.txt")
    print(len(data_list))
    create_data_file(data_list, '../finaldata.txt')


if __name__ == "__main__":
    begin_process()
