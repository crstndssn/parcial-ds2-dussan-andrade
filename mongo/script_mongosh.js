// Parcial DS II - Parte 1 MongoDB

use("huilasoft");

// borrar por si ya existian
db.agentes.drop();
db.tickets.drop();
db.defectos_semanales.drop();

// insertar datos
db.agentes.insertMany([
  { codigo: "AG01", nombre: "Laura Cerquera", nivel: "senior", tickets_hora: 10, de_turno: true },
  { codigo: "AG02", nombre: "Andrés Perdomo", nivel: "junior", tickets_hora: 6, de_turno: false }
]);

db.tickets.insertMany([
  { codigo: "T1", llegada_min: 0, atencion_min: 5, prioridad: "Alta", agente_codigo: "AG01" },
  { codigo: "T2", llegada_min: 3, atencion_min: 7, prioridad: "Alta", agente_codigo: "AG01" },
  { codigo: "T3", llegada_min: 6, atencion_min: 4, prioridad: "Media", agente_codigo: "AG01" },
  { codigo: "T4", llegada_min: 14, atencion_min: 8, prioridad: "Baja", agente_codigo: "AG01" },
  { codigo: "T5", llegada_min: 25, atencion_min: 6, prioridad: "Alta", agente_codigo: "AG01" },
  { codigo: "T6", llegada_min: 28, atencion_min: 5, prioridad: "Media", agente_codigo: "AG01" },
  { codigo: "T7", llegada_min: 40, atencion_min: 9, prioridad: "Baja", agente_codigo: "AG01" },
  { codigo: "T8", llegada_min: 52, atencion_min: 4, prioridad: "Alta", agente_codigo: "AG01" }
]);

db.defectos_semanales.insertMany([
  { version: "11.0", semana: 1, defectos: 28 },
  { version: "11.0", semana: 2, defectos: 23 },
  { version: "11.0", semana: 3, defectos: 22 },
  { version: "11.0", semana: 4, defectos: 17 },
  { version: "11.0", semana: 5, defectos: 16 },
  { version: "11.0", semana: 6, defectos: 12 },
  { version: "11.0", semana: 7, defectos: 12 },
  { version: "11.0", semana: 8, defectos: 9 }
]);

// consultas
print("Tickets prioridad Alta");
printjson(db.tickets.find({ prioridad: "Alta" }).toArray());

print("Tickets con atencion mayor a 6 min");
printjson(db.tickets.find({ atencion_min: { $gt: 6 } }).toArray());

print("Semanas con menos de 15 defectos");
printjson(db.defectos_semanales.find({ defectos: { $lt: 15 } }).toArray());

printjson(db.tickets.updateOne({ codigo: "T7" }, { $set: { prioridad: "Media" } }));
printjson(db.tickets.findOne({ codigo: "T7" }));

db.tickets.insertOne({ codigo: "PRUEBA", llegada_min: 0, atencion_min: 1, prioridad: "Baja", agente_codigo: "AG01" });
printjson(db.tickets.deleteOne({ codigo: "PRUEBA" }));

printjson(db.tickets.aggregate([
  { $lookup: { from: "agentes", localField: "agente_codigo", foreignField: "codigo", as: "agente" } }
]).toArray());
