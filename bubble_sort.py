import time

def bubble_sort(elements, draw_elements, speed, custom_array):
    n = len(elements)
    for i in range(n):
        for j in range(0, n-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                draw_elements(elements, {j: (255, 0, 0), j+1: (0, 255, 0)}, custom_array)
                time.sleep(speed)
                yield True
    draw_elements(elements, show_values=custom_array)
    return elements
