def check_value_count(class_name, cell_list):
    if len(cell_list) != 9:
        raise ValueError('cell list length must be 9')

    counter = [0] * 10
    for cell in cell_list:
        if cell.value == 0:
            continue
        counter[cell.value] += 1

        if counter[cell.value] > 1:
            raise ValueError(f'{class_name} value error')
