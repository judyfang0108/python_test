import re
import os

def php_to_file():
    #利用re過濾掉php中不要的文字
    zh2Hant_pattern = re.compile(r'public static \$zh2Hant = \[([^]]*)]', re.M)
    zh2Hans_pattern = re.compile(r'public static \$zh2Hans = \[([^]]*)]', re.M)
    pair_pattern = re.compile(r'\'([^\']+)\' => \'([^\']+)\'')
    #讀php
    with open('ZhConversion.php', 'r', encoding='UTF-8') as inFile:
        data = inFile.read()
    #php to file(簡轉繁)
    with open('simple_to_traditional.txt', 'w', encoding='UTF-8') as outFile:
        for p in zh2Hant_pattern.findall(data):
            for pp in pair_pattern.findall(p):
                outFile.write('%s\t%s\n' % pp)
    #php to file(繁轉簡)
    with open('traditional_to_simple.txt', 'w', encoding='UTF-8') as outFile:
        for w in zh2Hans_pattern.findall(data):
            for ww in pair_pattern.findall(w):
                outFile.write('%s\t%s\n' % ww)

def file_to_dict(file_path):
    translate_dict={}
    with open(file_path, 'r', encoding='UTF-8') as f:
        line = f.readline()
        while(line):
            line = line.strip().split('\t')
            translate_dict.update( {line[0] : line[1]})
            line = f.readline()
    return translate_dict

def max_match(sen, d):#盡量配對到最長的長度
    for n in range(len(d)):
        seg = sen[:n]
        if d.get(seg):
            return d.get(seg)
        n -= 1
    return sen[0]

def trans(sen, d):
    ans = []
    idx = 0
    while idx < len(sen):
        r = max_match(sen[idx:], d)
        idx += len(r)
        ans.append(r)
    return ''.join(ans)

if __name__ == '__main__':
    php_to_file()
    s2t=file_to_dict('simple_to_traditional.txt')
    t2s=file_to_dict('traditional_to_simple.txt')
    a=trans('臺灣人很憂鬱',t2s)#繁轉簡
    b=trans('台湾人很忧郁',s2t)#簡轉繁
    print(a)
    print(b)
    
        
    