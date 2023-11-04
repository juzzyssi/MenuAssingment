

##-------=======LISTS=======-------##


screenresolution = [1280,720] ## List that supplies the rest of the code with the screen resolution


##-------=======LIBRARIES IMPORTS=======-------##


from math import*
from pygame import *          ## importing some code libraries
from pygame import font


##-------=======INITIALIZATIONS=======-------##


font.init() ## Initializes the font


##-------=======VARIABLES=======-------##


payed_confirmation = False
button_confirmation_3 = False

screen = display.set_mode((screenresolution[0],screenresolution[1])) ## creates a window with the given res

layer1 = Surface(screen.get_size(), SRCALPHA)
layer2 = Surface(screen.get_size(), SRCALPHA)

text_font_1 = font.Font("Montserrat-Regular.ttf", 20) ## Assigns a font to the text that is later rendered
text_font_2 = font.Font("Montserrat-Medium.ttf", 18) ## Assigns a font to the text that is later rendered
text_font_4 = font.Font("Montserrat-Medium.ttf", 30) ## Assigns a font to the text that is later rendered
text_font_5 = font.Font("Montserrat-Medium.ttf", 40) ## Assigns a font to the text that is later rendered
text_font_3 = font.Font("OpenSans_Condensed-Medium.ttf", 18) ## Assigns a font to the text that is later rendered

transition = False ## Transition trigger

FPS = 34 ## Setting the desired frame rate
clock = time.Clock() ## Seting a variable which code limits the frames per second

currentwindow = "Window_1" ## Sets the starting window code

proceed1 = False
proceed2 = False
proceed3 = False

shopcart = []

products = ["Hamburger", "Beverage", "Hot Dog", "Brownie", "Water Bottle", "Pop Corn"]

texts = [0,0,0,0,0,0]

pieces = len(products)

cooldown = False

start_count = 0

total_texts = 0


##-------=======FUNCTIONS=======-------##


def sensemouse(x,y,width,height):

    if mx >= x and mx <= x + width and my >= y and my <= y + height:
        return True
    else:
        return False

def rendtext(text, font, text_col):  ## renders some text & returns its value
    img = font.render(text, True, text_col)
    return img

def gettextres(image): ## returns the res of a image use the get_rect()
    text_rect = image.get_rect()
    return text_rect.width, text_rect.height

def disptext(layer, image, x, y): ## Displays an image, but I will use it for text renders
    layer.blit(image, (x,y))

def inbetween(inicial_value, resultant_value, frames): ## Returns the value per frame of a difference

    difference = resultant_value - inicial_value
    difperframe = difference / frames
    return difperframe

def setTrue(variable):
    variable = True
    return variable
    
def rectbutton(red, green, blue, x, y, width, height, radius, rr, rg, rb): ## Makes a button with the specified visual characteristics and a signal activator

    r = red
    g = green ## sets the colour variables
    b = blue

    if radius != 0:
        draw.rect(screen, (241, 177, 53), (x - (width/2),y - (height/2), width, height), radius) ## Draws the outline rectangle if a radius over 0 is provided
        
    draw.rect(screen, (r,g,b), (x - (width/2), y - (height/2), width, height), 0) ## Draws a rectangle

    rframe = inbetween(r, rr, 10)
    gframe = inbetween(g, rg, 10) ## calculates the value per frame each color has for the transition
    bframe = inbetween(b, rb, 10)

    if mx > x - (width/2) and mx < x + (width/2) and my > y - (height/2) and my < y + (height/2): ## Triggers when the mouse is inside the button parameter

##        print("Button within accepted range")

        draw.rect(screen, (r + ((10* 0.2) * rframe), g + ((10*0.2) * gframe), b + ((10*0.2) * bframe)), (x - (width/2), y - (height/2), width, height), 0) ## Draws the rectangle

def visual_illusion(screen):
    
    sy = 20
    ty = screenresolution[1] / 2
    rmy = my - (screenresolution[1] / 2)
    srmy = rmy * (sy / ty)

    sx = 20
    tx = screenresolution[0] / 2
    rmx = mx - (screenresolution[0] / 2)
    smrx = rmx * (sx / tx)

    screen.blit(background, (-20 - (smrx), -20 - (srmy)))
    screen.blit(Shine, (0, 0))
    screen.blit(menupic, (6.5, 6.5))
    screen.blit(selecbox, (473 + 13 + 45, 50))

