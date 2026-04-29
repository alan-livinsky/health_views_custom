# z_health_healthprof

Módulo de personalización local para GNU Health / Tryton sobre el modelo `gnuhealth.healthprofessional`.

## Descripción general

Este módulo extiende el modelo de **profesionales de salud** de GNU Health con campos adicionales y una vista de lista (árbol) mejorada. Está diseñado para instalaciones locales que necesitan identificar rápidamente si un profesional está marcado como médico dentro del sistema.

## Qué hace

### Campo calculado en el modelo

Agrega el campo booleano computado `party_is_healthprof` al modelo `gnuhealth.healthprofessional`.

```python
# health.py — extiende gnuhealth.healthprofessional
party_is_healthprof = fields.Function(
    fields.Boolean('Es médico?'),
    'get_party_is_healthprof'
)

def get_party_is_healthprof(self, name):
    return bool(self.name and self.name.is_healthprof)
```

- No persiste en base de datos (es un campo `Function`).
- Delega la verificación al campo `is_healthprof` de la entidad (`party`) vinculada.

### Vista personalizada (árbol heredado)

Hereda la vista árbol estándar `health.gnuhealth_healthprofessional_tree` e inyecta dos columnas nuevas **después** del campo `name`:

| Campo | Etiqueta visible |
|---|---|
| `main_specialty` | Especialidad principal |
| `is_doctor` | Es médico? |

### Registro en Tryton

El módulo se registra como:

```
trytond.modules.z_health_healthprof
```

Punto de entrada en `setup.py`:

```ini
[trytond.modules]
z_health_healthprof = trytond.modules.z_health_healthprof
```

## Dependencias

| Dependencia | Versión |
|---|---|
| Python | >= 3.10 |
| Tryton (`trytond`) | >= 6.0, < 6.1 |
| GNU Health (`gnuhealth`) | == 4.2.0 |
| Módulo Tryton `ir` | incluido en Tryton core |

## Versión del módulo

- Versión del módulo: **4.2.0**
- Compatible con Tryton: **6.0**
- Licencia: **GPL-3**

## Instalación

### Instalación normal

```bash
pip install .
```

### Instalación en modo editable (desarrollo)

```bash
pip install -e .
```

Esto instala el paquete como `trytond_z_health_healthprof` y registra el módulo en Tryton automáticamente vía el punto de entrada `trytond.modules`.

Luego, desde el administrador de Tryton, activar el módulo `z_health_healthprof` en la base de datos correspondiente.

## Estructura del proyecto

```
z_health_healthprof_custom/
├── __init__.py                      # Registro del modelo en el Pool de Tryton
├── health.py                        # Extensión del modelo HealthProfessional
├── health_views_custom.xml          # Registro de la vista heredada en ir.ui.view
├── view/
│   └── gnuhealth_healthprofessional_tree.xml  # XPath que inyecta columnas en el árbol
├── tryton.cfg                       # Metadatos del módulo (versión, dependencias, XML)
├── pyproject.toml                   # Configuración del sistema de build
├── setup.py                         # Empaquetado (nombre, dependencias, entry_points)
├── MANIFEST.in
└── README.md
```
