c_banana = {'ara': 4.800,
             'mudas': 6.0,
            'insumos': 5.600,
            'mao_obra': 6.000,
            'energia': 160.0}
p_banana = [3, 500, 1500]

c_abacaxi = {'ara': 4.800,
            'mudas': 2.151,
            'insumos': 7.500,
            'mao_obra': 6200,
            'energia': 187}
p_abacaxi = [5, 1000, 5000]

c_uva ={'ara': 15.000,       
        'mudas': 15.500,     
        'insumos': 14.385,  
        'mao_obra': 17.070,  
        'energia': 2.550 } 
p_uva =[9, 700, 6300] 

c_melancia = {'ara': 14.000,       
             'mudas': 11.500,     
             'insumos': 12.000,   
            'mao_obra': 17.000,  
            'energia': 2.000 }
p_melancia = [2, 1200, 2400]  

c_tangerina = {'ara': 11.000,       
            'mudas': 9.500,     
            'insumos': 10.000,   
            'mao_obra': 12.000,  
            'energia': 1.800 }
p_tangerina = [4, 1300, 5200]


menu = print('''Suas opções são:
                1 - banana
                2 - abacaxi
                3 - uva
                4 - melancia
                5 - tangerina''')

opcao = input("Diga a sua opção de cultivo: ")

hectares = float(input('Digite a quantidade de hectares exigidos:  '))


if opcao == '1':
    custo_totalb = sum(c_banana.values())
    lucroBrutob = p_banana[2] * hectares
    lucroLiquidob = lucroBrutob - custo_totalb
    print(f"O custo total é de {custo_totalb:.3f}, seu lucro bruto é {lucroBrutob:.3f}, o valor final de lucro é {lucroLiquidob:.3f}")

elif opcao == '2':
    custo_totalAb = sum(c_abacaxi.values())
    lucroBrutoAb = p_abacaxi[2] * hectares
    lucroLiquidoAb = lucroBrutoAb - custo_totalAb
    print(f"O custo total é de {custo_totalAb:.3f}, seu lucro bruto é {lucroBrutoAb:.3f}, o valor final de lucro é {lucroLiquidoAb:.3f}")

elif opcao == '3':
    custo_totalUv = sum(c_uva.values())
    lucroBrutoUv = p_uva[2] * hectares
    lucroLiquidoUv = lucroBrutoUv - custo_totalUv
    print(f"O custo total é de {custo_totalUv:.3f}, seu lucro bruto é {lucroBrutoUv:.3f}, o valor final de lucro é {lucroLiquidoUv:.3f}")

elif opcao == '4':
    custo_totalMe = sum(c_melancia.values())
    lucroBrutoMe = p_melancia[2] * hectares
    lucroLiquidoMe = lucroBrutoMe - custo_totalMe
    print(f"O custo total é de {custo_totalMe:.3f}, seu lucro bruto é {lucroBrutoMe:.3f}, o valor final de lucro é {lucroLiquidoMe:.3f}")

elif opcao == '5':
    custo_totalTang = sum(c_tangerina.values())
    lucroBrutoTang = p_tangerina[2] * hectares
    lucroLiquidoTang = lucroBrutoTang - custo_totalTang
    print(f"O custo total é de {custo_totalTang:.3f}, seu lucro bruto é {lucroBrutoTang:.3f}, o valor final de lucro é {lucroLiquidoTang:.3f}")

else:
    print('Erro! Produto não encontrado!')

