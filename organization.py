# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:48:32 2018
#19 column 0 is number of wtd
#4 row starts list of jpegs

@author: ttl80
"""

import os
import sys
import hashlib

#Creates folders for different file types
def makeFolders(downloadDirectory, fileTypes):
    for fileType in fileTypes.keys():
        directory = downloadDirectory + "\\" + fileType
        
        if not os.path.exists(directory):
            os.mkdir(directory)

#Moves file to its proper folder and delete any duplicates
def moveFile(moveFile, downloadDirectory, fileTypes):
    #The file format is what is after the period in the file name
    if "." in moveFile:
        temp = moveFile.split(".")
        fileFormat = temp[-1] 
    else:
        return

    for fileType in fileTypes.keys():
        if fileFormat in fileTypes[fileType]:
            srcPath = downloadDirectory + "\\" + moveFile
            dstPath = downloadDirectory + "\\" + fileType + "\\" + moveFile

            #If the file doesn't have a duplicate in the new folder, move it
            if not os.path.isfile(dstPath):
                os.rename(srcPath, dstPath)
            #If the file already exists with that name and has the same md5 sum
            elif os.path.isfile(dstPath) and \
                 checkSum(srcPath) == checkSum(dstPath):
                os.remove(srcPath)
                print "removed " + srcPath
	    return

#Get md5 checksum of a file. Chunk size is how much of the file to read at a time.
def checkSum(fileDir, chunkSize = 8192):
        md5 = hashlib.md5()
        f = open(fileDir)
        while True:
            chunk = f.read(chunkSize)
            #If the chunk is empty, reached end of file so stop
            if not chunk:
                break
            md5.update(chunk)
        f.close()
        return md5.hexdigest()
		
def main():

    #Dictionary contains file types as keys and lists of their corresponding file formats
    fileTypes = {}
    fileTypes["WTD_M"] = ["jpg", "gif", "png", "jpeg", "bmp"]
    fileTypes["WTD_F"] = ["mp3", "wav", "aiff", "flac", "aac"]
    fileTypes["WTD_C"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", \
                          "MOV", "mp4"]
    fileTypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf"]
    fileTypes["Exe"] = ["exe"]
    fileTypes["Compressed"] = ["zip", "tar", "7", "rar"]
    fileTypes["Virtual_Machine_and_iso"] = ["vmdk", "ova", "iso"]
    
    #The second command line argument is the download directory
    downloadDirectory = sys.argv[1]
    downloadFiles = os.listdir(downloadDirectory)
    makeFolders(downloadDirectory, fileTypes)

    for filename in downloadFiles:
        moveFile(filename, downloadDirectory, fileTypes)

main()