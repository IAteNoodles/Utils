def partition(number: int) -> list:
    if number == 1:
        print(1, ":", {(1,)})
        return [[1]]
    pre_partitions = partition(number - 1)
    part = list()
    for parts in pre_partitions:
        parts.append(1)
        parts.sort(reverse=True)
        part.append(parts)
    for parts in pre_partitions:
        sum_ = 0
        count = len(parts)
        while True:
            sum_ += parts[count - 1]
            count -= 1
            if count == len(parts) - 2:
                break
        new_part = parts[:len(parts) - 2]
        new_part.append(sum_)
        new_part.sort(reverse=True)
        part.append(new_part)
    partitions = set()
    for parts in part:
        partitions.add(tuple(parts))
    print(number, ":", partitions)
    return part


if __name__ == "__main__":
    partition(19)
