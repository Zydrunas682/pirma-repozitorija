def similar_index_values(sarasas):
     all_values = [sum(values) for values in zip(*sarasas)]
     return all_values


sum_similar_indexes = similar_index_values(sarasas)       
print(sum_similar_indexes)