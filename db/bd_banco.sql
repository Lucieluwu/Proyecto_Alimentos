CREATE DATABASE Donappetite;

USE Donappetite;

CREATE TABLE PERSONA (
    ci INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(100),
    paterno VARCHAR(100),
    materno VARCHAR(100),
    celular VARCHAR(20),
    direccion VARCHAR(200),
    sexo VARCHAR(1),
    fecha_nacimiento DATE
);

CREATE TABLE USUARIO (
    iduser INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    rol VARCHAR(50),
    nom_user VARCHAR(100),
    correo VARCHAR(100),
    password VARCHAR(200),
    ci INT,
    FOREIGN KEY (ci) REFERENCES PERSONA(ci)
);

CREATE TABLE VOLUNTARIO (
    iduser INT NOT NULL PRIMARY KEY,
    horario VARCHAR(150),
    FOREIGN KEY (iduser) REFERENCES USUARIO(iduser)
);

CREATE TABLE ORGANIZACION (
    idorg INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    contacto VARCHAR(200),
    departamento VARCHAR(100),
    tipo VARCHAR(100),
    ci INT,
    FOREIGN KEY (ci) REFERENCES PERSONA(ci)
);

CREATE TABLE DONACION (
    iddona INT PRIMARY KEY AUTO_INCREMENT,
    tipo VARCHAR(100),
    fecha DATE
);

CREATE TABLE ALIMENTO (
    idalim INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion VARCHAR(200),
    categoria VARCHAR(100),
    fecha_ven DATE,
    tipo VARCHAR(100),
    peso DECIMAL(10,2),
    estado VARCHAR(100),
    stock INT
);

CREATE TABLE ACTIVIDAD (
    idact INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(200),
    tipo VARCHAR(100),
    estado VARCHAR(100),
    horario TIME,
    fecha_limite DATE,
    idadmin INT,
    idvol INT,
    FOREIGN KEY (idadmin) REFERENCES USUARIO(iduser),
    FOREIGN KEY (idvol) REFERENCES USUARIO(iduser)
);

CREATE TABLE RECIBE (
    iduser INT,
    iddona INT,
    idact INT,
    fecha DATE,
    hora TIME,
    PRIMARY KEY (iduser, iddona),
    FOREIGN KEY (iduser) REFERENCES USUARIO(iduser),
    FOREIGN KEY (iddona) REFERENCES DONACION(iddona),
    FOREIGN KEY (idact) REFERENCES ACTIVIDAD(idact)
);

CREATE TABLE SOLICITA (
    iduser INT,
    iddona INT,
    idact INT,
    fecha DATE,
    hora TIME,
    PRIMARY KEY (iduser, iddona),
    FOREIGN KEY (iduser) REFERENCES USUARIO(iduser),
    FOREIGN KEY (iddona) REFERENCES DONACION(iddona),
    FOREIGN KEY (idact) REFERENCES ACTIVIDAD(idact)
);

CREATE TABLE REALIZA (
    iduser INT,
    iddona INT,
    idact INT,
    fecha DATE,
    hora TIME,
    PRIMARY KEY (iduser, iddona),
    FOREIGN KEY (iduser) REFERENCES USUARIO(iduser),
    FOREIGN KEY (iddona) REFERENCES DONACION(iddona),
    FOREIGN KEY (idact) REFERENCES ACTIVIDAD(idact)
);

CREATE TABLE CONTIENE (
    iddona INT,
    idalim INT,
    cantidad INT,
    PRIMARY KEY (iddona, idalim),
    FOREIGN KEY (iddona) REFERENCES DONACION(iddona),
    FOREIGN KEY (idalim) REFERENCES ALIMENTO(idalim)
);
