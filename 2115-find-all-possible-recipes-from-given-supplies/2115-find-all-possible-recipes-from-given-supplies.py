from collections import deque

class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:

        graph = {}
        indegree = {}
        recipe_set = set(recipes)

        for i, recipe in enumerate(recipes):
            indegree[recipe] = 0

            for ingredient in ingredients[i]:
                if ingredient not in graph:
                    graph[ingredient] = []

                graph[ingredient].append(recipe)
                indegree[recipe] += 1

        queue = deque(supplies)
        result = []

        while queue:
            curr = queue.popleft()

            if curr in recipe_set:
                result.append(curr)

            if curr in graph:
                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return result