# hse_hw1_meth

## 1
Взял отчет RNA из старого ДЗ и SRR5836473_1
SRR5836473_1            |  RNA
:-------------------------:|:-------------------------:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2020.59.52.png)  |  ![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.06.png)

SRR5836473_1            |  RNA
:-------------------------:|:-------------------------:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2020.59.52.png)  |  ![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.26.png)

SRR5836473_1            |  RNA
:-------------------------:|:-------------------------:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.01.07.png)  |  ![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.58.png)

## 2
### a
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2016.37.32.png)
### b
bash script
```
!ls *pe.bam | xargs -P 4 -tI{} deduplicate_bismark  --bam  --paired  -o s_{} {}
```
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2016.53.53.png)
### c
2 часа ок
### d
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.23.02.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.23.45.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.23.56.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.24.05.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.24.14.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.24.22.png)

