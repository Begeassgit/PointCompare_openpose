import os
import compare
import subprocess


def loadAllJSONFileName(dir_path,flag):
    filename=os.listdir(dir_path)
    if flag==True:
        filename.remove('plot_keypoints.json')
    print(filename)
    return filename

def startAnalyse(openpose_path,data_path,resultJson_path,resultImage_path):
    shell_run=".\\bin\OpenPoseDemo.exe --image_dir "+ data_path + \
            " --write_json "+ resultJson_path + \
            " --write_images "+ resultImage_path +\
            " --net_resolution 320x160 --part_candidates true"
    process=subprocess.Popen(shell_run,cwd=openpose_path,shell=True,stdout=subprocess.PIPE,encoding="GBK")
    process.communicate()

def compareJson(data_path,standard_path,angle_path):
    data_files=loadAllJSONFileName(data_path,True)
    standard_files=loadAllJSONFileName(standard_path,False)
    compare_result={}
    compare_temp=[]
    key=0
    for standard in standard_files:
        compare_temp.clear()
        compare_result[key]=compare_temp
        key=key+1
        for data in data_files:
            compare_temp.append(compare.toCompare(data_path+"/"+data,standard_path+"/"+standard,angle_path))
        
    return compare_result

def toEvaluation(result_dict):
    number=[]
    for list in result_dict.values():
        number.append(max(list))
    print(number)
    final_evaluation=0
    for value in number:
        final_evaluation=final_evaluation+value
    final_evaluation=final_evaluation/len(number)
    print(final_evaluation)


if __name__=="__main__":

    print("In put a number to select a function")
    print("1-----key frame excavation")
    print("2-----evaluation")
    
    select_func=input()
    if select_func==1:
        openpose_path="D:\openpose-1.7.0 gpu\openpose\\"
        data_path=".\PointCompare_openpose\\frame\\"
        resultJson_path=".\PointCompare_openpose\\json\\"
        resultImage_path=".\PointCompare_openpose\\result_img\\"
    
        startAnalyse(openpose_path,data_path,resultJson_path,resultImage_path)
    else:
        dict=compareJson("json","standard","angle.json")
        toEvaluation(dict)
    
