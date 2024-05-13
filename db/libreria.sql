DELIMITER //
CREATE FUNCTION nom_user(xiduser INT)
RETURNS VARCHAR(50)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE nombre VARCHAR(50);
    SELECT nom_user INTO nombre
    FROM usuario
    WHERE iduser = xiduser;
    RETURN nombre;
END //
DELIMITER ;

DELIMITER //
CREATE FUNCTION obt_estado(xidact INT)
RETURNS VARCHAR(50)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE xestado VARCHAR(50);
    SELECT estado INTO xestado
    FROM actividad
    WHERE idact = xidact;
    RETURN xestado;
END //
DELIMITER ;



