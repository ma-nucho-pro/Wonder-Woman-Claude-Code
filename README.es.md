<div align="center">

<img src="assets/wonder-woman-logo.png" alt="Wonder Woman — plugin de verificación para Claude Code" width="300">

# Wonder Woman para Claude Code

### Haz que Claude lo demuestre antes de afirmarlo.

**Plugin multiagente de verificación con 16 jueces para Claude Code.**  
Wonder Woman investiga, cuestiona, contrasta, intenta refutar y vuelve a revisar las afirmaciones factuales **antes de que lleguen al usuario**.

**Creado por [ARKEA AI](https://github.com/ma-nucho-pro) — Roberto Manuel Jara Peche**  
[GitHub](https://github.com/ma-nucho-pro) · [Instagram](https://www.instagram.com/robertmanuchojp/) · [YouTube](https://www.youtube.com/@ManuchoAI) · [LinkedIn](https://www.linkedin.com/in/roberto-manuel-jara-peche-10867240b/)

**[Descargar ZIP](https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code/archive/refs/heads/main.zip)** ·
**[Releases](https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code/releases)** ·
**[Instalar](#instalación-en-60-segundos)** ·
**[Verificar](#comprueba-que-se-cargó)** ·
**[16 jueces](#el-tribunal-de-16-jueces)** ·
**[English](README.md)**

</div>

---

## Qué es este repositorio

Este es el paquete **FULL para Claude Code** de Wonder Woman.

No es solamente un prompt ni un `SKILL.md`. Incluye:

- la skill principal de verificación;
- un hook de inicio de sesión;
- **20 subagentes definidos para Claude Code**;
- **15 jueces especialistas** y **1 Supreme Judge**;
- Knowledge Gate, Resource Scout, Researcher y Corrector;
- protocolos para fuentes, claims, citas, reproducibilidad y loops de verificación;
- schemas de veredictos y pruebas adversariales.

El hilo principal de Claude Code coordina el proceso y delega trabajo a subagentes aislados.

> **Importante:** Wonder Woman está diseñada para reducir afirmaciones no respaldadas. No promete que un LLM pueda volverse 100 % incapaz de equivocarse.

---

## Cómo funciona

```text
PREGUNTA
   ↓
Knowledge Gate
   ↓
Resource Scout
   ↓
Researcher(s)
   ↓
BORRADOR PRIVADO
   ↓
CLAIM LEDGER
   ↓
15 JUECES ESPECIALISTAS
   ↓
JUEZ 16 — SUPREME JUDGE
   ↓
PASS ─────────────→ USUARIO
FAIL → INVESTIGAR → CORREGIR → JUECES NUEVOS ↻
```

Un FAIL no se convierte en una simple advertencia. El borrador vuelve a investigación y revisión. El límite predeterminado es de cinco rondas adjudicadas y **nunca obliga a aprobar**.

---

# Instalación en 60 segundos

## Opción 1 — Clonar el repositorio (recomendado)

Necesitas **Claude Code instalado y autenticado** y Git.

```bash
git clone https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code.git
cd Wonder-Woman-Claude-Code
claude plugin validate .
claude --plugin-dir .
```

Claude Code arrancará con Wonder Woman cargada para esa sesión.

---

## Opción 2 — Descargar el repositorio como ZIP

1. Pulsa **[Descargar ZIP](https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code/archive/refs/heads/main.zip)**.
2. Descomprime `Wonder-Woman-Claude-Code-main.zip`.
3. Abre una terminal dentro de la carpeta extraída.
4. Ejecuta:

```bash
claude plugin validate .
claude --plugin-dir .
```

---

## Opción 3 — Usar el ZIP empaquetado del plugin

Si descargas `wonder-woman-claude-code-plugin-v0.3.0.zip` desde **[Releases](https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code/releases)**, Claude Code puede cargarlo sin descomprimirlo.

### Windows

```powershell
claude --plugin-dir ".\wonder-woman-claude-code-plugin-v0.3.0.zip"
```

### macOS / Linux

```bash
claude --plugin-dir ./wonder-woman-claude-code-plugin-v0.3.0.zip
```

`--plugin-dir` carga el plugin durante esa sesión de Claude Code.

---

## Comprueba que se cargó

Dentro de Claude Code:

1. Ejecuta `/context` y busca **Custom Agents**.
2. Comprueba que aparezcan los agentes de Wonder Woman.
3. Si modificaste archivos, ejecuta `/reload-plugins`.
4. Para forzar manualmente la verificación:

```text
/wonder-woman:wonder-woman
```

El plugin también incluye un hook `SessionStart` que inyecta el bootstrap de verificación al iniciar la sesión con el plugin cargado.

---

## El tribunal de 16 jueces

| # | Juez | Revisa |
|---:|---|---|
| 01 | **Knowledge Examiner** | Falsa certeza y conocimiento no demostrado |
| 02 | **Premise Auditor** | Premisas falsas, ambiguas o incompletas |
| 03 | **Evidence Prosecutor** | Claims sin evidencia suficiente |
| 04 | **Source Authority Auditor** | Calidad y autoridad de las fuentes |
| 05 | **Primary Source Hunter** | Fuentes oficiales/primarias que faltan |
| 06 | **Freshness Inspector** | Información desactualizada |
| 07 | **Citation Entailment Inspector** | Si la cita realmente respalda el claim |
| 08 | **Hallucination Hunter** | Datos, APIs, URLs, estudios o cifras inventados |
| 09 | **Falsification Agent** | Intenta demostrar que el borrador está equivocado |
| 10 | **Logic Auditor** | Saltos lógicos y conclusiones no respaldadas |
| 11 | **Assumption Hunter** | Suposiciones y puntos ciegos |
| 12 | **Contradiction Hunter** | Contradicciones internas y con la evidencia |
| 13 | **Numerical Auditor** | Cálculos, porcentajes, unidades y estadísticas |
| 14 | **Context & Tool Auditor** | Archivos, herramientas, resultados y contexto |
| 15 | **Independent Blind Reviewer** | Revisión completa independiente |
| 16 | **Supreme Judge** | PASS / FAIL / CLARIFY / SAFE_ABSTENTION |

---

## Reglas centrales

```text
NINGUNA AFIRMACIÓN FACTUAL MATERIAL DEBE LLEGAR AL USUARIO
HASTA SUPERAR VERIFICACIÓN INDEPENDIENTE,
ADVERSARIAL Y BASADA EN EVIDENCIA.

EL CONSENSO NO ES EVIDENCIA.
LA CONFIANZA NO ES EVIDENCIA.
LA MEMORIA DEL MODELO NO ES EVIDENCIA PRIMARIA.
NUNCA FORZAR UN PASS.
```

---

## Actualizar

Si instalaste mediante Git:

```bash
git pull
claude plugin validate .
claude --plugin-dir .
```

Si usas el ZIP de Release, descarga la versión nueva y arranca Claude Code con ese archivo.

---

## Solución de problemas

### El plugin no valida

```bash
claude plugin validate .
```

### Los agentes no aparecen

Dentro de Claude Code:

```text
/reload-plugins
/context
```

También puedes abrir `/plugin` y revisar la pestaña **Errors**.

### Diagnóstico más profundo

```bash
claude --debug --plugin-dir .
```

### Wonder Woman dice que FULL mode no se ejecutó

Es intencional: tiene prohibido afirmar que corrieron 16 jueces independientes si el entorno realmente no hizo llamadas independientes a subagentes.

---

## Skill portable para Claude/ChatGPT

Este repositorio es específicamente para el **plugin FULL de Claude Code**.

Para la versión portable de Agent Skill usa:

**https://github.com/ma-nucho-pro/Wonder-Woman**

No subas todo este plugin de Claude Code como si fuera una Skill normal de Claude o ChatGPT.

---

## Creador, licencia y créditos

**Wonder Woman para Claude Code fue creado por ARKEA AI y Roberto Manuel Jara Peche.**

- Creador: **Roberto Manuel Jara Peche**
- Organización: **ARKEA AI**
- GitHub: https://github.com/ma-nucho-pro
- Instagram: https://www.instagram.com/robertmanuchojp/
- YouTube: https://www.youtube.com/@ManuchoAI
- LinkedIn: https://www.linkedin.com/in/roberto-manuel-jara-peche-10867240b/

Wonder Woman es software de código abierto bajo **Apache License 2.0**. Puedes usar, modificar y redistribuir el proyecto —también comercialmente— cumpliendo los términos de la licencia. Las redistribuciones deben conservar los avisos aplicables de licencia, copyright y atribución descritos en [`LICENSE`](LICENSE) y [`NOTICE`](NOTICE). Los avisos de terceros están en [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

Si Wonder Woman te ayuda, se agradecen una estrella en GitHub y compartir el repositorio oficial. La licencia define la atribución obligatoria; seguir redes sociales o dar una estrella nunca es una condición de uso.

> **Nota de marca:** Apache-2.0 licencia el software; no concede derechos de marca. El nombre ARKEA AI y el material gráfico original del proyecto no quedan licenciados como marcas por la licencia de software.

Consulta también [`AUTHORS.md`](AUTHORS.md).

---

<div align="center">

### Evidencia antes que confianza.
### Verificación antes que respuesta.

**Repositorio:** https://github.com/ma-nucho-pro/Wonder-Woman-Claude-Code

</div>
