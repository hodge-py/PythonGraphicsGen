import numpy as np
from mayavi.mlab import *
from mayavi import mlab
from PIL import Image
import random
import PyQt5

"""
Main Code
"""

class PyGraphicsGen:
    """
    PyGraphicsGen is the main class to generate wallpapers, animations, etc.
    """

    def __init__(self,forward = -.5, right = -.5, up = 0, pitch = 0, roll = 0):
        self.forward = forward
        self.right = right
        self.up = up
        self.pitch = pitch
        self.roll = roll


    def array2dLand(self,data,background=(0,0,0),screenshot=True,mode='rgba',anti=True,showfig=True,imgSize=(1920,1080),colorMaps='gist_earth'):
        """
        :param data: 2d numpy array
        :param background: sets color of scene background
        :param screenshot: if the photo should be saved
        :param mode: rgba or rgb. rgba will have a transparent background
        :param anti: antialiasing on or off
        :param showfig: show mayavi gui
        :param imgSize: set the pixel size
        :param colorMaps: color scheme of figure
        :return:
        """
        mlab.move(self.forward, self.right, self.up)
        fig = mlab.figure(1,bgcolor=background,size=imgSize)
        norm = data
        imshow(norm,colormap=colorMaps)

        if screenshot == True and mode == 'rgba':
            screen = mlab.screenshot(figure=fig,mode=mode,antialiased=anti)
            screen = Image.fromarray(np.uint8(screen * 255))
            screen.save(f"test{random.randint(0,10000)}.png")
        elif screenshot == True and mode == 'rgb':
            screen = mlab.screenshot(figure=fig, mode=mode,antialiased=anti)
            screen = Image.fromarray(np.uint8(screen))
            screen.save(f"test{random.randint(0, 10000)}.png")
        if showfig:
            mlab.show()


    def surf2dArray(self,data,background=(0,0,0),screenshot=True,mode='rgba',anti=True,showfig=True,imgSize=(1920,1080),colorMaps='gist_earth'):
        """
        :param data: 2d numpy array
        :param background: sets color of scene background
        :param screenshot: if the photo should be saved
        :param mode: rgba or rgb. rgba will have a transparent background
        :param anti: antialiasing on or off
        :param showfig: show mayavi gui
        :param imgSize: set the pixel size
        :param colorMaps: color scheme of figure
        :return:
        """
        fig = mlab.figure(1, bgcolor=background,size=imgSize)
        norm = data
        surf(norm, colormap=colorMaps)

        if screenshot == True and mode == 'rgba':
            screen = mlab.screenshot(figure=fig,mode=mode,antialiased=anti)
            screen = Image.fromarray(np.uint8(screen * 255))
            screen.save(f"test{random.randint(0,10000)}.png")
        elif screenshot == True and mode == 'rgb':
            screen = mlab.screenshot(figure=fig, mode=mode,antialiased=anti)
            screen = Image.fromarray(np.uint8(screen))
            screen.save(f"test{random.randint(0, 10000)}.png")
        if showfig:
            mlab.show()


    def array2dLandAnim(self):
        """
        :param self:
        :return:
        """
        pass

    def surf2dLArray(self):
        """

        :param self:
        :return:
        """
        pass


    def setMoveCamera(self,forward,right,up):
        """
        Moves the camera to the given coordinates
        :param forward:
        :param right:
        :param up:
        :return:
        """
        self.forward = forward
        self.right = right
        self.up = up

