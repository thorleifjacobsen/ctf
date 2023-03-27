with open('TextInDoc.txt') as f:
    data = f.read()

# l=l
# b=5
# w is unset so "".

flag = data[239] + \
       data[169] + \
       data[42] + \
       data[2] + \
       data[169] + \
       data[48] + \
       data[290] + \
       data[58] + \
       chr(int(data[17] + "2" + data[101])) + \
       data[58] + \
       data[59] + \
       data[42] + \
       data[42] + \
       data[59] + \
       data[33] + \
       chr(int(data[15] + data[46])) + \
       data[290] + \
       data[239] + \
       data[169] + \
       chr(95) + \
       data[58] + \
       "l" + \
       data[59] + \
       "" + \
       chr(20+44+55) + \
       chr(int(data[17] + "2"+ "5"))

print(flag)