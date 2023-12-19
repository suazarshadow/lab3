import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Зчитування даних з файлу
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [tuple(map(int, line.strip().split())) for line in lines]
    return np.array(points)

# Знаходження опуклої оболонки
def compute_convex_hull(points):
    hull = ConvexHull(points)
    return hull

# Відображення опуклої оболонки та точок на графіку
def plot_convex_hull(points, hull):
    fig, ax = plt.subplots(figsize=(960/80, 540/80))
    
    # Відображення точок
    plt.plot(points[:, 1], points[:, 0], 'bo', label='')
    
    # Відображення опуклої оболонки
    for simplex in hull.simplices:
        plt.plot(points[simplex, 1], points[simplex, 0], 'k-')

    ax.axis('off')
    
    plt.title('Опукла оболонка')
    plt.xlabel('X-координата')
    plt.ylabel('Y-координата')
    plt.legend()
    plt.grid(True)
    
    # Збереження графіку у файл (наприклад, у форматі PNG)
    plt.savefig('convex_hull_plot.png')
    
    # Відображення графіку
    plt.show()

# Основна функція
def main():
    # Зчитування даних з файлу
    dataset = read_dataset('DS5.txt')
    
    # Знаходження опуклої оболонки
    convex_hull = compute_convex_hull(dataset)
    
    # Відображення графіку
    plot_convex_hull(dataset, convex_hull)

if __name__ == "__main__":
    main()