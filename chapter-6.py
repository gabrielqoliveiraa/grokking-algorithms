from collections import deque

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []




def person_is_seller(nome):
    return nome[-1] == "m"



def search(nome):
    queue_search = deque()
    marked = []

    queue_search += graph[nome]
    marked.append(nome)

    while queue_search:
        person = queue_search.popleft()
        if not person in marked:
            print(person)
            queue_search += graph[person]
            marked.append(person)


search("you")