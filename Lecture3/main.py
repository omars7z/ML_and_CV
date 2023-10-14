import matplotlib.pyplot as plt

plt.figure("ONE", figsize=(10, 10))
for i in range(5):
    image = plt.imread("Lecture3\screenshot5.png")
    plt.subplot(5, 4, i+1)
    plt.title("Color image")
    plt.axis("off")
    plt.imshow(image)

plt.show()