print('''
**********************************************************************
     __________________________
    / \                         \       
   /   \            ____         \    
  / \/  \          /\   \         \  
 /  /\   \         \ \   \         \  
 \    \   \     ____\_\   \______   \  
  \     /\ \   /\                \   \  
   \   /\/  \  \ \_______    _____\   \  
    \  \/ /  \  \/______/\   \____/    \  
     \   / /\ \         \ \   \         \  
      \   /\/  \         \ \   \         \  
       \  \/ /  \         \ \   \         \  
  The   \   /    \         \ \   \         \  
         \  \  /\ \         \ \   \         \  
Bible     \   /\   \         \ \___\         \  
           \  \     \         \/___/          \  
adventure   \    \/  \                         \  
             \   /\   \_________________________\  
 by           \    \ / ______________________  /  
               \    / ______________________  / 
Richard You     \  /_________________________/ 
                                              
**********************************************************************
''')

qNoah = input("God pour out the rain to earth for 40 days, and Noah was making the boat. Would you help Noah to make the boat together? Yes or No ")
qNoah = qNoah.lower()

if qNoah == "yes":
    print("You have survived from the flood by making the ark with Noah! \n")
    qJesus = input("You were following Jesus, but people persecuted Jesus and his followers. Will you deny that you are follower? Yes or No ")
    qJesus.lower()
    if qJesus == "yes":
        print('You denied Jesus when he was persecuted, but you still have a chance! \n')
        qBelieve = input("After Jesus died, he resurrected from the grave three days after his death. Will you believe Jesus is the God of Heaven and the earth? Yes or No ")
        qBelieve.lower()
        if qBelieve == "yes":
            print('You are now child of God because you believe that Jesus is Lord.')
        else:
            print('You denied Jesus but also reject that Jesus is God even you saw he came back from the dead. Hope you will believe in Jesus soon.')
    else:
        print('You still followed Jesus in the persecution! You died with Jesus, but you are right next to Jesus in Heaven since you followed Him')
else:
    print('You have died from the flood')





