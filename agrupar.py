
in_file = "Lotes.txt"
out_file = "lotes2.txt"
linha_especifica = 0
texto = '"OP - Chave";"OP - Número";"OP - Dt.Emissão";"Ins. - Código";"Ins. - Descrição";"Lote / Ordem de produção";"Produtos - Código";"Produtos - Nome Produto";"Produtos - Inf. Lote Movimentos";"Ent. - Nr. Lote"'

search_for = "71371" or "Ins. - Código"
line_num = 0
lines_found = 0

with open(out_file, 'w') as out_f:
    with open(in_file, "r") as in_f:
        for line in in_f:
            line_num += 1
            if search_for in line:
                lines_found += 1
                print("Found '{}' in line {}...".format(search_for, line_num))
                out_f.write(line)
 
        print("Encontrei {} linhas...".format(lines_found))
   

file = open('lotes2.txt', 'r')
lines = file.readlines()
file.close()

lines.insert(linha_especifica, texto + "\n")

file = open('lotes2.txt', 'w')
file.writelines(lines)
file.close()
