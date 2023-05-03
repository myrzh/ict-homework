boxes = []
with open("tasks/26.txt", encoding="utf8") as f:
    count = int(f.readline().strip())
    for _ in range(count):
        boxes.append(int(f.readline().strip()))

boxes.sort()
max_count = 0
for start_index in range(len(boxes) - 1):
    suitable_boxes = [boxes[start_index]]
    for box in boxes[start_index:]:
        if box - suitable_boxes[-1] >= 3:
            suitable_boxes.append(box)
    if len(suitable_boxes) >= max_count:
        max_count = len(suitable_boxes)
        first_box = suitable_boxes[0]
    else:
        break

print(max_count, first_box)
