class GloveStorage:

    def __init__(self):
        self.container = []

    def add(self, gloves):
        self.container.extend(gloves)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.container):
            result = self.container[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        storage_str = "GloveStorage ["
        for glove in self.container:
            storage_str += glove.__str__() + ", "
        storage_str = storage_str.rstrip(", ")
        storage_str += "]"
        return storage_str

    def sort_by_quantity(self):

        A = self.container
        A.sort(key=lambda x: x.get_quantity(), reverse=True)

    # return merge_sort(A)


def merge_sort(A, a=0, b=None):
    if b is None: b = len(A)
    if 1 < b - a:
        c = (a + b + 1) // 2
        merge_sort(A, a, c)
        merge_sort(A, c, b)

        L, R = A[a:c], A[c:b]
        merge(L, R, A, len(L), len(R), a, b)


def merge(L, R, A, i, j, a, b):
    if a < b:
        if (j <= 0) or (i > 0 and L[i - 1] > R[j - 1]):
            A[b - 1] = L[i - 1]
            i = i - 1
        else:
            A[b - 1] = R[j - 1]
            j = j - 1
            merge(L, R, A, i, j, a, b - 1)
