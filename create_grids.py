
import math

def createCommand(inputAmount, videoFileFormat, gridX, gridY, newVidSizeX, newVidSizeY, filterFile, outFile):
    
    # inputs are formatted here for the command
    def createVideoInputs(toAmount, fileFormat):
        temp = ""
        
        for i in range(toAmount):
            temp += " -i " + str(i) + "." + fileFormat + " "
        
        return temp
     
    def createFilter(inputAmount, gridX, gridY, newVidSizeX, newVidSizeY, filterFile):
    
        filterBaseArg = " -filter_complex_script "
    
        # the resolution is determined by the size of the videos
        def defineBase(finalVideoX, finalVideoY, clipsOnX, clipsOnY):
            return " nullsrc=size=" + str(finalVideoX * clipsOnX) + "x" + str(finalVideoY * clipsOnY) + " [base]; "

        def tagInputs(toAmount, x, y):
            
            inputs = ""
            
            for i in range(0, toAmount):
                inputs += " [" + str(i) + ":v] "
                inputs += " setpts=PTS-STARTPTS, "
                inputs += " scale=" + str(x) + "x" + str(y) + " " 
                inputs += " [clip" + str(i) + "]; "
            
            return inputs


        def createVideoOverlays(toAmount, gridX, gridY, vidX, vidY):
            
            overlays = " [base][clip0] overlay=shortest=1 [temp1]; "
            
            for i in range(1, toAmount):
                overlays += "[temp" + str(i) + "][clip" + str(i) + "] overlay=shortest=1"
                overlays += (":x = " + str((i % gridX) * vidX)) if i % gridX > 0 else ""
                overlays += (":y = " + str(math.floor((i) / gridY) * vidY)) if i >= gridY else ""
                overlays += " [temp" + str(i + 1) + "]; " if i != (toAmount - 1) else ""
                
            return overlays
            
        
        tempFile = open(filterFile, "w")
        
        tempFile.write(defineBase(newVidSizeX, newVidSizeY, gridX, gridY) + tagInputs(inputAmount, newVidSizeX, newVidSizeY) + createVideoOverlays(inputAmount, gridX, gridY, newVidSizeX, newVidSizeY))
        
        tempFile.flush()
        tempFile.close()
        
        return filterBaseArg + "\"" + filterFile + "\" "
    
    def createOutput(outFile):
        return " -c:v libx264 " + outFile

    
    return "ffmpeg " + createVideoInputs(inputAmount, videoFileFormat) + createFilter(inputAmount, gridX, gridY, newVidSizeX, newVidSizeY, filterFile) + createOutput(outFile)


# amount of items in grid
# filetype of items
# amount of columns on the horizontal axis
# amount of rows on the vertical axis
# size of each video - x-axis
# size of each video - y-axis
# file to save the filter for the command
# output file name
print(createCommand(9, "mp4", 3, 3, 1080, 1080, "filter_script.txt", "out.mp4"))