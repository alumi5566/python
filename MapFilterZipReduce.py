from functools import reduce

"""
 Lambda: 匿名函式
 i.e.
 def rabbit(x):
    x += 1
    return x
 >> rabbit(123)
 等於
 a = lambda x : x + 1
 >> a(123)

 lambda也接受多個參數
 i.e.
 a = lambda x , y : x + y + 1
 a(123, 456)
"""
a = lambda x, y: x + y + 1
print("lambda sample", a(123, 456))


# 複雜lambda sample
def milktea(y):
    return lambda x: x * y


fat = milktea(2)  # 此時fat = lambda x : x * 2
print("fat(8): ", fat(8))
print("fat(好喝): ", fat("好喝"))
"""
 Filter:
 Filter有兩個參數，第一個參數如果是None，就是第二個參數裡面為True的element篩選出來回傳 (回傳也是一個list)
 第一個參數也可以是一個function，就會把這個function套用到第二個參數中的每一個elemment，然後把計算結果為True的的element篩選出來回傳
 第二個參數就是一個可以iterate的data
"""


def odd(x):
    return x % 2


ten = range(10)
filter_result = filter(odd, ten)
print("Filter out all even ", list(filter_result))

"""
 結合lambda和Filter:
"""
filter_result_combince = filter(lambda x: x % 2, ten)
print("Filter out all even (combine)", list(filter_result_combince))

"""
 Map:
 Map也有兩個參數，一個function和一個可以iterate的data
 將function套用到第二個參數中每一個element運算，回傳運算過後的結果
"""
map_result = map(lambda x: x * 2, ten)
print("Mapping double ", list(map_result))


# Map練習:
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    str = ''
    return str + name[0].upper() + name[1:].lower()


nameList = ['adam', 'LISA', 'barT']
nameListMap = list(map(normalize, nameList))
print("nameListMap: ", nameListMap)
"""
 Zip:
 將兩個list中的element組合再一起，以tuple的list回傳
"""
zip_result = zip([1, 3, 5, 7, 8], [2, 4, 6, 8, 10])
print("Zip result: ", list(zip_result))
# Zip的回傳是Tuple，可以利用map+lambda把zip的回傳包成list
fake_zip_result = map(lambda x, y: [x, y], [1, 3, 5, 7, 8], [2, 4, 6, 8, 10])
print("Fake Zip result: ", list(fake_zip_result))
# 快速轉置矩陣
# 呼叫函式的時候，如果在可迭代物件的引數前面加上 * 符號，可以進行解包（unpack）：將可迭代物件內的每個內容物各自成為引數。
matrix = [[1, 2],
          [3, 4],
          [5, 6]]
zip_matrix = zip(*matrix)
# 所以使用 * unpack，等於 zip(*matrix)就等於zip([1, 2], [3, 4], [5, 6]):
print("zip_matrix: ", list(zip_matrix))
# 如果轉置後希望維持原本 list of lists 的結構
zip_matrix_list = [list(row) for row in zip(*matrix)]
print("zip_matrix_list: ", zip_matrix_list)

# dict 反轉範例
my_dict = {'a': 1, 'b': 2, 'c': 3}
# 快速複習用來列出 dict 內容的函式
# my_dict.keys() >>> dict_keys(['a', 'b', 'c'])
# my_dict.values() >>> dict_values([1, 2, 3])
# my_dict.items() >>> dict_items([('a', 1), ('b', 2), ('c', 3)])
# dict 反轉，兩種寫法
## 1. dict comprehension
revert_my_dict = {value: key for key, value in my_dict.items()}
print("revert_my_dict ", revert_my_dict)
## 2. 使用 zip()
revert_my_dict_zip = dict(zip(my_dict.values(), my_dict.keys()))
print("revert_my_dict_zip ", revert_my_dict_zip)

"""
 Reduce:
 Reduce也有兩個參數，一個function和一個可以iterate的data
 以結果來說是把function套用在你的data的element上面，回傳運算過後的結果
 過程是
 (1) 先把function套用在list中的首兩個element 
 (2) function套用在step(1)的結果和第三個element
 ...
 直到全部的element處理完
"""
ten = range(1, 11)
reduce_result = reduce(lambda x, y: x * y, ten)
print("reduce_result ", reduce_result)

# MapReduce練習:
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456。
def str2float(s):
    n = 1
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
        return digits[s]

    def f_mul(x, y):
        nonlocal n # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
        if y == '.':
            n = 0
            return x
        elif n == 1:
            return x * 10 + y
        else:
            n -= 1
        return x + y * pow(10, n)
    return reduce(f_mul, map(char2num, s))

print('str2float(\'123.456\') =', str2float('123.456'))