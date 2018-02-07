class Tree: # класс в котором храним дерево вида {вершина: [левыйребенок, правый]}
    def __init__(self):
        self.ver = {}# словарь детей
    def add(self, name, left, right): # добавить в словарь вершину и ее детей
        self.ver[name] = [left, right]
    def get_child_left(self, parent): # вернуть левого ребенка вершины, если такого нет, то False
        if parent not in self.ver:
            return False
        else:
            return self.ver[parent][0]
    def get_child_right(self, parent): # # вернуть правого ребенка вершины, если такого нет, то False
        if parent not in self.ver:
            return False
        else:
            return self.ver[parent][1]

def make_Tree(): # Функция создания дерева
    """
    В качестве потомков (левого и правого) берем элементы с минимумом повторений
    в исходной строке. И удаляем эти элементы из с писка с количеством повторений.
    Создаем новый элемент: имя которого слеено из имен потомков, число повторений  =
    суммарному числу повторений потомков и добавляем его в список повторений.

    """
    left = inclusion.pop(inclusion.index(min(inclusion)))
    right = inclusion.pop(inclusion.index(min(inclusion)))
    name = left[1] + right[1]
    tree.add(name, left[1], right[1])
    new = [left[0] + right[0], name]
    inclusion.append(new)

def make_code(edge_now , code_now = ''): # Функция кодирования элементов в дереве
    """
    Присваеваем код вершине и смотрим есть ли у нее потомки, если да:
    то рекурсивно запускаем для потомков, у левого к коду добавляем 0, правому 1.
    :param edge_now: Вершина, которую кодируем в данный момент
    :param code_now: Код для вершины, которую кодируем
    """
    if edge_now in code_symbol:
        code_symbol[edge_now] = code_now
    else:
        left_child = tree.get_child_left(edge_now)
        right_child = tree.get_child_right(edge_now)
        if left_child:
            make_code(left_child, code_now + '0')
        if right_child:
            make_code(right_child, code_now + '1')

ish_str = input()
inclusion = [] #  Список с количесвом повторений символов в исходной строке
symbols = [] # Список всех символов, для сортированного вывода кодов символов
code_symbol = {} # Словарь с кодами символов вида символ: код
for symbol in ish_str: #  считаем количество повторений символов в исходной строке
    if symbol not in code_symbol:
        inclusion.append([ish_str.count(symbol), symbol])
        code_symbol[symbol] = -1
        symbols.append(symbol)
symbols.sort()
tree = Tree() # Создаем дерево
while len(inclusion) != 1: # Строим дерево пока в списке повторений не останется только корень
    make_Tree()
root = inclusion[0][1] # находим корень дерева
if len(symbols) == 1: # обрабатываем случай, если в строке только один повторяющийся элемент
    make_code(root, '0')
else:
    make_code(root)
code_str = '' # Результирующая закодированная строка
for symbol in ish_str: # Кодируем строку по словарю кодов
    code_str += code_symbol[symbol]
print(len(symbols), len(code_str)) # Печатаем количество различных символов в исходной строке и длину закодированной строки
for symb in symbols: # печатаем коды символов
    print(symb + ':', code_symbol[symb])
print(code_str) # Печатаем закодированную строку