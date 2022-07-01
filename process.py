import json
import math


def readFile(name):
    with open(name,'r') as json_file:
        json_data=json.load(json_file)
        return json_data
   
def dataProcess(data):
    data_after={}
    for x in range(0,15):
        data_after[x]=data['part_candidates'][0][str(x)][0:2]
    #将part_candidates的数据放入新字典data_after 数据只存坐标
    #数据只采集到关键点14 去除15至24
    print("------Finish Data Preprocess------")
    return data_after

def calculateAngle(data,point_one,point_two,point_three,result_angle):
    """
    根据三点坐标计算夹角
    :param point_one 点1
    :param point_two 点2
    :param point_three 点3
    :param result_angle 选择结果角
    """
    print("------所算坐标点为------")
    print(data[point_one][0],data[point_one][1])
    print(data[point_two][0],data[point_two][1])
    print(data[point_three][0],data[point_three][1])

    side_a=math.sqrt((data[point_two][0] - data[point_three][0])*
    (data[point_two][0] - data[point_three][0])+
    (data[point_two][1] - data[point_three][1])*
    (data[point_two][1] - data[point_three][1]))

    side_b=math.sqrt((data[point_one][0] - data[point_three][0])*
    (data[point_one][0] - data[point_three][0])+
    (data[point_one][1] - data[point_three][1])*
    (data[point_one][1] - data[point_three][1]))

    side_c=math.sqrt((data[point_one][0] - data[point_two][0])*
    (data[point_one][0] - data[point_two][0])+
    (data[point_one][1] - data[point_two][1])*
    (data[point_one][1] - data[point_two][1]))

    
    if(result_angle==1):
        angle_one=math.degrees(math.acos((side_a*side_a-side_b*side_b-side_c*side_c)/(-2*side_b*side_c)))
        result=angle_one
    elif(result_angle==2):
        angle_two=math.degrees(math.acos((side_b*side_b-side_a*side_a-side_c*side_c)/(-2*side_a*side_c)))
        result=angle_two
    else:
        angle_three=math.degrees(math.acos((side_c*side_c-side_a*side_a-side_b*side_b)/(-2*side_a*side_b)))
        result=angle_three
    return result

def saveResultToDict(file,angle_file):
    point_data=dataProcess(readFile(file))
    angle_list=readFile(angle_file)['angleList']
    angle_result={}
    key=0
    for value in angle_list:
        angle_result[key]=(calculateAngle(point_data,angle_list[value][0],angle_list[value][1],angle_list[value][2],2))
        key=key+1
    return angle_result

def compareKey(angle_data,angle_standard):
    different_count=0
    for count in range(0,13):
        if(((angle_data[count]-angle_standard[count])>=5.0) or ((angle_data[count]-angle_standard[count])<=-5.0)):
            different_count=different_count+1
    evaluate_percentage=different_count/13
    print("----------------RESULT--------------")
    print("角度不一致率："+ str(evaluate_percentage))


if __name__=="__main__":
    print("------计算比对图------")
    result=saveResultToDict('json/512-1.json','angle.json')
    
    print("------------------------------------------")
    print("------------------------------------------")

    print("------计算标准图------")
    standard=saveResultToDict('json/512.json','angle.json')

    print("--------------角度结果---------------")
    print(result)
    print("------------标准角度结果--------------")
    print(standard)
   
    compareKey(result,standard)

