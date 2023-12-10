class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = self.calculate_total_pages()

    def calculate_total_pages(self):
        return -(-len(self.items) // self.pageSize)  # Ceiling division

    def get_visible_items(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prev_page(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def next_page(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def first_page(self):
        self.currentPage = 1
        return self

    def last_page(self):
        self.currentPage = self.totalPages
        return self

    def go_to_page(self, page_num):
        page_num = int(page_num)
        self.currentPage = max(1, min(self.totalPages, page_num))
        return self

# Example usage
alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabet_list, 4)

print(p.get_visible_items())

p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(10)
print(p.get_visible_items())