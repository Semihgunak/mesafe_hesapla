import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 2D uzaydaki noktaları temsil eden liste
points = [(1, 2), (4, 6), (5, 8), (10, 15)]

# Tüm nokta çiftleri arasındaki mesafeleri hesaplayalım
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Hesaplanan mesafeleri yazdırma
print("Tüm mesafeler:", distances)

# Minimum mesafeyi bulma ve yazdırma
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
