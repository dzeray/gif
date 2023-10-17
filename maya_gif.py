from PIL import Image

image_2=Image.open('maya1.jpg')
new_image_2 = image_2.resize((230,307))
new_image_2.save('myimage_200.jpg')

image_path_1=['myimage_200.jpg', 'myimage_201.jpg', 'myimage_202.jpg']
image_list_2=[Image.open(file) for file in image_path_1]

image_list_2[0].save('maya_gif.gif', save_all=True, append_images=image_list_2[1:], duration=500, loop=0)