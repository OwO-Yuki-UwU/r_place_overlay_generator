from PIL import Image

# Adjust parameters here
image_file_name = "image.png"
output_overlay_image_name = "overlay.png"
image_place_location_x = 245
image_place_location_y = 938
canvas_width = 2000
canvas_height = 1000




overlay_img = Image.new(mode = "RGBA", size = (canvas_width * 3, canvas_height * 3), color = (0, 0, 0, 0))

place_img = Image.open(image_file_name)
place_img = place_img.resize((place_img.width * 3, place_img.height * 3), resample = Image.NEAREST)

overlay_img.paste(place_img, (image_place_location_x * 3, image_place_location_y * 3))

new_image_place_location_x = image_place_location_x * 3
new_image_place_location_y = image_place_location_y * 3

# Remove other lines
x = new_image_place_location_x
y = new_image_place_location_y
first_remove = True
while y < new_image_place_location_y + place_img.height:
    while x < new_image_place_location_x + place_img.width: # Remove line
        overlay_img.putpixel((x, y), (0, 0, 0, 0))
        x += 1

    if first_remove == False:
        x = new_image_place_location_x
        y += 1

        while x < new_image_place_location_x + place_img.width: # Remove line
            overlay_img.putpixel((x, y), (0, 0, 0, 0))
            x += 1

    x = new_image_place_location_x
    y += 2
    first_remove = False

# Remove other collumns
y = new_image_place_location_y
x = new_image_place_location_x
first_remove = True
while x < new_image_place_location_x + place_img.width:
    while y < new_image_place_location_y + place_img.height: # Remove collumns
        overlay_img.putpixel((x, y), (0, 0, 0, 0))
        y += 1

    if first_remove == False:
        y = new_image_place_location_y
        x += 1

        while y < new_image_place_location_y + place_img.height: # Remove collumns
            overlay_img.putpixel((x, y), (0, 0, 0, 0))
            y += 1

    y = new_image_place_location_y
    x += 2
    first_remove = False

overlay_img.save(output_overlay_image_name)
