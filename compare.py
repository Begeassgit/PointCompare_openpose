import json
import math


def readFile(name):
    with open(name,'r') as json_file:
        json_data=json.load(json_file)
        return json_data
   
def dataProcess(data):
    data_after={}
    data_temp_accurate={}

    """ abandon
    if len(data['part_candidates'][0]['0'])==0:
        if len(data['part_candidates'][0]['17'])==0:
            point17=[0,0]
        else:
            point17=data['part_candidates'][0]['17'][0:2]
    
        if len(data['part_candidates'][0]['18'])==0:
            point18=[0,0]
        else:
            point18=data['part_candidates'][0]['18'][0:2]

        x_0=(point17[0]+point18[0])/2.0
        y_0=(point17[1]+point18[1])/2.0

        data_after[0]=[x_0,y_0]
    else:
        data_after[0]=data['part_candidates'][0]['0'][0:2]
    """
    
    for x in range(0,15):
        if len(data['part_candidates'][0][str(x)])>3:
            data_temp_accurate=data['part_candidates'][0][str(x)][2::3]
            accurate=max(data_temp_accurate)
            position=data['part_candidates'][0][str(x)].index(accurate)
            data_after[x]=[data['part_candidates'][0][str(x)][position-2],data['part_candidates'][0][str(x)][position-1]]
        elif len(data['part_candidates'][0][str(x)])==0:
            data_after[x]=[0,0]
        else:
            data_after[x]=data['part_candidates'][0][str(x)][0:2]

    """ abandon
    for x in range(1,15):
        if len(data['part_candidates'][0][str(x)])==0:
            data_after[x]=[0,0]
        else:
            data_after[x]=data['part_candidates'][0][str(x)][0:2]
    """
    
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
    """
    print("------所算坐标点为------")
    print(data[point_one][0],data[point_one][1])
    print(data[point_two][0],data[point_two][1])
    print(data[point_three][0],data[point_three][1])
    """
    

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
    evaluate_percentage=0
    evaluate_number=[]
    for count in range(0,13):
        if(((angle_data[count]-angle_standard[count])>=45.0) or ((angle_data[count]-angle_standard[count])<=-45.0)):
            evaluate_number.append(0.0)
        else:
            evaluate_number.append((angle_standard[count]-abs(angle_data[count]-angle_standard[count]))/angle_standard[count])
    for number in evaluate_number:
        evaluate_percentage=evaluate_percentage+number
    evaluate_percentage=evaluate_percentage/13
    print("----------------RESULT--------------")
    print("角度评价分数："+ str(evaluate_percentage))

    return evaluate_percentage

def toCompare(image_json,standard_json,angle_json):
    """
    parameter order: data,standard,angle
    """
    result=saveResultToDict(image_json,angle_json)
    standard=saveResultToDict(standard_json,angle_json)
    print("--------------角度结果---------------")
    print(result)
    print("------------标准角度结果--------------")
    print(standard)
    return compareKey(result,standard)
    


if __name__=="__main__":
    print("------计算比对图------")
    result=saveResultToDict('json/frame_132_keypoints.json','angle.json')
    
    print("------------------------------------------")
    print("------------------------------------------")

    print("------计算标准图------")
    standard=saveResultToDict('standard/000000000108_keypoints.json','angle.json')

    print("--------------角度结果---------------")
    print(result)
    print("------------标准角度结果--------------")
    print(standard)
   
    compareKey(result,standard)

