class GloveStorage:

    def __init__(self):
        self.container = []

    def add(self, glove):
        self.container.append(glove)

    # def add_all(self, list):
    #     self.container.append(list)

    def sort_by_quantity(self):

        def merge_sort(container):
            if len(container) <= 1:
                return container

            mid = len(container) // 2
            left = container[:mid]
            right = container[mid:]

            left = merge_sort(left)
            right = merge_sort(right)

            return merge(left, right)

        def merge(left, right):
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i].get_quantity() <= right[j].get_quantity():
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        return merge_sort(self.container)

    def Print(self):
        for x in self.container:
            print(x)