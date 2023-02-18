
def ret_initials(subject_name):  
    remover_palavras  = ['da', 'de', 'do' ]
    lista_frase = subject_name.split()
    result = [palavra for palavra in lista_frase if palavra.lower() not in remover_palavras]
    retorno = ' '.join(result)
    subject_name = retorno.split(' ')
    initials = ''
    for i in subject_name:
        initials = initials + i[0].upper()
    print(initials)
    return initials

def calc_bmi(weight, height):
    if(weight and height != 0):
        return (weight / (height * height) )
    else:
        return 0 

def calc_raiz_q(x):
    return x ** (1/2)

def calc_bsa(weight, height):
    cm = 100
    if(weight and height != 0):
        return calc_raiz_q((height * cm ) * weight / 3600)
    else:
        return 0 
    
#pensar saida caso não inserida no formulario os parametros de entradas, ja q eles não sao obrigatorio
def calc_sbp_dbp(empe, repous):
    if(empe or repous !=  None):            
        return (empe - repous)
    else: 
        return 0

def calc_postural_drop(sbp_chambe, dbp_chambe):
    if(sbp_chambe > 20 or dbp_chambe > 10):
        return True
    else:
        return False

def normalize_data(obj):
    # obtém os valores mínimo e máximo para cada campo
    valores = MeuModelo.objects.aggregate(*[Min(field) for field in MeuModelo._meta.fields], *[Max(field) for field in MeuModelo._meta.fields])
    
    # cria um novo objeto normalizado
    obj_normalizado = MeuModelo()
    for field in MeuModelo._meta.fields:
        # obtém o valor atual do campo e o valor mínimo e máximo para normalização
        valor_atual = getattr(obj, field.name)
        min_valor = valores[field.name + '__min']
        max_valor = valores[field.name + '__max']
        
        # normaliza o valor do campo
        valor_normalizado = (valor_atual - min_valor) / (max_valor - min_valor)
        
        # define o valor normalizado no novo objeto
        setattr(obj_normalizado, field.name, valor_normalizado)

    return obj_normalizado


    