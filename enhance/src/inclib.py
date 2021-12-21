import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

def plotDistribution(image):
    '''
    function to plot pixel intensity distribution of an image
    '''
    dist = np.zeros(256)
    x = np.arange(256)
    for row in image:
        for elem in row:
            if elem < 256:
                dist[elem] += 1 
            else:
                dist[0] += 1
    return plt.plot(x, dist)



def HE(inimage, W=3, a=1, b=1, c=1, k=1):
    '''
    function to compute the transform of the input image
    '''

    # Variables
    # kernel dimensions(W)
    # parameters (a, b, c, k)


    # calculate global mean of the image mg(i, j)
    M, N = inimage.shape[0], inimage.shape[1]

    # transformed result image
    # res = np.empty(M*N, dtype='int32')
    res = np.empty(inimage.shape, dtype='int32')

    # for dim, image in enumerate(inimage):
    for dim in range(inimage.shape[2]):
        image = inimage[:, :, dim]
        resindex = 0

        # Global Mean
        mg = 0
        for i in range(M):
            for j in range(N):
                mg += image[i, j]
        mg /= M*N

        # for each pixel in the image, calculate the transformed intensity
        for i in range(M):
            for j in range(N):

                # local mean
                ml = 0
                for k in range(W):
                    for l in range(W):
                        ml += image[i+k, j+l] if (i+k < M and j+l < N) else 0
                ml /= W*W

                # local standard deviation
                stdDiv = 0
                for k in range(W):
                    for l in range(W):
                        stdDiv += (image[i+k, j+l] - ml)**2 if(i+k < M and j+l < N) else ml**2
                stdDiv = ( stdDiv/(W**2) )**0.5

                # get transformed intensity value of the current pixel
                mul1 = (k*mg)/(stdDiv+b)
                mul2 = ( image[i][j] - (c*ml) ) + ( ml**a )
                # and store in the result image
                res[i, j, dim] = (mul1*mul2)//255
                # resindex += 1
    
    # reshape the array into input image dimension and return
    # res = res.reshape(M, N)
    return res