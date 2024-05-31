from collections import defaultdict
import itertools

precalculated_distances = defaultdict(lambda: {})
characteristic_elements = [['I', 'E'], ['S', 'N'], ['T', 'F'], ['J', 'P']]
all_types = []

def generate_types(index, acc):
   if index == 4:
      all_types.append(acc)
      return
   generate_types(index + 1, acc + characteristic_elements[index][0])
   generate_types(index + 1, acc + characteristic_elements[index][1])

generate_types(0, "")

def calculate_distances(lhs, rhs):
   dist = 0
   for i in range(4):
      dist += int(lhs[i] != rhs[i])
   return dist

def calculate_all_distances(lhs_index):
   precalculated_distances[all_types[lhs_index]][all_types[lhs_index]] = 0
   if lhs_index == 15:
      return
   for rhs_index in range(lhs_index + 1, 16):
    dist = calculate_distances(all_types[lhs_index], all_types[rhs_index])
    precalculated_distances[all_types[lhs_index]][all_types[rhs_index]] = dist
    precalculated_distances[all_types[rhs_index]][all_types[lhs_index]] = dist
    calculate_all_distances(rhs_index)

calculate_all_distances(0)

T = int(input())
for _ in range(T):
  N = int(input())
  distinct_students = defaultdict(lambda: 0)
  for student in  input().split():
    if distinct_students[student] < 3:
        distinct_students[student] += 1
  serialized_students = list(itertools.chain(*[[student for _ in range(count)] for (student, count) in distinct_students.items()]))
  length = len(serialized_students)
  min_distance = 987654321
  for i in range(length):
     for j in range(i + 1, length):
        for k in range(j + 1, length):
           dist1 = precalculated_distances[serialized_students[i]][serialized_students[j]]
           dist2 = precalculated_distances[serialized_students[j]][serialized_students[k]]
           dist3 = precalculated_distances[serialized_students[k]][serialized_students[i]]
           total_dist = dist1 + dist2 + dist3
           if total_dist < min_distance:
              min_distance = total_dist
  print(min_distance)