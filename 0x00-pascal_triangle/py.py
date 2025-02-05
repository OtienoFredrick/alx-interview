def pythonfn(n):
    empty_list = [];

    if n < 0:
        return empty_list
    for i in range(n):
        list_ = []

        for j in range(i + 1):
            if j == 0 or j == i:
                list_.append(1)
            else:
                list_.append(empty_list[i-1][j-1] + empty_list[i-1][j])

        empty_list.append(list_)
    return empty_list
    print("")
if __name__ == "__main__":
    print(pythonfn(5))
