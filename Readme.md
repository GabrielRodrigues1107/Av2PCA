# Sistema de Cadastro de Alunos 📝

**Trabalho prático AV2**  
Matéria: Princípios de Construção de Algoritmos (PCA)

**Alunos:**  
- Gabriel Rodrigues – matrícula: 06014806  
- Pedro Henrique Pimentel– matrícula: 06014147 

---

## Descrição

Sistema de gestão de registros de estudantes criado em **Python** com a biblioteca **Pandas**.  
Permite registrar, consultar, modificar e excluir dados de alunos, salvando as informações em um arquivo CSV.

---

## Finalidade

O sistema elimina a necessidade de gerenciar manualmente os registros dos alunos, oferecendo:  
- Registro automatizado com criação de matrícula sequencial  
- Armazenamento duradouro em arquivo CSV  
- Busca eficaz por nome ou matrícula  
- Interface simples e intuitiva pelo terminal  
- Edição seletiva de campos específicos  
- Remoção segura com verificação  

---

## Dados Armazenados

O sistema guarda as seguintes informações por estudante:  
- Matrícula (gerada automaticamente)  
- Nome completo  
- Endereço completo: rua, número, bairro, cidade e estado  
- Telefone  
- E-mail  

---

## Pré-requisitos

- Python instalado  
- Biblioteca Pandas  

---

## Instalação das Dependências

Instale a biblioteca Pandas:  

```bash
pip install pandas
