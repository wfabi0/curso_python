create database escola;

use escola;

create table Aluno(
    id_aluno int auto_increment primary key,
    nome varchar(50) not null,
    email varchar(50) not null,
    telefone varchar(11) not null
);
