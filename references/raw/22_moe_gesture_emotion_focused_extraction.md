# 萌えキャラクターの描き方 しぐさ・感情表現編 — Focused / Deduplicated Extraction

> Source role: Character Embodiment source 2/4.
> Source form reviewed: 177 scanned pages from the user-supplied archive.
> Copyrighted scans are NOT bundled. Only paraphrased extraction and project rules are stored.
> Era note: the book's visual styling is 2011-era moe illustration; transferable behavior/anatomy rules are kept, period-specific style conventions are not made default.

## What this book adds that source 1 did not

Source 1 concentrated on `personality -> visible traits / expression / pose`.
This source adds the mechanical bridge for making those visible traits physically coherent:

`intention -> hand -> forearm -> elbow -> shoulder -> torso -> pelvis -> legs -> contact/support -> pose`.

It also demonstrates that emotion is not only a face problem: face, hands, shoulders, hair, torso, legs, clothing and camera-facing relation work together.

---

## ACTIVE RULES

### CG01 — Start from behavioral intent, not a stock pose
Choose what the character is doing / avoiding / offering / hiding / reaching for before choosing a pose.
A pose should be a consequence of action and emotion, not a decorative preset.

### CG02 — Hand meaning depends on the whole arm chain
A hand gesture must be checked together with wrist rotation, elbow location, shoulder tension and torso direction.
Do not paste a hand sign onto an otherwise unrelated body.

### CG03 — Fingers need grouped rhythm, not five independent sticks
Finger curvature, overlap and spacing should form readable groups.
For AI prompting, describe the hand action and palm orientation first; only specify individual fingers when essential.

### CG04 — Shoulder / neck compression is an emotion amplifier
Raised or inward shoulders shorten the visible neck and compress the upper body, often reading as guarded, embarrassed, cute, cold or defensive.
Open/lowered shoulders read more relaxed or confident depending on context.
Use with personality/context; do not hard-code.

### CG05 — Arm inside/outside surfaces must agree with rotation
Forearm and upper-arm orientation, elbow direction, palm direction and shoulder must remain mechanically consistent.
This is an anatomy validator for generated poses.

### CG06 — Face parts are layered controls
Eyebrows, eyes, pupils/gaze, mouth, head tilt and hair framing are separate channels.
Character identity should survive changes in each channel.

### CG07 — Hair can amplify or suppress emotion
Hair silhouette, swing, spread and face coverage can reinforce motion, shyness, disorder, energy or restraint.
Hair must still preserve the character's core hairstyle identity.

### CG08 — Torso is a flexible mass, not a front-facing sticker
The ribcage/torso needs volume, side profile and twist.
Chest/pelvis orientation can differ and should create the body rhythm before clothing is added.

### CG09 — Full-body expression needs center of gravity and support
A pose is believable only when weight/support is readable.
Track:
- support foot / knee / hip / hand / seat / bed / wall
- center of gravity
- pelvis direction
- torso counterbalance
- free-limb motion

### CG10 — Use a line-of-action / body rhythm before detail
Establish the dominant flow of the body before anatomy and clothing detail.
The source shows S/M-like shape families; in this Skill they are kept only as visual-rhythm examples, not gender/sexiness formulas.

### CG11 — Sitting / lying / kneeling require contact deformation
The body must respond to the support surface: hip compression, bent joints, limb overlap and gravity direction.
Do not float characters one centimeter above chairs, floors or beds.

### CG12 — Running / jumping need opposite-limb coordination
Motion becomes readable through opposing arm/leg action, torso lean, hair/clothing lag and clear airborne/support phase.

### CG13 — Leaning forward changes relationship, not just anatomy
Forward lean can imply curiosity, intimacy, challenge, urgency, service, fatigue or seduction depending on gaze, distance and context.
The camera/relationship layer must decide the meaning.

### CG14 — Gaze-to-camera is a relationship control
Direct camera gaze, averted gaze and partial/side gaze change the viewer-character relationship.
Treat gaze as staging, not merely eye direction.

