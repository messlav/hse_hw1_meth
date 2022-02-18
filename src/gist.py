df = pd.read_csv("s_SRR3824222_1_bismark_bt2_pe.deduplicated.bedGraph", delimiter='\t', skiprows=1, header=None)

plt.figure(figsize=[15, 10])

plt.hist(df[3], bins=100, density=True)

plt.title('Распределение метилирования цитозинов Epiblast', fontsize=10)
plt.show()
