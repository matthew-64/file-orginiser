# file-orginiser
## Problem:

There is a directory which contains several hundred thousand files that make up an elevation model of the UK and each file a has the name of a grid square eg SH60NE. (See below)

![alt text](https://digimap.edina.ac.uk/webhelp/os/data_information/os_products/images/100kmsq.gif)


loading thousands of files in one folder to scroll through is very inefficient and time consuming.

## Solution:
The files needed to be sorted into alphabetical directories of the first two letters of the filename. For example AA. This should result in a directory being created with the name of each designated square in the image above with the relevant files sorted into that directory.

## How to use
`cd <directory where all the files are stored>`  
`git clone https://github.com/matthew-64/file-orginiser.git`  
`python3 file-orginiser/main.py`  
`rm -r file-orginiser/`  
`rm .git`

