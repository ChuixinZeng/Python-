# -*- coding:gbk -*-

import sys
print(sys.getdefaultencoding()) # Ĭ�ϸ�ʽ


s = "���"
s_gbk = s.encode('gbk')
print(s_gbk) # GBK
print("utf-8",s.encode()) # utf-8

# gbkת����UTF8�������������ת��Unicode������Unicodeת��utf-8
gbk_to_utf8 = s_gbk.decode("gbk").encode('utf-8')
print("utf-8",gbk_to_utf8)