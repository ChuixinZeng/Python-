# -*- coding:gbk -*-

# ���ļ�ͷ�����ļ���ʽ��GBK�ģ�����ļ�����ΪGBK�����ǲ������Ļ����ᱨ��Ĭ��ִ�г����ʱ�򣬻���utf-8

import sys
print(sys.getdefaultencoding()) # Ĭ�ϸ�ʽ


s = "���" # ����unicode��ǰ��ĵ�ֻ���ļ��ı��룬����Python������������;���Unicode��������Ϊ��������ʲô���ͻ�ĳ�ʲô

# ������s�Ѿ���Unicode����£��Ͳ���Ҫ��decode�����ˣ�ֱ��encode��gbk������
print(s.encode('gbk'))
print(s.encode('utf-8'))
# ��Ĭ�ϵ�Unicodeת����utf-���ٰ�utf-8 decode encodeΪgb2312����bytes��ʽ��ʾ b'\xc4\xe3\xba\xc3'
print(s.encode('utf-8').decode('utf-8').encode('gb2312'))

# gb2312��ת�������ģ������ǰ�bytesת�������ַ�����

print(s.encode('utf-8').decode('utf-8').encode('gb2312').decode('gb2312'))