"""
level_01.py
"""

raw_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def trans(text):
    a_to_z = "abcdefghijklmnopqrstuvwxyzab"

    for i in text:
        if i in a_to_z:
            print(a_to_z[a_to_z.index(i)+2], end='')
        else:
            print(i, end='')

trans(raw_text)
print()
trans('map')
print()
