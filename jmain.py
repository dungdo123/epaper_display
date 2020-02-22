
import epd2in9b
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
#import imagedata

COLORED = 1
UNCOLORED = 0
im1 = Image.open('jun_lee_1.bmp')
im1 = im1.resize((128,296), resample=0)
im2 = Image.open('tae_icon_2.bmp')
im2 = im2.resize((128,296), resample=0)

def main():
    epd = epd2in9b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF]* (epd.width * epd.height // 8)
    frame_red = [0xFF]* (epd.width * epd.height // 8)
   # frame_black = [int(i) for i in frame_black1]
   # frame_red = [int(j) for j in frame_red1] 


    # write strings to the buffer
    #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 16)
    #epd.draw_string_at(frame_black, 4, 30, "e-Paper Demo", font, COLORED)
    #epd.draw_string_at(frame_red, 6, 10, "Hello jun!", font, UNCOLORED)
    # display the frames
    #epd.display_frame(frame_black, frame_red)
    # display images
    
    frame_black = epd.get_frame_buffer(im1)
    frame_red = epd.get_frame_buffer(im2)
    
    epd.display_frame(frame_black, frame_red)

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.IMAGE_BLACK, imagedata.IMAGE_RED)

if __name__ == '__main__':
    main()

