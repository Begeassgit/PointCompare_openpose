# PointCompare_openpose
a single Python script (or project in the future) for comparing the different point angles between different pictures.
## Notice
* To run the process.py, you need to output a JSON file, which is output from openpose
* You need a JSON file (usually called angle.json) to save the angles that you want to calculate
### More informations about output
https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/02_output.md
## Some examples
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
* and to customize JSON file, you should change the code in this place
```
result=saveResultToDict('512-1.json','angle.json')
```

### add a github project to finish key frames extraction:
https://github.com/amanwalia123/KeyFramesExtraction
