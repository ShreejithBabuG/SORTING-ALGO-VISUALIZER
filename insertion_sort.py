import time

def insertion_sort(elements, draw_elements, speed, custom_array):
    for i in range(1, len(elements)):
        key = elements[i]
        j = i-1
        while j >= 0 and key < elements[j]:
            elements[j+1] = elements[j]
            j -= 1
            draw_elements(elements, {j+1: (255, 0, 0), i: (0, 255, 0)}, custom_array)
            time.sleep(speed)
            yield True
        elements[j+1] = key
    draw_elements(elements, show_values=custom_array)
    return elements
