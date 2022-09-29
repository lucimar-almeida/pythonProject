using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
namespace ExemploClasses
{
    class cliente
    {
        // 1. Atributos da classe
        private String nome;
        private int codigo;
 
        // 2. Métodos construtores
        public Cadastro() {}
 
        public Cadastro(int cpf, int cnpj)
        {
            this.Cpf = cpf;
            this.Cnpj = cnpj;
        }
 


        //3. Métodos acessores
        public void setNome(String nome)
        {
            this.nome = nome;
        }
 
        public String getNome()
        {
            return this.nome;
        }
 
        public void setCodigo(int codigo)
        {
            this.codigo = codigo;
        }
 
        public String getRg()
        {
            return this.rg;
        }
 
        public void setIdade(int idade)
        {
            this.idade = idade;
        }
 
        public int getIdade()
        {
            return this.idade;
        }
    }
}