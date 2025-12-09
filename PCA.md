Planejamento inicial

Trabalho PCA AV2: criar um sistema de cadastro de alunos que permita inserir, consultar, editar e remover dados.

Escolhido Python e a biblioteca Pandas para facilitar o gerenciamento de dados.

Criação do arquivo CSV

Implementada a função para carregar os dados de um arquivo CSV.

Caso o arquivo não exista, o sistema cria um DataFrame vazio com as colunas necessárias.

Criação do DataFrame

Estrutura inicial definida com as colunas:
Matricula, Nome, Rua, Número, Bairro, Cidade, UF, Telefone, Email

Garantia de compatibilidade para salvar e ler dados posteriormente.

Função para gerar matrícula automática

Se o DataFrame estiver vazio, a matrícula inicia em 1.

Caso já existam alunos, a matrícula é incrementada a partir do maior número existente.

Estrutura de dicionário para dados do aluno

Cada aluno é representado como um dicionário

Dados coletados via input() no terminal.

Finalizando a parte da matrícula e iniciando o menu

Matrícula automática testada e funcionando.

Criado esqueleto do menu principal com opções: Inserir, Pesquisar, Editar, Remover, Sair.

Desenvolvimento das funções de menu

Inserir aluno: adiciona registro ao DataFrame e salva no CSV.

Pesquisar aluno: permite buscar por matrícula ou nome.

Editar aluno: altera campos específicos, mantendo os valores não modificados.

Remover aluno: exige confirmação antes de deletar o registro.

Testes e ajustes do menu

Garantido que o menu exibe corretamente todas as opções.

Tratamento de erros implementado: entradas inválidas, matrículas não encontradas, campos obrigatórios.

Validações e detalhes finais

UF convertida para maiúsculas automaticamente.

Busca por nome é case-insensitive (não diferencia maiúsculas e minúsculas).

Mensagens de sucesso e erro implementadas para feedback ao usuário.

Testes finais do programa

Todos os fluxos do menu testados: inserção, pesquisa, edição, remoção.

Arquivo CSV gerado corretamente.

Todas as funcionalidades confirmadas e o código está pronto para uso.