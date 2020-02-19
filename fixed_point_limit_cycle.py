def cube_digits_sum(n):
    '''
    Function computes the sum of the cube digits of positive integer n
    '''
    number = str(n)
    total = 0
    for i in range(len(number)):
        total = total + int(number[i]) ** 3
    return total


def fixed_point_or_limit_cycle(n):
    '''
    Function check if it's arrived at a fixed point or limit cycle
    '''
    cube_list = [n]
    while True:
        if cube_list[-1] == cube_digits_sum(cube_list[-1]):
            print(f"{cube_digits_sum(cube_list[-1])} is a fixed point")
            break
        if cube_digits_sum(cube_list[-1]) in cube_list:
            print(f"{cube_digits_sum(cube_list[-1])} is a limit cycle")
            break
        cube_list.append(cube_digits_sum(cube_list[-1]))
    return f"{cube_list} and the sum is {sum(cube_list)}"

if __name__ == "__main__":
    n = int(input("Please type the number: "))
    print(fixed_point_or_limit_cycle(n))
