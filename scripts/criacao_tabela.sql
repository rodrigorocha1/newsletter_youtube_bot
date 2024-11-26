CREATE TABLE canais(
	id_canal string,
	nome_canal string,
	url_canal string
);

CREATE UNIQUE INDEX idx_canal on canais(id_canal);

PRAGMA index_list(canais);

PRAGMA index_info('idx_canal');


CREATE TABLE resumo_video(
	id_video string UNIQUE PRIMARY KEY,
	id_canal string,
	nm_video string,
	transcricao string
	
);

FOREIGN KEY (id_canal) REFERENCES canal(id_canal);

SELECT *
from canais c ;


SELECT *
from VIDEOS ;

TRUNCATE TABLE VIDEOS CASCADE;


 """Método para selecionar o id canal usando o nome do canal

        Args:
            nome_canal (str): nome do canal

        Returns:
            _type_: _description_
        """