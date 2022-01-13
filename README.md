# Where's Wally? 
### A live-version game with drones and Yolov5

Members
---

- 0710809 侯俊宇(ECE) [Github](https://github.com/jerry8137)
- 0710851 洪愷尹(ECE) [Github](https://github.com/KaiYin77)

How to run
---
1. Environment
    ```  bash=
    conda env create -f environment.yml
    ```
2. Training stage 
    ```bash=
    #Train custom data for Yolov5
    python train.py --img 640 
                    --batch 16 
                    --epochs 20 
                    --data dataset.yaml 
                    --weights yolov5s.pt
    ```
3. Run Where's Wally 
    ```bash=
    #Connect server's wifi to Drone & Run
    python run_wally.py
    ```

Demo
---
![](https://i.imgur.com/rWjpbMr.jpg)


Framework
---
![](https://i.imgur.com/Z2lPyJE.jpg)

Issue
---
- 1 Label issue : In Model Training Stage
    - ISSUE
        - First label whole body not only red white stripe shirt.
        - Model performs bad → Detect human not only wally.
        - ![Imgur](https://im5.ezgif.com/tmp/ezgif-5-984026a6ae.gif)
    - Solution
        - Re-label and focus on red-white stripe shirt!
        - Let model learn shirts’ feature specifically
        - ![](https://i.imgur.com/N9ocQ93.png)
        - ![](https://im5.ezgif.com/tmp/ezgif-5-b260a19f37.gif)
- 2. PID’s parameter tuning
    - ISSUE
        - There are four sets of PID’s pararmeters need to tune.
    - Human tuning
            1. 先調Kp讓震幅起來
            2. 再調Ki讓error趨近於零
            3. 最後Kd讓曲線smooth
    ![https://upload.wikimedia.org/wikipedia/commons/3/33/PID_Compensation_Animated.gif](https://upload.wikimedia.org/wikipedia/commons/3/33/PID_Compensation_Animated.gif)
    - Experience process
        - 可以觀察到最後的結果是在零附近做震盪！
        - 以下為實驗過程中的參數error變化

            | error_1 | error_2 | error_3 | error_4 | 
            | -------- | -------- | -------- | ------- |
            | x:left/right   | y:up/down     | z:forward/backward    |yaw    |

- 1.![](https://i.imgur.com/2fnW2q8.png)
- 2.![](https://i.imgur.com/WWYAl01.png)
- 3.![](https://i.imgur.com/gcFdEXf.png)

Future work
---
- Short-term
    1. Better Tracking logic.
    2. Improve model's stability.
    3. Fine-tune PID's parameters.
- Long-term
    1. Build outdoor version.
    2. Combine multiple drones to find Wally.
    3. Build interaction behavior between drones and Wally. 
