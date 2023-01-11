while True:
    print('***Seja bem vindo ao conversor de unidades!***')
    print('**********************************************')
    print('************Escolha uma opção!****************')
    print('Temperatura -->[1]         comprimento --> [2]')
    print('Moeda -->[3]                      área --> [4]')
    print('                                              ')
    opcao_inicial=input('Insira o número correspondente: ')

    if (opcao_inicial>='1') and (opcao_inicial<='5'):
        break
    else:print('Insira uma opção válida!')



    if opcao_inicial=='1':
        while True:
            recebe_temp=float(input('Insira o valor da temperatura: '))
            print('***Agora você vai escolher a unidade***')
            print('ºC -->[1]      ºF --> [2]      K --> [3]')
            recebe_uni_temp=input('Insira o número correspondente: ')
            
            if recebe_uni_temp=='1':
                temp_K=recebe_temp+273
                temp_F=32+(1.8*recebe_temp)
                print(f'A temperatura de {recebe_temp}ºC corresponde a {temp_F:.4f}ºF e a {temp_K:.4f}K.')
                break
            elif recebe_uni_temp=='2':
                temp_C=((recebe_temp-32)/9)*5
                temp_K=temp_C+273
                print(f'A temperatura de {recebe_temp}ºF corresponde a {temp_C:.4f}ºC e a {temp_K:.4f}K.')
                break
            elif recebe_uni_temp=='3':
                temp_C=recebe_temp-273
                temp_F=(1.8*temp_C)+32
                print(f'A temperatura de {recebe_temp}K corresponde a {temp_F:.4f}ºF e a {temp_C:.4f}ºC.')
                break
            else:
                print('Você digitou um caractere inválido! Tente novamente:')

if opcao_inicial=='2':
   
    while True:
        recebe_comp=float(input('Insira o valor do comprimento: '))
        print('***Agora você vai escolher a unidade***')
        print('m -->[1]      mm --> [2]      cm --> [3]')
        print('        km -->[4]      in --> [5]')
        recebe_uni_comp=input('Insira o número correspondente: ')
        
        if recebe_uni_comp=='1':#entrada em m
            comp_mm=recebe_comp*1000
            comp_cm=recebe_comp*100
            comp_km=recebe_comp/1000
            comp_in=recebe_comp*39.37
            uni_ini='m'
            break
        elif recebe_uni_comp=='2':#entrada em mm
            comp_m=recebe_comp/1000
            comp_cm=recebe_comp/10
            comp_km=recebe_comp/1000000
            comp_in=recebe_comp/25.4
            uni_ini='mm'
            break
        elif recebe_uni_comp=='3':#entrada em cm
            comp_mm=recebe_comp*10
            comp_m=recebe_comp/100
            comp_km=recebe_comp/100000
            comp_in=recebe_comp/2.54
            uni_ini='cm'
            break
        elif recebe_uni_comp=='4':#entrada em km
            comp_mm=recebe_comp*1000000
            comp_cm=recebe_comp*100000
            comp_m=recebe_comp*1000
            comp_in=recebe_comp*39370
            uni_ini='Km'
            break
        elif recebe_uni_comp=='5': #entrada em in
            comp_mm=recebe_comp*25.4
            comp_cm=recebe_comp*2.54
            comp_km=recebe_comp/39370
            comp_m=recebe_comp/39.37
            uni_ini='in'
            break
            
        else:
                print('Você digitou um caractere inválido! Tente novamente:')
         

      

    while True:
        print('***Agora você vai escolher a unidade desejada***')
        print('m -->[1]      mm --> [2]      cm --> [3]')
        print('        km -->[4]      in --> [5]')
        recebe_uni_comp_desejada=input('Insira o número correspondente: ')

        if recebe_uni_comp_desejada=='1':
                print(f'O comprimento de {recebe_comp:.2f}{uni_ini} corresponde a {comp_m:.2f} m.')
                break
        elif recebe_uni_comp_desejada=='2':
                print(f'O comprimento de {recebe_comp:.2f}{uni_ini} corresponde a {comp_mm:.2f} mm.')
                break
        elif recebe_uni_comp_desejada=='3':
                print(f'O comprimento de {recebe_comp:.2f}{uni_ini} corresponde a {comp_cm:.2f} cm.')
                break
        elif recebe_uni_comp_desejada=='4':
                print(f'O comprimento de {recebe_comp:.2f}{uni_ini} corresponde a {comp_km:.2f} km.')
                break
        elif recebe_uni_comp_desejada=='5':
                print(f'O comprimento de {recebe_comp:.2f}{uni_ini} corresponde a {comp_in:.2f} in.')
                break
        else:
                print('Você digitou um caractere inválido! Tente novamente:')
                
