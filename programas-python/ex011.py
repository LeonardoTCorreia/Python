print('Vou te ajudar a pintar sua parede camarada!')
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m²'.format(largura, altura, area))
print('Será necessário {:.4f}l de tinta para pintar a parede!'.format(tinta))
