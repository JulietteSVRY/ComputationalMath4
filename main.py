from graph_draw import *
import matplotlib.pyplot as plt
import colors as color

print('\n' + color.BOLD + color.RED + "Решение функций методом интерполяции кубическими сплайнами.", color.END)
print(color.GREEN,
              "1: x", '\n',
              "2: cos(x ** 2 - 4 * x + 1)", '\n',
              "3: x ** 2 - 2 * x", '\n', color.END)

func = input(color.UNDERLINE + color.YELLOW + "Введите функцию: " + color.END)
a, b, k = map(float, input(color.UNDERLINE + color.YELLOW + "Введите интервал [a; b] и шаг [k]: " + color.END).split())


func = "cos(x ** 2 - 4 * x + 1)"
a, b, k = -5, 5, 50
points = [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]
draw_function(func, a, b, 100 * k)
draw_function_cubic_spline_interpolation(func, a, b, k)


def calc(function: str, array: list[list]) -> None:
    draw_function(function, array[0][0], array[-1][0], 100 * len(array), subplot=131)

    draw_array_cubic_spline_interpolation(array, color="b", subplot=131)

    #draw_approximating_function(
     #   array, array[0][0], array[-1][0], color="red", subplot=131
    #)

    draw_deviations(function, array, color="gray", subplot=133)

    plt.subplot(131)

    print(color.RED, "До:", color.END, '\n',
          color.YELLOW, "r:", color.END, color.GREEN, get_correlation_coefficient(array), color.END, '\n',
          color.YELLOW, "R^2:", color.END, color.GREEN, get_R(array), '\n', color.END)


    pop_max_deviation(function, array, subplot=131)

    draw_function(function, array[0][0], array[-1][0], 100 * len(array), subplot=132)

    draw_array_cubic_spline_interpolation(array, color="b", subplot=132)

    #draw_approximating_function(
      #  array, array[0][0], array[-1][0], color="y", subplot=132
    #)

    draw_deviations(function, array, color="black", subplot=133)

    plt.subplot(132)

    print(color.RED, "После:", color.END, '\n',
          color.YELLOW, "r:", color.END, color.GREEN, get_correlation_coefficient(array), color.END, '\n',
          color.YELLOW, "R^2:", color.END, color.GREEN, get_R(array), '\n', color.END)

    plt.show()


#Сюда calc

calc(function='cos(x ** 2 - 4 * x + 1)', array=[[1, 0], [2, -0.2], [3, 0.3], [4, 0.8], [5, -0.1]])
