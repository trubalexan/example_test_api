"""
This class has methods to compare two data sets in json format
"""


class CompareData:
    def __init__(self, data_list, base_list, base_required=()):
        self.data_check = data_list
        self.data_base = base_list
        self.data_base_required = base_required
        self.answer_data = {}
        self.answer = True

    def data_length_compare(self):
        """This method is making comparison of two lists """
        # Find duplicates
        if len(self.data_check) != len(set(self.data_check)):
            self.answer = False
            self.answer_data["data_received"] = f'Duplicates found in received data'
        if len(self.data_base) != len(set(self.data_base)):
            self.answer = False
            self.answer_data["data_original"] = f'Duplicates found in original data'
        # Crosscheck for missing or extra items
        if len(self.data_check) != len(self.data_base):
            if len(self.data_check) > len(self.data_base):
                for dc in self.data_check:
                    if dc not in self.data_base:
                        self.answer_data["extra item:"] = f'Extra item >>>{dc}<<< present'
                        self.answer = False
            else:
                for dc in self.data_base:
                    if dc not in self.data_check:
                        if dc in self.data_base_required:
                            self.answer_data["missing item:"] = f'Missing item >>>{dc}<<<'
                            self.answer = False

    def data_compare(self):
        """
        Crosscheck of particular value in the other list
        :return:
        """
        for j in self.data_check:
            if j in self.data_base:
                index_item = [i for i, val in enumerate(self.data_base) if val == j]
                # print(index_item)
                if len(index_item) < 1:
                    self.answer_data[j] = f'Is not found in the original list'
                elif len(index_item) > 1:
                    self.answer_data[j] = f'Is duplicated in the original list'
            else:
                self.answer_data[j] = f'Not found in the original list'
        for j in self.data_base:
            if j in self.data_check:
                index_item = [i for i, val in enumerate(self.data_check) if val == j]
                # print(index_item)
                if len(index_item) > 1:
                    self.answer_data[j] = 'Is duplicated in the received list'
            else:
                self.answer_data[j] = f'Not found in the received list'

    def get_results(self):
        self.data_length_compare()
        self.data_compare()
        if self.answer_data:
            self.answer = False
        return self.answer, self.answer_data


if __name__ == "__main__":
    pass