if opcao_inicial=='3':

    while True:
        atualiza_moeda=input('Você deseja atualizar o valor das moedas? [sim/nao]: ')
        
        if atualiza_moeda=='sim':
            print('*****O Real Brasileiro é a referência (R$ 1.00)******')
            print('***Agora você vai entrar com os valores das moedas***')
            base_real=1.0
            base_dolar=float(input('Entre com o valor atual do Dólar Americano: '))
            base_euro=float(input('Entre com o valor atual do Euro: '))
            base_libra=float(input('Entre com o valor atual da Libra Esterlina: '))
            print('**********************Operação concluída**********************')
            print('                                                              ')
            break

        elif atualiza_moeda=='nao':
            base_libra=0.16
            base_dolar=0.19
            base_euro=0.18
            base_real=1.0
            break
        
        else:
            print('Digite "sim" ou "nao"!')

    while True:  
        print('                                                   ')
        recebe_moeda=float(input('Insira o valor em dinheiro a ser convertido: '))
        print('                                                   ')
        print('***********Qual é a moeda dessa quantia?************')
        print('Dólar Americano --> [1]      Real Brasileiro --> [2]')
        print('Euro --> [3]                 Libra Esterlina --> [4]')
        print('                                                    ')
        recebe_uni_moeda=input('Insira o número correspondente: ')

        
        if recebe_uni_moeda=='1':#dolar
            euro=(recebe_moeda*base_euro)/base_dolar
            real=(recebe_moeda*base_real)/base_dolar
            libra=(recebe_moeda*base_libra)/base_dolar
            
            uni_ini='$'
            break
        elif recebe_uni_moeda=='2':#real
            euro=(recebe_moeda*base_euro)/base_real
            dolar=(recebe_moeda*base_dolar)/base_real
            libra=(recebe_moeda*base_libra)/base_real
            
            uni_ini='R$'
            break
        elif recebe_uni_moeda=='3':#euro
            real=(recebe_moeda*base_real)/base_euro
            dolar=(recebe_moeda*base_dolar)/base_euro
            libra=(recebe_moeda*base_libra)/base_euro

            uni_ini='€'
            break
        elif recebe_uni_moeda=='4':#libra
            real=(recebe_moeda*base_real)/base_libra
            dolar=(recebe_moeda*base_dolar)/base_libra
            euro=(recebe_moeda*base_euro)/base_libra

            uni_ini='£'
            break
        
        else:
            print('Você digitou um caractere inválido! Tente novamente:')
    while True:       
        print('                                                    ')
        print('*****Agora você vai escolher a Moeda desejada*******')
        print('Dólar Americano --> [1]      Real Brasileiro --> [2]')
        print('Euro --> [3]                 Libra Esterlina --> [4]')
        print('                                                    ')
        recebe_uni_moeda_desejada=input('Insira o número correspondente: ')

        if recebe_uni_moeda_desejada=='1':
            print(f'A quantia de {uni_ini} {recebe_moeda:.2f} corresponde a $ {dolar:.2f}.')
            break
        elif recebe_uni_moeda_desejada=='2':
            print(f'A quantia de {uni_ini} {recebe_moeda:.2f} corresponde a R$ {real:.2f}.')
            break
        elif recebe_uni_moeda_desejada=='3':
            print(f'A quantia de {uni_ini} {recebe_moeda:.2f} corresponde a € {euro:.2f}.')
            break
        elif recebe_uni_moeda_desejada=='4':
            print(f'A quantia de {uni_ini} {recebe_moeda:.2f} corresponde a £ {libra:.2f}.')
            break
            
        else:
            print('Você digitou um caractere inválido! Tente novamente:')
        



                   
    



