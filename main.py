from PIL import Image

image=Image.open('image0.jpg')
new_image = image.resize((233,266))
new_image.save('myimage_500.jpg')


image_path_list=['myimage_500.jpg', 'myimage_501.jpg', 'myimage_502.jpg']
image_list= [Image.open(file) for file in image_path_list]

image_list[0].save('my_gif.gif',save_all=True, append_images=image_list[1:], duration=150, loop=0)


