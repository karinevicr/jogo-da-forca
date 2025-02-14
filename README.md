## Introdução

&nbsp;&nbsp;&nbsp;&nbsp;Este projeto tem como propósito o mapeamento de requisitos funcionais de um jogo da velha. O principal objetivo desta atividade é verificar e testar os conhecimentos em GitFlow.

&nbsp;&nbsp;&nbsp;&nbsp;Para acessar a atividade, é necessário acessar o link do repositório. Você pode encontrar esse link aqui: [Repositório no GitHub](https://github.com/karinevicr/jogo-da-forca.git)

## Levantamento de Requisitos

&nbsp;&nbsp;&nbsp;&nbsp;Os requisitos para o jogo da velha online estão detalhados no arquivo `Requisitos_Forca.md`. Este documento contém os requisitos funcionais e não funcionais do sistema.

## Histórico GitFlow

&nbsp;&nbsp;&nbsp;&nbsp;Abaixo se encontram maiores detalhes do processo de versionamento dos códigos.

### Padrão de Nomenclatura das Branches:

- **main**: Contém o código estável e pronto para produção. Somente código testado e aprovado deve ser mergeado aqui.
- **develop**: Branch de integração contínua, onde todas as novas funcionalidades e correções são mescladas antes de serem liberadas para produção.
- **feat/[nome-da-feature]**: Utilizada para o desenvolvimento de novas funcionalidades. Exemplo: `feat/requisitos-funcionais`.
- **bugfix/[nome-do-bug]**: Utilizada para correção de bugs. Exemplo: `bugfix/corrige-requisito-funcional`.
- **docs/[nome-da-documentação]**: Utilizada para documentação de alguma parte do projeto nos arquivos .md. Exemplo: `docs/adiciona-introdução`.

&nbsp;&nbsp;&nbsp;&nbsp;É importante frisar que no processo de GitFlow existem outras nomenclaturas de branches, porém, especificamente nesse projeto, foram adotadas somente essas. Caso deseje saber mais sobre políticas e criação de branches, você pode consultar este [link](https://fga-eps-mds.github.io/2018.2-ComexStat/docs/politicaBranches).
