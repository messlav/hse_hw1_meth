# hse_hw1_meth

## 1
Взял отчет RNA из старого ДЗ и SRR5836473_1
SRR5836473_1            |  RNA
:-------------------------:|:-------------------------:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2020.59.52.png)  |  ![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.06.png)


На картинках видно, что к концу секвенирования метилирования резко падает quality score, значит что-то происходит с ридами.



SRR5836473_1            |  RNA
:-------------------------:|:-------------------------:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.19.png)  |  ![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.26.png)

Как ми мидим у RNA график имеет нормальное распределение, которое является для него теоретическим. У метилированого же с графиком все плохо

SRR5836473_1            |  RNA
:-------------------------:|:-------------------------:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.01.07.png)  |  ![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.00.58.png)

Дупликаций у метилированого первого уровня - почти все, в отличии от RNA, у которого график более равномерно распределен
## 2
colab https://colab.research.google.com/drive/10j6JGdhSrv4vZQ9GDwwH8SQehlR84Exp?usp=sharing
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

На всех графиках изображены проценты CpG мелитирования:
Epiblast - 74%
8Cell - 45%
ICM - 25%
### e
code for one
```
df = pd.read_csv("s_SRR3824222_1_bismark_bt2_pe.deduplicated.bedGraph", delimiter='\t', skiprows=1, header=None)

plt.figure(figsize=[15, 10])

plt.hist(df[3], bins=100, density=True)

plt.title('Распределение метилирования цитозинов Epiblast', fontsize=10)
plt.show()
```
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.25.30.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.25.36.png)
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/Снимок%20экрана%202022-02-18%20в%2021.25.42.png)

Наверное, единственный вывод, который можно сделать это то что для каждоого образца процент процент метилированных цитозинов и частота зависят по-разному. В первом и третьем образце чаще всего метилируется 0%, что не очень хорошо, т.к. метилирование принимает участие в экспрессии гена. При этом второй образец метилируется чаще всего 100%

### f
Покрытие:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/image_cov.png)
Метилирование:
![](https://github.com/messlav/hse_hw1_meth/blob/main/images/image_cov2.png)
