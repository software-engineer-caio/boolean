# Construindo a logica do not

var_1 = True
var_2 = False

print('var_1 {} quando negada fica {}'.format(var_1, not var_2))
print('var_2 {} quando negada fica {}'.format(var_2, not var_1))

# Construindo a logica do AND {E}

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

print('Quando var_1_t é {} E var_2_t {} o resultado é {}'.format(var_1_t,var_2_t,var_1_t and var_2_t))
print('Quando var_1_f é {} E var_2_t {} o resultado é {}'.format(var_1_f,var_2_t,var_1_f and var_2_t))
print('Quando var_1_t é {} E var_2_f {} o resultado é {}'.format(var_1_t,var_2_f,var_1_t and var_2_t))
print('Quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f and var_2_t))


#Construindo a logica do OR (OU)

print('Quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f or var_2_t))
print('Quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f or var_2_t))
print('Quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f or var_2_t))
print('Quando var_1_f é {} E var_2_f {} o resultado é {}'.format(var_1_f,var_2_f,var_1_f or var_2_t))

#Multiplas regras de logica

var_1_t = True
var_1_f = False
var_2_t = True
var_2_f = False

var_resultado = ((var_1_t and var_2_f) or ((var_1_f or var_2_t) and (not var_2_f)))
print('O resultado da logica é {}'.format(var_resultado))


var_a_t = False
var_b_t = True
# T T = FALSE
# T F = TRUE
# F F = False
# F T = True
var_s = (not var_a_t and var_b_t) or (not var_b_t and var_a_t)
print ('O resultado da logica do exercicio é {}'.format(var_s))
