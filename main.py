import cv2
import numpy as np

MIN_LENGTH_PERCENTAGE = 70  # default value


def create_line_func(x1, y1, x2, y2):
    m = 0
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
    return lambda x: int(m * (x - x1) + y1)


def filter_lines(lines):
    grouped_lines = {}
    filtered_lines = {}
    for line in lines:
        x1, y1, x2, y2 = line[0]
        y = create_line_func(x1, y1, x2, y2)
        if grouped_lines.get(((0, y(0)), (1, y(1)))) is None:
            grouped_lines[((0, y(0)), (1, y(1)))] = [x1, x2]
        else:
            start, end = grouped_lines.get(((0, y(0)), (1, y(1))))
            grouped_lines[((0, y(0)), (1, y(1)))][0] = min(x1, start)
            grouped_lines[((0, y(0)), (1, y(1)))][1] = max(x2, end)
    for points, start_end in grouped_lines.items():
        start_x, end_x = start_end
        if end_x - start_x >= MIN_LENGTH:
            filtered_lines[points] = start_end
    return filtered_lines


def detect_and_draw_lines(image_path):
    image = cv2.imread(image_path)
    global MIN_LENGTH
    MIN_LENGTH = (MIN_LENGTH_PERCENTAGE / 100) * image.shape[1]
    print(image.shape)
    print(MIN_LENGTH)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=50, threshold2=150, apertureSize=5)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=50, maxLineGap=15)
    if lines is not None:
        grouped_lines = filter_lines(lines)
        for points, start_end_x in grouped_lines.items():
            p1, p2 = points
            start_x, end_x = start_end_x
            y = create_line_func(*p1, *p2)

            cv2.line(image, (start_x, int(y(start_x))), (end_x, int(y(end_x))), (0, 255, 0), 1)
    cv2.imshow('Vertical Lines', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_and_draw_lines('./images_test/1.jpg')
