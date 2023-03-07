print('\033[34mEsse é um programa para converter metros em centímetros e milímetros.\033[m ')
m = float(input('\033[30mMetros:\033[m'))
cm = m * 100
mm = cm * 10
print('\033[34mVocê tem\033[m'
      '\033[33m {}cm\033[m '
      '\n\033[34mE\033[m \033[33m{}mm\033[m'.format(cm, mm))