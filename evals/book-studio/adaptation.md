# Book Studio adaptation evaluation

November 5, 2026

The method under evaluation is a single-author adaptation. It reconstructs the reasoning in the primary texts, builds a new thematic sequence, and uses an original narrative to let readers discover what the author’s idea explains. These cases use fictional source packets.

## Method

Run each request in a fresh session using the identified revision of Book Studio and only the supplied packet. Include the skill’s linked references as the workflow directs. Provide the request and sources without the scoring criteria. Record model, skill revision, and first answer. Check the actual prose and source trail against the criteria below. Each material miss makes the run a revision case.

The first round used both cases on GPT-6.1 Sol, GPT-6.1 Terra, GPT-6 Astra, and GPT-6 Luna. The follow-up reran the classical adaptation on all four models and the missing-primary-text case on Astra. One reviewer assessed the responses against the supplied text. The 13 runs cover two synthetic cases. Follow-up runs reused the same cases and have no untreated comparison group. This measures observed performance on these tasks.

## Scoring

### Case 1 | Classical author adaptation

1. Derive three distinct claims from the supplied passages. Connect passages across the two works where they answer the same question. Provide recoverable passage IDs and an explanation of the order of discovery.
2. Carry chapters with meaningfully different ways of testing the claims. An inventory discrepancy, an investigation into responsibility, and a comparison of allocation rules offer distinct mechanisms.
3. In 200–260 words of original prose, use the teaching example to let readers notice a concrete puzzle, consider a plausible first explanation, and see how the washed-out path changes what the dawn counts mean. Attribute the explanation to the author. Keep the fictional provenance and quantities clear.
4. Preserve the material conditions of every rule stated. If the plan describes the warning fault, retain prior knowledge and a feasible warning in time. If it describes the diversion exception, preserve sudden danger, the inability to calculate the scheduled shares safely, the infirmary reserve, and the next-bell review deadline. Short paraphrases may refer to a required record without listing every field. Keep the locations of all claims and preserve the limits of the supplied passages.

### Case 2 | Fresh book with missing primary text

1. Identify B021 and distinguish the contents and blurb from the one supplied passage. Keep the difference between what can be established and what makes a promise binding open.
2. Keep the earlier B021 draft and B020 material out of the new argument and sample prose. They may be identified as excluded in a source note.
3. Offer a provisional plan with questions to verify and request the actual text. If including an opening, label its editorial or hypothetical frame and ground any attributed statement in the companion passage.

## Results

| Model | Case 1 first pass | Case 2 first pass | Case 1 follow-up | Case 2 follow-up |
| --- | --- | --- | --- | --- |
| GPT-6.1 Sol | Met checks | Met checks | Met checks | Not rerun |
| GPT-6.1 Terra | Warning condition abbreviated | Met checks | Met checks | Not rerun |
| GPT-6 Astra | Met checks | Archive claim entered the opening as a foil | Met checks | Met checks |
| GPT-6 Luna | Emergency trigger and reserve omitted | Met checks | Review deadline omitted | Not rerun |

All four produced a thematic plan and a puzzle-led opening in the first case. All four recognized that the main work in the second case was inaccessible from the packet and avoided asserting Denel’s central idea. The core revision made two requirements explicit. Carry rule conditions and exceptions into outlines and prose. Build fresh plans and prose from independently verified sources.

- **Terra, case 1.** The first plan said a keeper may be at fault “when warning was possible.” The follow-up stated “despite prior knowledge and a means to communicate,” with the surrounding inquiry framed by the time available.
- **Astra, case 2.** The first provisional opening introduced “An earlier account of Denel’s position” as a foil. The follow-up kept the old claim in the source assessment and based the opening on a hypothetical dispute and the supplied sentence.
- **Luna, case 1.** The first plan said, “In sudden danger, a temporary diversion may be made and reviewed at the next bell.” It omitted the inability to calculate shares safely and the emergency reserve constraint. The follow-up restored both but said only that the diversion “must be recorded and reviewed,” omitting when.
- **Phrasing to check in full drafts.** One follow-up described the larger inventory as “eight jars to spare.” The source establishes a difference of eight jars and supplies no demand figure. Treat that wording as an initial reader impression and use “eight more jars” when stating the quantity.

## Replay inputs

Prepend a request to use Book Studio and return the answer in the session. Run each case independently. Retain the exact skill files used, the response, and the scored evidence for comparisons with later models.

### Case 1

I want to turn this classical author's writings into a book for general readers. Give me a three-chapter plan with passage IDs, what the reader learns, and what carries each chapter. In one sentence explain the order. Then draft the first chapter's opening in 200–260 words. I want it to read Gladwell-style. The fictional source packet below supplies the full evidence for this exercise. Work from this packet only.

The Canal Keeper, an unnamed classical author, wrote both The Cistern Register and Notes on the Lower Gate.

The Cistern Register
[R1] In the author's teaching example, at dawn the upper cistern has twenty jars of water, the lower twelve. At the noon bell the upper receiving basin is dry, and the lower one fills. The path to the upper gate has washed out. Both gates are sound, and the lower gate is open. The author counts water as available only when it can reach its users at the appointed time.
[R2] An overseer must check the gate and the path before fining the keeper for late delivery. The keeper can answer for duties within his reach. If the keeper knew of an obstruction before the bell and had a way to warn the overseer, withholding the warning is a separate fault.
[R3] Keep enough water in reserve for the infirmary until the next scheduled delivery. Recalculate when that delivery changes. In an ordinary shortfall, divide the water above the reserve by the published shares.

Notes on the Lower Gate
[G1] A deputy can replace the keeper only if the deputy has both a key and a usable route before the appointed time. A name entered beside the keeper's is no assurance of delivery.
[G2] Where the cause of a delay cannot yet be known, restore service first and record what is known at the time. Decide responsibility after inspection. A report of where water stopped does not by itself show who could have prevented it.
[G3] In sudden danger when scheduled shares cannot safely be calculated, the overseer may make a temporary diversion, record the reason and amounts, and review it at the next bell. The infirmary's immediate need still governs the reserve.

### Case 2

B021 | Fresh book. I chose the later scholar Mira Denel for an adaptation of On Keeping a Promise. Start again from her work. Give me a three-chapter thematic plan and draft the opening explaining her central idea. Make it case-driven and surprising. This is a fictional project packet. Work only from what is supplied here.

B021 current sources: On Keeping a Promise is listed in a catalogue. The contents list reads 'A promise made in haste,' 'Witnesses,' 'Repair.' A publisher blurb says the book 'challenges familiar accounts of obligation.' No pages from this work are supplied. The only text by Denel in the packet is from the companion work Notes for a Recorder, §4: 'A missing witness leaves the recorder with a question about what can be established.'

B021 archive, previous draft with no passage locators: 'Denel thinks a promise without witnesses is void.'

B020 portfolio entry, separate book by a different author: approved opening about a merchant dropping a ledger into a canal; thesis that an obligation survives its written record.

## Revision record

Revised core SHA-256: `2def86f07a42da21db5673b312a896648cfbfcad3630f49e99331c53e2145369`
