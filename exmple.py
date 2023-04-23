import os 
import csv
import sys
import argparse

#Input agrument function pending

input_dir = "D:\\New_task\\SDD_Toolchain\\sw.sys.chorus_main_doxygen_reports\\mc_sw"
output_dir= "D:\\New_task\\output_dir"

def collect_path(input_dir):
    collect_xml_path = []
    print(input_dir)
    print(output_dir)
    for root,dir,file_name in os.walk(input_dir):
        # print("Root Directory",root)
        # print("Parent Directory",dir)
        if 'xml' in root:
            collect_xml_path.append(root)
    # print("List of xml paths",collect_xml_path)
    return collect_xml_path
 

def store_path(xml_path_list):
    #In this function we write logic to data in csv  
    with open('component_list.csv','w+',newline='') as csv_file:
        writer = csv.writer(csv_file)
        components=["Components"]
        writer.writerow(components)
        for items in xml_path_list:
            writer.writerow([items])
    
# calling collect_path function 
xml_path_list = collect_path(input_dir)

store_path(xml_path_list)
print("<-- Script Run Sucessfully -->")