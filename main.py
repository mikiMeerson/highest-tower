# מיקי מאירסון 207349010
# נעם תשובה 207576109
import random

H = []  # Max height array
P = []  # Recover solution


class Box:
    def __init__(self, h, w, l):
        self.height = h
        self.width = w
        self.length = l

    def print(self):
        print("Length: {}, Width: {}, Height: {}".format(self.length, self.width, self.height))


def generate_dimensions(n):
    heights = []
    lengths = []
    widths = []

    for i in range(n):
        heights.append(random.randint(1, 200))
        lengths.append(random.randint(1, 200))
        widths.append(random.randint(1, 200))

    return heights, lengths, widths


def create_boxes(heights, widths, lengths):
    """ Recieves 3 arrays of n boxes dimensions
        Returns a single array of boxes, sorted by length and then by width
    """
    # Create boxes array
    box_list = []
    for i in range(len(heights)):
        box_list.append(Box(heights[i], widths[i], lengths[i]))

    # Primary sort - length
    # Secondary sort - width
    box_list = sorted(box_list, key=lambda x: (x.length, x.width), reverse=True)
    return box_list


def tower(n: int, boxes):
    """ Bottom-up algorithm to find maximum height possible
        H[i] is the the maximum possible height when the i-th box is used
        P[i] is the last box taken upon reaching the i-th box
        recursive formula:
            - if i=0: H[i] = height[i]
            - else: H[i] = max(H[j]) + height[i] | length[j] > length[i] and width[j] > width[i]
        """
    H[0] = boxes[0].height
    for i in range(1, n):
        H[i] = boxes[i].height
    for i in range(1, n):
        for j in range(n):
            if boxes[j].length > boxes[i].length and boxes[j].width > boxes[i].width:
                if H[j] + boxes[i].height > H[i]:
                    H[i] = H[j] + boxes[i].height
                    P[i] = j
    max_height = -float('inf')
    max_i = -1
    for i in range(n):
        if H[i] > max_height:
            max_height = H[i]
            max_i = i
    return max_height, max_i


def recover_tower(i, boxes):
    if P[i] is None:
        print(" Box {}".format(i + 1), end="")
    else:
        recover_tower(P[i], boxes)
        print(" --> Box {}".format(i + 1), end="")


def main_tower(size):
    print("Generating {} boxes:".format(size))
    height, length, width = generate_dimensions(size)
    boxes = create_boxes(height, width, length)

    # Show available boxes, sorted
    print("\nPrinting boxes in sorted order (primary + secondary)...")
    for i in range(size):
        print("Box {}:".format(i + 1))
        boxes[i].print()

    max_height, max_i = tower(size, boxes)

    print("\nRecovering Highest possible tower...")
    recover_tower(max_i, boxes)
    print("\nWith the height of {}".format(max_height))


if __name__ == '__main__':
    sizes = [20, 30]
    for size in sizes:
        H = [-1] * size
        P = [None] * size
        main_tower(size)
        print('************************************************************')
