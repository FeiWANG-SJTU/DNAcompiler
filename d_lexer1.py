#generate token stream
def d_lex(characters):
    reserved=['==','=','(',')',';','+','-','*','/','<=','>=','!=',':',\
              '<','>','and','or','xor','not','nand','nor','xnor','for','while','if','else']
    chas=characters.split()
    tokens=[]
    for cha in chas :
        if cha in reserved: # if a reserved word 如果是保留字
            tokens.append([cha,'reserved'])
        elif cha.isdigit(): # if a number 如果是数字
            tokens.append(['num',cha])
        else :   #if a variable 如果是变量
            tokens.append(['id',cha])
    return tokens
            
