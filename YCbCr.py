import matplotlib.pyplot as plt
import numpy as np


def rgb2ycbcr(im):
    """
    Convert from RGB image to YCbCr image
    Input:  im = uint8 3D numpy array of RGB image of size (h*w*3)
    Output: uint8 3D numpy array of YCbCr image of size (h*w*3)
    """
    
    M = np.array([[.299, .587, .114], 
                  [-.1687, -.3313, .5], 
                  [.5, -.4187, -.0813]])
    #do at this               
    ycbcr = np.dot(im,M.T)
    ycbcr[:, :, [1, 2]] += 128
 
    return np.uint8(ycbcr)
    
def ycbcr2rgb(im):
    """
    Convert from YCbCr image to RGB image
    Input:  im = uint8 3D numpy array of YCbCr image of size (h*w*3)
    Output: uint8 3D numpy array of RGB image of size (h*w*3)
    """
    #do at this
    Minv = np.array([[1, 0, 1.402], 
                     [1, -0.34414, -0.71414], 
                     [1, 1.772, 0]])
    #do at this                
    a = im.astype(float)
    a[:, :, [1, 2]] -= 128
    
    return np.clip(np.dot(a,Minv.T),0,255).astype(np.uint8)

if __name__=="__main__":
    img = plt.imread('cat.jpg')
    print(img.max(), img.dtype)

    imgycbcr = rgb2ycbcr(img)
    imgrgb = ycbcr2rgb(imgycbcr)

    print(imgycbcr.max(), imgycbcr.dtype)
    print(imgrgb.max(), imgrgb.dtype)

    plt.subplot(2,3,1)
    plt.imshow(imgycbcr[:,:,0], cmap='gray', vmin=0, vmax=255)
    plt.title('Y')
    plt.subplot(2,3,2)
    plt.imshow(imgycbcr[:,:,1], cmap='gray', vmin=0, vmax=255)
    plt.title('Cb')
    plt.subplot(2,3,3)
    plt.imshow(imgycbcr[:,:,2], cmap='gray', vmin=0, vmax=255)
    plt.title('Cr')

    plt.subplot(2,3,4)
    plt.imshow(imgrgb)
    plt.title('Converted RGB')
    plt.subplot(2,3,5)
    plt.imshow(img)
    plt.title('Original')
    plt.show()
