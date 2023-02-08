questions = {
    1: {
        'label': 'cantidad de viajes por línea en el año',
        'query': '''
            SELECT
                linea,
                TO_CHAR(SUM(pax_total), '999,999,999') AS viajes
            FROM molinetes
            GROUP BY linea
            ORDER BY SUM(pax_total) DESC
        '''
    },
    2: {
        'label': 'promedio diario de viajes por línea',
        'query': '''
            SELECT
	            linea,
	            TO_CHAR(FLOOR(AVG(viajes)), '999,999,999') AS promedio_viajes
            FROM (
                SELECT
                    linea,
                    fecha,
                    SUM(pax_total) AS viajes
                FROM molinetes
                GROUP BY linea, fecha
            ) viajes_por_fecha
            GROUP BY linea
            ORDER BY linea
        '''
    },
    3: {
        'label': 'top 3 estaciones más utilizadas por línea anualmente',
        'query': '''
            WITH cte AS ( 
                SELECT
                    linea,
                    estacion,
                    SUM(pax_total) AS viajes,
                    ROW_NUMBER() OVER (
                        PARTITION BY linea
                        ORDER BY linea, SUM(pax_total) DESC
                    ) AS rn
                FROM molinetes
                GROUP BY linea, estacion
                ORDER BY linea, SUM(pax_total) DESC
            )
            SELECT
                linea,
                estacion,
                TO_CHAR(viajes, '999,999,999') AS viajes
            FROM cte
            WHERE rn <= 3;
        '''
    },
    4: {
        'label': 'promedio de viajes en la semana',
        'query': '''
            SELECT
                CASE EXTRACT(ISODOW FROM fecha) 
                    WHEN 1 THEN 'lunes'
                    WHEN 2 THEN 'martes'
                    WHEN 3 THEN 'miercoles'
                    WHEN 4 THEN 'jueves'
                    WHEN 5 THEN 'viernes'
                    WHEN 6 THEN 'sabado'
                    WHEN 7 THEN 'domingo'
                END AS dia_de_la_semana,
                TO_CHAR(FLOOR(AVG(viajes)), '999,999,999') AS promedio_viajes
            FROM (
                SELECT
                    fecha,
                    SUM(pax_total) AS viajes
                FROM molinetes
                GROUP BY fecha
            ) viajes_por_fecha
            GROUP BY EXTRACT(ISODOW FROM fecha)
        '''
    },
    5: {
        'label': 'cantidad de viajes por mes',
        'query': '''
            SELECT
	            EXTRACT(MONTH FROM fecha) AS mes,
	            TO_CHAR(SUM(pax_total), '999,999,999') AS viajes
            FROM molinetes
            GROUP BY EXTRACT(MONTH FROM fecha)
        '''
    }
}