CREATE TABLE interacciones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    role TEXT,
    pregunta TEXT,
    respuesta TEXT,
    origen TEXT
);
