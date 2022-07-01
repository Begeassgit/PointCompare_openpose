# PointCompare_openpose
a single Python script (or project in the future) for comparing the different point angles between different pictures.
## Notice
* To analyse the angle, you need to output a JSON file, which is output from openpose
* You need a JSON file (usually called angle.json) to save the angles that you want to calculate
### More informations about output
https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/02_output.md
### Some examples
* JSON files usually have some data like:
```
{"version":1.3,"people":[{"person_id":[-1],
    "pose_keypoints_2d":["point data ....."],
    "face_keypoints_2d":[],
    "hand_left_keypoints_2d":[],
    "hand_right_keypoints_2d":[],
    "pose_keypoints_3d":[],
    "face_keypoints_3d":[],
    "hand_left_keypoints_3d":[],
    "hand_right_keypoints_3d":[]}],
    "part_candidates":[{"0":[137.963,126.925,0.792984],"1":[201.923,153.329,0.577929],
        "2":[217.187,149.119,0.457619],"3":[193.626,238.075,0.910687],
        "4":[126.932,263.079,0.786809],"5":[185.252,158.847,0.623371],
        "6":[124.154,247.776,0.84867],"7":[82.465,264.423,0.791976],
        "8":[279.712,264.425,0.467731],"9":[293.607,268.584,0.390299],
        "10":[172.771,297.8,0.622025,246.395,336.673,0.26257],
        "11":[194.935,415.788,0.744108],"12":[267.614,260.286,0.432985],
        "13":[172.737,306.13,0.0513543,140.849,328.38,0.809349],
        "14":[139.391,431.111,0.714025],"15":[],"16":[138.022,115.845,0.932685],
        "17":[],"18":[158.806,115.794,0.898122],"19":[100.514,449.15,0.460775],
        "20":[107.485,450.568,0.486681],"21":[217.295,426.87,0.0516792,149.164,439.452,0.599773],
        "22":[163.049,426.989,0.419062],"23":[168.576,424.189,0.352371],"24":[206.149,421.405,0.65861]}]}
```
### Run compare.py only
* To run the compare.py, you need to output a JSON file, which is output from openpose
* You need a JSON file (usually called angle.json) to save the angles that you want to calculate
* And to customize JSON file, you should change the code in this place (in compare.py, under the if__name__==.....)
```
result=saveResultToDict('your path','angle.json')
standard=saveResultToDict('your path','angle.json')
```
### Run evaluation.py
* This python file can compare the different between some key frames come from the video and some standard images
* You can get key frames use this project
### A github project to finish key frames extraction:
https://github.com/amanwalia123/KeyFramesExtraction
* You can use openpose to process key frames to get the JSON files and result images
* After get the JSON files and result images, you need to process the standard images by openpose to get JSON files as standard JSON files (if you already have some JSON files, you can skip this step)
### Process some key frame images
```
    openpose_path="D:\openpose-1.7.0 gpu\openpose\\"
    data_path=".\PointCompare_openpose\\frame\\"
    resultJson_path=".\PointCompare_openpose\\json\\"
    resultImage_path=".\PointCompare_openpose\\result_img\\"
    
    startAnalyse(openpose_path,data_path,resultJson_path,resultImage_path)
```
* paramter meaning
 openpose_path: openpose release file root (GPU recommended)
 you can get it though: https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases
 you need make sure the program can find the path of folder (bin) under it
* data_path: to save key frame images in this path
* resultJson_path: to JSON files related key frame images in this path
* resultImage_path: to save result images in this path

* startAnalyse(openpose_path,data_path,resultJson_path,resultImage_path) ---- to call openposedemo.exe through the shell
* not support the linux yet (will finish it by openpose python api)

### Evaluate some images
```
dict=compareJson(JSON PATH,Standard JSON PATH,Angle JSON PATH)
toEvaluation(dict)
```
### Result
* result for each JSON file by compared with standard will like:
```
------Finish Data Preprocess------
------Finish Data Preprocess------
--------------角度结果(angle result)---------------
{0: 106.30489867166193, 1: 172.13999140218203, 2: 89.32737480862963, 3: 77.97339528710519, 4: 130.21846414372092, 5: 144.12570362987137, 6: 140.61387604194263, 7: 136.7694992629127, 8: 42.45397874826594, 9: 69.67496258866323, 10: 133.56493920205568, 11: 67.64922633931246, 12: 149.83759507316927}
------------标准角度结果(standard result)--------------
{0: 132.0932267767729, 1: 44.476266743386184, 2: 3.201976453022322, 3: 173.4314705473779, 4: 140.88479543841532, 5: 167.54312809184162, 6: 140.52671241693534, 7: 74.1230118745824, 8: 88.10172507384806, 9: 112.58233685255657, 10: 172.20390234661673, 11: 146.69709010387672, 12: 112.88838189623857}
----------------RESULT--------------
角度评价分数(angle evaluation score)：0.5914060536979144
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
1.0
```
