# -*- coding: utf-8 -*-

from source.libs.born_generator import BornGen
from source.libs.gera_nome import GeraNome
from source.libs.validacpf_kleyton import ValidaCPF
import csv


class MassGen:

    def gen_10k(self):

        with open('./registros.csv', 'w') as reg:
            writer_reg = csv.writer(reg, delimiter=';')

            [writer_reg.writerow([GeraNome().nomeCompleto, BornGen().dt_nasc,
                                  ValidaCPF().gera_cpf()]) for _ in range(10000)]


if __name__ == '__main__':
    MassGen().gen_10k()