def visual_illusion_2(screen):
    
    sy = 20
    ty = screenresolution[1] / 2
    rmy = my - (screenresolution[1] / 2)
    srmy = rmy * (sy / ty)

    sx = 20
    tx = screenresolution[0] / 2
    rmx = mx - (screenresolution[0] / 2)
    smrx = rmx * (sx / tx)

    screen.blit(background, (-20 - (smrx), -20 - (srmy)))
    screen.blit(Shine, (0, 0))
    
##-------=======VISUAL RESOURCES=======-------##


background = image.load('Big_Background.png')

menupic = image.load('Menu_pictures.png')  ## Importing resources for later use

selecbox = image.load('Selection_Box.png')

title = image.load('Title.png')

loadingscreen = image.load('Loading_screen.png')

Shine = image.load('Background_Shine.png')

Hamshine = image.load('Hamburger_Shine.png')

Bevshine = image.load('Beverage_shine.png')

Hotshine = image.load('HotDog_Shine.png')

Broshine = image.load('Brownie_shine.png')

Botshine = image.load('Water_bottle_shine.png')

Popshine = image.load('Popcorn_Shine.png')

totalbox = image.load('Total_Box.png')


##-------=======TEXT RENDERING=======-------##

hamind = rendtext("Hamburger:", text_font_2, (230,230,230))

hampri = rendtext("x $5.00", text_font_2, (230,230,230))

##-------=======DICTIONARIES=========-------##

food_Attributes = {
            "Hamburger": ["Hamburger", Hamshine, 0, [], 4.99, []],
            "Beverage": ["Beverage",Bevshine, 0, [], 2.49, []],
            "Hot Dog": ["Hot Dog", Hotshine, 0, [], 2.99, []],
            "Brownie": ["Brownie", Broshine, 0, [], 3.99, []],
            "Water Bottle": ["Water Bottle", Botshine, 0, [], 1.49, []],
            "Pop Corn": ["Pop Corn", Popshine, 0, [], 3.99, []]
        }

##-------=======CODING=======-------##


print("starting")

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    # -------------------------------
    # Your code here

    ## Background resources:

    mb = mouse.get_pressed()

    mx,my = mouse.get_pos()

    ## Window 1:

    if currentwindow == "Window_1" and not transition:

        sy = 20

        ssy = 3

        ty = screenresolution[1]/2

        rmy = my - (screenresolution[1] / 2)

        srmy = rmy * (sy / ty)

        ssrmy = rmy * (ssy / ty)

        sx = 20

        ssx = 5

        tx = screenresolution[0]/2

        rmx = mx - (screenresolution[0]/2)

        smrx = rmx * (sx / tx)

        ssmrx = rmx * (ssx / tx)

        clock.tick(FPS)

        screen.blit(background, (-20 - (smrx), -20 - (srmy)))

        screen.blit(Shine, (0,0))

        title_width, title_height = title.get_size()

        screen.blit(title, (((screenresolution[0]/2) - title_width/2) - (ssmrx), (screenresolution[1]/2 - title_height/2 - 40) - (ssrmy)))

        if (screenresolution[0]/2 - 110 <= mx <= screenresolution[0]/2 + 110) and (screenresolution[1]/2 - 25 + 75 <= my <= screenresolution[1]/2 + 25 + 75) and mb[0]:

            proceed1 = True

            currentwindow = "None"

        rectbutton(0, 73, 103, screenresolution[0]/2, screenresolution[1]/2 + 75, 220, 50, 0, 20, 173, 203) ## Button 1

        button1_text = rendtext("Proceed to order", text_font_1, (255,255,255))

        text1_width, text1_height = gettextres(button1_text)

        disptext(screen, button1_text, screenresolution[0]/2 - text1_width / 2, screenresolution[1]/2 + 75 - text1_height / 2)

        display.flip()

## Proceed trigger from window 1

    if proceed1:

        print(f"procceding (1)")

        currentwindow = "Window_2"

        transition = True

        proceed1 = False

