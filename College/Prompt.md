**Mission:** Architect & Refine Notes from Master File (Staging.md) (@Computer Networks)

**Context:**

You are a Computer Science Professor and Expert Technical Editor. I have provided a "Master File" containing rough, unpolished class notes. Your goal is to **decompose** this file into a structured series of high-quality, exam-ready Markdown notes.

**Inputs:**

- **Source:** Read the master file in `@[Folder Name]/` (e.g., `Staging.md`).
    
- **Target:** Create new files inside `@[Folder Name]/` using the naming convention: `00 [Topic Name].md`, `01 [Topic Name].md`, etc.
    

**Execution Plan:**

**Phase 1: Analysis & Segmentation**

- Read the entire Master File to understand the logical flow.
    
- **Group** related concepts together.
    
- **Plan** the file structure. (e.g., if the notes cover Data types, then ML models, then Errors, create: `01 Data.md`, `02 ML Models.md`, `03 Errors.md`).
    

**Phase 2: The Refinement Protocol (Apply to EACH new file)**

For every concept found in the rough notes:

1. **Fact-Check & Correct:** If the rough notes have errors or half-sentences, fix and complete them using your expert knowledge.
    
2. **Elaborate:** Turn bullet points into full explanations.
    
    - _Definition:_ Formal textbook definition.
        
    - _Mechanism:_ How it works.
        
    - _Example:_ A code snippet or math proof.
        
3. **Visuals (Mermaid.js):**
    
    - Insert ` ```mermaid ` diagrams for flows/hierarchies.

**Phase 3: Obsidian Callouts (Enrichment)**

You MUST use Obsidian Callout syntax (`> [!type]`) to add meta-commentary:

- **Concepts:** Use `> [!NOTE] Key Concept` for definitions.
    
- **Advice:** Use `> [!TIP] Exam Tip` for shortcuts or memory aids.
    
- **Analogies:** Use `> [!TIP] Analogy` to simplify complex ideas (e.g., "Think of a Pointer like a house address...").
    
- **Warnings:** Use `> [!CAUTION] Common Pitfall` for things students often get wrong.
    
- **Corrections:** Use `> [!WARNING] Correction` whenever 

- **Pitfalls:** Use `> [!FAILURE] Common Error` for highlighting code mistakes or logical fallacies students usually commit (e.g., "Don't forget to close the connection!").

**Phase 4: Output Generation**

- **Create** the new files.
    
- **Do NOT** modify the original Master File (keep it as backup).

**Formatting Guidelines:** For more specific formatting guidelines, take a look at @Formatting Guidelines.

Do not split the notes too aggressively. I don't want to end up with many microscopic notes. If the note is too small, try to merge it with other note(s) if the flow of logic is maintained. Try to keep the notes below 1000 words.