### CG15 — Same emotion, different personality = different body solution
Do not use one "happy pose" or one "sad pose" for everyone.
Personality changes amplitude, openness, gesture size, gaze, self-touch, stance and hair motion.

### CG16 — Same pose can still describe different characters
If several characters share a pose, differentiate with:
- expression amplitude
- hand tension
- shoulder state
- hairstyle / hair movement
- clothing attitude
- accessory/prop use
- gaze
- spacing / personal-space behavior

### CG17 — Self-touch is a high-value emotional signal
Touching cheek, hair, sleeve, chest, hands or face can signal embarrassment, uncertainty, self-soothing, thought, restraint or intimacy.
Specify which body part is touched and why; avoid random "cute hand near face" prompts.

### CG18 — Emotion should propagate from face to whole body
For strong emotion, check a coherent chain:
`face -> shoulders -> hands -> torso -> pelvis -> legs -> hair/clothing`.
If only the face changes, the result often reads as posed or artificial.

### CG19 — Pose families are reusable, pose templates are not
Run / jump / sit / lie / lean are useful base families.
Each must be recompiled from character, current action, environment and camera.
Do not clone the source examples verbatim.

### CG20 — Costume and prop must follow gesture
Sleeves, skirts, coats, bags, weapons and held objects should react to pose, gravity and hand placement.
This connects directly to Costume Design and Blue Archive's character/weapon language.

### CG21 — Build character concepts from theme + behavior + costume + props
The book's original-character section demonstrates that a character theme becomes legible through the combination of body behavior, clothing and small objects, not by hairstyle alone.

### CG22 — Illustration review should separate design, pose and rendering
The source's final illustration analyses distinguish character design, pose, costume, silhouette and finish.
In this Skill, image quality review should keep those dimensions separate so a beautiful render cannot hide a weak character/pose design.

---

## MERGE WITH SOURCE 1

### MERGE
- personality -> expression amplitude
- shoulders / hands as character signals
- hair movement as behavior
- clothing attitude
- emotional variation by character

### ADD
- full arm-chain mechanics
- torso/pelvis orientation
- support/contact and gravity
- line-of-action
- locomotion pose families
- gaze-to-camera relationship
- same-pose/different-character diagnostics
- self-touch semantics
- full-body emotion propagation

### CORRECT / LIMIT
- Source examples sometimes frame curves and S/M pose families in a gendered or eroticized 2011 moe convention.
  Keep the underlying body-flow idea; remove the assumption that one curve family defines femininity or desirability.
- Do not inherit the book's period-specific faces, proportions, costume trends or fanservice conventions as the default visual style.
- Do not make "cute" synonymous with compressed shoulders, inward feet or hand-near-face. Those are options, not rules.

---

## CROSS-MODULE ROUTING

### With Directing Actors / Weston
Use action first:
`what is the character doing to someone/something?`
Then compile that action into visible gesture.

### With Proferes / staging
Character movement through space controls relationship and scene meaning.
Pose is a local staging state, not an isolated illustration.

### With Blue Archive P0
BA determines the final commercial anime visual language, identity anchors, outfit/faction consistency and high-value pose taste.
This book supplies the body/gesture grammar underneath it.

### With Costume Design
Clothing state and accessories must react to body mechanics and communicate role.

### With Cinematography
Camera distance/height/gaze relation may strengthen, weaken or reverse the intended emotional read.

### With Murch
Reaction pose / gaze change / gesture completion can define meaningful cut points.

---

## DEFAULT AI CHARACTER ROUTE AFTER SOURCE 2/4

`role/faction`
-> `personality pair`
-> `current objective/action`
-> `emotion + intensity`
-> `gaze relationship`
-> `shoulder/torso state`
-> `hand/self-touch/prop behavior`
-> `pelvis/stance/support`
-> `hair/clothing motion`
-> `BA/project visual design`
-> `camera`
-> `light`
-> `prompt`