## Transition command

    if transition:

        a = 1.2457

        aa = - 1.2457

        transitioncolour = (10,33,63)

        for time in range(0,35,1):

            y = a * (time - 34) ** 2 + 360
            yy = aa * (time - 34) ** 2 + 360
            layer1.fill((0,0,0,0))

            A = 0.1 * time

            draw.rect(layer1, (0,0,0,A), (0,0, screenresolution[0], screenresolution[1]), 0)
            
            layer1.blit(loadingscreen,(0,0 - screenresolution[1] + yy))
            layer1.blit(loadingscreen,(0,screenresolution[1] - yy))
  
            screen.blit(layer1, (0, 0))  # Draw the layer on the screen
            display.flip()

            clock.tick(FPS)

        layer1.fill((0,0,0,0))

        for time in range(34, 69, 1):

            y = a * (time - 34) ** 2 + 360
            yy = aa * (time - 34) ** 2 + 360

            layer1.fill((0,0,0,255))

            layer1.blit(loadingscreen,(0,0 - screenresolution[1] + yy))
            layer1.blit(loadingscreen,(0,screenresolution[1] - yy))

            screen.blit(layer1, (0, 0))  # Draw the layer on the screen
            display.flip()

            clock.tick(FPS)

        transition = False

    if currentwindow == "Window_2" and not transition: ## Window 2, spent so much time learning stuff to pull it off easier than almost none of the original code is left, therefore no notes
                
        visual_illusion(screen)

        for index, (food, attributes) in enumerate(zip(products, food_Attributes.values())): ## It displays all of the shine images and adds the product to the dictionary
            shine_img, current_value = attributes[1], attributes[2]

            x = 36
            y = 89 + (92 * index)


            food_int = sensemouse(x, y, 412, 93)

            if food_int:
                screen.blit(shine_img, (6.5, 6.5))

                if mb[0]:
                    if not cooldown:
                        shopcart.append(food)
##                        print(f"Added {food} to the list")
##                        print(shopcart)
                        food_Attributes[food][2] += 1
##                        print(f"Total amount: {food_Attributes[food][2]}")
                    cooldown = True

        column_difference_1 = 0

        Test = rendtext("Testing", text_font_4, (0,0,0))

        text_ind_height = Test.get_height()

        for section, food in zip(range(0, len(products), 1), products): ## It removes the products from the dictionary

            x = 560
            y = (80 + 30) + (((section + column_difference_1) * text_ind_height) + ((section + column_difference_1) * 10))

            hover = sensemouse(x, y, selecbox.get_width(), text_ind_height)

            if food_Attributes[food][2] >= 1:

                if mb[0] and not cooldown and hover:

                    food_Attributes[food][2] += -1
                    cooldown = True

            elif food_Attributes[food][2] == 0:

                column_difference_1 += -1

## OLD CODE:

        Hamburger = rendtext("HAMBURGER", text_font_2, (255,255,255))

        Beverage = rendtext("BEVERAGE", text_font_2, (255,255,255))

        Hotdog = rendtext("HOT DOG", text_font_2, (255,255,255))

        Brownie = rendtext("BROWNIE", text_font_2, (255,255,255))

        Waterbottle = rendtext("WATER BOTTLE", text_font_2, (255,255,255))

        Popcorn = rendtext("POP CORN", text_font_2, (255,255,255))

        disptext(layer2, Waterbottle, 126, 468)

        disptext(layer2, Brownie, 224, 392)

        disptext(layer2, Beverage, 238, 185)

        disptext(layer2, Hamburger, 168, 108)

        disptext(layer2, Hotdog, 179, 300)

        disptext(layer2, Popcorn, 110, 595)

        screen.blit(layer2, (0,0))

