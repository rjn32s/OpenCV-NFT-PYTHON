import numpy as np
import cv2
import random
import cvzone
import random_name_generator as rng

# Take the input of NFT you want
def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
	"""
	@brief      Overlays a transparant PNG onto another image using CV2
	
	@param      background_img    The background image
	@param      img_to_overlay_t  The transparent image to overlay (has alpha channel)
	@param      x                 x location to place the top-left corner of our overlay
	@param      y                 y location to place the top-left corner of our overlay
	@param      overlay_size      The size to scale our overlay to (tuple), no scaling if None
	
	@return     Background image with overlay on top
	"""
	
	bg_img = background_img.copy()
	
	if overlay_size is not None:
		img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

	# Extract the alpha mask of the RGBA image, convert to RGB 
	b,g,r,a = cv2.split(img_to_overlay_t)
	overlay_color = cv2.merge((b,g,r))
	
	# Apply some simple filtering to remove edge noise
	mask = cv2.medianBlur(a,5)

	h, w, _ = overlay_color.shape
	roi = bg_img[y:y+h, x:x+w]

	# Black-out the area behind the logo in our original ROI
	img1_bg = cv2.bitwise_and(roi.copy(),roi.copy(),mask = cv2.bitwise_not(mask))
	
	# Mask out the logo from the logo image.
	img2_fg = cv2.bitwise_and(overlay_color,overlay_color,mask = mask)

	# Update the original image with our new ROI
	bg_img[y:y+h, x:x+w] = cv2.add(img1_bg, img2_fg)

	return bg_img






number_of_nft = int(input("Enter the number of NFT You WANT : ) $$  "))



i = 0
while i <= number_of_nft:
    # Add the Background
    #bg_i = random.randint(1,11)
    addr_bg = 'D:/NFT/myAsset/background/bg_' + str(random.randint(1,11)) + '.png'
    bg_img = cv2.imread(addr_bg)
    #print(bg_img.shape)
    body_img = cv2.imread('D:/NFT/myAsset/body/body_'+str(random.randint(1,11))+'.png',cv2.IMREAD_UNCHANGED)
    eye_img = cv2.imread('D:/NFT/myAsset/eye/eye_'+str(random.randint(1,11))+'.png',cv2.IMREAD_UNCHANGED)
    glass_img = cv2.imread('D:/NFT/myAsset/glasses/glass_'+str(random.randint(1,11))+'.png',cv2.IMREAD_UNCHANGED)
    nose_img = cv2.imread('D:/NFT/myAsset/nose/nose_'+str(random.randint(1,11))+'.png',cv2.IMREAD_UNCHANGED)
    lips_img = cv2.imread('D:/NFT/myAsset/lips/lips_'+str(random.randint(1,11))+'.png',cv2.IMREAD_UNCHANGED)
    shirt_img = cv2.imread('D:/NFT/myAsset/shirt/shirt_'+str(random.randint(1,11))+'.png',cv2.IMREAD_UNCHANGED)
    
    step_1 = overlay_transparent(bg_img,body_img,0,0)
    #print(step_1.shape)
    step_2 = overlay_transparent(step_1,eye_img,0,0)
    step_3 = overlay_transparent(step_2,glass_img,0,0)
    step_4 = overlay_transparent(step_3,nose_img,0,0)
    step_5 = overlay_transparent(step_4,lips_img,0,0)
    step_6 = overlay_transparent(step_5,shirt_img,0,0)
    #cv2.imshow('output',cv2.resize(step_6,(600,400)))
    #cv2.waitKey(0)
    #out = rng.generate(descent=rng.Descent.ENGLISH, sex=rng.Sex.MALE, limit=1)
    #print(out)
    
    cv2.imwrite('D:/NFT/output/image'+str(i)+'.png',step_6)
    i+=1