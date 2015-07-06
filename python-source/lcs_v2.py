'''
source: http://stackoverflow.com/questions/2892931/longest-common-substring-from-more-than-two-strings-python
'''


#file = open('sequences.txt', 'r')
lines = []

#with open('sequences.txt') as f:
 #   lines.append(f.readlines())

lines = [line.rstrip('\n') for line in open('sequences.txt')]

#print(lines)

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


#print long_substr(['uiqyweiuyqwabiuexyqffnieiqnqey',
 #                 '0908908098ab098098098ff',
  #               'zxbcmnzbxcjabhdpoweiqpwffo', '823091823adaskjahsdkjahdffffff'])



print long_substr(lines)