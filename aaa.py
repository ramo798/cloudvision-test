s = 'あいうえお'

b = s.encode('unicode-escape')



print(b)


s_from_b = b.decode('unicode-escape')

print(s_from_b)