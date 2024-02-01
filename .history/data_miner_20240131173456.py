from dataset_mining import DataMining
from PIL import Image
import os
import time

def main():

    try:


        data_miner = DataMining()
#       data_miner.create_table() already created
    
        for _ in range(105):
            # obtain the screenshot of the trading screen and area 
            whole_image = data_miner.screenshot()
            
            # obtain the left side of the trading space 
            # represents what is currently 'live' to feed into CNN
            current_image = data_miner.cut_image(whole_image)

            # show the entire trading space
            whole_image.show()

            # use this specified left screen click to help with image tagging flow
            # deliberately click on the cmd terminal
            data_miner.left_screen_click()

            # convert the current 'live' left side of the image to bianry values 
            # store into DB as BLOB
            current_binary_image = data_miner.binary_image(current_image)


            trend, phase, after = data_miner.label()


            data_miner.move100bars()


            data_miner.left_screen_click()



            os.system('taskkill /f /im PhotosApp.exe')
            time.sleep(.1)
            data_miner.insert_label(current_binary_image, trend, phase, after)
            

        data_miner.db_connection.close()
    
    except KeyboardInterrupt:
        print("\nOperation interrupted. exiting...")
    
    finally:
        if data_miner:
            data_miner.db_connection.close()

if __name__== "__main__":
    main()