# LIGHT_COLOR_PERCEPTION_CORE.md

This layer checks physics/perception. It does not own art style.

## Light-source graph
For important scenes define source type, direction, relative intensity, hardness, color family,
coverage, visibility, and narrative role. Keep primary / secondary / bounce / ambient hierarchy clear.

## Form readability
Keep a coherent light family and shadow family. Cast shadows follow source direction.
Use contact/occlusion darkening only where justified. Reflected light should not erase the main form separation.

## Color architecture
Define dominant gamut, support gamut, neutral zone, accent colors, value range, chroma range,
warm/cool relationship, and forbidden/random colors. High chroma is a budget, not a default.

## Context rule
Color is relational: judge adjacent colors, illumination, surrounding value, saturation contrast,
and scene-wide color cast. Do not evaluate swatches in isolation.

## Material-light response
Assign important surfaces one response model:
diffuse / glossy / reflective / translucent / subsurface / emissive.
Highlight, reflection, transmission and shadow behavior must match that response.

## Atmosphere / depth
Atmosphere may change contrast, saturation, hue, edge clarity, visible light shafts and depth separation.
Do not force one warm-foreground/cool-background recipe.

## Color script
Sequential media should plan palette across the whole sequence:
dominant gamut, value/chroma range, warm/cool bias, accent, atmosphere, emotional function,
and transition from the previous unit.

## Modern-style compatibility
Anime cel shading, manga limited color, game key art, neon, pastel youth style, graphic flat color,
commercial clean look, horror, painterly fantasy and photoreal are all valid if project references select them.

Rule: coherent light/color/material behavior without forcing one visual taste.
