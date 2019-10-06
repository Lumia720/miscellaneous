# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 12:01:41 2018
#19 column 0 is number of wtd
#4 row starts list of jpegs
@author: ttl80
"""
import os
import xlrd
import shutil

def makeFolders(file_dir, fileTypes):
    for fileType in fileTypes:
        directory = file_dir + "/Training/" + fileType
        
        if not os.path.exists(directory):
            os.mkdir(directory)

#Moves file to its proper folder and delete any duplicates
def moveFile(moveFile, file_direc_old, file_direc_new, n):
    srcPath = file_direc_old + "/" + moveFile
    dstPath = file_direc_new + "/" + str(n) + moveFile
    if os.path.isfile(srcPath):
        if not os.path.isfile(dstPath):
            shutil.copy2(srcPath, dstPath)

    #If the file doesn't have a duplicate in the new folder, move it
    
    
            #If the file already exists with that name and has the same md5 sum
    
def main():
    file_location = "H:/2018/WhiteTailedDeer/Loimaa_2017.xlsx"
    file_dir = "H:/2018/WhiteTailedDeer"
    workbook = xlrd.open_workbook(file_location)
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0,0)
    print(sheet.cell_value(0,0))
    print(sheet.nrows)
    for col in range(sheet.ncols):
        print(sheet.cell_value(0,col))
    fileTypes = {"WTD_M","WTD_F","WTD_C","WTD_Un", "WTD_Multiple", "Empty","Moose", "Human", "Raccoon", "Badger", "Roe", "Undef", "Fox", "Dog", "Cat", "Bird", "Rabbit"}
    makeFolders(file_dir, fileTypes)        
    # first check if there is a raindeer
    # if it ONE  then split all picture with one reinderr into folders of gender and age
    # esle, send the photo to multiple folder
    # else = If there is  no reindeer, check if the image is empty
    # else if the image is not empty, send the image into a cathegory it belongs to
    for nro in range(3,sheet.nrows):
        s = sheet.cell_value(nro,0)
        a,ncam = s.split('CAM', 1)
        if sheet.cell_value(nro,18):
            if float(sheet.cell_value(nro, 18)) == 1:
                if float(sheet.cell_value(nro, 20)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"WTD_C", ncam) 
                if float(sheet.cell_value(nro, 22)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"WTD_F", ncam)
                if float(sheet.cell_value(nro, 23)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"WTD_M", ncam)
                if float(sheet.cell_value(nro, 21)) > 0 or float(sheet.cell_value(nro, 24)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"WTD_Un", ncam)
            else:
                moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"WTD_Multiple", ncam) 
        else:
            if sheet.cell_value(nro,17): moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Empty", ncam)
            else:
                if float(sheet.cell_value(nro, 16)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Undef", ncam) 
                if float(sheet.cell_value(nro, 15)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Roe", ncam) 
                if float(sheet.cell_value(nro, 14)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Raccoon", ncam) 
                if float(sheet.cell_value(nro, 13)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Rabbit", ncam) 
                if float(sheet.cell_value(nro, 12)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Moose", ncam) 
                if float(sheet.cell_value(nro, 11)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Human", ncam) 
                if float(sheet.cell_value(nro, 9)) > 0:  moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Dog", ncam) 
                if float(sheet.cell_value(nro, 8)) > 0:  moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Cat", ncam) 
                if float(sheet.cell_value(nro, 7)) > 0:  moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Bird", ncam) 
                if float(sheet.cell_value(nro, 6)) > 0:  moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Badger", ncam) 
                if float(sheet.cell_value(nro, 10)) > 0: moveFile(sheet.cell_value(nro, 1), file_dir +  "/9/2017/"+str(ncam), file_dir +  "/Training/" +"Fox", ncam) 
    print("ready")
    
main()