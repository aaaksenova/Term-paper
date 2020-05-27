#!/usr/bin/python
# -*- coding: utf-8 -*-
import re, math, codecs, os

def parse(text):
    sentence = []  # Обновляемый список слов в предложении
    k = -1  # Счетчик позиции. Вот если у нас "т" из т.е., мы можем не обрабатывать следующие 3 символа
    for i in range(1, len(text)-2):
        try:      
            if i <= k:  # Если счетчик больше, то мы уже учли это слово
                continue
            elif len(text[i]) != 7:
                continue
            else:
                k = -1
                if not (text[i][0] == '!' or text[i][0] == '?' or text[i][0] == '.' or text[i][0] == '…') :
                        if ((text[i][0] == 'то' or text[i][0] == 'То') 
                            and text[i][6] == 'предик' and text[i+1][0] == 'есть'):
                            sentence.append('тоесть')
                            k = i + 1  # Не смотрим на следующее "есть"
                        elif (text[i][0] == 'так' or text[i][0] == 'Так') and text[i+1][0] == 'как':
                            sentence.append('таккак')
                            k = i + 1
                        elif (text[i][0] == 'потому' or text[i][0] == 'Потому') and text[i+1][0] == 'что':
                            sentence.append('потомучто')
                            k = i + 1
                        elif (text[i][0] == 'в' or text[i][0] == 'В') and text[i+1][0] == 'смысле':
                            sentence.append('всмысле') 
                            k = i + 1
                        elif (text[i][0] == 'А' or text[i][0] == 'А') and text[i+1][0] == 'именно':
                            sentence.append('аименно')
                            k = i + 1
                        elif ((text[i][0] == 'т' or text[i][0] == 'Т') 
                              and text[i+1][0] == '.' and text[i+2][0] == 'е'):
                            sentence.append(u'тоесть')
                            k = i + 3 
                        elif (text[i][0] == 'т' or text[i][0] == 'Т') and text[i+1][0] == '.' and text[i+2][0] == 'к':
                            sentence.append('таккак')
                            k = i + 3
                        elif text[i][6] == 'PUNC' or text[i][0] == '–':  # Если не !.?... но знак препинания, не добавляем
                            continue
                        else:
                            sentence.append(text[i][2])
                elif not (text[i+1][0] == 'п' or text[i+1][0] == 'д'): 
                    # Если у нас точка, и она не входит в "т.п." и "т.д."
                    with open('lemmas.txt', 'a') as fw:
                        if sentence:
                            fw.write(' '.join(sentence).lower() + '\n')
                    sentence = []

        except:
            pass

text = []
# tokens = 0
# texts = 0
with codecs.open('/home/dryzhova/ruwac-filtered_part.out', 'r', encoding='utf-8') as ruwac:
    for line in ruwac:
        if '</text>' in line:
            parse(text)
#           texts += 1
            text = []
        else:
            line = line.split()
            text.append(line)
#           tokens += 1
# print(texts)
# print(tokens)