## NOT OLD CODE:

        for food in products: ## RENDERS TEXT IMAGES FOR THE CORRESPONDENT VALUES IN EACH PRODUCT

            textimg = rendtext(f"{food} (${food_Attributes[food][4]}) x ", text_font_4, (255,255,255))

            numimg = rendtext(f"{food_Attributes[food][2]}", text_font_4, (255,255,255))

            food_Attributes[food][5].clear()

            food_Attributes[food][3].clear()

            food_Attributes[food][3].append(textimg)

            food_Attributes[food][5].append(numimg)

        text_height = 35

        column_diff = 0

        for column_order, pro in zip(range(0, 6, 1), products): ## DISPLAYS THE COLUMNS ONLY WHEN NECESARY

            column = column_order + column_diff

            if food_Attributes[pro][2] != 0:

                x = 560 + (selecbox.get_width() / 2) - (food_Attributes[pro][5][0].get_width() / 2)

                y = (80  + 30) + ((column * text_height) + (column * 10))

                disptext(screen, food_Attributes[pro][3][0], x - (food_Attributes[pro][3][0].get_width() / 2) - 45, y)

                ax = x + (food_Attributes[pro][3][0].get_width() / 2) 

                disptext(screen, food_Attributes[pro][5][0], ax, y)

            elif food_Attributes[pro][2] == 0:

                column_diff += -1

        screen.blit(totalbox, ((473 + 13 + 45) + (selecbox.get_width() / 2) - (totalbox.get_width() / 2), 50 + selecbox.get_height() - (totalbox.get_height() / 2)))

        TOTAL = rendtext("TOTAL : ", text_font_4, (0,0,0))

        totalprice = 0

        buttontext2 = rendtext("Proceed to payment", text_font_4, (255,255,255))

        for index in products:

            amount = food_Attributes[index][2]

            piece_price = food_Attributes[index][4]

            totalprice += (amount * piece_price)

            tax = round(totalprice * 0.13, 2)

            totalimg = rendtext(f"${round(totalprice + tax, 2)}", text_font_4, (0,0,0))

            x_pos_2 = totalimg.get_width() + TOTAL.get_width()

        totalprice += tax

        TAXES = rendtext(f"Taxes: ${tax}", text_font_2, (255,255,255))

        disptext(screen, TAXES, (473 + 13 + 45) + (selecbox.get_width() / 2) - (TAXES.get_width() / 2), 50 + selecbox.get_height() - 80)

        disptext(screen, totalimg, (473 + 13 + 45) + (selecbox.get_width() / 2) - (x_pos_2 / 2) + TOTAL.get_width(),  50 + selecbox.get_height() - (TOTAL.get_height() / 2)) ##UNCOMPLETE

        disptext(screen, TOTAL, (473 + 13 + 45) + (selecbox.get_width() / 2) - (x_pos_2 / 2), 50 + selecbox.get_height() - (TOTAL.get_height() / 2))
        
        rectbutton(0, 73, 103, ((473 + 13 + 45) + (selecbox.get_width() / 2)),((50 + selecbox.get_height()) + ((screenresolution[1] - (50 + selecbox.get_height())) /  2)), totalbox.get_width() - 60, ((totalbox.get_height() / 5) * 4), 0, 20, 173, 203)

        x_button2_pos = (473 + 13 + 45) + (selecbox.get_width() / 2) - (buttontext2.get_width() / 2)

        y_button2_pos = (50 + selecbox.get_height()) + ((screenresolution[1] - (selecbox.get_height() + 50)) / 2) - (buttontext2.get_height() / 2)

        disptext(screen, buttontext2, x_button2_pos, y_button2_pos ) ## UNCOMPLETE

        window3trigger = sensemouse(705, 561, totalbox.get_width() - 60, ((totalbox.get_height() / 5) * 4))

        if window3trigger:

            if mb[0]:

                proceed2 = True

    if proceed2:

        print("proceeding(2)")

        proceed2 = False

        currentwindow = "window_3"

        transition = True

    if currentwindow == "window_3" and not transition:

        visual_illusion_2(screen)

        paytext = rendtext("Pay", text_font_4, (255,255,255))

        almostfinaltext = rendtext(f"The total amount is of: ${round(totalprice, 2)}", text_font_4, (255,255,255))

        disptext(screen, almostfinaltext, (screenresolution[0] / 2) - (almostfinaltext.get_width() / 2), (screenresolution[1] / 2) - almostfinaltext.get_height() - 40)

        PAYED = rendtext("Enjoy your movie!", text_font_5, (255,255,255))

        backbutton = rendtext("Back", text_font_2, (255,255,255))

        window2_button = sensemouse(15, 15, 120, 40)

        if not button_confirmation_3:

            rectbutton(0, 173, 53, screenresolution[0] / 2, screenresolution[1] / 2 + 60, 200, 65, 0, 50, 125, 103)
            disptext(screen, paytext, (screenresolution[0] / 2) - (paytext.get_width() / 2), (screenresolution[1] / 2) - paytext.get_height() + 75)

        button_mouse_hover = sensemouse(screenresolution[0] / 2 - 100, screenresolution[1] / 2 - 32 + 60, 200, 65)

        if button_confirmation_3:

            disptext(screen, PAYED, (screenresolution[0] / 2) - (PAYED.get_width() / 2), (screenresolution[1] / 2) - PAYED.get_height() + 75)
            payed_confirmation = True

        if button_mouse_hover:
            if mb[0]:

                cooldown = True
                button_confirmation_3 = True
                print("button confirmation")

        if not payed_confirmation:

            rectbutton(0, 73, 103, 60 + 15, 25 + 15, 120, 40, 0, 20, 173, 203)

            disptext(screen, backbutton, (60 + 15) - (backbutton.get_width() / 2), (25 + 15) - (backbutton.get_height() / 2))

            if window2_button and mb[0]:

                proceed3 = True

    if proceed3:

        proceed3 = False

        currentwindow = "Window_2"

        transition = True

    if not mb[0]:

        cooldown = False

        
    # -------------------------------
    display.flip()

    print(mx,my)

quit()                 
