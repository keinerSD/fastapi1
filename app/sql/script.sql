-- Crear base de datos
CREATE DATABASE neondb;

-- Crear tabla

CREATE TABLE appointment (
	id_appointment integer PRIMARY KEY,
	id_student integer NOT NULL,
	id_staff integer NOT NULL,
	date timestamp NOT NULL,
	motif text,
	state varchar(20) DEFAULT 'Pendiente'
);
CREATE TABLE derivations (
	id_derivation integer PRIMARY KEY,
	id_query integer NOT NULL,
	destination_institution varchar(150) NOT NULL,
	reason text,
	derivation_date date DEFAULT CURRENT_DATE
);
CREATE TABLE emergencies (
	id_emergency integer PRIMARY KEY,
	id_student integer NOT NULL,
	date timestamp DEFAULT CURRENT_TIMESTAMP,
	descripcion text,
	attention_provided text,
	id_staff integer
);
CREATE TABLE medical_equipment (
	id_equipment integer PRIMARY KEY,
	name varchar(150) NOT NULL,
	descripcion text,
	serial_number varchar(100),
	acquisition_date date,
	state varchar(50) DEFAULT 'Operativo',
	location varchar(150)
);
CREATE TABLE medical_history (
	id_history integer PRIMARY KEY,
	id_student integer NOT NULL,
	blood_type varchar(5)
);
CREATE TABLE nursing_staff (
	id_staff integer PRIMARY KEY,
	name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	range varchar(50),
	phone varchar(20),
	email varchar(100),
	state varchar(20) DEFAULT 'Activo'
);
CREATE TABLE queries (
	id_query integer PRIMARY KEY,
	id_appointment integer,
	diagnosis text,
	treatment text,
	observations text,
	query_date timestamp DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE students (
	id_student serial PRIMARY KEY,
	tuition varchar(20) NOT NULL CONSTRAINT students_tuition_key UNIQUE,
	name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	birthdate date,
	gender varchar(10),
	phone varchar(20),
	email varchar(100),
	address text
);
CREATE TABLE university_accidents (
	id_accident integer PRIMARY KEY,
	id_student integer NOT NULL,
	place varchar(150),
	descripcion text,
	date timestamp DEFAULT CURRENT_TIMESTAMP,
	attended_by integer
);
CREATE TABLE vital_signs (
	id_signs integer PRIMARY KEY,
	id_query integer NOT NULL,
	blood_pressure varchar(20),
	temperature numeric(4, 2),
	weight numeric(5, 2),
	height numeric(4, 2)
);

-- Insertar registro

INSERT INTO students (tuition, name, last_name, birthdate, gender, phone, email, address) VALUES
('20260001', 'Ana', 'Gomez', '2003-05-12', 'F', '5551234567', 'ana.gomez@universidad.edu', 'Calle 123, Ciudad'),
('20260002', 'Luis', 'Martinez', '2002-11-23', 'M', '5559876543', 'luis.martinez@universidad.edu', 'Av. Central 45'),
('20260003', 'Carla', 'Perez', '2003-02-18', 'F', '5554567890', 'carla.perez@universidad.edu', 'Calle 7 #12');

INSERT INTO nursing_staff (id_staff, name, last_name, range, phone, email, state)
VALUES
(1, 'Laura', 'Rodriguez', 'Enfermera', '5553216547', 'laura.rodriguez@universidad.edu', 'Activo'),
(2, 'Carlos', 'Sanchez', 'Jefe de Enfermería', '5556543210', 'carlos.sanchez@universidad.edu', 'Activo'),
(3, 'Marta', 'Lopez', 'Enfermera', '5557890123', 'marta.lopez@universidad.edu', 'Activo')

INSERT INTO appointment (id_appointment, id_student, id_staff, date, motif, state)
VALUES
(1, 1, 1, '2026-02-15 10:00', 'Revisión de lesión en tobillo', 'Completada'),
(2, 2, 2, '2026-02-16 14:00', 'Revisión de corte en mano', 'Completada'),
(3, 3, 3, '2026-02-17 09:00', 'Chequeo general por mareo', 'Completada')

INSERT INTO queries (id_query, id_appointment, diagnosis, treatment, observations, query_date)
VALUES
(1, 1, 'Esguince de tobillo', 'Reposo y fisioterapia', 'Paciente estable', '2026-02-15 10:30'),
(2, 2, 'Corte superficial en mano', 'Vendaje y desinfección', 'Revisar sutura en 3 días', '2026-02-16 14:20'),
(3, 3, 'Mareo y dolor de cabeza', 'Hidratación y reposo', 'Se recomienda examen neurológico si persiste', '2026-02-17 09:10')

INSERT INTO medical_equipment (id_equipment, name, descripcion, serial_number, acquisition_date, state, location)
VALUES
(1, 'Tensiómetro', 'Para medir presión arterial', 'TS-001', '2022-03-10', 'Operativo', 'Consultorio 1'),
(2, 'Oxímetro', 'Para medir saturación de oxígeno', 'OX-045', '2023-01-15', 'Operativo', 'Consultorio 2'),
(3, 'Camilla', 'Para atención de pacientes', 'CM-210', '2021-09-05', 'En mantenimiento', 'Sala de emergencias')

INSERT INTO emergencies (id_emergency, id_student, date, descripcion, attention_provided, id_staff)
VALUES
(1, 1, '2026-02-15 10:30', 'Caída en escaleras', 'Primera atención y traslado a hospital', 2),
(2, 2, '2026-02-16 14:20', 'Corte en mano', 'Lavado, vendaje y observación', 1),
(3, 3, '2026-02-17 09:10', 'Mareo repentino', 'Reposo y evaluación médica', 3)

INSERT INTO derivations (id_derivation, id_query, destination_institution, reason, derivation_date)
VALUES
(1, 1, 'Hospital General', 'Fractura de muñeca', '2026-02-15'),
(2, 2, 'Clínica Santa María', 'Evaluación de hipertensión', '2026-02-16'),
(3, 3, 'Hospital Universitario', 'Dolor abdominal', '2026-02-17')

INSERT INTO university_accidents (id_accident, id_student, place, descripcion, date, attended_by)
VALUES
(1, 1, 'Escaleras bloque A', 'Caída y torcedura de tobillo', '2026-02-15 10:15', 1),
(2, 2, 'Laboratorio de química', 'Corte con vidrio', '2026-02-16 14:10', 2),
(3, 3, 'Patio central', 'Desmayo repentino', '2026-02-17 09:05', 3)

INSERT INTO vital_signs (id_signs, id_query, blood_pressure, temperature, weight, height) 
  VALUES
(1, 1, '120/80', 36.50, 70.25, 1.75),
(2, 2, '130/85', 37.20, 82.40, 1.68),
(3, 3, '110/70', 38.10, 65.00, 1.60);

INSERT INTO medical_history (id_history, id_student, blood_type) VALUES
(1, 1, 'O+'),
(2, 2, 'A-'),
(3, 3, 'B+')
