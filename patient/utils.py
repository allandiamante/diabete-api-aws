from patient.models import  HRVTime, HRVFreq, HRVNonLinear
from django.db.models import Min, Max, Avg

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


def normalize_datas(HRV):
    # Recupera os valores mínimos e máximos de cada campo numérico
    valores_min = []
    valores_max = []
    valores_avg = []

    for field in HRV._meta.fields[3:]:      
      valores_min.append(HRV.objects.aggregate(Min(field.name)))
      valores_max.append(HRV.objects.aggregate(Max(field.name)))
      valores_avg.append(HRV.objects.aggregate(Avg(field.name)))

    data = HRV.objects.all()
    novos_itens = []
    novo_item = {}
    print(HRV._meta.fields[:3])
    # print(len(data))
    # print(data.values())
    for item in data.values():
      

      for field, valor in item.items():
        novo_item[field + '_normalized'] = valor

        if field in HRV.numeric_fields:

          valor_min = valores_min[HRV.numeric_fields.index(field)][f"{field}__min"]
          valor_max = valores_max[HRV.numeric_fields.index(field)][f"{field}__max"]
          valor_avg = valores_avg[HRV.numeric_fields.index(field)][f"{field}__avg"]

          if( valor != None):
            if valor_max == valor_min:
              # Define o valor normalizado como 0 ou outro valor padrão.
              novo_item[field + '_normalized'] = 0
            else:
              # Normaliza o valor.
              novo_item[field + '_normalized'] = (valor - valor_min) / (valor_max - valor_min)
          else:
            if valor_max == valor_min:
                novo_item[field + '_normalized'] = 0
            else:            
                novo_item[field + '_normalized'] = (valor_avg - valor_min) / (valor_max - valor_min)
      novos_itens.append(novo_item.copy())
    return novos_itens