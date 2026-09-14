# CHARACTER_EMBODIMENT_CORE

> Character Embodiment bridge, sources 3/4 integrated.
> This layer converts psychology and scene intent into observable, physically coherent character behavior.
> Final audit waits for the remaining main character-design book.

## 0. Ownership

- Story/Character owns internal motivation, relationship and long-term arc.
- Character Embodiment owns what that inner state looks like **right now**.
- Costume owns role/function/material logic.
- Blue Archive / project Case Library owns final commercial anime visual language and taste.
- Director/Staging owns where the character is and whom the action is directed toward.
- Camera/Light own presentation, not personality itself.

## 1. Default character route

ROLE / FACTION
-> PERSONALITY PAIR
-> CURRENT OBJECTIVE / ACTION
-> EMOTION + INTENSITY
-> RELATIONSHIP TARGET
-> GAZE
-> FACE BEHAVIOR
-> SHOULDERS / TORSO
-> HAND / SELF-TOUCH / PROP
-> PELVIS / STANCE / SUPPORT
-> HAIR / CLOTHING RESPONSE
-> PROJECT / BLUE ARCHIVE VISUAL LANGUAGE
-> CAMERA
-> LIGHT
-> PROMPT

## 2. Personality compression

Default image/video tasks use:
- one base personality
- one secondary / contrast trait
- one current objective/action
- one current emotion

Do not require a full literary biography unless the task needs story depth.


## 2.5 Visual differentiation

After personality/action are defined, load `CHARACTER_DIFFERENTIATION_CORE.md` when:
- designing a new character
- designing siblings/rivals/friends/team members
- differentiating same-uniform characters
- building an ensemble
- making alternate outfits without losing identity

Do not solve differentiation by hair color alone.

Useful handoff:
`personality/action -> face identity -> hair silhouette -> wardrobe behavior -> gesture -> prop/social behavior -> group contrast`.

## 3. Action before pose

Never start from `cute pose`, `sexy pose`, `cool pose` as the first instruction.
Start from a playable/observable action:
- avoid
- invite
- challenge
- conceal
- protect
- tease
- inspect
- comfort
- demand
- listen
- hesitate
- retreat
- reach
- rest

Then solve the pose.

## 4. Face behavior

Preserve base character identity.
Control separately:
- base eye shape
- gaze / focus target
- eyebrow tension
- eyelid openness
- mouth shape / amplitude
- blush/tears only when motivated
- head angle
- hair framing

Emotion modifies the face; it does not replace the face.

## 5. Upper-body behavior

### Shoulder state
open / neutral / lowered / raised / inward / asymmetric

### Torso state
upright / forward / backward / twist / side bend / compressed / expanded

### Hand state
open / closed / pointing / gripping / hiding / self-touch / prop-touch / other-touch / blocking / inviting

A hand gesture must agree with wrist, elbow, shoulder and torso.

## 6. Full-body behavior

Track:
- line_of_action
- ribcage_direction
- pelvis_direction
- center_of_gravity
- support_points
- stance_width
- foot_direction
- free_limb_motion
- motion_phase

No floating sitting/lying pose. Contact with floor/chair/bed/wall must read.

## 7. Emotional propagation

For medium/strong emotion, check the complete chain:
`face -> shoulder -> hand -> torso -> pelvis -> leg -> hair/clothing`.

A calm or reserved character may intentionally stop propagation early.
That reduced amplitude itself can express personality.

## 8. Gesture semantics

Do not reduce gestures to icon tags.
For every meaningful gesture ask:
- what is touched?
- palm orientation?
- distance from face/torso?
- elbow direction?
- shoulder state?
- who is the gesture directed toward?
- what changes if the viewer/camera is the target?

## 9. Self-touch

Self-touch is a useful channel for:
- embarrassment
- hesitation
- self-soothing
- thought
- restraint
- cold / discomfort
- intimacy

Use only when motivated; avoid generic "hand near face" repetition.

## 10. Hair / costume behavior

Hair and clothes have two jobs:
1. preserve identity / faction
2. react to action, gravity and emotional amplitude

Fast action -> lag / lift / spread may appear.
Stillness -> organized or hanging forms dominate.
Do not destroy signature hairstyle or costume continuity merely to make motion dramatic.

## 11. Pose families

Useful base families:
- stand
- walk/run
- jump
- sit/kneel/crouch
- lie/recline
- lean/bend
- reach/interact

These are construction families, not finished poses.
Always regenerate from character + objective + environment + camera.

## 12. Character differentiation test

If two characters are given the same scene/action, they should still differ in at least several of:
- gaze
- expression amplitude
- shoulder openness
- hand tension
- stance width
- personal distance
- movement amplitude
- hair response
- clothing attitude
- prop handling

If only hair color changes, the character layer failed.

## 13. Camera relation

Gaze and body orientation to camera define viewer relationship:
- direct engagement
- unaware/observed
- avoidance
- challenge
- invitation
- private introspection

Camera must not accidentally contradict intended relationship.

## 14. Deep Story Mode

Only activate when needed:
- want
- contradiction
- relationship pressure
- wound
- secret
- arc state

These fields explain recurring behavior over time; they are not mandatory for a single image.

## 15. Style firewall

This layer must never force:
- 2011-era moe face/proportion
- stereotype hairstyle-personality mapping
- S/M curve as a gender rule
- generic cute inward pose
- generic sexy pose

Blue Archive / project references retain higher visual-style priority.
