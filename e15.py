def main():
    gridsize = 20
    paths = 1

    for i in range(0, gridsize):
        paths *= (2 * gridsize) - i
        paths /= i + 1

    print("In a {}x{} grid there are {} possible paths.".format(gridsize, gridsize, paths))

main()