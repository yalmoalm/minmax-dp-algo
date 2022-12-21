def getminmax(a):

    comprison = 1
    size_a = len(a)
    max = 0
    min = 0

    if a[0] < a[1]:
        min, max = a[0], a[1]


    else:
        max, min = a[0], a[1]



    for i in range(2, len(a) - 1, 2):

        comprison += 1

        if a[i] <= a[i + 1]:
            comprison += 1
            if a[i] < min:
                min = a[i]
            comprison += 1
            if a[i + 1] > max:
                max = a[i + 1]


        else:
            comprison += 1
            if a[i] > max:
                max = a[i]
            comprison += 1
            if a[i + 1] < min:
                min = a[i + 1]


        if size_a % 2 != 0:
            comprison += 1
            if a[size_a - 1] < min:
                min = a[size_a - 1]
            else:
                comprison += 1
                if a[size_a - 1] > max:
                    max = a[size_a - 1]


    return ('max: ', max, 'min: ', min, comprison)



def main():

    A = [10, 8, 9, 3, 4, 7, 6, 13, 9]
    print(getminmax(A))


if __name__ == '__main__':
    main()
