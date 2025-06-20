
# FINGER COUNT 

import cv2
import mediapipe as mp

mphands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils

hand=mphands.Hands(max_num_hands=1) # max_num_hands=1 ,only for one hand

video=cv2.VideoCapture(0)
while True:
    success,image=video.read()
    conv_img=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    if not success:
        break
    
    result=hand.process(conv_img)
    print(result.multi_hand_landmarks)
    
    #marking tip id
    tipids=[4,8,12,16,20]
    lmlist=[]
    
    if result.multi_hand_landmarks:
        
        
        for hand_landmarks in result.multi_hand_landmarks:
            for id,lm in enumerate(hand_landmarks.landmark):   #this step is used to print index and x,y values
                # print(id,lm)
                cx=lm.x   # we only need x and y not z, so assigning x to cx
                cy=lm.y   # assigning y to cy
                lmlist.append([id,cx,cy])  # adding index, x coordinate and y coordinate to lmlist
                # print(lmlist)
                if len(lmlist)!=0 and len(lmlist)==21:   # this step is used to check weather all 5 fingers are in screen
                     fingerlist=[]
                     for i in range(5):
                         if lmlist[tipids[i]][2]>lmlist[tipids[i]-2][2]:  #4y>2y ie, if hand closed fingerlist add 0, if hand open fingerlist add 1
                             fingerlist.append(0)
                         else:
                             fingerlist.append(1)
                     print(fingerlist)
                    
            mp_drawing.draw_landmarks(image,hand_landmarks,mphands.HAND_CONNECTIONS)    
            
    
    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
