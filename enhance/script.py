from numpy.lib.function_base import copy

# include helper functions from the inclib.py file
from src.inclib import *


def main():
    # read input image data
    img = image.imread('imgcrop.jpg')

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
    transImg1 = HE(img, 3, 1.2, 0.5, 0.5, 10)
    # transImg1 = HE(img, 5, 1.4, 0.1, 0.1, 10)


  #  transImg1 = HE(img, 3, 1.8, 0.25, 0.25, 1)
#    plt.imshow(transImg1)
    plotDistribution(transImg1[:,:,0])
    plotDistribution(transImg1[:,:,1])
    plotDistribution(transImg1[:,:,2])
    plt.show()
    # plot the image
    # plt.imshow(transImg1)
    # plt.imshow(transImg1[:,:,:], cmap='binary')
    # plt.imshow(transImg1[:,:,1], cmap='Blues')
    # plt.imshow(transImg1[:,:,2], cmap='Greens')
    # plt.show()
    # plt.imshow(img[:,:,:], cmap='binary')
    # plt.show()

#    plotDistribution(img[:, :, 0])
 #   plotDistribution(img[:, :, 1])
  #  plotDistribution(img[:, :, 2])
    # plotDistribution(transImg)
  #  plt.show()

if __name__ == '__main__':
    main()
