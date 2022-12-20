class Graph:
    matrix_of_graph = [[]]
    list_of_names = []
    list_of_marks = []

    def __init__(self):
        self.matrix_of_graph = [[]]
        self.list_of_names = []
        self.list_of_marks = []

    def ADD_V(self, name):
        for i in range(len(self.list_of_names)):
            if self.list_of_names[i] == name:
                print("Не удалось добавить вершину с именем " + name + ", так как такая вершина уже существует.\n")
                return
        self.list_of_names.append(name)
        self.list_of_marks.append(False)
        self.matrix_of_graph.append([0] * len(self.list_of_names))
        for i in range(len(self.matrix_of_graph)):
            self.matrix_of_graph[i].append(0)

    def EDIT_V(self, name, new_name):
        edit_index = self.get_index_name(name)
        if edit_index == -1:
            return
        for i in range(len(self.list_of_names)):
            if self.list_of_names[i] == new_name:
                print("Не удалось изменить вершину с именем " + name + ", так как такая вершина с именем " + new_name + " уже существует.\n")
                return
        self.list_of_names[edit_index] = new_name

    def DEL_V(self, name):
        del_index = self.get_index_name(name)
        if del_index == -1:
            return
        del self.list_of_names[del_index]
        del self.list_of_marks[del_index]
        del self.matrix_of_graph[del_index]
        for i in range(len(self.list_of_names)):
            del self.matrix_of_graph[i][del_index]

    def ADD_E(self, name_1, name_2, value):
        if value <= 0:
            print("Вес дуги должен быть больше 0")
            return
        i1 = self.get_index_name(name_1)
        i2 = self.get_index_name(name_2)
        if i1 == -1 or i2 == -1:
            return
        self.matrix_of_graph[i1][i2] = value
        self.matrix_of_graph[i2][i1] = value


    def EDIT_E(self, name_1, name_2, new_value):
        if new_value <= 0:
            print("Вес дуги должен быть больше 0")
            return
        i1 = self.get_index_name(name_1)
        i2 = self.get_index_name(name_2)
        if i1 == -1 or i2 == -1:
            return
        if self.matrix_of_graph[i1][i2] == 0:
            print(f"Дуги между вершинами {name_1} и {name_2} не существует")
            return
        self.matrix_of_graph[i1][i2] = new_value
        self.matrix_of_graph[i2][i1] = new_value

    def DEL_E(self, name_1, name_2):
        i1 = self.get_index_name(name_1)
        i2 = self.get_index_name(name_2)
        if i1 == -1 or i2 == -1:
            return
        self.matrix_of_graph[i1][i2] = 0
        self.matrix_of_graph[i2][i1] = 0

    def FIRST(self, name):
        v_index = self.get_index_name(name)
        if v_index == -1:
            return
        for i in range(len(self.list_of_names)):
            if self.matrix_of_graph[v_index][i] != 0 and i != v_index:
                return i
        return -1

    def LAST(self, name):
        v_index = self.get_index_name(name)
        if v_index == -1:
            return
        i_last = -1
        for i in range(len(self.list_of_names)):
            if self.matrix_of_graph[v_index][i] != 0 and i != v_index:
                i_last = i
        return i_last

    def NEXT(self, name, after_i):
        v_index = self.get_index_name(name)
        if v_index == -1:
            return
        for i in range(after_i + 1, len(self.list_of_names)):
            if self.matrix_of_graph[v_index][i] != 0 and i != v_index:
                return i
        if after_i == self.LAST(name):
            return -1

    def VERTEX(self, name, index):
        v_index = self.get_index_name(name)
        if v_index == -1:
            return
        if(self.matrix_of_graph[v_index][index] != 0):
            return index
        print("С вершиной " + name + " нет смежных вершин с индексом " + str(index))
        return -1
        pass

    def get_index_name(self, name):
        for i in range(len(self.list_of_names)):
            if self.list_of_names[i] == name:
                return i
        print("Вершины с именем " + name + " не существует")
        return -1

    def show(self):
        print("Матрица смежности графа: \n")
        print("+", end=" ")
        for i in range(len(self.list_of_names)):
            print(self.list_of_names[i], end = " ")
        print("\n")
        for i in range(len(self.list_of_names)):
            print(self.list_of_names[i], end=" ")
            for j in range(len(self.list_of_names)):
                print(self.matrix_of_graph[i][j], end=" ")
            print("\n")

    def dfs(self, index_node, index_parent):
        self.list_of_marks[index_node] = True
        for i in range(len(self.list_of_names)):
            if self.matrix_of_graph[index_node][i] != 0 and i != index_parent and self.list_of_marks[i] != True:
                self.dfs(i, index_node)

    def find_briges(self):
        i = 0
        j = 1
        list_of_briges = []
        finish = len(self.list_of_names)
        while(i < finish):
            while(j < finish):
                bufer = self.matrix_of_graph[j][i]
                self.matrix_of_graph[j][i] = 0
                self.matrix_of_graph[i][j] = 0
                self.dfs(0, -1)
                is_brige = 0
                for p in range(finish):
                    if self.list_of_marks[p] == False:
                        is_brige = 1
                        break
                if(is_brige == 1):
                    list_of_briges.append(self.list_of_names[i] + " <---> " + self.list_of_names[j])
                self.matrix_of_graph[j][i] = bufer
                self.matrix_of_graph[i][j] = bufer
                for p in range(finish):
                    self.list_of_marks[p] = False
                j += 1
            i += 1
            j = i + 1
        if len(list_of_briges) < finish and len(list_of_briges) > 0:
            print("Список мостов графа:\n")
            for k in range(len(list_of_briges)):
                print(list_of_briges[k], "\n")
        elif len(list_of_briges) == 0:
            print("В вашем графе не имеется мостов.\n")
        elif len(list_of_briges) >= finish:
            print("Не все вершины вашего графа связаны. \n")



def main():
    new_graph = Graph()
    new_graph.ADD_V("A")
    new_graph.ADD_V("B")
    new_graph.ADD_V("C")
    new_graph.ADD_V("D")
    new_graph.ADD_E("A", "B", 1)
    new_graph.ADD_E("B", "C", 1)
    new_graph.ADD_E("C", "D", 1)
    new_graph.show()
    new_graph.find_briges()

if __name__ == "__main__":
    main()