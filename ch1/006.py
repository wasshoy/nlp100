s1 = 'paraparaparadise'
s2 = 'paragraph'
x = {s1[i:i + 2] for i in range(len(s1) - 1)}
y = {s2[i:i + 2] for i in range(len(s2) - 1)}
print('x:', x)
print('y:', y)
# 和集合
print('和集合:', x | y)
# 積集合
print('積集合:', x & y)
# 差集合
print('差集合:', x - y)
# 'se'が含まれるか
is_isnt_x = ' is ' if 'se' in x else "isn't"
is_isnt_y = ' is ' if 'se' in y else "isn't"
print(f'"se" {is_isnt_x} in x.')
print(f'"se" {is_isnt_y} in y.')
