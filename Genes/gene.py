import pandas as pd
from tabulate import tabulate
#pip install pandas
#pip install openpyxl
#pip install tabulate

#all_PCOS= pd.read_excel('C:\\Users\\Souvik\\Downloads\\ALL.PCOS.xlsx')
all_PCOS= pd.read_excel('ALL.PCOS.xlsx')
all_PCOS = all_PCOS['Genes of PCOS'].tolist()

#vaginal = pd.read_excel('C:\\Users\\Souvik\\Downloads\\vaginal.genes.disgenet.xlsx')
vaginal = pd.read_excel('vaginal.genes.disgenet.xlsx')
vaginal = vaginal['Genes'].tolist()

#uterine = pd.read_excel('C:\\Users\\Souvik\\Downloads\\uterine.genes.disgenet.xlsx')
uterine = pd.read_excel('uterine.genes.disgenet.xlsx')
uterine = uterine['Uterine'].tolist()

#ovarian = pd.read_excel('C:\\Users\\Souvik\\Downloads\\ovarian.genes.disgenet.xlsx')
ovarian = pd.read_excel('ovarian.genes.disgenet.xlsx')
ovarian = ovarian['Ovarian'].tolist()

#fallopian = pd.read_excel('C:\\Users\\Souvik\\Downloads\\Fallopiantube.genes.disgenet.xlsx')
fallopian = pd.read_excel('Fallopiantube.genes.disgenet.xlsx')
fallopian = fallopian['Fallopian'].tolist()

#endometrial = pd.read_excel('C:\\Users\\Souvik\\Downloads\\endometrial.genes.disgenet.xlsx')
endometrial = pd.read_excel('endometrial.genes.disgenet.xlsx')
endometrial = endometrial['Endometrial'].tolist()

#cervical = pd.read_excel('C:\\Users\\Souvik\\Downloads\\cervical.genes.disgenet.xlsx')
cervical = pd.read_excel('cervical.genes.disgenet.xlsx')
cervical = cervical['Cervical'].tolist()



for gene in all_PCOS:
    if gene in vaginal:
        vag = 1
    else:
        vag = 0

    if gene in uterine:
        utr = 1
    else:
        utr = 0

    if gene in ovarian:
        ova = 1
    else:
        ova = 0

    if gene in fallopian:
        fall = 1
    else:
        fall = 0

    if gene in endometrial:
        end = 1
    else:
        end = 0

    if gene in cervical:
        cer = 1
    else:
        cer = 0


    if(vag == utr == ova == fall == end == cer == 0 ):
        continue
    else:
        temp_list = [gene, vag, utr, ova, fall, end, cer]
        print(tabulate([temp_list],
                   headers=['Gene', 'Vaginal', 'Uterine', 'Ovarian', 'Fallopian', 'Endometrial', 'cervical']))
