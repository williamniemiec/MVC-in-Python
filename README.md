# MVC in Python
![](https://github.com/williamniemiec/MVC-in-Python/blob/master/media/mvcPython.png?raw=true)

This project aims to show an application that uses the design pattern MVC (Model View Controller) using Python. Instead of create a project only with the essential MVC files, I decided to let the files from an application that i made, because I believe that this will make understanding easier of how the mechanics of MVC works in Python, in addiction to give you a general view of how to make a project with this pattern.

## Application execution
If you want to execute the application to see how it works, you have to download the database file that the app uses. This file is in <code>db/mvc.sql</code>. After that, it's necessary to load the file in a server (local or online) with support to MySQL database. I executed the app using a local server (as I use Windows, I used "Wampp" to make a local server, but if you use another operational system, there are other similar softwares, like Xampp [for Linux] or Mamp [for Mac]).
Furthermore the app use "mysql connector" library; if you don't have it, it's necessary install it.
### Links
- [mysql connector](https://pypi.org/project/mysql-connector-python/)
- [Wampp](http://www.wampserver.com/en/)
- [Mamp](https://www.mamp.info/)
- [Xampp](https://www.apachefriends.org/pt_br/index.html)

## Project organization
The project is in the src folder. In it, there are four folders and two files.

### /src
|Name| Type| Function
|------- | --- | ----
| Controllers | Directory| Contains all application controllers
| Core | Directory| Contains the class that is responsable for the MVC operations in Python
| Models | Directory| Contains all model application classes
| Views | Directory| Contains all responsible classes for the visual of the application
| config.py | File| MVC configuration file (it is important for Core class)
| Main.py | File| File responsible for the application start

### /tests
|Name| Type| Function
|------- | --- | ----
| Core | Directory| Contains all tests related to the Core class

## Export for personal project
As I said, the primary objective of this project is to aid other people that aim to make projects with the MVC design pattern. Although the project was developed in Python, it is possible to use the algorithm used to export to any programming language.
To use this project as a template for your project, it is enough to make the same directory structure (Controllers, Models,...) and put these directories in your project. The only files that are static, that is, do not change from a project to oter are the following files: 
 - <code>"Core/Core.py"</code>
 - <code>"Main.py"</code> (by default it always will call for "HomeController") 
 - <code>"config.php"</code>.

## Application photos
#### Inicial window
![Inicial window (Home)](https://github.com/williamniemiec/MVC-in-Python/blob/master/media/home.PNG?raw=true)
#### Show window
![Show window (if you run the app, try to click with the mouse right button on a row))](https://github.com/williamniemiec/MVC-in-Python/blob/master/media/showTreeView.PNG?raw=true)
#### Another show window without TreeView
![Another show window without TreeView widget](https://github.com/williamniemiec/MVC-in-Python/blob/master/media/show.PNG?raw=true)
<hr>

# --{ Português }--

O objetivo desse projeto é mostrar uma implementação de uma aplicação que utilize o padrão de projeto MVC (Model View Controller) utilizando Python. Ao invés de criar um projeto apenas com os arquivos essenciais do MVC, resolvi deixar no projeto os arquivos de uma aplicação que fiz, pois acredito que facilitará o entendimento de como a mecânica do MVC funciona no Python além de dar uma ideia geral de como fazer um projeto que siga esse padrão.

## Execução da aplicação

Caso você decida executar a aplicação para ver como ela funciona, você deverá baixar o arquivo do banco de dados que a aplicação utiliza. Este se encontra em <code>db/mvc.sql</code>. Após isso, é necessário carregar o arquivo em um servidor (local ou online) com suporte à banco de dados MySQL. Eu executei utilizando um servidor local; como utilizo Windows, utilizei o "WAMPP" para criar um servidor local, mas caso você utilize outro sistema operacional, há outros softwares similares, como o XAMPP (para Linux) e MAMP (para Mac)
Além disso, a aplicação utiliza a biblioteca "mysql connector"; caso você não tenha, é necessário instalar ela. 
### Links
- [mysql connector](https://pypi.org/project/mysql-connector-python/)
- [Wampp](http://www.wampserver.com/en/)
- [Mamp](https://www.mamp.info/)
- [Xampp](https://www.apachefriends.org/pt_br/index.html)

## Organização do projeto

O projeto está contido noo diretório src. Nele, há 4 diretórios e 2 arquivos.

### /src
|Nome | Tipo | Função
|------- | --- | ----
| Controllers | Diretório | Contém todos os controllers da aplicação
| Core | Diretório | Contém a classe que é responsável pelo funcionamento do MVC no Python
| Models | Diretório | Contém todas as classes Models da aplicação
| Views | Diretório | Contém as classes responsáveis pela parte visual do programa
| config.py | Arquivo| Arquivo de configurações do MVC (importante para funcionamento da classe Core)
| Main.py | Arquivo| Arquivo responsável por iniciar a aplicação

### /tests
|Nome | Tipo | Função
|------- | --- | ----
| Core | Diretório | Contém os testes relativos a classe Core

## Exportação para projeto pessoal
Como dito anteriormente, o objetivo desse projeto é auxiliar outras pessoas que queiram realizar projetos que utilizem o padrão de projeto MVC. Apesar de ter sido feito em Python, é possível utilizar as mesmas ideias para implementar em outras linguagens.
Para utilizar esse projeto como um template para seu projeto, basta criar a mesma estrutura de diretórios (Controllers, Models,...) e colocar nesses diretórios arquivos do seu projeto. Os únicos arquivos que são estáticos, isto é, não mudam de um projeto para o outro são os arquivos <code>"Core/Core.py"</code>,  <code>"Main.py"</code> (por padrão sempre chamará o "HomeController") e o <code>"config.php"</code>.
