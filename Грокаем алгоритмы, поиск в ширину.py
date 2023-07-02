# функция проверки человека
def person_is_seller(name): # эта функция проверяет, заканчивается ли имя на букву "М", если да, то этот человек считается продавцом манго 
    return name[-1] == "m"
# создание графа
graph = {}
graph["you"] = ["alice", "bob", "claire"] # связь первого уровня - мои друзья
graph["bob"] = ["anuj", "peggy"]  # далее идет связь 2-го уровня, друзья моих друзей
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []

# создание двухсторонней очереди (дека)
from collections import deque # импорт функции двусторонней очереди

def search(name):
    search_queue = deque() # создание новой очереди
    search_queue += graph["you"] # все мои друзья добавляются в очередь поиска
    searched = [] # этот массив используем для отслеживания уже проверенных людей
    while search_queue: # пока очередь не пуста
        person = search_queue.popleft() # из очереди извлекается первый человек
        if not person in searched: # человек проверяется только в том случае, если не проверялся ранее
            if person_is_seller(person): # проверяем, является ли данный человек продавцом манго
                print(person, "is a mango seller") # если является, то выводим текст имя + "это продавец манго"
                return True
            else:
                search_queue += graph[person] # если не является продавцом, то добавляем всех друзей этого человека в очередь поиска
    print("Seller not found")
    return False # Если выполнение дошло до этой строчки, значит в очереди нет продавца манго
search("you")
