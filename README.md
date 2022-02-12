# Simple FFmpeg Grids

Run by typing "python create_grids.py" in terminal. It will create a file called "filter_script.txt" and output the command to create a grid. If the grid needs to be modified, just edit the last line of the python program. It has comments detailing how to edit it. This is much simpler than trying to follow one of the many guides online.

# [The following description was copied from the collab](https://colab.research.google.com/drive/1quez5NEtIxhPY8qKAnhwyf3ZF5eyYVs1?usp=sharing)

### A python file to quickly generate simple FFmpeg grids. 

In the example below, the FFmpeg command it generates will be 3x3 grid with files named in the following format. Just edit the forms to quickly set your desired format.

#### Output example format

| column #1  |  column #2       |  column #3|
|----------|:-------------|:------|
| 0.mp4 |  1.mp4 | 2.mp4 |
| 3.mp4 |    4.mp4   |  5.mp4 |
| 6.mp4 | 7.mp4 | 8.mp4 |


There is a filter script that will also be generated with the file specified from the inputs. This is generated because with increasingly large inputs, the command for the console will be too large. This fixes that problem. You will need to move this script to the same directory that the FFmpeg command is ran from in the terminal.

#### Example of 100 videos in a 10x10 grid
[link to video](https://youtu.be/CWhya8R--UI)

[![co.png](media/out.png)](https://www.youtube.com/watch?v=CWhya8R--UI)
