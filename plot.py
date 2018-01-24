import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig


def read(filename):
    percentages = []
    averages = []

    handle = open(filename, "r")

    for line in handle:
        backtracks = line.split("\t")
        backtracks_int = []
        percentage = float(backtracks.pop(0))

        for backtrack in backtracks:
            backtracks_int.append(int(backtrack))

        percentages.append(percentage)
        averages.append(sum(backtracks_int)/len(backtracks_int))

    return percentages, averages


def plot_twist(percentages, averages):
    plt.plot(percentages, averages)
    savefig("foo.png")


if __name__ == "__main__":
    percentages, averages = read("sudoku.txt")
    plot_twist(percentages, averages)

