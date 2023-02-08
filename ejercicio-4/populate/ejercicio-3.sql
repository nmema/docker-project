CREATE TABLE IF NOT EXISTS molinetes (
    periodo INT,
    fecha DATE,
    desde VARCHAR(8),
    hasta VARCHAR(8),
    linea VARCHAR(6),
    molinete VARCHAR(255),
    estacion VARCHAR(255),
    pax_pagos INT,
    pax_pases_pagos INT,
    pax_franq INT,
    pax_total INT
);