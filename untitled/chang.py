if __name__ == '__main__':
      textlist =list() #unknown
      textlist2 = list()
      flag = 'unknown'
      with open('./val.jsonl','r',encoding='utf-8') as f1:
            for line in f1:
                  if line.find(flag)>0:
                        textlist.append(line)
                  else:
                        textlist2.append(line)

      with open('./val_known.jsonl', 'w', encoding='UTF-8') as f2:
            for abb in textlist2:
                  f2.write(abb)

      with open('./val_unknown.jsonl', 'w', encoding='UTF-8') as f3:
            for abb in textlist:
                  f3.write(abb)