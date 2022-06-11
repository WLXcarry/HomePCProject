from LAC import LAC

if __name__ == '__main__':
    textlist = list()
    #resultlist = list()
    lac = LAC(mode='lac')
    with open('./asdfg.txt', 'r', encoding='utf-8') as f1:
        for line in f1:
            line.replace('\n', '')
            textlist.append(line)
    #print(textlist)
    #lac = hub.Module(name='lac')

    #for listx in textlist:
       # resluts = lac.run(listx)
        #print(resluts)
       # resultlist.append(resluts)
    text1 = '''小明同学在北京  的北京大  学读书'''
    test_text = [text1, '小陈今天不去上课']

    # 设定分词的输入，其输入是一个句子集合
    inputs = {"text": textlist}

    result = ''
    # 调用模型进行分词操作，将结果放入results中
    # lac.load_customization('mydict.txt')
    results = lac.lexical_analysis(data=inputs)
   #results = lac.run(test_text)
    #print(results)
    for abb in resultlist:
        for a, b in enumerate(abb['tag']):
            lenght = len(abb['word'][a])
            word = abb['word'][a]
            if b == 'LOC':
                result += word[0] + '\t' + 'B-LOC' + '\n'
                for a in word[1:]:
                    result += a + '\t' + 'I-LOC' + '\n'
            elif b == 'PER':
                result += word[0] + '\t' + 'B-PER' + '\n'
                for a in word[1:]:
                    result += a + '\t' + 'I-PER' + '\n'
            elif b == 'ORG':
                result += word[0] + '\t' + 'B-ORG' + '\n'
                for a in word[1:]:
                    result += a + '\t' + 'I-ORG' + '\n'
            else:
                for a in word:
                    result += a + '\t' + 'O' + '\n'
        result += '\n'

    with open('./nerResult.txt', 'w', encoding='UTF-8') as f2:
        f2.write(result)

