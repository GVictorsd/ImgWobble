from numpy.lib.function_base import copy

# include helper functions from the inclib.py file
from inclib import *


def main():
    # read input image data
    img = image.imread('img1.jpg')

    # plot pixel distribution density

    # plotDistribution(img[:, :, 0])
    # plotDistribution(img[:, :, 1])
    # plotDistribution(img[:, :, 2])

    N = img.shape[0]
    M = img.shape[1]

    # slice a two dimension array from the image
    # and apply transformation
    # for b in range(1, 5):
    #     transImg1 = HE(img, 3, 1.2, 1/4, b/4, 10)
    #     plt.imshow(transImg1, cmap='binary')
    #     plt.savefig(f'f{b}.jpg', dpi=300, bbox_inches='tight')
    #     break
    # plt.imshow(img, cmap='Reds')
    # plt.savefig('saved.png', dpi=300, bbox_inches='tight')

    # transImg1 = HE(img, 3, 1.2, 0.25, 0.25, 10)
    transImg1 = HE(img, 3, 1, 0.25, 0.25, 10)
    plt.imshow(transImg1, cmap='binary')
    plt.show()
    # plot the image
    # plt.imshow(transImg1)
    # plt.imshow(transImg1[:,:,:], cmap='binary')
    # plt.imshow(transImg1[:,:,1], cmap='Blues')
    # plt.imshow(transImg1[:,:,2], cmap='Greens')
    # plt.show()
    # plt.imshow(img[:,:,:], cmap='binary')
    # plt.show()

    # plotDistribution(img[:, :, 0])
    # plotDistribution(transImg)
    # plt.show()

if __name__ == '__main__':
    main()