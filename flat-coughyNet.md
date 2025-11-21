# 📦 flatshot Project Snapshot

**Generated:** 2025-11-21 15:07:17

## raw structure
```
├── .env
├── README.md
├── astro.config.mjs
├── categorizer.py
├── components.json
├── duplicator.py
├── env.d.ts
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── public
│   ├── images
│   │   ├── Cry As Punishment En.jpg
│   │   ├── Cry As Punishment Fa.jpg
│   │   ├── Threshold.jpeg
│   │   ├── bedoone_khodahafezi.jpg
│   │   ├── gardanravan.jpg
│   │   ├── sum.png
│   │   ├── tasmim 11.jpg
│   │   ├── vincenzo.png
│   │   ├── اثاثیاست یک دست میز و صندلی نگران.png
│   │   └── محل تبلیغات شما.png
│   ├── pdf
│   │   ├── bedoone_khodahafezi.pdf
│   │   ├── khianat_va_mokafat.pdf
│   │   ├── tasmim_baraye_cobra_11.pdf
│   │   ├── vincenzo.pdf
│   │   ├── اثاثیاست یک دست میز و صندلی نگران.pdf
│   │   └── محل تبلیغات شما.pdf
│   └── scripts
│       ├── nav-effects.js
│       └── navbar.js
├── registry.json
├── src
│   ├── assets
│   │   └── backgrounds
│   │       ├── bwca-dusk.png
│   │       └── bwca-night.png
│   ├── blog
│   │   ├── post-1.md
│   │   ├── post-2.md
│   │   ├── post-3.md
│   │   └── post-4.md
│   ├── categoryMapFa.ts
│   ├── content.config.ts
│   ├── data
│   │   └── nav.ts
│   ├── lib
│   │   └── utils.ts
│   ├── pages
│   │   └── rss.xml.js
│   ├── poems
│   │   ├── Sum Things Up.md
│   │   └── Violent Bloom.md
│   ├── stories
│   │   ├── cry_as_punishment.md
│   │   └── make love, not with eggs.md
│   ├── stories-fa
│   │   ├── bedoone_khodahafezi.md
│   │   ├── khianat_va_mokafat.md
│   │   ├── tasmim_baraye_cobra_11.md
│   │   ├── vincenzo.md
│   │   ├── اثاثیاست یک دست میز و صندلی نگران.md
│   │   └── محل تبلیغات شما.md
│   ├── styles
│   │   └── global.css
│   ├── utils
│   │   └── formatDate.ts
│   └── wiki
│       ├── Psychoactive
│       │   ├── Auditory_effects
│       │   │   ├── auditory-acuity-enhancement.fa.md
│       │   │   ├── auditory-acuity-enhancement.md
│       │   │   ├── auditory-acuity-suppression.fa.md
│       │   │   ├── auditory-acuity-suppression.md
│       │   │   ├── auditory-effects.fa.md
│       │   │   ├── auditory-effects.md
│       │   │   ├── auditory-hallucination.fa.md
│       │   │   ├── auditory-hallucination.md
│       │   │   ├── auditory-misinterpretation.fa.md
│       │   │   ├── auditory-misinterpretation.md
│       │   │   ├── autonomous-voice-communication.fa.md
│       │   │   ├── autonomous-voice-communication.md
│       │   │   ├── external-auditory-hallucination.fa.md
│       │   │   ├── external-auditory-hallucination.md
│       │   │   ├── internal-auditory-hallucination.fa.md
│       │   │   ├── internal-auditory-hallucination.md
│       │   │   ├── temporal-scaling.fa.md
│       │   │   └── temporal-scaling.md
│       │   ├── Cognitive_effects
│       │   │   ├── addiction-suppression.fa.md
│       │   │   ├── addiction-suppression.md
│       │   │   ├── amnesia.fa.md
│       │   │   ├── amnesia.md
│       │   │   ├── analysis-depression.fa.md
│       │   │   ├── analysis-depression.md
│       │   │   ├── analysis-enhancement.fa.md
│       │   │   ├── analysis-enhancement.md
│       │   │   ├── anhedonia.fa.md
│       │   │   ├── anhedonia.md
│       │   │   ├── anxiety-suppression.fa.md
│       │   │   ├── anxiety-suppression.md
│       │   │   ├── anxiety.fa.md
│       │   │   ├── anxiety.md
│       │   │   ├── atemporality.fa.md
│       │   │   ├── atemporality.md
│       │   │   ├── catharsis.fa.md
│       │   │   ├── catharsis.md
│       │   │   ├── cognitive-dysphoria.fa.md
│       │   │   ├── cognitive-dysphoria.md
│       │   │   ├── cognitive-effects.fa.md
│       │   │   ├── cognitive-effects.md
│       │   │   ├── cognitive-euphoria.fa.md
│       │   │   ├── cognitive-euphoria.md
│       │   │   ├── cognitive-fatigue.fa.md
│       │   │   ├── cognitive-fatigue.md
│       │   │   ├── compulsive-redosing.fa.md
│       │   │   ├── compulsive-redosing.md
│       │   │   ├── conceptual-thinking.fa.md
│       │   │   ├── conceptual-thinking.md
│       │   │   ├── confusion.fa.md
│       │   │   ├── confusion.md
│       │   │   ├── creativity-depression.fa.md
│       │   │   ├── creativity-depression.md
│       │   │   ├── creativity-enhancement.fa.md
│       │   │   ├── creativity-enhancement.md
│       │   │   ├── delirium.fa.md
│       │   │   ├── delirium.md
│       │   │   ├── delusions.fa.md
│       │   │   ├── delusions.md
│       │   │   ├── depersonalization.fa.md
│       │   │   ├── depersonalization.md
│       │   │   ├── depression-reduction.fa.md
│       │   │   ├── depression-reduction.md
│       │   │   ├── depression.fa.md
│       │   │   ├── depression.md
│       │   │   ├── depressions.fa.md
│       │   │   ├── depressions.md
│       │   │   ├── derealization.fa.md
│       │   │   ├── derealization.md
│       │   │   ├── disinhibition.fa.md
│       │   │   ├── disinhibition.md
│       │   │   ├── dream-potentiation.fa.md
│       │   │   ├── dream-potentiation.md
│       │   │   ├── dream-suppression.fa.md
│       │   │   ├── dream-suppression.md
│       │   │   ├── ego-dissolution.fa.md
│       │   │   ├── ego-dissolution.md
│       │   │   ├── ego-inflation.fa.md
│       │   │   ├── ego-inflation.md
│       │   │   ├── ego-replacement.fa.md
│       │   │   ├── ego-replacement.md
│       │   │   ├── emotion-intensification.fa.md
│       │   │   ├── emotion-intensification.md
│       │   │   ├── emotion-suppression.fa.md
│       │   │   ├── emotion-suppression.md
│       │   │   ├── empathy-affection-and-sociability-enhancement.fa.md
│       │   │   ├── empathy-affection-and-sociability-enhancement.md
│       │   │   ├── enhancements.fa.md
│       │   │   ├── enhancements.md
│       │   │   ├── euthymia.fa.md
│       │   │   ├── euthymia.md
│       │   │   ├── existential-self-realization.fa.md
│       │   │   ├── existential-self-realization.md
│       │   │   ├── feelings-of-impending-doom.fa.md
│       │   │   ├── feelings-of-impending-doom.md
│       │   │   ├── focus-intensification.fa.md
│       │   │   ├── focus-intensification.md
│       │   │   ├── focus-suppression.fa.md
│       │   │   ├── focus-suppression.md
│       │   │   ├── glossolalia.fa.md
│       │   │   ├── glossolalia.md
│       │   │   ├── identity-alteration.fa.md
│       │   │   ├── identity-alteration.md
│       │   │   ├── immersion-intensification.fa.md
│       │   │   ├── immersion-intensification.md
│       │   │   ├── increased-introspection.fa.md
│       │   │   ├── increased-introspection.md
│       │   │   ├── increased-music-appreciation.fa.md
│       │   │   ├── increased-music-appreciation.md
│       │   │   ├── increased-sense-of-humor.fa.md
│       │   │   ├── increased-sense-of-humor.md
│       │   │   ├── intensifications.fa.md
│       │   │   ├── intensifications.md
│       │   │   ├── irritability.fa.md
│       │   │   ├── irritability.md
│       │   │   ├── language-depression.fa.md
│       │   │   ├── language-depression.md
│       │   │   ├── mania.fa.md
│       │   │   ├── mania.md
│       │   │   ├── memory-enhancement.fa.md
│       │   │   ├── memory-enhancement.md
│       │   │   ├── memory-suppression.fa.md
│       │   │   ├── memory-suppression.md
│       │   │   ├── mindfulness.fa.md
│       │   │   ├── mindfulness.md
│       │   │   ├── motivation-depression.fa.md
│       │   │   ├── motivation-depression.md
│       │   │   ├── motivation-enhancement.fa.md
│       │   │   ├── motivation-enhancement.md
│       │   │   ├── multiple-thought-streams.fa.md
│       │   │   ├── multiple-thought-streams.md
│       │   │   ├── no-umbrella-reviews-done-below-this-line.fa.md
│       │   │   ├── no-umbrella-reviews-done-below-this-line.md
│       │   │   ├── novel.fa.md
│       │   │   ├── novel.md
│       │   │   ├── novelty-enhancement.fa.md
│       │   │   ├── novelty-enhancement.md
│       │   │   ├── panic-attack.fa.md
│       │   │   ├── panic-attack.md
│       │   │   ├── paranoia.fa.md
│       │   │   ├── paranoia.md
│       │   │   ├── perceived-exposure-to-inner-mechanics-of-consciousness.fa.md
│       │   │   ├── perceived-exposure-to-inner-mechanics-of-consciousness.md
│       │   │   ├── perception-of-eternalism.fa.md
│       │   │   ├── perception-of-eternalism.md
│       │   │   ├── perception-of-interdependent-opposites.fa.md
│       │   │   ├── perception-of-interdependent-opposites.md
│       │   │   ├── perception-of-predeterminism.fa.md
│       │   │   ├── perception-of-predeterminism.md
│       │   │   ├── perception-of-self-design.fa.md
│       │   │   ├── perception-of-self-design.md
│       │   │   ├── personal-bias-suppression.fa.md
│       │   │   ├── personal-bias-suppression.md
│       │   │   ├── personal-meaning-intensification.fa.md
│       │   │   ├── personal-meaning-intensification.md
│       │   │   ├── personality-regression.fa.md
│       │   │   ├── personality-regression.md
│       │   │   ├── psychological.fa.md
│       │   │   ├── psychological.md
│       │   │   ├── psychosis.fa.md
│       │   │   ├── psychosis.md
│       │   │   ├── rejuvenation.fa.md
│       │   │   ├── rejuvenation.md
│       │   │   ├── simultaneous-emotions.fa.md
│       │   │   ├── simultaneous-emotions.md
│       │   │   ├── sleepiness.fa.md
│       │   │   ├── sleepiness.md
│       │   │   ├── sociability-depression.fa.md
│       │   │   ├── sociability-depression.md
│       │   │   ├── spirituality-intensification.fa.md
│       │   │   ├── spirituality-intensification.md
│       │   │   ├── suggestibility-intensification.fa.md
│       │   │   ├── suggestibility-intensification.md
│       │   │   ├── suggestibility-suppression.fa.md
│       │   │   ├── suggestibility-suppression.md
│       │   │   ├── suicidal-ideation.fa.md
│       │   │   ├── suicidal-ideation.md
│       │   │   ├── thought-acceleration.fa.md
│       │   │   ├── thought-acceleration.md
│       │   │   ├── thought-connectivity.fa.md
│       │   │   ├── thought-connectivity.md
│       │   │   ├── thought-deceleration.fa.md
│       │   │   ├── thought-deceleration.md
│       │   │   ├── thought-disorganization.fa.md
│       │   │   ├── thought-disorganization.md
│       │   │   ├── thought-loop.fa.md
│       │   │   ├── thought-loop.md
│       │   │   ├── thought-organization.fa.md
│       │   │   ├── thought-organization.md
│       │   │   ├── time-compression.fa.md
│       │   │   ├── time-compression.md
│       │   │   ├── time-dilation.fa.md
│       │   │   ├── time-dilation.md
│       │   │   ├── time-reversal.fa.md
│       │   │   ├── time-reversal.md
│       │   │   ├── transpersonal.fa.md
│       │   │   ├── transpersonal.md
│       │   │   ├── unity-and-interconnectedness.fa.md
│       │   │   ├── unity-and-interconnectedness.md
│       │   │   ├── wakefulness.fa.md
│       │   │   └── wakefulness.md
│       │   ├── Disconnective_effects
│       │   │   ├── cognitive-disconnection.fa.md
│       │   │   ├── cognitive-disconnection.md
│       │   │   ├── detachment-plateaus.fa.md
│       │   │   ├── detachment-plateaus.md
│       │   │   ├── disconnective-effects.fa.md
│       │   │   ├── disconnective-effects.md
│       │   │   ├── dj-vu.fa.md
│       │   │   ├── dj-vu.md
│       │   │   ├── holes-spaces-and-voids.fa.md
│       │   │   ├── holes-spaces-and-voids.md
│       │   │   ├── physical-disconnection.fa.md
│       │   │   ├── physical-disconnection.md
│       │   │   ├── structures.fa.md
│       │   │   ├── structures.md
│       │   │   ├── visual-disconnection.fa.md
│       │   │   └── visual-disconnection.md
│       │   ├── Gustatory_and_olfactory_effects
│       │   │   ├── gustatory-and-olfactory-effects.fa.md
│       │   │   ├── gustatory-and-olfactory-effects.md
│       │   │   ├── gustatory-depression.fa.md
│       │   │   ├── gustatory-depression.md
│       │   │   ├── gustatory-hallucination.fa.md
│       │   │   ├── gustatory-hallucination.md
│       │   │   ├── gustatory-intensification.fa.md
│       │   │   ├── gustatory-intensification.md
│       │   │   ├── olfactory-depression.fa.md
│       │   │   ├── olfactory-depression.md
│       │   │   ├── olfactory-hallucination.fa.md
│       │   │   ├── olfactory-hallucination.md
│       │   │   ├── olfactory-intensification.fa.md
│       │   │   └── olfactory-intensification.md
│       │   ├── Multisensory_effects
│       │   │   ├── anticipatory-response.fa.md
│       │   │   ├── anticipatory-response.md
│       │   │   ├── component-controllability.fa.md
│       │   │   ├── component-controllability.md
│       │   │   ├── dosage-independent-intensity.fa.md
│       │   │   ├── dosage-independent-intensity.md
│       │   │   ├── machinescapes.fa.md
│       │   │   ├── machinescapes.md
│       │   │   ├── memory-replays.fa.md
│       │   │   ├── memory-replays.md
│       │   │   ├── multisensory-effects.fa.md
│       │   │   ├── multisensory-effects.md
│       │   │   ├── scenarios-and-plots.fa.md
│       │   │   ├── scenarios-and-plots.md
│       │   │   ├── spatial-disorientation.fa.md
│       │   │   ├── spatial-disorientation.md
│       │   │   ├── spontaneous-physical-movements.fa.md
│       │   │   ├── spontaneous-physical-movements.md
│       │   │   ├── synaesthesia.fa.md
│       │   │   └── synaesthesia.md
│       │   ├── Physical_effects
│       │   │   ├── alterations.fa.md
│       │   │   ├── alterations.md
│       │   │   ├── amplifications.fa.md
│       │   │   ├── amplifications.md
│       │   │   ├── appetite-intensification.fa.md
│       │   │   ├── appetite-intensification.md
│       │   │   ├── appetite-suppression.fa.md
│       │   │   ├── appetite-suppression.md
│       │   │   ├── bodily-control-enhancement.fa.md
│       │   │   ├── bodily-control-enhancement.md
│       │   │   ├── body-odor-alteration.fa.md
│       │   │   ├── body-odor-alteration.md
│       │   │   ├── bronchodilation.fa.md
│       │   │   ├── bronchodilation.md
│       │   │   ├── changes-in-felt-bodily-form.fa.md
│       │   │   ├── changes-in-felt-bodily-form.md
│       │   │   ├── changes-in-felt-gravity.fa.md
│       │   │   ├── changes-in-felt-gravity.md
│       │   │   ├── cough-suppression.fa.md
│       │   │   ├── cough-suppression.md
│       │   │   ├── decreased-libido.fa.md
│       │   │   ├── decreased-libido.md
│       │   │   ├── excessive-yawning.fa.md
│       │   │   ├── excessive-yawning.md
│       │   │   ├── increased-libido.fa.md
│       │   │   ├── increased-libido.md
│       │   │   ├── increased-respiration.fa.md
│       │   │   ├── increased-respiration.md
│       │   │   ├── increased-salivation.fa.md
│       │   │   ├── increased-salivation.md
│       │   │   ├── laughter-fits.fa.md
│       │   │   ├── laughter-fits.md
│       │   │   ├── motor-control-loss.fa.md
│       │   │   ├── motor-control-loss.md
│       │   │   ├── mouth-numbing.fa.md
│       │   │   ├── mouth-numbing.md
│       │   │   ├── muscle-relaxation.fa.md
│       │   │   ├── muscle-relaxation.md
│       │   │   ├── nausea-suppression.fa.md
│       │   │   ├── nausea-suppression.md
│       │   │   ├── orgasm-depression.fa.md
│       │   │   ├── orgasm-depression.md
│       │   │   ├── pain-relief.fa.md
│       │   │   ├── pain-relief.md
│       │   │   ├── perception-of-bodily-heaviness.fa.md
│       │   │   ├── perception-of-bodily-heaviness.md
│       │   │   ├── perception-of-bodily-lightness.fa.md
│       │   │   ├── perception-of-bodily-lightness.md
│       │   │   ├── physical-autonomy.fa.md
│       │   │   ├── physical-autonomy.md
│       │   │   ├── physical-effects.fa.md
│       │   │   ├── physical-effects.md
│       │   │   ├── physical-euphoria.fa.md
│       │   │   ├── physical-euphoria.md
│       │   │   ├── pupil-constriction.fa.md
│       │   │   ├── pupil-constriction.md
│       │   │   ├── pupil-dilation.fa.md
│       │   │   ├── pupil-dilation.md
│       │   │   ├── sedation.fa.md
│       │   │   ├── sedation.md
│       │   │   ├── seizure-suppression.fa.md
│       │   │   ├── seizure-suppression.md
│       │   │   ├── stamina-intensification.fa.md
│       │   │   ├── stamina-intensification.md
│       │   │   ├── stimulation.fa.md
│       │   │   ├── stimulation.md
│       │   │   ├── suppressions.fa.md
│       │   │   └── suppressions.md
│       │   ├── Smell & taste effects
│       │   │   ├── smell-and-taste-effects.fa.md
│       │   │   └── smell-and-taste-effects.md
│       │   ├── Tactile_effects
│       │   │   ├── spontaneous-bodily-sensations.fa.md
│       │   │   ├── spontaneous-bodily-sensations.md
│       │   │   ├── tactile-effects.fa.md
│       │   │   ├── tactile-effects.md
│       │   │   ├── tactile-hallucination.fa.md
│       │   │   ├── tactile-hallucination.md
│       │   │   ├── tactile-intensification.fa.md
│       │   │   ├── tactile-intensification.md
│       │   │   ├── tactile-suppression.fa.md
│       │   │   └── tactile-suppression.md
│       │   ├── Uncomfortable physical effects
│       │   │   ├── abnormal-heartbeat.fa.md
│       │   │   ├── abnormal-heartbeat.md
│       │   │   ├── back-pain.fa.md
│       │   │   ├── back-pain.md
│       │   │   ├── bodily-pressures.fa.md
│       │   │   ├── bodily-pressures.md
│       │   │   ├── bodily.fa.md
│       │   │   ├── bodily.md
│       │   │   ├── brain-zaps.fa.md
│       │   │   ├── brain-zaps.md
│       │   │   ├── cardiovascular.fa.md
│       │   │   ├── cardiovascular.md
│       │   │   ├── cerebrovascular.fa.md
│       │   │   ├── cerebrovascular.md
│       │   │   ├── constipation.fa.md
│       │   │   ├── constipation.md
│       │   │   ├── decreased-blood-pressure.fa.md
│       │   │   ├── decreased-blood-pressure.md
│       │   │   ├── decreased-heart-rate.fa.md
│       │   │   ├── decreased-heart-rate.md
│       │   │   ├── dehydration.fa.md
│       │   │   ├── dehydration.md
│       │   │   ├── diarrhea.fa.md
│       │   │   ├── diarrhea.md
│       │   │   ├── difficulty-urinating.fa.md
│       │   │   ├── difficulty-urinating.md
│       │   │   ├── dizziness.fa.md
│       │   │   ├── dizziness.md
│       │   │   ├── dry-mouth.fa.md
│       │   │   ├── dry-mouth.md
│       │   │   ├── frequent-urination.fa.md
│       │   │   ├── frequent-urination.md
│       │   │   ├── headache.fa.md
│       │   │   ├── headache.md
│       │   │   ├── increased-blood-pressure.fa.md
│       │   │   ├── increased-blood-pressure.md
│       │   │   ├── increased-bodily-temperature.fa.md
│       │   │   ├── increased-bodily-temperature.md
│       │   │   ├── increased-heart-rate.fa.md
│       │   │   ├── increased-heart-rate.md
│       │   │   ├── increased-perspiration.fa.md
│       │   │   ├── increased-perspiration.md
│       │   │   ├── increased-phlegm-production.fa.md
│       │   │   ├── increased-phlegm-production.md
│       │   │   ├── itchiness.fa.md
│       │   │   ├── itchiness.md
│       │   │   ├── muscle-contractions.fa.md
│       │   │   ├── muscle-contractions.md
│       │   │   ├── muscle-cramps.fa.md
│       │   │   ├── muscle-cramps.md
│       │   │   ├── muscle-tension.fa.md
│       │   │   ├── muscle-tension.md
│       │   │   ├── muscle-twitching.fa.md
│       │   │   ├── muscle-twitching.md
│       │   │   ├── nausea.fa.md
│       │   │   ├── nausea.md
│       │   │   ├── optical-sliding.fa.md
│       │   │   ├── optical-sliding.md
│       │   │   ├── photophobia.fa.md
│       │   │   ├── photophobia.md
│       │   │   ├── physical-fatigue.fa.md
│       │   │   ├── physical-fatigue.md
│       │   │   ├── respiratory-depression.fa.md
│       │   │   ├── respiratory-depression.md
│       │   │   ├── restless-legs.fa.md
│       │   │   ├── restless-legs.md
│       │   │   ├── runny-nose.fa.md
│       │   │   ├── runny-nose.md
│       │   │   ├── seizure.fa.md
│       │   │   ├── seizure.md
│       │   │   ├── skin-flushing.fa.md
│       │   │   ├── skin-flushing.md
│       │   │   ├── stomach-bloating.fa.md
│       │   │   ├── stomach-bloating.md
│       │   │   ├── stomach-cramp.fa.md
│       │   │   ├── stomach-cramp.md
│       │   │   ├── teeth-grinding.fa.md
│       │   │   ├── teeth-grinding.md
│       │   │   ├── temperature-regulation-suppression.fa.md
│       │   │   ├── temperature-regulation-suppression.md
│       │   │   ├── temporary-erectile-dysfunction.fa.md
│       │   │   ├── temporary-erectile-dysfunction.md
│       │   │   ├── uncomfortable-physical-effects.fa.md
│       │   │   ├── uncomfortable-physical-effects.md
│       │   │   ├── vasoconstriction.fa.md
│       │   │   ├── vasoconstriction.md
│       │   │   ├── vasodilation.fa.md
│       │   │   ├── vasodilation.md
│       │   │   ├── vibrating-vision.fa.md
│       │   │   ├── vibrating-vision.md
│       │   │   ├── vomiting.fa.md
│       │   │   ├── vomiting.md
│       │   │   ├── wate.fa.md
│       │   │   └── wate.md
│       │   ├── Visual_effects
│       │   │   ├── 8a-perceived-exposure-to-semantic-concept-network.fa.md
│       │   │   ├── 8a-perceived-exposure-to-semantic-concept-network.md
│       │   │   ├── 8b-perceived-exposure-to-inner-mechanics-of-consciousness.fa.md
│       │   │   ├── 8b-perceived-exposure-to-inner-mechanics-of-consciousness.md
│       │   │   ├── after-images.fa.md
│       │   │   ├── after-images.md
│       │   │   ├── autonomous-entity.fa.md
│       │   │   ├── autonomous-entity.md
│       │   │   ├── breathing.fa.md
│       │   │   ├── breathing.md
│       │   │   ├── brightness-alteration.fa.md
│       │   │   ├── brightness-alteration.md
│       │   │   ├── color-depression.fa.md
│       │   │   ├── color-depression.md
│       │   │   ├── color-enhancement.fa.md
│       │   │   ├── color-enhancement.md
│       │   │   ├── color-replacement.fa.md
│       │   │   ├── color-replacement.md
│       │   │   ├── color-shifting.fa.md
│       │   │   ├── color-shifting.md
│       │   │   ├── color-tinting.fa.md
│       │   │   ├── color-tinting.md
│       │   │   ├── diffraction.fa.md
│       │   │   ├── diffraction.md
│       │   │   ├── double-vision.fa.md
│       │   │   ├── double-vision.md
│       │   │   ├── drifting.fa.md
│       │   │   ├── drifting.md
│       │   │   ├── environmental-cubism.fa.md
│       │   │   ├── environmental-cubism.md
│       │   │   ├── environmental-orbism.fa.md
│       │   │   ├── environmental-orbism.md
│       │   │   ├── environmental-patterning.fa.md
│       │   │   ├── environmental-patterning.md
│       │   │   ├── external-hallucination.fa.md
│       │   │   ├── external-hallucination.md
│       │   │   ├── flowing.fa.md
│       │   │   ├── flowing.md
│       │   │   ├── geometry.fa.md
│       │   │   ├── geometry.md
│       │   │   ├── hallucinatory-states.fa.md
│       │   │   ├── hallucinatory-states.md
│       │   │   ├── internal-hallucination.fa.md
│       │   │   ├── internal-hallucination.md
│       │   │   ├── magnification.fa.md
│       │   │   ├── magnification.md
│       │   │   ├── melting.fa.md
│       │   │   ├── melting.md
│       │   │   ├── morphing.fa.md
│       │   │   ├── morphing.md
│       │   │   ├── object-activation.fa.md
│       │   │   ├── object-activation.md
│       │   │   ├── object-alteration.fa.md
│       │   │   ├── object-alteration.md
│       │   │   ├── pattern-recognition-enhancement.fa.md
│       │   │   ├── pattern-recognition-enhancement.md
│       │   │   ├── pattern-recognition-suppression.fa.md
│       │   │   ├── pattern-recognition-suppression.md
│       │   │   ├── peripheral-information-misinterpretation.fa.md
│       │   │   ├── peripheral-information-misinterpretation.md
│       │   │   ├── perspective-hallucination.fa.md
│       │   │   ├── perspective-hallucination.md
│       │   │   ├── recursion.fa.md
│       │   │   ├── recursion.md
│       │   │   ├── scenery-slicing.fa.md
│       │   │   ├── scenery-slicing.md
│       │   │   ├── settings-sceneries-and-landscapes.fa.md
│       │   │   ├── settings-sceneries-and-landscapes.md
│       │   │   ├── shadow-people.fa.md
│       │   │   ├── shadow-people.md
│       │   │   ├── symmetrical-texture-repetition.fa.md
│       │   │   ├── symmetrical-texture-repetition.md
│       │   │   ├── texture-liquidation.fa.md
│       │   │   ├── texture-liquidation.md
│       │   │   ├── tracers.fa.md
│       │   │   ├── tracers.md
│       │   │   ├── transformations.fa.md
│       │   │   ├── transformations.md
│       │   │   ├── unspeakable-horrors.fa.md
│       │   │   ├── unspeakable-horrors.md
│       │   │   ├── visual-acuity-enhancement.fa.md
│       │   │   ├── visual-acuity-enhancement.md
│       │   │   ├── visual-acuity-suppression.fa.md
│       │   │   ├── visual-acuity-suppression.md
│       │   │   ├── visual-effects.fa.md
│       │   │   ├── visual-effects.md
│       │   │   ├── visual-flipping.fa.md
│       │   │   ├── visual-flipping.md
│       │   │   ├── visual-haze.fa.md
│       │   │   ├── visual-haze.md
│       │   │   ├── visual-processing-acceleration.fa.md
│       │   │   ├── visual-processing-acceleration.md
│       │   │   ├── visual-processing-deceleration.fa.md
│       │   │   ├── visual-processing-deceleration.md
│       │   │   ├── visual-stretching.fa.md
│       │   │   └── visual-stretching.md
│       │   ├── effects.fa.md
│       │   └── effects.md
│       └── Psychoactives
│           ├── 2C-x
│           │   ├── 2c-b.fa.md
│           │   ├── 2c-b.md
│           │   ├── 2c-c.fa.md
│           │   ├── 2c-c.md
│           │   ├── 2c-d.fa.md
│           │   ├── 2c-d.md
│           │   ├── 2c-e.fa.md
│           │   ├── 2c-e.md
│           │   ├── 2c-h.fa.md
│           │   ├── 2c-h.md
│           │   ├── 2c-i.fa.md
│           │   ├── 2c-i.md
│           │   ├── 2c-p.fa.md
│           │   ├── 2c-p.md
│           │   ├── 2c-t-2.fa.md
│           │   ├── 2c-t-2.md
│           │   ├── 2c-t-21.fa.md
│           │   ├── 2c-t-21.md
│           │   ├── 2c-t-7.fa.md
│           │   ├── 2c-t-7.md
│           │   ├── 2c-t-x.fa.md
│           │   ├── 2c-t-x.md
│           │   ├── 2c-t.fa.md
│           │   ├── 2c-t.md
│           │   ├── 2c-x.fa.md
│           │   ├── 2c-x.md
│           │   ├── 2c-xderivatives.fa.md
│           │   └── 2c-xderivatives.md
│           ├── Cannabinoids
│           │   ├── 5f-akb48.fa.md
│           │   ├── 5f-akb48.md
│           │   ├── 5f-pb-22.fa.md
│           │   ├── 5f-pb-22.md
│           │   ├── ab-fubinaca.fa.md
│           │   ├── ab-fubinaca.md
│           │   ├── apica.fa.md
│           │   ├── apica.md
│           │   ├── cannabinoids.fa.md
│           │   ├── cannabinoids.md
│           │   ├── cbd.fa.md
│           │   ├── cbd.md
│           │   ├── cbda.fa.md
│           │   ├── cbda.md
│           │   ├── cbdh.fa.md
│           │   ├── cbdh.md
│           │   ├── cbdp.fa.md
│           │   ├── cbdp.md
│           │   ├── delta-10-thc.fa.md
│           │   ├── delta-10-thc.md
│           │   ├── delta-11-thc.fa.md
│           │   ├── delta-11-thc.md
│           │   ├── delta-8-thc.fa.md
│           │   ├── delta-8-thc.md
│           │   ├── hhc.fa.md
│           │   ├── hhc.md
│           │   ├── jwh-018.fa.md
│           │   ├── jwh-018.md
│           │   ├── jwh-073.fa.md
│           │   ├── jwh-073.md
│           │   ├── phytocannabinoids.fa.md
│           │   ├── phytocannabinoids.md
│           │   ├── semi-synthetic-phytocannabinoids.fa.md
│           │   ├── semi-synthetic-phytocannabinoids.md
│           │   ├── sts-135.fa.md
│           │   ├── sts-135.md
│           │   ├── synthetic-cannabinoids.fa.md
│           │   ├── synthetic-cannabinoids.md
│           │   ├── thc-o-acetate.fa.md
│           │   ├── thc-o-acetate.md
│           │   ├── thc.fa.md
│           │   ├── thc.md
│           │   ├── thca.fa.md
│           │   ├── thca.md
│           │   ├── thcb.fa.md
│           │   ├── thcb.md
│           │   ├── thch.fa.md
│           │   ├── thch.md
│           │   ├── thcp.fa.md
│           │   ├── thcp.md
│           │   ├── thj-018.fa.md
│           │   ├── thj-018.md
│           │   ├── thj-2201.fa.md
│           │   └── thj-2201.md
│           ├── Classical_psychedelics
│           │   ├── classical-psychedelics.fa.md
│           │   └── classical-psychedelics.md
│           ├── DOx
│           │   ├── 25-dma.fa.md
│           │   ├── 25-dma.md
│           │   ├── dob.fa.md
│           │   ├── dob.md
│           │   ├── doc.fa.md
│           │   ├── doc.md
│           │   ├── doi.fa.md
│           │   ├── doi.md
│           │   ├── dom.fa.md
│           │   ├── dom.md
│           │   ├── dox.fa.md
│           │   ├── dox.md
│           │   ├── doxderivatives.fa.md
│           │   └── doxderivatives.md
│           ├── Deliriants
│           │   ├── antihistamines.fa.md
│           │   ├── antihistamines.md
│           │   ├── atropine.fa.md
│           │   ├── atropine.md
│           │   ├── benzydamine.fa.md
│           │   ├── benzydamine.md
│           │   ├── deliriants.fa.md
│           │   ├── deliriants.md
│           │   ├── elemicin.fa.md
│           │   ├── elemicin.md
│           │   ├── hyoscyamine.fa.md
│           │   ├── hyoscyamine.md
│           │   ├── myristicin.fa.md
│           │   ├── myristicin.md
│           │   ├── promethazine.fa.md
│           │   ├── promethazine.md
│           │   ├── scopolamine.fa.md
│           │   ├── scopolamine.md
│           │   ├── tropane-alkaloids.fa.md
│           │   └── tropane-alkaloids.md
│           ├── Depressants
│           │   ├── 14-butanediol.fa.md
│           │   ├── 14-butanediol.md
│           │   ├── 2-methyl-2-butanol.fa.md
│           │   ├── 2-methyl-2-butanol.md
│           │   ├── 7-hydroxymitragynine.fa.md
│           │   ├── 7-hydroxymitragynine.md
│           │   ├── acetylfentanyl.fa.md
│           │   ├── acetylfentanyl.md
│           │   ├── alcohol.fa.md
│           │   ├── alcohol.md
│           │   ├── alcohols.fa.md
│           │   ├── alcohols.md
│           │   ├── alprazolam.fa.md
│           │   ├── alprazolam.md
│           │   ├── baclofen.fa.md
│           │   ├── baclofen.md
│           │   ├── barbiturates.fa.md
│           │   ├── barbiturates.md
│           │   ├── benzodiazepines.fa.md
│           │   ├── benzodiazepines.md
│           │   ├── bromazepam.fa.md
│           │   ├── bromazepam.md
│           │   ├── buprenorphine.fa.md
│           │   ├── buprenorphine.md
│           │   ├── carisoprodol.fa.md
│           │   ├── carisoprodol.md
│           │   ├── clonazepam.fa.md
│           │   ├── clonazepam.md
│           │   ├── clonazolam.fa.md
│           │   ├── clonazolam.md
│           │   ├── clonidine.fa.md
│           │   ├── clonidine.md
│           │   ├── codeine.fa.md
│           │   ├── codeine.md
│           │   ├── depressants.fa.md
│           │   ├── depressants.md
│           │   ├── deschloroetizolam.fa.md
│           │   ├── deschloroetizolam.md
│           │   ├── desomorphine.fa.md
│           │   ├── desomorphine.md
│           │   ├── dextropropoxyphene.fa.md
│           │   ├── dextropropoxyphene.md
│           │   ├── diacetylmorphine.fa.md
│           │   ├── diacetylmorphine.md
│           │   ├── diazepam.fa.md
│           │   ├── diazepam.md
│           │   ├── diclazepam.fa.md
│           │   ├── diclazepam.md
│           │   ├── dihydrocodeine.fa.md
│           │   ├── dihydrocodeine.md
│           │   ├── diphenhydramine.fa.md
│           │   ├── diphenhydramine.md
│           │   ├── eszopiclone.fa.md
│           │   ├── eszopiclone.md
│           │   ├── ethylmorphine.fa.md
│           │   ├── ethylmorphine.md
│           │   ├── etizolam.fa.md
│           │   ├── etizolam.md
│           │   ├── f-phenibut.fa.md
│           │   ├── f-phenibut.md
│           │   ├── fentanyl.fa.md
│           │   ├── fentanyl.md
│           │   ├── flualprazolam.fa.md
│           │   ├── flualprazolam.md
│           │   ├── flubromazepam.fa.md
│           │   ├── flubromazepam.md
│           │   ├── flubromazolam.fa.md
│           │   ├── flubromazolam.md
│           │   ├── flunitrazepam.fa.md
│           │   ├── flunitrazepam.md
│           │   ├── flunitrazolam.fa.md
│           │   ├── flunitrazolam.md
│           │   ├── gabaa-1-agonists.fa.md
│           │   ├── gabaa-1-agonists.md
│           │   ├── gabapentin.fa.md
│           │   ├── gabapentin.md
│           │   ├── gabapentinoids.fa.md
│           │   ├── gabapentinoids.md
│           │   ├── gaboxadol.fa.md
│           │   ├── gaboxadol.md
│           │   ├── gbl.fa.md
│           │   ├── gbl.md
│           │   ├── ghb.fa.md
│           │   ├── ghb.md
│           │   ├── hydrocodone.fa.md
│           │   ├── hydrocodone.md
│           │   ├── hydromorphone.fa.md
│           │   ├── hydromorphone.md
│           │   ├── ibotenic-acid.fa.md
│           │   ├── ibotenic-acid.md
│           │   ├── kava.fa.md
│           │   ├── kava.md
│           │   ├── kratom.fa.md
│           │   ├── kratom.md
│           │   ├── lorazepam.fa.md
│           │   ├── lorazepam.md
│           │   ├── lormetazepam.fa.md
│           │   ├── lormetazepam.md
│           │   ├── methadone.fa.md
│           │   ├── methadone.md
│           │   ├── methaqualone.fa.md
│           │   ├── methaqualone.md
│           │   ├── metizolam.fa.md
│           │   ├── metizolam.md
│           │   ├── midazolam.fa.md
│           │   ├── midazolam.md
│           │   ├── mirtazapine.fa.md
│           │   ├── mirtazapine.md
│           │   ├── morphine.fa.md
│           │   ├── morphine.md
│           │   ├── muscimol.fa.md
│           │   ├── muscimol.md
│           │   ├── nifoxipam.fa.md
│           │   ├── nifoxipam.md
│           │   ├── nitromethaqualone.fa.md
│           │   ├── nitromethaqualone.md
│           │   ├── o-desmethyltramadol.fa.md
│           │   ├── o-desmethyltramadol.md
│           │   ├── opioids.fa.md
│           │   ├── opioids.md
│           │   ├── other-gabaergics.fa.md
│           │   ├── other-gabaergics.md
│           │   ├── oxycodone.fa.md
│           │   ├── oxycodone.md
│           │   ├── oxymorphone.fa.md
│           │   ├── oxymorphone.md
│           │   ├── pentobarbital.fa.md
│           │   ├── pentobarbital.md
│           │   ├── pethidine.fa.md
│           │   ├── pethidine.md
│           │   ├── phenibut.fa.md
│           │   ├── phenibut.md
│           │   ├── phenobarbital.fa.md
│           │   ├── phenobarbital.md
│           │   ├── pregabalin.fa.md
│           │   ├── pregabalin.md
│           │   ├── pyrazolam.fa.md
│           │   ├── pyrazolam.md
│           │   ├── secobarbital.fa.md
│           │   ├── secobarbital.md
│           │   ├── sufentanil.fa.md
│           │   ├── sufentanil.md
│           │   ├── tapentadol.fa.md
│           │   ├── tapentadol.md
│           │   ├── temazepam.fa.md
│           │   ├── temazepam.md
│           │   ├── thienodiazepines.fa.md
│           │   ├── thienodiazepines.md
│           │   ├── tizanidine.fa.md
│           │   ├── tizanidine.md
│           │   ├── tramadol.fa.md
│           │   ├── tramadol.md
│           │   ├── u-47700.fa.md
│           │   ├── u-47700.md
│           │   ├── zolpidem.fa.md
│           │   ├── zolpidem.md
│           │   ├── zopiclone.fa.md
│           │   └── zopiclone.md
│           ├── Dissociatives
│           │   ├── 2-fluorodeschloroketamine.fa.md
│           │   ├── 2-fluorodeschloroketamine.md
│           │   ├── 2-oxo-pce.fa.md
│           │   ├── 2-oxo-pce.md
│           │   ├── 2-oxo-pcm.fa.md
│           │   ├── 2-oxo-pcm.md
│           │   ├── 3-cl-pcp.fa.md
│           │   ├── 3-cl-pcp.md
│           │   ├── 3-ho-pce.fa.md
│           │   ├── 3-ho-pce.md
│           │   ├── 3-ho-pcp.fa.md
│           │   ├── 3-ho-pcp.md
│           │   ├── 3-meo-pce.fa.md
│           │   ├── 3-meo-pce.md
│           │   ├── 3-meo-pcmo.fa.md
│           │   ├── 3-meo-pcmo.md
│           │   ├── 3-meo-pcp.fa.md
│           │   ├── 3-meo-pcp.md
│           │   ├── 4-meo-pcp.fa.md
│           │   ├── 4-meo-pcp.md
│           │   ├── adamantanes.fa.md
│           │   ├── adamantanes.md
│           │   ├── arylcyclohexylamines.fa.md
│           │   ├── arylcyclohexylamines.md
│           │   ├── dextromethorphan.fa.md
│           │   ├── dextromethorphan.md
│           │   ├── dextrorphan.fa.md
│           │   ├── dextrorphan.md
│           │   ├── diarylethylamines.fa.md
│           │   ├── diarylethylamines.md
│           │   ├── diphenidine.fa.md
│           │   ├── diphenidine.md
│           │   ├── dissociatives.fa.md
│           │   ├── dissociatives.md
│           │   ├── ephenidine.fa.md
│           │   ├── ephenidine.md
│           │   ├── eticyclidine.fa.md
│           │   ├── eticyclidine.md
│           │   ├── hydroxetamine.fa.md
│           │   ├── hydroxetamine.md
│           │   ├── ketamine.fa.md
│           │   ├── ketamine.md
│           │   ├── methoxetamine.fa.md
│           │   ├── methoxetamine.md
│           │   ├── morphinans.fa.md
│           │   ├── morphinans.md
│           │   ├── phencyclidine.fa.md
│           │   ├── phencyclidine.md
│           │   ├── r-ketamine.fa.md
│           │   ├── r-ketamine.md
│           │   ├── s-ketamine.fa.md
│           │   └── s-ketamine.md
│           ├── Empathogens
│           │   ├── 5-apb.fa.md
│           │   ├── 5-apb.md
│           │   ├── 5-mapb.fa.md
│           │   ├── 5-mapb.md
│           │   ├── 6-apb.fa.md
│           │   ├── 6-apb.md
│           │   ├── 6-apdb.fa.md
│           │   ├── 6-apdb.md
│           │   ├── benzofurans.fa.md
│           │   ├── benzofurans.md
│           │   ├── empathogens.fa.md
│           │   ├── empathogens.md
│           │   ├── mda.fa.md
│           │   ├── mda.md
│           │   ├── mdai.fa.md
│           │   ├── mdai.md
│           │   ├── mdea.fa.md
│           │   ├── mdea.md
│           │   ├── mdma.fa.md
│           │   ├── mdma.md
│           │   ├── mdxx.fa.md
│           │   ├── mdxx.md
│           │   ├── methylone.fa.md
│           │   ├── methylone.md
│           │   ├── pma.fa.md
│           │   ├── pma.md
│           │   ├── pmma.fa.md
│           │   └── pmma.md
│           ├── Entheogens
│           │   ├── acacia-confusa.fa.md
│           │   ├── acacia-confusa.md
│           │   ├── amanita-muscaria.fa.md
│           │   ├── amanita-muscaria.md
│           │   ├── argyreia-nervosa.fa.md
│           │   ├── argyreia-nervosa.md
│           │   ├── banisteriopsis-caapi.fa.md
│           │   ├── banisteriopsis-caapi.md
│           │   ├── blue-lotus.fa.md
│           │   ├── blue-lotus.md
│           │   ├── cannabis.fa.md
│           │   ├── cannabis.md
│           │   ├── datura.fa.md
│           │   ├── datura.md
│           │   ├── entheogens.fa.md
│           │   ├── entheogens.md
│           │   ├── iboga.fa.md
│           │   ├── iboga.md
│           │   ├── ipomoea-tricolor.fa.md
│           │   ├── ipomoea-tricolor.md
│           │   ├── mimosa-hostilis.fa.md
│           │   ├── mimosa-hostilis.md
│           │   ├── nicotiana.fa.md
│           │   ├── nicotiana.md
│           │   ├── peyote.fa.md
│           │   ├── peyote.md
│           │   ├── psilocybin-mushrooms.fa.md
│           │   ├── psilocybin-mushrooms.md
│           │   ├── salvia-divinorum.fa.md
│           │   ├── salvia-divinorum.md
│           │   ├── san-pedro.fa.md
│           │   ├── san-pedro.md
│           │   ├── syrian-rue.fa.md
│           │   ├── syrian-rue.md
│           │   ├── yopo.fa.md
│           │   └── yopo.md
│           ├── Lysergamides
│           │   ├── 1b-lsd.fa.md
│           │   ├── 1b-lsd.md
│           │   ├── 1cp-al-lad.fa.md
│           │   ├── 1cp-al-lad.md
│           │   ├── 1cp-lsd.fa.md
│           │   ├── 1cp-lsd.md
│           │   ├── 1cp-mipla.fa.md
│           │   ├── 1cp-mipla.md
│           │   ├── 1p-eth-lad.fa.md
│           │   ├── 1p-eth-lad.md
│           │   ├── 1p-lsd.fa.md
│           │   ├── 1p-lsd.md
│           │   ├── 1v-lsd.fa.md
│           │   ├── 1v-lsd.md
│           │   ├── al-lad.fa.md
│           │   ├── al-lad.md
│           │   ├── ald-52.fa.md
│           │   ├── ald-52.md
│           │   ├── eth-lad.fa.md
│           │   ├── eth-lad.md
│           │   ├── lae-32.fa.md
│           │   ├── lae-32.md
│           │   ├── lsa.fa.md
│           │   ├── lsa.md
│           │   ├── lsd.fa.md
│           │   ├── lsd.md
│           │   ├── lsh.fa.md
│           │   ├── lsh.md
│           │   ├── lsm-775.fa.md
│           │   ├── lsm-775.md
│           │   ├── lsz.fa.md
│           │   ├── lsz.md
│           │   ├── lysergamides.fa.md
│           │   ├── lysergamides.md
│           │   ├── mipla.fa.md
│           │   ├── mipla.md
│           │   ├── pargy-lad.fa.md
│           │   ├── pargy-lad.md
│           │   ├── pro-lad.fa.md
│           │   └── pro-lad.md
│           ├── Mescaline_homologues
│           │   ├── 3c-e.fa.md
│           │   ├── 3c-e.md
│           │   ├── 3c-p.fa.md
│           │   ├── 3c-p.md
│           │   ├── allylescaline.fa.md
│           │   ├── allylescaline.md
│           │   ├── escaline.fa.md
│           │   ├── escaline.md
│           │   ├── mescaline-homologues.fa.md
│           │   ├── mescaline-homologues.md
│           │   ├── mescaline.fa.md
│           │   ├── mescaline.md
│           │   ├── methallylescaline.fa.md
│           │   ├── methallylescaline.md
│           │   ├── proscaline.fa.md
│           │   └── proscaline.md
│           ├── Miscellaneous
│           │   ├── 5-hydroxytryptophan.fa.md
│           │   ├── 5-hydroxytryptophan.md
│           │   ├── acetylcholine-boosters.fa.md
│           │   ├── acetylcholine-boosters.md
│           │   ├── acetylcholinesterase-inhibitors.fa.md
│           │   ├── acetylcholinesterase-inhibitors.md
│           │   ├── alkyl-nitrites.fa.md
│           │   ├── alkyl-nitrites.md
│           │   ├── amyl-nitrite.fa.md
│           │   ├── amyl-nitrite.md
│           │   ├── ayahuasca.fa.md
│           │   ├── ayahuasca.md
│           │   ├── calea-ternifolia.fa.md
│           │   ├── calea-ternifolia.md
│           │   ├── changa.fa.md
│           │   ├── changa.md
│           │   ├── chloroform.fa.md
│           │   ├── chloroform.md
│           │   ├── diethyl-ether.fa.md
│           │   ├── diethyl-ether.md
│           │   ├── dxm-and-dph.fa.md
│           │   ├── dxm-and-dph.md
│           │   ├── dxm.fa.md
│           │   ├── dxm.md
│           │   ├── entada-rheedii.fa.md
│           │   ├── entada-rheedii.md
│           │   ├── galantamine.fa.md
│           │   ├── galantamine.md
│           │   ├── ibogaine.fa.md
│           │   ├── ibogaine.md
│           │   ├── inhalants.fa.md
│           │   ├── inhalants.md
│           │   ├── isobutyl-nitrite.fa.md
│           │   ├── isobutyl-nitrite.md
│           │   ├── isopropyl-nitrite.fa.md
│           │   ├── isopropyl-nitrite.md
│           │   ├── miscellaneous.fa.md
│           │   ├── miscellaneous.md
│           │   ├── nitrous-oxide.fa.md
│           │   ├── nitrous-oxide.md
│           │   ├── oneirogens.fa.md
│           │   ├── oneirogens.md
│           │   ├── opioid-receptor-agonists.fa.md
│           │   ├── opioid-receptor-agonists.md
│           │   ├── polysubstance-combinations.fa.md
│           │   ├── polysubstance-combinations.md
│           │   ├── progesterone.fa.md
│           │   ├── progesterone.md
│           │   ├── salvinorin-a.fa.md
│           │   ├── salvinorin-a.md
│           │   ├── salvinorin-b-methoxymethyl-ether.fa.md
│           │   ├── salvinorin-b-methoxymethyl-ether.md
│           │   ├── sigmaergics.fa.md
│           │   ├── sigmaergics.md
│           │   ├── various.fa.md
│           │   ├── various.md
│           │   ├── xenon.fa.md
│           │   └── xenon.md
│           ├── Miscellaneousـphenethylamines
│           │   ├── 2c-b-fly.fa.md
│           │   ├── 2c-b-fly.md
│           │   ├── bromo-dragonfly.fa.md
│           │   ├── bromo-dragonfly.md
│           │   ├── k-2c-b.fa.md
│           │   ├── k-2c-b.md
│           │   ├── miscellaneousphenethylamines.fa.md
│           │   ├── miscellaneousphenethylamines.md
│           │   ├── tma-2.fa.md
│           │   ├── tma-2.md
│           │   ├── tma-6.fa.md
│           │   └── tma-6.md
│           ├── N-Benzylـphenethylamines
│           │   ├── 25b-nboh.fa.md
│           │   ├── 25b-nboh.md
│           │   ├── 25b-nbome.fa.md
│           │   ├── 25b-nbome.md
│           │   ├── 25c-nboh.fa.md
│           │   ├── 25c-nboh.md
│           │   ├── 25c-nbome.fa.md
│           │   ├── 25c-nbome.md
│           │   ├── 25d-nbome.fa.md
│           │   ├── 25d-nbome.md
│           │   ├── 25e-nboh.fa.md
│           │   ├── 25e-nboh.md
│           │   ├── 25i-nboh.fa.md
│           │   ├── 25i-nboh.md
│           │   ├── 25i-nbome.fa.md
│           │   ├── 25i-nbome.md
│           │   ├── 25n-nbome.fa.md
│           │   ├── 25n-nbome.md
│           │   ├── n-benzylphenethylamines.fa.md
│           │   └── n-benzylphenethylamines.md
│           ├── Neurotransmitters
│           │   ├── acetylcholine.fa.md
│           │   ├── acetylcholine.md
│           │   ├── amino-acids.fa.md
│           │   ├── amino-acids.md
│           │   ├── aminobutyric-acid.fa.md
│           │   ├── aminobutyric-acid.md
│           │   ├── catecholamines.fa.md
│           │   ├── catecholamines.md
│           │   ├── dopamine.fa.md
│           │   ├── dopamine.md
│           │   ├── epinephrine.fa.md
│           │   ├── epinephrine.md
│           │   ├── histamine.fa.md
│           │   ├── histamine.md
│           │   ├── l-glutamate.fa.md
│           │   ├── l-glutamate.md
│           │   ├── melatonin.fa.md
│           │   ├── melatonin.md
│           │   ├── monoamines.fa.md
│           │   ├── monoamines.md
│           │   ├── neurotransmitters.fa.md
│           │   ├── neurotransmitters.md
│           │   ├── norepinephrine.fa.md
│           │   ├── norepinephrine.md
│           │   ├── other.fa.md
│           │   ├── other.md
│           │   ├── peptides.fa.md
│           │   ├── peptides.md
│           │   ├── phenethylamine.fa.md
│           │   ├── phenethylamine.md
│           │   ├── phenethylamines.fa.md
│           │   ├── phenethylamines.md
│           │   ├── semax.fa.md
│           │   ├── semax.md
│           │   ├── serotonin.fa.md
│           │   ├── serotonin.md
│           │   ├── trace-amines.fa.md
│           │   ├── trace-amines.md
│           │   ├── tryptamine.fa.md
│           │   └── tryptamine.md
│           ├── Nootropics
│           │   ├── 5-htp.fa.md
│           │   ├── 5-htp.md
│           │   ├── adrafinil.fa.md
│           │   ├── adrafinil.md
│           │   ├── alpha-gpc.fa.md
│           │   ├── alpha-gpc.md
│           │   ├── aniracetam.fa.md
│           │   ├── aniracetam.md
│           │   ├── armodafinil.fa.md
│           │   ├── armodafinil.md
│           │   ├── bromantane.fa.md
│           │   ├── bromantane.md
│           │   ├── choline-bitartrate.fa.md
│           │   ├── choline-bitartrate.md
│           │   ├── choline.fa.md
│           │   ├── choline.md
│           │   ├── citicoline.fa.md
│           │   ├── citicoline.md
│           │   ├── coluracetam.fa.md
│           │   ├── coluracetam.md
│           │   ├── creatine.fa.md
│           │   ├── creatine.md
│           │   ├── dietary-supplements.fa.md
│           │   ├── dietary-supplements.md
│           │   ├── eugeroics.fa.md
│           │   ├── eugeroics.md
│           │   ├── gaba.fa.md
│           │   ├── gaba.md
│           │   ├── l-theanine.fa.md
│           │   ├── l-theanine.md
│           │   ├── l-tyrosine.fa.md
│           │   ├── l-tyrosine.md
│           │   ├── meclofenoxate.fa.md
│           │   ├── meclofenoxate.md
│           │   ├── memantine.fa.md
│           │   ├── memantine.md
│           │   ├── modafinil.fa.md
│           │   ├── modafinil.md
│           │   ├── n-acetylcysteine.fa.md
│           │   ├── n-acetylcysteine.md
│           │   ├── n-methylbisfluoromodafinil.fa.md
│           │   ├── n-methylbisfluoromodafinil.md
│           │   ├── noopept.fa.md
│           │   ├── noopept.md
│           │   ├── nootropics.fa.md
│           │   ├── nootropics.md
│           │   ├── others.fa.md
│           │   ├── others.md
│           │   ├── oxiracetam.fa.md
│           │   ├── oxiracetam.md
│           │   ├── phenylpiracetam.fa.md
│           │   ├── phenylpiracetam.md
│           │   ├── piracetam.fa.md
│           │   ├── piracetam.md
│           │   ├── pramiracetam.fa.md
│           │   ├── pramiracetam.md
│           │   ├── racetams.fa.md
│           │   ├── racetams.md
│           │   ├── s-adenosyl-methionine.fa.md
│           │   ├── s-adenosyl-methionine.md
│           │   ├── tianeptine.fa.md
│           │   └── tianeptine.md
│           ├── Others
│           │   ├── 5-meo-dibf.fa.md
│           │   ├── 5-meo-dibf.md
│           │   ├── efavirenz.fa.md
│           │   └── efavirenz.md
│           ├── Psychoactives.fa.md
│           ├── Psychoactives.md
│           ├── Stimulants
│           │   ├── 2-ai.fa.md
│           │   ├── 2-ai.md
│           │   ├── 2-fa.fa.md
│           │   ├── 2-fa.md
│           │   ├── 2-fea.fa.md
│           │   ├── 2-fea.md
│           │   ├── 2-fma.fa.md
│           │   ├── 2-fma.md
│           │   ├── 3-fa.fa.md
│           │   ├── 3-fa.md
│           │   ├── 3-fea.fa.md
│           │   ├── 3-fea.md
│           │   ├── 3-fma.fa.md
│           │   ├── 3-fma.md
│           │   ├── 3-fpm.fa.md
│           │   ├── 3-fpm.md
│           │   ├── 3-mmc.fa.md
│           │   ├── 3-mmc.md
│           │   ├── 34-ctmp.fa.md
│           │   ├── 34-ctmp.md
│           │   ├── 4-fa.fa.md
│           │   ├── 4-fa.md
│           │   ├── 4-fma.fa.md
│           │   ├── 4-fma.md
│           │   ├── 4f-eph.fa.md
│           │   ├── 4f-eph.md
│           │   ├── 4f-mph.fa.md
│           │   ├── 4f-mph.md
│           │   ├── 8-chlorotheophylline.fa.md
│           │   ├── 8-chlorotheophylline.md
│           │   ├── aminorexes.fa.md
│           │   ├── aminorexes.md
│           │   ├── amphetamine.fa.md
│           │   ├── amphetamine.md
│           │   ├── amphetamines.fa.md
│           │   ├── amphetamines.md
│           │   ├── butylone.fa.md
│           │   ├── butylone.md
│           │   ├── caffeine.fa.md
│           │   ├── caffeine.md
│           │   ├── cathinone.fa.md
│           │   ├── cathinone.md
│           │   ├── cathinones.fa.md
│           │   ├── cathinones.md
│           │   ├── cocaine.fa.md
│           │   ├── cocaine.md
│           │   ├── cyclazodone.fa.md
│           │   ├── cyclazodone.md
│           │   ├── desoxypipradrol.fa.md
│           │   ├── desoxypipradrol.md
│           │   ├── dexmethylphenidate.fa.md
│           │   ├── dexmethylphenidate.md
│           │   ├── dextroamphetamine.fa.md
│           │   ├── dextroamphetamine.md
│           │   ├── ephedrine.fa.md
│           │   ├── ephedrine.md
│           │   ├── ephylone.fa.md
│           │   ├── ephylone.md
│           │   ├── ethcathinone.fa.md
│           │   ├── ethcathinone.md
│           │   ├── ethylone.fa.md
│           │   ├── ethylone.md
│           │   ├── ethylphenidate.fa.md
│           │   ├── ethylphenidate.md
│           │   ├── fenethylline.fa.md
│           │   ├── fenethylline.md
│           │   ├── hexedrone.fa.md
│           │   ├── hexedrone.md
│           │   ├── isopropylphenidate.fa.md
│           │   ├── isopropylphenidate.md
│           │   ├── lisdexamfetamine.fa.md
│           │   ├── lisdexamfetamine.md
│           │   ├── mcpp.fa.md
│           │   ├── mcpp.md
│           │   ├── mdpv.fa.md
│           │   ├── mdpv.md
│           │   ├── mephedrone.fa.md
│           │   ├── mephedrone.md
│           │   ├── methamphetamine.fa.md
│           │   ├── methamphetamine.md
│           │   ├── methcathinone.fa.md
│           │   ├── methcathinone.md
│           │   ├── methiopropamine.fa.md
│           │   ├── methiopropamine.md
│           │   ├── methylnaphthidate.fa.md
│           │   ├── methylnaphthidate.md
│           │   ├── methylphenidate.fa.md
│           │   ├── methylphenidate.md
│           │   ├── mexedrone.fa.md
│           │   ├── mexedrone.md
│           │   ├── n-ethylhexedrone.fa.md
│           │   ├── n-ethylhexedrone.md
│           │   ├── n-ethylpentedrone.fa.md
│           │   ├── n-ethylpentedrone.md
│           │   ├── nicotine.fa.md
│           │   ├── nicotine.md
│           │   ├── nm-2-ai.fa.md
│           │   ├── nm-2-ai.md
│           │   ├── pentedrone.fa.md
│           │   ├── pentedrone.md
│           │   ├── phenidates.fa.md
│           │   ├── phenidates.md
│           │   ├── phenmetrazines.fa.md
│           │   ├── phenmetrazines.md
│           │   ├── php.fa.md
│           │   ├── php.md
│           │   ├── piperazines.fa.md
│           │   ├── piperazines.md
│           │   ├── prolintane.fa.md
│           │   ├── prolintane.md
│           │   ├── propylhexedrine.fa.md
│           │   ├── propylhexedrine.md
│           │   ├── pvp.fa.md
│           │   ├── pvp.md
│           │   ├── pyrrolidinophenones.fa.md
│           │   ├── pyrrolidinophenones.md
│           │   ├── rti-111.fa.md
│           │   ├── rti-111.md
│           │   ├── stimulants.fa.md
│           │   ├── stimulants.md
│           │   ├── theacrine.fa.md
│           │   ├── theacrine.md
│           │   ├── tropanes.fa.md
│           │   ├── tropanes.md
│           │   ├── xanthines.fa.md
│           │   └── xanthines.md
│           ├── Tryptamines
│           │   ├── Base Tryptamines
│           │   │   ├── amt.fa.md
│           │   │   ├── amt.md
│           │   │   ├── det.fa.md
│           │   │   ├── det.md
│           │   │   ├── dipt.fa.md
│           │   │   ├── dipt.md
│           │   │   ├── dmt.fa.md
│           │   │   ├── dmt.md
│           │   │   ├── dpt.fa.md
│           │   │   ├── dpt.md
│           │   │   ├── ept.fa.md
│           │   │   ├── ept.md
│           │   │   ├── met.fa.md
│           │   │   ├── met.md
│           │   │   ├── mipt.fa.md
│           │   │   ├── mipt.md
│           │   │   ├── mpt.fa.md
│           │   │   ├── mpt.md
│           │   │   ├── tryptamines.fa.md
│           │   │   └── tryptamines.md
│           │   └── Substituted tryptamines
│           │       ├── 4-aco-det.fa.md
│           │       ├── 4-aco-det.md
│           │       ├── 4-aco-dipt.fa.md
│           │       ├── 4-aco-dipt.md
│           │       ├── 4-aco-dmt.fa.md
│           │       ├── 4-aco-dmt.md
│           │       ├── 4-aco-met.fa.md
│           │       ├── 4-aco-met.md
│           │       ├── 4-aco-mipt.fa.md
│           │       ├── 4-aco-mipt.md
│           │       ├── 4-ho-det.fa.md
│           │       ├── 4-ho-det.md
│           │       ├── 4-ho-dipt.fa.md
│           │       ├── 4-ho-dipt.md
│           │       ├── 4-ho-dpt.fa.md
│           │       ├── 4-ho-dpt.md
│           │       ├── 4-ho-ept.fa.md
│           │       ├── 4-ho-ept.md
│           │       ├── 4-ho-met.fa.md
│           │       ├── 4-ho-met.md
│           │       ├── 4-ho-mipt.fa.md
│           │       ├── 4-ho-mipt.md
│           │       ├── 4-ho-mpt.fa.md
│           │       ├── 4-ho-mpt.md
│           │       ├── 5-meo-dalt.fa.md
│           │       ├── 5-meo-dalt.md
│           │       ├── 5-meo-dipt.fa.md
│           │       ├── 5-meo-dipt.md
│           │       ├── 5-meo-dmt.fa.md
│           │       ├── 5-meo-dmt.md
│           │       ├── 5-meo-mipt.fa.md
│           │       ├── 5-meo-mipt.md
│           │       ├── 56-mdo-dmt.fa.md
│           │       ├── 56-mdo-dmt.md
│           │       ├── baeocystin.fa.md
│           │       ├── baeocystin.md
│           │       ├── bufotenin.fa.md
│           │       ├── bufotenin.md
│           │       ├── psilocin.fa.md
│           │       ├── psilocin.md
│           │       ├── psilocybin.fa.md
│           │       ├── psilocybin.md
│           │       ├── substituted-tryptamines.fa.md
│           │       └── substituted-tryptamines.md
│           └── β-Carbolines
│               ├── carbolines.fa.md
│               ├── carbolines.md
│               ├── harmaline.fa.md
│               ├── harmaline.md
│               ├── harmine.fa.md
│               ├── harmine.md
│               ├── tetrahydroharmine.fa.md
│               └── tetrahydroharmine.md
└── tsconfig.json
```

---
### `.env`
```
CHOKIDAR_USEPOLLING=true

```

---
### `astro.config.mjs`
```mjs
import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  output: "static",
  vite: { 
    plugins: [tailwindcss()],
    // Remove the entire server.watch section or set usePolling to false
    server: {
      watch: {
        usePolling: false, // Or remove this entire block
      },
    },
  },
});
```

---
### `categorizer.py`
```py
import os
import shutil
import yaml

# CHANGE THIS if your path is different
ROOT = "src/wiki"

def extract_frontmatter(file_path):
    """
    Extract YAML frontmatter from a markdown file.
    Returns a dict or None.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or not lines[0].strip().startswith("---"):
        return None

    yaml_lines = []
    for line in lines[1:]:
        if line.strip().startswith("---"):
            break
        yaml_lines.append(line)

    try:
        return yaml.safe_load("".join(yaml_lines))
    except Exception as e:
        print(f"[WARN] Could not parse YAML in {file_path}: {e}")
        return None


def categorize_files():
    for root, _, files in os.walk(ROOT):
        for file in files:
            if not file.endswith(".md"):
                continue

            full_path = os.path.join(root, file)

            # Skip files already inside a category folder
            # (ROOT/category/file.md → category already done)
            rel_path = os.path.relpath(full_path, ROOT)
            if os.path.dirname(rel_path) != "":
                continue

            front = extract_frontmatter(full_path)
            if not front:
                print(f"[SKIP] No frontmatter: {file}")
                continue

            category = front.get("category")
            if not category:
                print(f"[SKIP] No category in: {file}")
                continue

            # Create category folder if missing
            category_folder = os.path.join(ROOT, category)
            if not os.path.exists(category_folder):
                print(f"[CREATE] Folder: {category_folder}")
                os.makedirs(category_folder, exist_ok=True)

            # Move file
            new_path = os.path.join(category_folder, file)

            print(f"[MOVE] {file} → {category}/")
            shutil.move(full_path, new_path)


if __name__ == "__main__":
    print("📂 Running Wiki Categorizer…")
    categorize_files()
    print("✅ Done.")

```

---
### `components.json`
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/global.css",
    "baseColor": "gray",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "registries": {}
}

```

---
### `duplicator.py`
```py
import os
import shutil

# ROOT folder of your wiki (change if needed)
ROOT = "src/wiki"

def duplicate_md_files():
    for root, _, files in os.walk(ROOT):
        for file in files:
            # Only target English files (*.md but not *.fa.md)
            if file.endswith(".md") and not file.endswith(".fa.md"):
                
                original_path = os.path.join(root, file)
                fa_filename = file.replace(".md", ".fa.md")
                fa_path = os.path.join(root, fa_filename)

                # If .fa.md already exists, skip
                if os.path.exists(fa_path):
                    print(f"[SKIP] Already exists: {fa_path}")
                    continue

                # Duplicate the file
                shutil.copy2(original_path, fa_path)
                print(f"[CREATE] {fa_path}")

    print("✅ Done duplicating .md → .fa.md files.")

if __name__ == "__main__":
    duplicate_md_files()

```

---
### `env.d.ts`
```ts
/// <reference types="astro/client" />

```

---
### `package.json`
```json
{
  "name": "coughynet",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro",
    "clean": "rimraf node_modules .astro .vite"
  },
  "dependencies": {
    "@astrojs/rss": "^4.0.13",
    "@tailwindcss/vite": "^4.1.17",
    "@types/node": "24.10.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "tailwind-merge": "^3.4.0",
    "tailwindcss": "^4.1.17"
  },
  "devDependencies": {
    "astro": "^5.15.5",
    "tw-animate-css": "^1.4.0"
  }
}
```

---
### `pnpm-lock.yaml`
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      '@astrojs/rss':
        specifier: ^4.0.13
        version: 4.0.13
      '@tailwindcss/vite':
        specifier: ^4.1.17
        version: 4.1.17(vite@6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2))
      '@types/node':
        specifier: 24.10.0
        version: 24.10.0
      class-variance-authority:
        specifier: ^0.7.1
        version: 0.7.1
      clsx:
        specifier: ^2.1.1
        version: 2.1.1
      tailwind-merge:
        specifier: ^3.4.0
        version: 3.4.0
      tailwindcss:
        specifier: ^4.1.17
        version: 4.1.17
    devDependencies:
      astro:
        specifier: ^5.15.5
        version: 5.15.5(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2)(rollup@4.53.2)(typescript@5.9.3)
      tw-animate-css:
        specifier: ^1.4.0
        version: 1.4.0

packages:

  '@astrojs/compiler@2.13.0':
    resolution: {integrity: sha512-mqVORhUJViA28fwHYaWmsXSzLO9osbdZ5ImUfxBarqsYdMlPbqAqGJCxsNzvppp1BEzc1mJNjOVvQqeDN8Vspw==}

  '@astrojs/internal-helpers@0.7.4':
    resolution: {integrity: sha512-lDA9MqE8WGi7T/t2BMi+EAXhs4Vcvr94Gqx3q15cFEz8oFZMO4/SFBqYr/UcmNlvW+35alowkVj+w9VhLvs5Cw==}

  '@astrojs/markdown-remark@6.3.8':
    resolution: {integrity: sha512-uFNyFWadnULWK2cOw4n0hLKeu+xaVWeuECdP10cQ3K2fkybtTlhb7J7TcScdjmS8Yps7oje9S/ehYMfZrhrgCg==}

  '@astrojs/prism@3.3.0':
    resolution: {integrity: sha512-q8VwfU/fDZNoDOf+r7jUnMC2//H2l0TuQ6FkGJL8vD8nw/q5KiL3DS1KKBI3QhI9UQhpJ5dc7AtqfbXWuOgLCQ==}
    engines: {node: 18.20.8 || ^20.3.0 || >=22.0.0}

  '@astrojs/rss@4.0.13':
    resolution: {integrity: sha512-ugW4DmGn8kgfl8/qecU3EcKCAuEBrZqY7eYfa6at0sY7HGEwRdzsOafLE437RwDMP2ZuxfKnCNABs99YVhX0kg==}

  '@astrojs/telemetry@3.3.0':
    resolution: {integrity: sha512-UFBgfeldP06qu6khs/yY+q1cDAaArM2/7AEIqQ9Cuvf7B1hNLq0xDrZkct+QoIGyjq56y8IaE2I3CTvG99mlhQ==}
    engines: {node: 18.20.8 || ^20.3.0 || >=22.0.0}

  '@babel/helper-string-parser@7.27.1':
    resolution: {integrity: sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.28.5':
    resolution: {integrity: sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.28.5':
    resolution: {integrity: sha512-KKBU1VGYR7ORr3At5HAtUQ+TV3SzRCXmA/8OdDZiLDBIZxVyzXuztPjfLd3BV1PRAQGCMWWSHYhL0F8d5uHBDQ==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/types@7.28.5':
    resolution: {integrity: sha512-qQ5m48eI/MFLQ5PxQj4PFaprjyCTLI37ElWMmNs0K8Lk3dVeOdNpB3ks8jc7yM5CDmVC73eMVk/trk3fgmrUpA==}
    engines: {node: '>=6.9.0'}

  '@capsizecss/unpack@3.0.0':
    resolution: {integrity: sha512-+ntATQe1AlL7nTOYjwjj6w3299CgRot48wL761TUGYpYgAou3AaONZazp0PKZyCyWhudWsjhq1nvRHOvbMzhTA==}
    engines: {node: '>=18'}

  '@emnapi/runtime@1.7.0':
    resolution: {integrity: sha512-oAYoQnCYaQZKVS53Fq23ceWMRxq5EhQsE0x0RdQ55jT7wagMu5k+fS39v1fiSLrtrLQlXwVINenqhLMtTrV/1Q==}

  '@esbuild/aix-ppc64@0.25.12':
    resolution: {integrity: sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.25.12':
    resolution: {integrity: sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.25.12':
    resolution: {integrity: sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.25.12':
    resolution: {integrity: sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.25.12':
    resolution: {integrity: sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.25.12':
    resolution: {integrity: sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.25.12':
    resolution: {integrity: sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.25.12':
    resolution: {integrity: sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.25.12':
    resolution: {integrity: sha512-8bwX7a8FghIgrupcxb4aUmYDLp8pX06rGh5HqDT7bB+8Rdells6mHvrFHHW2JAOPZUbnjUpKTLg6ECyzvas2AQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.25.12':
    resolution: {integrity: sha512-lPDGyC1JPDou8kGcywY0YILzWlhhnRjdof3UlcoqYmS9El818LLfJJc3PXXgZHrHCAKs/Z2SeZtDJr5MrkxtOw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.25.12':
    resolution: {integrity: sha512-0y9KrdVnbMM2/vG8KfU0byhUN+EFCny9+8g202gYqSSVMonbsCfLjUO+rCci7pM0WBEtz+oK/PIwHkzxkyharA==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.25.12':
    resolution: {integrity: sha512-h///Lr5a9rib/v1GGqXVGzjL4TMvVTv+s1DPoxQdz7l/AYv6LDSxdIwzxkrPW438oUXiDtwM10o9PmwS/6Z0Ng==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.25.12':
    resolution: {integrity: sha512-iyRrM1Pzy9GFMDLsXn1iHUm18nhKnNMWscjmp4+hpafcZjrr2WbT//d20xaGljXDBYHqRcl8HnxbX6uaA/eGVw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.25.12':
    resolution: {integrity: sha512-9meM/lRXxMi5PSUqEXRCtVjEZBGwB7P/D4yT8UG/mwIdze2aV4Vo6U5gD3+RsoHXKkHCfSxZKzmDssVlRj1QQA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.25.12':
    resolution: {integrity: sha512-Zr7KR4hgKUpWAwb1f3o5ygT04MzqVrGEGXGLnj15YQDJErYu/BGg+wmFlIDOdJp0PmB0lLvxFIOXZgFRrdjR0w==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.25.12':
    resolution: {integrity: sha512-MsKncOcgTNvdtiISc/jZs/Zf8d0cl/t3gYWX8J9ubBnVOwlk65UIEEvgBORTiljloIWnBzLs4qhzPkJcitIzIg==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.25.12':
    resolution: {integrity: sha512-uqZMTLr/zR/ed4jIGnwSLkaHmPjOjJvnm6TVVitAa08SLS9Z0VM8wIRx7gWbJB5/J54YuIMInDquWyYvQLZkgw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.25.12':
    resolution: {integrity: sha512-xXwcTq4GhRM7J9A8Gv5boanHhRa/Q9KLVmcyXHCTaM4wKfIpWkdXiMog/KsnxzJ0A1+nD+zoecuzqPmCRyBGjg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.25.12':
    resolution: {integrity: sha512-Ld5pTlzPy3YwGec4OuHh1aCVCRvOXdH8DgRjfDy/oumVovmuSzWfnSJg+VtakB9Cm0gxNO9BzWkj6mtO1FMXkQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.25.12':
    resolution: {integrity: sha512-fF96T6KsBo/pkQI950FARU9apGNTSlZGsv1jZBAlcLL1MLjLNIWPBkj5NlSz8aAzYKg+eNqknrUJ24QBybeR5A==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.25.12':
    resolution: {integrity: sha512-MZyXUkZHjQxUvzK7rN8DJ3SRmrVrke8ZyRusHlP+kuwqTcfWLyqMOE3sScPPyeIXN/mDJIfGXvcMqCgYKekoQw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openharmony-arm64@0.25.12':
    resolution: {integrity: sha512-rm0YWsqUSRrjncSXGA7Zv78Nbnw4XL6/dzr20cyrQf7ZmRcsovpcRBdhD43Nuk3y7XIoW2OxMVvwuRvk9XdASg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openharmony]

  '@esbuild/sunos-x64@0.25.12':
    resolution: {integrity: sha512-3wGSCDyuTHQUzt0nV7bocDy72r2lI33QL3gkDNGkod22EsYl04sMf0qLb8luNKTOmgF/eDEDP5BFNwoBKH441w==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/win32-arm64@0.25.12':
    resolution: {integrity: sha512-rMmLrur64A7+DKlnSuwqUdRKyd3UE7oPJZmnljqEptesKM8wx9J8gx5u0+9Pq0fQQW8vqeKebwNXdfOyP+8Bsg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-ia32@0.25.12':
    resolution: {integrity: sha512-HkqnmmBoCbCwxUKKNPBixiWDGCpQGVsrQfJoVGYLPT41XWF8lHuE5N6WhVia2n4o5QK5M4tYr21827fNhi4byQ==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-x64@0.25.12':
    resolution: {integrity: sha512-alJC0uCZpTFrSL0CCDjcgleBXPnCrEAhTBILpeAp7M/OFgoqtAetfBzX0xM00MUsVVPpVjlPuMbREqnZCXaTnA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [win32]

  '@img/colour@1.0.0':
    resolution: {integrity: sha512-A5P/LfWGFSl6nsckYtjw9da+19jB8hkJ6ACTGcDfEJ0aE+l2n2El7dsVM7UVHZQ9s2lmYMWlrS21YLy2IR1LUw==}
    engines: {node: '>=18'}

  '@img/sharp-darwin-arm64@0.34.5':
    resolution: {integrity: sha512-imtQ3WMJXbMY4fxb/Ndp6HBTNVtWCUI0WdobyheGf5+ad6xX8VIDO8u2xE4qc/fr08CKG/7dDseFtn6M6g/r3w==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [arm64]
    os: [darwin]

  '@img/sharp-darwin-x64@0.34.5':
    resolution: {integrity: sha512-YNEFAF/4KQ/PeW0N+r+aVVsoIY0/qxxikF2SWdp+NRkmMB7y9LBZAVqQ4yhGCm/H3H270OSykqmQMKLBhBJDEw==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [x64]
    os: [darwin]

  '@img/sharp-libvips-darwin-arm64@1.2.4':
    resolution: {integrity: sha512-zqjjo7RatFfFoP0MkQ51jfuFZBnVE2pRiaydKJ1G/rHZvnsrHAOcQALIi9sA5co5xenQdTugCvtb1cuf78Vf4g==}
    cpu: [arm64]
    os: [darwin]

  '@img/sharp-libvips-darwin-x64@1.2.4':
    resolution: {integrity: sha512-1IOd5xfVhlGwX+zXv2N93k0yMONvUlANylbJw1eTah8K/Jtpi15KC+WSiaX/nBmbm2HxRM1gZ0nSdjSsrZbGKg==}
    cpu: [x64]
    os: [darwin]

  '@img/sharp-libvips-linux-arm64@1.2.4':
    resolution: {integrity: sha512-excjX8DfsIcJ10x1Kzr4RcWe1edC9PquDRRPx3YVCvQv+U5p7Yin2s32ftzikXojb1PIFc/9Mt28/y+iRklkrw==}
    cpu: [arm64]
    os: [linux]

  '@img/sharp-libvips-linux-arm@1.2.4':
    resolution: {integrity: sha512-bFI7xcKFELdiNCVov8e44Ia4u2byA+l3XtsAj+Q8tfCwO6BQ8iDojYdvoPMqsKDkuoOo+X6HZA0s0q11ANMQ8A==}
    cpu: [arm]
    os: [linux]

  '@img/sharp-libvips-linux-ppc64@1.2.4':
    resolution: {integrity: sha512-FMuvGijLDYG6lW+b/UvyilUWu5Ayu+3r2d1S8notiGCIyYU/76eig1UfMmkZ7vwgOrzKzlQbFSuQfgm7GYUPpA==}
    cpu: [ppc64]
    os: [linux]

  '@img/sharp-libvips-linux-riscv64@1.2.4':
    resolution: {integrity: sha512-oVDbcR4zUC0ce82teubSm+x6ETixtKZBh/qbREIOcI3cULzDyb18Sr/Wcyx7NRQeQzOiHTNbZFF1UwPS2scyGA==}
    cpu: [riscv64]
    os: [linux]

  '@img/sharp-libvips-linux-s390x@1.2.4':
    resolution: {integrity: sha512-qmp9VrzgPgMoGZyPvrQHqk02uyjA0/QrTO26Tqk6l4ZV0MPWIW6LTkqOIov+J1yEu7MbFQaDpwdwJKhbJvuRxQ==}
    cpu: [s390x]
    os: [linux]

  '@img/sharp-libvips-linux-x64@1.2.4':
    resolution: {integrity: sha512-tJxiiLsmHc9Ax1bz3oaOYBURTXGIRDODBqhveVHonrHJ9/+k89qbLl0bcJns+e4t4rvaNBxaEZsFtSfAdquPrw==}
    cpu: [x64]
    os: [linux]

  '@img/sharp-libvips-linuxmusl-arm64@1.2.4':
    resolution: {integrity: sha512-FVQHuwx1IIuNow9QAbYUzJ+En8KcVm9Lk5+uGUQJHaZmMECZmOlix9HnH7n1TRkXMS0pGxIJokIVB9SuqZGGXw==}
    cpu: [arm64]
    os: [linux]

  '@img/sharp-libvips-linuxmusl-x64@1.2.4':
    resolution: {integrity: sha512-+LpyBk7L44ZIXwz/VYfglaX/okxezESc6UxDSoyo2Ks6Jxc4Y7sGjpgU9s4PMgqgjj1gZCylTieNamqA1MF7Dg==}
    cpu: [x64]
    os: [linux]

  '@img/sharp-linux-arm64@0.34.5':
    resolution: {integrity: sha512-bKQzaJRY/bkPOXyKx5EVup7qkaojECG6NLYswgktOZjaXecSAeCWiZwwiFf3/Y+O1HrauiE3FVsGxFg8c24rZg==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [arm64]
    os: [linux]

  '@img/sharp-linux-arm@0.34.5':
    resolution: {integrity: sha512-9dLqsvwtg1uuXBGZKsxem9595+ujv0sJ6Vi8wcTANSFpwV/GONat5eCkzQo/1O6zRIkh0m/8+5BjrRr7jDUSZw==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [arm]
    os: [linux]

  '@img/sharp-linux-ppc64@0.34.5':
    resolution: {integrity: sha512-7zznwNaqW6YtsfrGGDA6BRkISKAAE1Jo0QdpNYXNMHu2+0dTrPflTLNkpc8l7MUP5M16ZJcUvysVWWrMefZquA==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [ppc64]
    os: [linux]

  '@img/sharp-linux-riscv64@0.34.5':
    resolution: {integrity: sha512-51gJuLPTKa7piYPaVs8GmByo7/U7/7TZOq+cnXJIHZKavIRHAP77e3N2HEl3dgiqdD/w0yUfiJnII77PuDDFdw==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [riscv64]
    os: [linux]

  '@img/sharp-linux-s390x@0.34.5':
    resolution: {integrity: sha512-nQtCk0PdKfho3eC5MrbQoigJ2gd1CgddUMkabUj+rBevs8tZ2cULOx46E7oyX+04WGfABgIwmMC0VqieTiR4jg==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [s390x]
    os: [linux]

  '@img/sharp-linux-x64@0.34.5':
    resolution: {integrity: sha512-MEzd8HPKxVxVenwAa+JRPwEC7QFjoPWuS5NZnBt6B3pu7EG2Ge0id1oLHZpPJdn3OQK+BQDiw9zStiHBTJQQQQ==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [x64]
    os: [linux]

  '@img/sharp-linuxmusl-arm64@0.34.5':
    resolution: {integrity: sha512-fprJR6GtRsMt6Kyfq44IsChVZeGN97gTD331weR1ex1c1rypDEABN6Tm2xa1wE6lYb5DdEnk03NZPqA7Id21yg==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [arm64]
    os: [linux]

  '@img/sharp-linuxmusl-x64@0.34.5':
    resolution: {integrity: sha512-Jg8wNT1MUzIvhBFxViqrEhWDGzqymo3sV7z7ZsaWbZNDLXRJZoRGrjulp60YYtV4wfY8VIKcWidjojlLcWrd8Q==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [x64]
    os: [linux]

  '@img/sharp-wasm32@0.34.5':
    resolution: {integrity: sha512-OdWTEiVkY2PHwqkbBI8frFxQQFekHaSSkUIJkwzclWZe64O1X4UlUjqqqLaPbUpMOQk6FBu/HtlGXNblIs0huw==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [wasm32]

  '@img/sharp-win32-arm64@0.34.5':
    resolution: {integrity: sha512-WQ3AgWCWYSb2yt+IG8mnC6Jdk9Whs7O0gxphblsLvdhSpSTtmu69ZG1Gkb6NuvxsNACwiPV6cNSZNzt0KPsw7g==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [arm64]
    os: [win32]

  '@img/sharp-win32-ia32@0.34.5':
    resolution: {integrity: sha512-FV9m/7NmeCmSHDD5j4+4pNI8Cp3aW+JvLoXcTUo0IqyjSfAZJ8dIUmijx1qaJsIiU+Hosw6xM5KijAWRJCSgNg==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [ia32]
    os: [win32]

  '@img/sharp-win32-x64@0.34.5':
    resolution: {integrity: sha512-+29YMsqY2/9eFEiW93eqWnuLcWcufowXewwSNIT6UwZdUUCrM3oFjMWH/Z6/TMmb4hlFenmfAVbpWeup2jryCw==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
    cpu: [x64]
    os: [win32]

  '@jridgewell/gen-mapping@0.3.13':
    resolution: {integrity: sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==}

  '@jridgewell/remapping@2.3.5':
    resolution: {integrity: sha512-LI9u/+laYG4Ds1TDKSJW2YPrIlcVYOwi2fUC6xB43lueCjgxV4lffOCZCtYFiH6TNOX+tQKXx97T4IKHbhyHEQ==}

  '@jridgewell/resolve-uri@3.1.2':
    resolution: {integrity: sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==}
    engines: {node: '>=6.0.0'}

  '@jridgewell/sourcemap-codec@1.5.5':
    resolution: {integrity: sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==}

  '@jridgewell/trace-mapping@0.3.31':
    resolution: {integrity: sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==}

  '@oslojs/encoding@1.1.0':
    resolution: {integrity: sha512-70wQhgYmndg4GCPxPPxPGevRKqTIJ2Nh4OkiMWmDAVYsTQ+Ta7Sq+rPevXyXGdzr30/qZBnyOalCszoMxlyldQ==}

  '@rollup/pluginutils@5.3.0':
    resolution: {integrity: sha512-5EdhGZtnu3V88ces7s53hhfK5KSASnJZv8Lulpc04cWO3REESroJXg73DFsOmgbU2BhwV0E20bu2IDZb3VKW4Q==}
    engines: {node: '>=14.0.0'}
    peerDependencies:
      rollup: ^1.20.0||^2.0.0||^3.0.0||^4.0.0
    peerDependenciesMeta:
      rollup:
        optional: true

  '@rollup/rollup-android-arm-eabi@4.53.2':
    resolution: {integrity: sha512-yDPzwsgiFO26RJA4nZo8I+xqzh7sJTZIWQOxn+/XOdPE31lAvLIYCKqjV+lNH/vxE2L2iH3plKxDCRK6i+CwhA==}
    cpu: [arm]
    os: [android]

  '@rollup/rollup-android-arm64@4.53.2':
    resolution: {integrity: sha512-k8FontTxIE7b0/OGKeSN5B6j25EuppBcWM33Z19JoVT7UTXFSo3D9CdU39wGTeb29NO3XxpMNauh09B+Ibw+9g==}
    cpu: [arm64]
    os: [android]

  '@rollup/rollup-darwin-arm64@4.53.2':
    resolution: {integrity: sha512-A6s4gJpomNBtJ2yioj8bflM2oogDwzUiMl2yNJ2v9E7++sHrSrsQ29fOfn5DM/iCzpWcebNYEdXpaK4tr2RhfQ==}
    cpu: [arm64]
    os: [darwin]

  '@rollup/rollup-darwin-x64@4.53.2':
    resolution: {integrity: sha512-e6XqVmXlHrBlG56obu9gDRPW3O3hLxpwHpLsBJvuI8qqnsrtSZ9ERoWUXtPOkY8c78WghyPHZdmPhHLWNdAGEw==}
    cpu: [x64]
    os: [darwin]

  '@rollup/rollup-freebsd-arm64@4.53.2':
    resolution: {integrity: sha512-v0E9lJW8VsrwPux5Qe5CwmH/CF/2mQs6xU1MF3nmUxmZUCHazCjLgYvToOk+YuuUqLQBio1qkkREhxhc656ViA==}
    cpu: [arm64]
    os: [freebsd]

  '@rollup/rollup-freebsd-x64@4.53.2':
    resolution: {integrity: sha512-ClAmAPx3ZCHtp6ysl4XEhWU69GUB1D+s7G9YjHGhIGCSrsg00nEGRRZHmINYxkdoJehde8VIsDC5t9C0gb6yqA==}
    cpu: [x64]
    os: [freebsd]

  '@rollup/rollup-linux-arm-gnueabihf@4.53.2':
    resolution: {integrity: sha512-EPlb95nUsz6Dd9Qy13fI5kUPXNSljaG9FiJ4YUGU1O/Q77i5DYFW5KR8g1OzTcdZUqQQ1KdDqsTohdFVwCwjqg==}
    cpu: [arm]
    os: [linux]

  '@rollup/rollup-linux-arm-musleabihf@4.53.2':
    resolution: {integrity: sha512-BOmnVW+khAUX+YZvNfa0tGTEMVVEerOxN0pDk2E6N6DsEIa2Ctj48FOMfNDdrwinocKaC7YXUZ1pHlKpnkja/Q==}
    cpu: [arm]
    os: [linux]

  '@rollup/rollup-linux-arm64-gnu@4.53.2':
    resolution: {integrity: sha512-Xt2byDZ+6OVNuREgBXr4+CZDJtrVso5woFtpKdGPhpTPHcNG7D8YXeQzpNbFRxzTVqJf7kvPMCub/pcGUWgBjA==}
    cpu: [arm64]
    os: [linux]

  '@rollup/rollup-linux-arm64-musl@4.53.2':
    resolution: {integrity: sha512-+LdZSldy/I9N8+klim/Y1HsKbJ3BbInHav5qE9Iy77dtHC/pibw1SR/fXlWyAk0ThnpRKoODwnAuSjqxFRDHUQ==}
    cpu: [arm64]
    os: [linux]

  '@rollup/rollup-linux-loong64-gnu@4.53.2':
    resolution: {integrity: sha512-8ms8sjmyc1jWJS6WdNSA23rEfdjWB30LH8Wqj0Cqvv7qSHnvw6kgMMXRdop6hkmGPlyYBdRPkjJnj3KCUHV/uQ==}
    cpu: [loong64]
    os: [linux]

  '@rollup/rollup-linux-ppc64-gnu@4.53.2':
    resolution: {integrity: sha512-3HRQLUQbpBDMmzoxPJYd3W6vrVHOo2cVW8RUo87Xz0JPJcBLBr5kZ1pGcQAhdZgX9VV7NbGNipah1omKKe23/g==}
    cpu: [ppc64]
    os: [linux]

  '@rollup/rollup-linux-riscv64-gnu@4.53.2':
    resolution: {integrity: sha512-fMjKi+ojnmIvhk34gZP94vjogXNNUKMEYs+EDaB/5TG/wUkoeua7p7VCHnE6T2Tx+iaghAqQX8teQzcvrYpaQA==}
    cpu: [riscv64]
    os: [linux]

  '@rollup/rollup-linux-riscv64-musl@4.53.2':
    resolution: {integrity: sha512-XuGFGU+VwUUV5kLvoAdi0Wz5Xbh2SrjIxCtZj6Wq8MDp4bflb/+ThZsVxokM7n0pcbkEr2h5/pzqzDYI7cCgLQ==}
    cpu: [riscv64]
    os: [linux]

  '@rollup/rollup-linux-s390x-gnu@4.53.2':
    resolution: {integrity: sha512-w6yjZF0P+NGzWR3AXWX9zc0DNEGdtvykB03uhonSHMRa+oWA6novflo2WaJr6JZakG2ucsyb+rvhrKac6NIy+w==}
    cpu: [s390x]
    os: [linux]

  '@rollup/rollup-linux-x64-gnu@4.53.2':
    resolution: {integrity: sha512-yo8d6tdfdeBArzC7T/PnHd7OypfI9cbuZzPnzLJIyKYFhAQ8SvlkKtKBMbXDxe1h03Rcr7u++nFS7tqXz87Gtw==}
    cpu: [x64]
    os: [linux]

  '@rollup/rollup-linux-x64-musl@4.53.2':
    resolution: {integrity: sha512-ah59c1YkCxKExPP8O9PwOvs+XRLKwh/mV+3YdKqQ5AMQ0r4M4ZDuOrpWkUaqO7fzAHdINzV9tEVu8vNw48z0lA==}
    cpu: [x64]
    os: [linux]

  '@rollup/rollup-openharmony-arm64@4.53.2':
    resolution: {integrity: sha512-4VEd19Wmhr+Zy7hbUsFZ6YXEiP48hE//KPLCSVNY5RMGX2/7HZ+QkN55a3atM1C/BZCGIgqN+xrVgtdak2S9+A==}
    cpu: [arm64]
    os: [openharmony]

  '@rollup/rollup-win32-arm64-msvc@4.53.2':
    resolution: {integrity: sha512-IlbHFYc/pQCgew/d5fslcy1KEaYVCJ44G8pajugd8VoOEI8ODhtb/j8XMhLpwHCMB3yk2J07ctup10gpw2nyMA==}
    cpu: [arm64]
    os: [win32]

  '@rollup/rollup-win32-ia32-msvc@4.53.2':
    resolution: {integrity: sha512-lNlPEGgdUfSzdCWU176ku/dQRnA7W+Gp8d+cWv73jYrb8uT7HTVVxq62DUYxjbaByuf1Yk0RIIAbDzp+CnOTFg==}
    cpu: [ia32]
    os: [win32]

  '@rollup/rollup-win32-x64-gnu@4.53.2':
    resolution: {integrity: sha512-S6YojNVrHybQis2lYov1sd+uj7K0Q05NxHcGktuMMdIQ2VixGwAfbJ23NnlvvVV1bdpR2m5MsNBViHJKcA4ADw==}
    cpu: [x64]
    os: [win32]

  '@rollup/rollup-win32-x64-msvc@4.53.2':
    resolution: {integrity: sha512-k+/Rkcyx//P6fetPoLMb8pBeqJBNGx81uuf7iljX9++yNBVRDQgD04L+SVXmXmh5ZP4/WOp4mWF0kmi06PW2tA==}
    cpu: [x64]
    os: [win32]

  '@shikijs/core@3.15.0':
    resolution: {integrity: sha512-8TOG6yG557q+fMsSVa8nkEDOZNTSxjbbR8l6lF2gyr6Np+jrPlslqDxQkN6rMXCECQ3isNPZAGszAfYoJOPGlg==}

  '@shikijs/engine-javascript@3.15.0':
    resolution: {integrity: sha512-ZedbOFpopibdLmvTz2sJPJgns8Xvyabe2QbmqMTz07kt1pTzfEvKZc5IqPVO/XFiEbbNyaOpjPBkkr1vlwS+qg==}

  '@shikijs/engine-oniguruma@3.15.0':
    resolution: {integrity: sha512-HnqFsV11skAHvOArMZdLBZZApRSYS4LSztk2K3016Y9VCyZISnlYUYsL2hzlS7tPqKHvNqmI5JSUJZprXloMvA==}

  '@shikijs/langs@3.15.0':
    resolution: {integrity: sha512-WpRvEFvkVvO65uKYW4Rzxs+IG0gToyM8SARQMtGGsH4GDMNZrr60qdggXrFOsdfOVssG/QQGEl3FnJ3EZ+8w8A==}

  '@shikijs/themes@3.15.0':
    resolution: {integrity: sha512-8ow2zWb1IDvCKjYb0KiLNrK4offFdkfNVPXb1OZykpLCzRU6j+efkY+Y7VQjNlNFXonSw+4AOdGYtmqykDbRiQ==}

  '@shikijs/types@3.15.0':
    resolution: {integrity: sha512-BnP+y/EQnhihgHy4oIAN+6FFtmfTekwOLsQbRw9hOKwqgNy8Bdsjq8B05oAt/ZgvIWWFrshV71ytOrlPfYjIJw==}

  '@shikijs/vscode-textmate@10.0.2':
    resolution: {integrity: sha512-83yeghZ2xxin3Nj8z1NMd/NCuca+gsYXswywDy5bHvwlWL8tpTQmzGeUuHd9FC3E/SBEMvzJRwWEOz5gGes9Qg==}

  '@swc/helpers@0.5.17':
    resolution: {integrity: sha512-5IKx/Y13RsYd+sauPb2x+U/xZikHjolzfuDgTAl/Tdf3Q8rslRvC19NKDLgAJQ6wsqADk10ntlv08nPFw/gO/A==}

  '@tailwindcss/node@4.1.17':
    resolution: {integrity: sha512-csIkHIgLb3JisEFQ0vxr2Y57GUNYh447C8xzwj89U/8fdW8LhProdxvnVH6U8M2Y73QKiTIH+LWbK3V2BBZsAg==}

  '@tailwindcss/oxide-android-arm64@4.1.17':
    resolution: {integrity: sha512-BMqpkJHgOZ5z78qqiGE6ZIRExyaHyuxjgrJ6eBO5+hfrfGkuya0lYfw8fRHG77gdTjWkNWEEm+qeG2cDMxArLQ==}
    engines: {node: '>= 10'}
    cpu: [arm64]
    os: [android]

  '@tailwindcss/oxide-darwin-arm64@4.1.17':
    resolution: {integrity: sha512-EquyumkQweUBNk1zGEU/wfZo2qkp/nQKRZM8bUYO0J+Lums5+wl2CcG1f9BgAjn/u9pJzdYddHWBiFXJTcxmOg==}
    engines: {node: '>= 10'}
    cpu: [arm64]
    os: [darwin]

  '@tailwindcss/oxide-darwin-x64@4.1.17':
    resolution: {integrity: sha512-gdhEPLzke2Pog8s12oADwYu0IAw04Y2tlmgVzIN0+046ytcgx8uZmCzEg4VcQh+AHKiS7xaL8kGo/QTiNEGRog==}
    engines: {node: '>= 10'}
    cpu: [x64]
    os: [darwin]

  '@tailwindcss/oxide-freebsd-x64@4.1.17':
    resolution: {integrity: sha512-hxGS81KskMxML9DXsaXT1H0DyA+ZBIbyG/sSAjWNe2EDl7TkPOBI42GBV3u38itzGUOmFfCzk1iAjDXds8Oh0g==}
    engines: {node: '>= 10'}
    cpu: [x64]
    os: [freebsd]

  '@tailwindcss/oxide-linux-arm-gnueabihf@4.1.17':
    resolution: {integrity: sha512-k7jWk5E3ldAdw0cNglhjSgv501u7yrMf8oeZ0cElhxU6Y2o7f8yqelOp3fhf7evjIS6ujTI3U8pKUXV2I4iXHQ==}
    engines: {node: '>= 10'}
    cpu: [arm]
    os: [linux]

  '@tailwindcss/oxide-linux-arm64-gnu@4.1.17':
    resolution: {integrity: sha512-HVDOm/mxK6+TbARwdW17WrgDYEGzmoYayrCgmLEw7FxTPLcp/glBisuyWkFz/jb7ZfiAXAXUACfyItn+nTgsdQ==}
    engines: {node: '>= 10'}
    cpu: [arm64]
    os: [linux]

  '@tailwindcss/oxide-linux-arm64-musl@4.1.17':
    resolution: {integrity: sha512-HvZLfGr42i5anKtIeQzxdkw/wPqIbpeZqe7vd3V9vI3RQxe3xU1fLjss0TjyhxWcBaipk7NYwSrwTwK1hJARMg==}
    engines: {node: '>= 10'}
    cpu: [arm64]
    os: [linux]

  '@tailwindcss/oxide-linux-x64-gnu@4.1.17':
    resolution: {integrity: sha512-M3XZuORCGB7VPOEDH+nzpJ21XPvK5PyjlkSFkFziNHGLc5d6g3di2McAAblmaSUNl8IOmzYwLx9NsE7bplNkwQ==}
    engines: {node: '>= 10'}
    cpu: [x64]
    os: [linux]

  '@tailwindcss/oxide-linux-x64-musl@4.1.17':
    resolution: {integrity: sha512-k7f+pf9eXLEey4pBlw+8dgfJHY4PZ5qOUFDyNf7SI6lHjQ9Zt7+NcscjpwdCEbYi6FI5c2KDTDWyf2iHcCSyyQ==}
    engines: {node: '>= 10'}
    cpu: [x64]
    os: [linux]

  '@tailwindcss/oxide-wasm32-wasi@4.1.17':
    resolution: {integrity: sha512-cEytGqSSoy7zK4JRWiTCx43FsKP/zGr0CsuMawhH67ONlH+T79VteQeJQRO/X7L0juEUA8ZyuYikcRBf0vsxhg==}
    engines: {node: '>=14.0.0'}
    cpu: [wasm32]
    bundledDependencies:
      - '@napi-rs/wasm-runtime'
      - '@emnapi/core'
      - '@emnapi/runtime'
      - '@tybys/wasm-util'
      - '@emnapi/wasi-threads'
      - tslib

  '@tailwindcss/oxide-win32-arm64-msvc@4.1.17':
    resolution: {integrity: sha512-JU5AHr7gKbZlOGvMdb4722/0aYbU+tN6lv1kONx0JK2cGsh7g148zVWLM0IKR3NeKLv+L90chBVYcJ8uJWbC9A==}
    engines: {node: '>= 10'}
    cpu: [arm64]
    os: [win32]

  '@tailwindcss/oxide-win32-x64-msvc@4.1.17':
    resolution: {integrity: sha512-SKWM4waLuqx0IH+FMDUw6R66Hu4OuTALFgnleKbqhgGU30DY20NORZMZUKgLRjQXNN2TLzKvh48QXTig4h4bGw==}
    engines: {node: '>= 10'}
    cpu: [x64]
    os: [win32]

  '@tailwindcss/oxide@4.1.17':
    resolution: {integrity: sha512-F0F7d01fmkQhsTjXezGBLdrl1KresJTcI3DB8EkScCldyKp3Msz4hub4uyYaVnk88BAS1g5DQjjF6F5qczheLA==}
    engines: {node: '>= 10'}

  '@tailwindcss/vite@4.1.17':
    resolution: {integrity: sha512-4+9w8ZHOiGnpcGI6z1TVVfWaX/koK7fKeSYF3qlYg2xpBtbteP2ddBxiarL+HVgfSJGeK5RIxRQmKm4rTJJAwA==}
    peerDependencies:
      vite: ^5.2.0 || ^6 || ^7

  '@types/debug@4.1.12':
    resolution: {integrity: sha512-vIChWdVG3LG1SMxEvI/AK+FWJthlrqlTu7fbrlywTkkaONwk/UAGaULXRlf8vkzFBLVm0zkMdCquhL5aOjhXPQ==}

  '@types/estree@1.0.8':
    resolution: {integrity: sha512-dWHzHa2WqEXI/O1E9OjrocMTKJl2mSrEolh1Iomrv6U+JuNwaHXsXx9bLu5gG7BUWFIN0skIQJQ/L1rIex4X6w==}

  '@types/fontkit@2.0.8':
    resolution: {integrity: sha512-wN+8bYxIpJf+5oZdrdtaX04qUuWHcKxcDEgRS9Qm9ZClSHjzEn13SxUC+5eRM+4yXIeTYk8mTzLAWGF64847ew==}

  '@types/hast@3.0.4':
    resolution: {integrity: sha512-WPs+bbQw5aCj+x6laNGWLH3wviHtoCv/P3+otBhbOhJgG8qtpdAMlTCxLtsTWA7LH1Oh/bFCHsBn0TPS5m30EQ==}

  '@types/mdast@4.0.4':
    resolution: {integrity: sha512-kGaNbPh1k7AFzgpud/gMdvIm5xuECykRR+JnWKQno9TAXVa6WIVCGTPvYGekIDL4uwCZQSYbUxNBSb1aUo79oA==}

  '@types/ms@2.1.0':
    resolution: {integrity: sha512-GsCCIZDE/p3i96vtEqx+7dBUGXrc7zeSK3wwPHIaRThS+9OhWIXRqzs4d6k1SVU8g91DrNRWxWUGhp5KXQb2VA==}

  '@types/nlcst@2.0.3':
    resolution: {integrity: sha512-vSYNSDe6Ix3q+6Z7ri9lyWqgGhJTmzRjZRqyq15N0Z/1/UnVsno9G/N40NBijoYx2seFDIl0+B2mgAb9mezUCA==}

  '@types/node@24.10.0':
    resolution: {integrity: sha512-qzQZRBqkFsYyaSWXuEHc2WR9c0a0CXwiE5FWUvn7ZM+vdy1uZLfCunD38UzhuB7YN/J11ndbDBcTmOdxJo9Q7A==}

  '@types/unist@3.0.3':
    resolution: {integrity: sha512-ko/gIFJRv177XgZsZcBwnqJN5x/Gien8qNOn0D5bQU/zAzVf9Zt3BlcUiLqhV9y4ARk0GbT3tnUiPNgnTXzc/Q==}

  '@ungap/structured-clone@1.3.0':
    resolution: {integrity: sha512-WmoN8qaIAo7WTYWbAZuG8PYEhn5fkz7dZrqTBZ7dtt//lL2Gwms1IcnQ5yHqjDfX8Ft5j4YzDM23f87zBfDe9g==}

  acorn@8.15.0:
    resolution: {integrity: sha512-NZyJarBfL7nWwIq+FDL6Zp/yHEhePMNnnJ0y3qfieCrmNvYct8uvtiV41UvlSe6apAfk0fY1FbWx+NwfmpvtTg==}
    engines: {node: '>=0.4.0'}
    hasBin: true

  ansi-align@3.0.1:
    resolution: {integrity: sha512-IOfwwBF5iczOjp/WeY4YxyjqAFMQoZufdQWDd19SEExbVLNXqvpzSJ/M7Za4/sCPmQ0+GRquoA7bGcINcxew6w==}

  ansi-regex@5.0.1:
    resolution: {integrity: sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==}
    engines: {node: '>=8'}

  ansi-regex@6.2.2:
    resolution: {integrity: sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==}
    engines: {node: '>=12'}

  ansi-styles@6.2.3:
    resolution: {integrity: sha512-4Dj6M28JB+oAH8kFkTLUo+a2jwOFkuqb3yucU0CANcRRUbxS0cP0nZYCGjcc3BNXwRIsUVmDGgzawme7zvJHvg==}
    engines: {node: '>=12'}

  anymatch@3.1.3:
    resolution: {integrity: sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==}
    engines: {node: '>= 8'}

  argparse@2.0.1:
    resolution: {integrity: sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==}

  aria-query@5.3.2:
    resolution: {integrity: sha512-COROpnaoap1E2F000S62r6A60uHZnmlvomhfyT2DlTcrY1OrBKn2UhH7qn5wTC9zMvD0AY7csdPSNwKP+7WiQw==}
    engines: {node: '>= 0.4'}

  array-iterate@2.0.1:
    resolution: {integrity: sha512-I1jXZMjAgCMmxT4qxXfPXa6SthSoE8h6gkSI9BGGNv8mP8G/v0blc+qFnZu6K42vTOiuME596QaLO0TP3Lk0xg==}

  astro@5.15.5:
    resolution: {integrity: sha512-A56u4H6gFHEb0yRHcGTOADBb7jmEwfDjQpkqVV/Z+ZWlu6mYuwCrIcOUtZjNno0chrRKmOeZWDofW23ql18y3w==}
    engines: {node: 18.20.8 || ^20.3.0 || >=22.0.0, npm: '>=9.6.5', pnpm: '>=7.1.0'}
    hasBin: true

  axobject-query@4.1.0:
    resolution: {integrity: sha512-qIj0G9wZbMGNLjLmg1PT6v2mE9AH2zlnADJD/2tC6E00hgmhUOfEB6greHPAfLRSufHqROIUTkw6E+M3lH0PTQ==}
    engines: {node: '>= 0.4'}

  bail@2.0.2:
    resolution: {integrity: sha512-0xO6mYd7JB2YesxDKplafRpsiOzPt9V02ddPCLbY1xYGPOX24NTyN50qnUxgCPcSoYMhKpAuBTjQoRZCAkUDRw==}

  base-64@1.0.0:
    resolution: {integrity: sha512-kwDPIFCGx0NZHog36dj+tHiwP4QMzsZ3AgMViUBKI0+V5n4U0ufTCUMhnQ04diaRI8EX/QcPfql7zlhZ7j4zgg==}

  base64-js@1.5.1:
    resolution: {integrity: sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==}

  boxen@8.0.1:
    resolution: {integrity: sha512-F3PH5k5juxom4xktynS7MoFY+NUWH5LC4CnH11YB8NPew+HLpmBLCybSAEyb2F+4pRXhuhWqFesoQd6DAyc2hw==}
    engines: {node: '>=18'}

  brotli@1.3.3:
    resolution: {integrity: sha512-oTKjJdShmDuGW94SyyaoQvAjf30dZaHnjJ8uAF+u2/vGJkJbJPJAT1gDiOJP5v1Zb6f9KEyW/1HpuaWIXtGHPg==}

  camelcase@8.0.0:
    resolution: {integrity: sha512-8WB3Jcas3swSvjIeA2yvCJ+Miyz5l1ZmB6HFb9R1317dt9LCQoswg/BGrmAmkWVEszSrrg4RwmO46qIm2OEnSA==}
    engines: {node: '>=16'}

  ccount@2.0.1:
    resolution: {integrity: sha512-eyrF0jiFpY+3drT6383f1qhkbGsLSifNAjA61IUjZjmLCWjItY6LB9ft9YhoDgwfmclB2zhu51Lc7+95b8NRAg==}

  chalk@5.6.2:
    resolution: {integrity: sha512-7NzBL0rN6fMUW+f7A6Io4h40qQlG+xGmtMxfbnH/K7TAtt8JQWVQK+6g0UXKMeVJoyV5EkkNsErQ8pVD3bLHbA==}
    engines: {node: ^12.17.0 || ^14.13 || >=16.0.0}

  character-entities-html4@2.1.0:
    resolution: {integrity: sha512-1v7fgQRj6hnSwFpq1Eu0ynr/CDEw0rXo2B61qXrLNdHZmPKgb7fqS1a2JwF0rISo9q77jDI8VMEHoApn8qDoZA==}

  character-entities-legacy@3.0.0:
    resolution: {integrity: sha512-RpPp0asT/6ufRm//AJVwpViZbGM/MkjQFxJccQRHmISF/22NBtsHqAWmL+/pmkPWoIUJdWyeVleTl1wydHATVQ==}

  character-entities@2.0.2:
    resolution: {integrity: sha512-shx7oQ0Awen/BRIdkjkvz54PnEEI/EjwXDSIZp86/KKdbafHh1Df/RYGBhn4hbe2+uKC9FnT5UCEdyPz3ai9hQ==}

  chokidar@4.0.3:
    resolution: {integrity: sha512-Qgzu8kfBvo+cA4962jnP1KkS6Dop5NS6g7R5LFYJr4b8Ub94PPQXUksCw9PvXoeXPRRddRNC5C1JQUR2SMGtnA==}
    engines: {node: '>= 14.16.0'}

  ci-info@4.3.1:
    resolution: {integrity: sha512-Wdy2Igu8OcBpI2pZePZ5oWjPC38tmDVx5WKUXKwlLYkA0ozo85sLsLvkBbBn/sZaSCMFOGZJ14fvW9t5/d7kdA==}
    engines: {node: '>=8'}

  class-variance-authority@0.7.1:
    resolution: {integrity: sha512-Ka+9Trutv7G8M6WT6SeiRWz792K5qEqIGEGzXKhAE6xOWAY6pPH8U+9IY3oCMv6kqTmLsv7Xh/2w2RigkePMsg==}

  cli-boxes@3.0.0:
    resolution: {integrity: sha512-/lzGpEWL/8PfI0BmBOPRwp0c/wFNX1RdUML3jK/RcSBA9T8mZDdQpqYBKtCFTOfQbwPqWEOpjqW+Fnayc0969g==}
    engines: {node: '>=10'}

  clone@2.1.2:
    resolution: {integrity: sha512-3Pe/CF1Nn94hyhIYpjtiLhdCoEoz0DqQ+988E9gmeEdQZlojxnOb74wctFyuwWQHzqyf9X7C7MG8juUpqBJT8w==}
    engines: {node: '>=0.8'}

  clsx@2.1.1:
    resolution: {integrity: sha512-eYm0QWBtUrBWZWG0d386OGAw16Z995PiOVo2B7bjWSbHedGl5e0ZWaq65kOGgUSNesEIDkB9ISbTg/JK9dhCZA==}
    engines: {node: '>=6'}

  comma-separated-tokens@2.0.3:
    resolution: {integrity: sha512-Fu4hJdvzeylCfQPp9SGWidpzrMs7tTrlu6Vb8XGaRGck8QSNZJJp538Wrb60Lax4fPwR64ViY468OIUTbRlGZg==}

  common-ancestor-path@1.0.1:
    resolution: {integrity: sha512-L3sHRo1pXXEqX8VU28kfgUY+YGsk09hPqZiZmLacNib6XNTCM8ubYeT7ryXQw8asB1sKgcU5lkB7ONug08aB8w==}

  cookie-es@1.2.2:
    resolution: {integrity: sha512-+W7VmiVINB+ywl1HGXJXmrqkOhpKrIiVZV6tQuV54ZyQC7MMuBt81Vc336GMLoHBq5hV/F9eXgt5Mnx0Rha5Fg==}

  cookie@1.0.2:
    resolution: {integrity: sha512-9Kr/j4O16ISv8zBBhJoi4bXOYNTkFLOqSL3UDB0njXxCXNezjeyVrJyGOWtgfs/q2km1gwBcfH8q1yEGoMYunA==}
    engines: {node: '>=18'}

  crossws@0.3.5:
    resolution: {integrity: sha512-ojKiDvcmByhwa8YYqbQI/hg7MEU0NC03+pSdEq4ZUnZR9xXpwk7E43SMNGkn+JxJGPFtNvQ48+vV2p+P1ml5PA==}

  css-tree@3.1.0:
    resolution: {integrity: sha512-0eW44TGN5SQXU1mWSkKwFstI/22X2bG1nYzZTYMAWjylYURhse752YgbE4Cx46AC+bAvI+/dYTPRk1LqSUnu6w==}
    engines: {node: ^10 || ^12.20.0 || ^14.13.0 || >=15.0.0}

  cssesc@3.0.0:
    resolution: {integrity: sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==}
    engines: {node: '>=4'}
    hasBin: true

  debug@4.4.3:
    resolution: {integrity: sha512-RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==}
    engines: {node: '>=6.0'}
    peerDependencies:
      supports-color: '*'
    peerDependenciesMeta:
      supports-color:
        optional: true

  decode-named-character-reference@1.2.0:
    resolution: {integrity: sha512-c6fcElNV6ShtZXmsgNgFFV5tVX2PaV4g+MOAkb8eXHvn6sryJBrZa9r0zV6+dtTyoCKxtDy5tyQ5ZwQuidtd+Q==}

  defu@6.1.4:
    resolution: {integrity: sha512-mEQCMmwJu317oSz8CwdIOdwf3xMif1ttiM8LTufzc3g6kR+9Pe236twL8j3IYT1F7GfRgGcW6MWxzZjLIkuHIg==}

  dequal@2.0.3:
    resolution: {integrity: sha512-0je+qPKHEMohvfRTCEo3CrPG6cAzAYgmzKyxRiYSSDkS6eGJdyVJm7WaYA5ECaAD9wLB2T4EEeymA5aFVcYXCA==}
    engines: {node: '>=6'}

  destr@2.0.5:
    resolution: {integrity: sha512-ugFTXCtDZunbzasqBxrK93Ik/DRYsO6S/fedkWEMKqt04xZ4csmnmwGDBAb07QWNaGMAmnTIemsYZCksjATwsA==}

  detect-libc@2.1.2:
    resolution: {integrity: sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==}
    engines: {node: '>=8'}

  deterministic-object-hash@2.0.2:
    resolution: {integrity: sha512-KxektNH63SrbfUyDiwXqRb1rLwKt33AmMv+5Nhsw1kqZ13SJBRTgZHtGbE+hH3a1mVW1cz+4pqSWVPAtLVXTzQ==}
    engines: {node: '>=18'}

  devalue@5.4.2:
    resolution: {integrity: sha512-MwPZTKEPK2k8Qgfmqrd48ZKVvzSQjgW0lXLxiIBA8dQjtf/6mw6pggHNLcyDKyf+fI6eXxlQwPsfaCMTU5U+Bw==}

  devlop@1.1.0:
    resolution: {integrity: sha512-RWmIqhcFf1lRYBvNmr7qTNuyCt/7/ns2jbpp1+PalgE/rDQcBT0fioSMUpJ93irlUhC5hrg4cYqe6U+0ImW0rA==}

  dfa@1.2.0:
    resolution: {integrity: sha512-ED3jP8saaweFTjeGX8HQPjeC1YYyZs98jGNZx6IiBvxW7JG5v492kamAQB3m2wop07CvU/RQmzcKr6bgcC5D/Q==}

  diff@5.2.0:
    resolution: {integrity: sha512-uIFDxqpRZGZ6ThOk84hEfqWoHx2devRFvpTZcTHur85vImfaxUbTW9Ryh4CpCuDnToOP1CEtXKIgytHBPVff5A==}
    engines: {node: '>=0.3.1'}

  dlv@1.1.3:
    resolution: {integrity: sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==}

  dset@3.1.4:
    resolution: {integrity: sha512-2QF/g9/zTaPDc3BjNcVTGoBbXBgYfMTTceLaYcFJ/W9kggFUkhxD/hMEeuLKbugyef9SqAx8cpgwlIP/jinUTA==}
    engines: {node: '>=4'}

  emoji-regex@10.6.0:
    resolution: {integrity: sha512-toUI84YS5YmxW219erniWD0CIVOo46xGKColeNQRgOzDorgBi1v4D71/OFzgD9GO2UGKIv1C3Sp8DAn0+j5w7A==}

  emoji-regex@8.0.0:
    resolution: {integrity: sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==}

  enhanced-resolve@5.18.3:
    resolution: {integrity: sha512-d4lC8xfavMeBjzGr2vECC3fsGXziXZQyJxD868h2M/mBI3PwAuODxAkLkq5HYuvrPYcUtiLzsTo8U3PgX3Ocww==}
    engines: {node: '>=10.13.0'}

  entities@6.0.1:
    resolution: {integrity: sha512-aN97NXWF6AWBTahfVOIrB/NShkzi5H7F9r1s9mD3cDj4Ko5f2qhhVoYMibXF7GlLveb/D2ioWay8lxI97Ven3g==}
    engines: {node: '>=0.12'}

  es-module-lexer@1.7.0:
    resolution: {integrity: sha512-jEQoCwk8hyb2AZziIOLhDqpm5+2ww5uIE6lkO/6jcOCusfk6LhMHpXXfBLXTZ7Ydyt0j4VoUQv6uGNYbdW+kBA==}

  esbuild@0.25.12:
    resolution: {integrity: sha512-bbPBYYrtZbkt6Os6FiTLCTFxvq4tt3JKall1vRwshA3fdVztsLAatFaZobhkBC8/BrPetoa0oksYoKXoG4ryJg==}
    engines: {node: '>=18'}
    hasBin: true

  escape-string-regexp@5.0.0:
    resolution: {integrity: sha512-/veY75JbMK4j1yjvuUxuVsiS/hr/4iHs9FTT6cgTexxdE0Ly/glccBAkloH/DofkjRbZU3bnoj38mOmhkZ0lHw==}
    engines: {node: '>=12'}

  estree-walker@2.0.2:
    resolution: {integrity: sha512-Rfkk/Mp/DL7JVje3u18FxFujQlTNR2q6QfMSMB7AvCBx91NGj/ba3kCfza0f6dVDbw7YlRf/nDrn7pQrCCyQ/w==}

  estree-walker@3.0.3:
    resolution: {integrity: sha512-7RUKfXgSMMkzt6ZuXmqapOurLGPPfgj6l9uRZ7lRGolvk0y2yocc35LdcxKC5PQZdn2DMqioAQ2NoWcrTKmm6g==}

  eventemitter3@5.0.1:
    resolution: {integrity: sha512-GWkBvjiSZK87ELrYOSESUYeVIc9mvLLf/nXalMOS5dYrgZq9o5OVkbZAVM06CVxYsCwH9BDZFPlQTlPA1j4ahA==}

  extend@3.0.2:
    resolution: {integrity: sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==}

  fast-deep-equal@3.1.3:
    resolution: {integrity: sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==}

  fast-xml-parser@5.3.1:
    resolution: {integrity: sha512-jbNkWiv2Ec1A7wuuxk0br0d0aTMUtQ4IkL+l/i1r9PRf6pLXjDgsBsWwO+UyczmQlnehi4Tbc8/KIvxGQe+I/A==}
    hasBin: true

  fdir@6.5.0:
    resolution: {integrity: sha512-tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==}
    engines: {node: '>=12.0.0'}
    peerDependencies:
      picomatch: ^3 || ^4
    peerDependenciesMeta:
      picomatch:
        optional: true

  flattie@1.1.1:
    resolution: {integrity: sha512-9UbaD6XdAL97+k/n+N7JwX46K/M6Zc6KcFYskrYL8wbBV/Uyk0CTAMY0VT+qiK5PM7AIc9aTWYtq65U7T+aCNQ==}
    engines: {node: '>=8'}

  fontace@0.3.1:
    resolution: {integrity: sha512-9f5g4feWT1jWT8+SbL85aLIRLIXUaDygaM2xPXRmzPYxrOMNok79Lr3FGJoKVNKibE0WCunNiEVG2mwuE+2qEg==}

  fontkit@2.0.4:
    resolution: {integrity: sha512-syetQadaUEDNdxdugga9CpEYVaQIxOwk7GlwZWWZ19//qW4zE5bknOKeMBDYAASwnpaSHKJITRLMF9m1fp3s6g==}

  fsevents@2.3.3:
    resolution: {integrity: sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==}
    engines: {node: ^8.16.0 || ^10.6.0 || >=11.0.0}
    os: [darwin]

  get-east-asian-width@1.4.0:
    resolution: {integrity: sha512-QZjmEOC+IT1uk6Rx0sX22V6uHWVwbdbxf1faPqJ1QhLdGgsRGCZoyaQBm/piRdJy/D2um6hM1UP7ZEeQ4EkP+Q==}
    engines: {node: '>=18'}

  github-slugger@2.0.0:
    resolution: {integrity: sha512-IaOQ9puYtjrkq7Y0Ygl9KDZnrf/aiUJYUpVf89y8kyaxbRG7Y1SrX/jaumrv81vc61+kiMempujsM3Yw7w5qcw==}

  graceful-fs@4.2.11:
    resolution: {integrity: sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==}

  h3@1.15.4:
    resolution: {integrity: sha512-z5cFQWDffyOe4vQ9xIqNfCZdV4p//vy6fBnr8Q1AWnVZ0teurKMG66rLj++TKwKPUP3u7iMUvrvKaEUiQw2QWQ==}

  hast-util-from-html@2.0.3:
    resolution: {integrity: sha512-CUSRHXyKjzHov8yKsQjGOElXy/3EKpyX56ELnkHH34vDVw1N1XSQ1ZcAvTyAPtGqLTuKP/uxM+aLkSPqF/EtMw==}

  hast-util-from-parse5@8.0.3:
    resolution: {integrity: sha512-3kxEVkEKt0zvcZ3hCRYI8rqrgwtlIOFMWkbclACvjlDw8Li9S2hk/d51OI0nr/gIpdMHNepwgOKqZ/sy0Clpyg==}

  hast-util-is-element@3.0.0:
    resolution: {integrity: sha512-Val9mnv2IWpLbNPqc/pUem+a7Ipj2aHacCwgNfTiK0vJKl0LF+4Ba4+v1oPHFpf3bLYmreq0/l3Gud9S5OH42g==}

  hast-util-parse-selector@4.0.0:
    resolution: {integrity: sha512-wkQCkSYoOGCRKERFWcxMVMOcYE2K1AaNLU8DXS9arxnLOUEWbOXKXiJUNzEpqZ3JOKpnha3jkFrumEjVliDe7A==}

  hast-util-raw@9.1.0:
    resolution: {integrity: sha512-Y8/SBAHkZGoNkpzqqfCldijcuUKh7/su31kEBp67cFY09Wy0mTRgtsLYsiIxMJxlu0f6AA5SUTbDR8K0rxnbUw==}

  hast-util-to-html@9.0.5:
    resolution: {integrity: sha512-OguPdidb+fbHQSU4Q4ZiLKnzWo8Wwsf5bZfbvu7//a9oTYoqD/fWpe96NuHkoS9h0ccGOTe0C4NGXdtS0iObOw==}

  hast-util-to-parse5@8.0.0:
    resolution: {integrity: sha512-3KKrV5ZVI8if87DVSi1vDeByYrkGzg4mEfeu4alwgmmIeARiBLKCZS2uw5Gb6nU9x9Yufyj3iudm6i7nl52PFw==}

  hast-util-to-text@4.0.2:
    resolution: {integrity: sha512-KK6y/BN8lbaq654j7JgBydev7wuNMcID54lkRav1P0CaE1e47P72AWWPiGKXTJU271ooYzcvTAn/Zt0REnvc7A==}

  hast-util-whitespace@3.0.0:
    resolution: {integrity: sha512-88JUN06ipLwsnv+dVn+OIYOvAuvBMy/Qoi6O7mQHxdPXpjy+Cd6xRkWwux7DKO+4sYILtLBRIKgsdpS2gQc7qw==}

  hastscript@9.0.1:
    resolution: {integrity: sha512-g7df9rMFX/SPi34tyGCyUBREQoKkapwdY/T04Qn9TDWfHhAYt4/I0gMVirzK5wEzeUqIjEB+LXC/ypb7Aqno5w==}

  html-escaper@3.0.3:
    resolution: {integrity: sha512-RuMffC89BOWQoY0WKGpIhn5gX3iI54O6nRA0yC124NYVtzjmFWBIiFd8M0x+ZdX0P9R4lADg1mgP8C7PxGOWuQ==}

  html-void-elements@3.0.0:
    resolution: {integrity: sha512-bEqo66MRXsUGxWHV5IP0PUiAWwoEjba4VCzg0LjFJBpchPaTfyfCKTG6bc5F8ucKec3q5y6qOdGyYTSBEvhCrg==}

  http-cache-semantics@4.2.0:
    resolution: {integrity: sha512-dTxcvPXqPvXBQpq5dUr6mEMJX4oIEFv6bwom3FDwKRDsuIjjJGANqhBuoAn9c1RQJIdAKav33ED65E2ys+87QQ==}

  import-meta-resolve@4.2.0:
    resolution: {integrity: sha512-Iqv2fzaTQN28s/FwZAoFq0ZSs/7hMAHJVX+w8PZl3cY19Pxk6jFFalxQoIfW2826i/fDLXv8IiEZRIT0lDuWcg==}

  iron-webcrypto@1.2.1:
    resolution: {integrity: sha512-feOM6FaSr6rEABp/eDfVseKyTMDt+KGpeB35SkVn9Tyn0CqvVsY3EwI0v5i8nMHyJnzCIQf7nsy3p41TPkJZhg==}

  is-docker@3.0.0:
    resolution: {integrity: sha512-eljcgEDlEns/7AXFosB5K/2nCM4P7FQPkGc/DWLy5rmFEWvZayGrik1d9/QIY5nJ4f9YsVvBkA6kJpHn9rISdQ==}
    engines: {node: ^12.20.0 || ^14.13.1 || >=16.0.0}
    hasBin: true

  is-fullwidth-code-point@3.0.0:
    resolution: {integrity: sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==}
    engines: {node: '>=8'}

  is-inside-container@1.0.0:
    resolution: {integrity: sha512-KIYLCCJghfHZxqjYBE7rEy0OBuTd5xCHS7tHVgvCLkx7StIoaxwNW3hCALgEUjFfeRk+MG/Qxmp/vtETEF3tRA==}
    engines: {node: '>=14.16'}
    hasBin: true

  is-plain-obj@4.1.0:
    resolution: {integrity: sha512-+Pgi+vMuUNkJyExiMBt5IlFoMyKnr5zhJ4Uspz58WOhBF5QoIZkFyNHIbBAtHwzVAgk5RtndVNsDRN61/mmDqg==}
    engines: {node: '>=12'}

  is-wsl@3.1.0:
    resolution: {integrity: sha512-UcVfVfaK4Sc4m7X3dUSoHoozQGBEFeDC+zVo06t98xe8CzHSZZBekNXH+tu0NalHolcJ/QAGqS46Hef7QXBIMw==}
    engines: {node: '>=16'}

  jiti@2.6.1:
    resolution: {integrity: sha512-ekilCSN1jwRvIbgeg/57YFh8qQDNbwDb9xT/qu2DAHbFFZUicIl4ygVaAvzveMhMVr3LnpSKTNnwt8PoOfmKhQ==}
    hasBin: true

  js-yaml@4.1.0:
    resolution: {integrity: sha512-wpxZs9NoxZaJESJGIZTyDEaYpl0FKSA+FB9aJiyemKhMwkxQg63h4T1KJgUGHpTqPDNRcmmYLugrRjJlBtWvRA==}
    hasBin: true

  kleur@3.0.3:
    resolution: {integrity: sha512-eTIzlVOSUR+JxdDFepEYcBMtZ9Qqdef+rnzWdRZuMbOywu5tO2w2N7rqjoANZ5k9vywhL6Br1VRjUIgTQx4E8w==}
    engines: {node: '>=6'}

  lightningcss-android-arm64@1.30.2:
    resolution: {integrity: sha512-BH9sEdOCahSgmkVhBLeU7Hc9DWeZ1Eb6wNS6Da8igvUwAe0sqROHddIlvU06q3WyXVEOYDZ6ykBZQnjTbmo4+A==}
    engines: {node: '>= 12.0.0'}
    cpu: [arm64]
    os: [android]

  lightningcss-darwin-arm64@1.30.2:
    resolution: {integrity: sha512-ylTcDJBN3Hp21TdhRT5zBOIi73P6/W0qwvlFEk22fkdXchtNTOU4Qc37SkzV+EKYxLouZ6M4LG9NfZ1qkhhBWA==}
    engines: {node: '>= 12.0.0'}
    cpu: [arm64]
    os: [darwin]

  lightningcss-darwin-x64@1.30.2:
    resolution: {integrity: sha512-oBZgKchomuDYxr7ilwLcyms6BCyLn0z8J0+ZZmfpjwg9fRVZIR5/GMXd7r9RH94iDhld3UmSjBM6nXWM2TfZTQ==}
    engines: {node: '>= 12.0.0'}
    cpu: [x64]
    os: [darwin]

  lightningcss-freebsd-x64@1.30.2:
    resolution: {integrity: sha512-c2bH6xTrf4BDpK8MoGG4Bd6zAMZDAXS569UxCAGcA7IKbHNMlhGQ89eRmvpIUGfKWNVdbhSbkQaWhEoMGmGslA==}
    engines: {node: '>= 12.0.0'}
    cpu: [x64]
    os: [freebsd]

  lightningcss-linux-arm-gnueabihf@1.30.2:
    resolution: {integrity: sha512-eVdpxh4wYcm0PofJIZVuYuLiqBIakQ9uFZmipf6LF/HRj5Bgm0eb3qL/mr1smyXIS1twwOxNWndd8z0E374hiA==}
    engines: {node: '>= 12.0.0'}
    cpu: [arm]
    os: [linux]

  lightningcss-linux-arm64-gnu@1.30.2:
    resolution: {integrity: sha512-UK65WJAbwIJbiBFXpxrbTNArtfuznvxAJw4Q2ZGlU8kPeDIWEX1dg3rn2veBVUylA2Ezg89ktszWbaQnxD/e3A==}
    engines: {node: '>= 12.0.0'}
    cpu: [arm64]
    os: [linux]

  lightningcss-linux-arm64-musl@1.30.2:
    resolution: {integrity: sha512-5Vh9dGeblpTxWHpOx8iauV02popZDsCYMPIgiuw97OJ5uaDsL86cnqSFs5LZkG3ghHoX5isLgWzMs+eD1YzrnA==}
    engines: {node: '>= 12.0.0'}
    cpu: [arm64]
    os: [linux]

  lightningcss-linux-x64-gnu@1.30.2:
    resolution: {integrity: sha512-Cfd46gdmj1vQ+lR6VRTTadNHu6ALuw2pKR9lYq4FnhvgBc4zWY1EtZcAc6EffShbb1MFrIPfLDXD6Xprbnni4w==}
    engines: {node: '>= 12.0.0'}
    cpu: [x64]
    os: [linux]

  lightningcss-linux-x64-musl@1.30.2:
    resolution: {integrity: sha512-XJaLUUFXb6/QG2lGIW6aIk6jKdtjtcffUT0NKvIqhSBY3hh9Ch+1LCeH80dR9q9LBjG3ewbDjnumefsLsP6aiA==}
    engines: {node: '>= 12.0.0'}
    cpu: [x64]
    os: [linux]

  lightningcss-win32-arm64-msvc@1.30.2:
    resolution: {integrity: sha512-FZn+vaj7zLv//D/192WFFVA0RgHawIcHqLX9xuWiQt7P0PtdFEVaxgF9rjM/IRYHQXNnk61/H/gb2Ei+kUQ4xQ==}
    engines: {node: '>= 12.0.0'}
    cpu: [arm64]
    os: [win32]

  lightningcss-win32-x64-msvc@1.30.2:
    resolution: {integrity: sha512-5g1yc73p+iAkid5phb4oVFMB45417DkRevRbt/El/gKXJk4jid+vPFF/AXbxn05Aky8PapwzZrdJShv5C0avjw==}
    engines: {node: '>= 12.0.0'}
    cpu: [x64]
    os: [win32]

  lightningcss@1.30.2:
    resolution: {integrity: sha512-utfs7Pr5uJyyvDETitgsaqSyjCb2qNRAtuqUeWIAKztsOYdcACf2KtARYXg2pSvhkt+9NfoaNY7fxjl6nuMjIQ==}
    engines: {node: '>= 12.0.0'}

  longest-streak@3.1.0:
    resolution: {integrity: sha512-9Ri+o0JYgehTaVBBDoMqIl8GXtbWg711O3srftcHhZ0dqnETqLaoIK0x17fUw9rFSlK/0NlsKe0Ahhyl5pXE2g==}

  lru-cache@10.4.3:
    resolution: {integrity: sha512-JNAzZcXrCt42VGLuYz0zfAzDfAvJWW6AfYlDBQyDV5DClI2m5sAmK+OIO7s59XfsRsWHp02jAJrRadPRGTt6SQ==}

  magic-string@0.30.21:
    resolution: {integrity: sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ==}

  magicast@0.3.5:
    resolution: {integrity: sha512-L0WhttDl+2BOsybvEOLK7fW3UA0OQ0IQ2d6Zl2x/a6vVRs3bAY0ECOSHHeL5jD+SbOpOCUEi0y1DgHEn9Qn1AQ==}

  markdown-table@3.0.4:
    resolution: {integrity: sha512-wiYz4+JrLyb/DqW2hkFJxP7Vd7JuTDm77fvbM8VfEQdmSMqcImWeeRbHwZjBjIFki/VaMK2BhFi7oUUZeM5bqw==}

  mdast-util-definitions@6.0.0:
    resolution: {integrity: sha512-scTllyX6pnYNZH/AIp/0ePz6s4cZtARxImwoPJ7kS42n+MnVsI4XbnG6d4ibehRIldYMWM2LD7ImQblVhUejVQ==}

  mdast-util-find-and-replace@3.0.2:
    resolution: {integrity: sha512-Tmd1Vg/m3Xz43afeNxDIhWRtFZgM2VLyaf4vSTYwudTyeuTneoL3qtWMA5jeLyz/O1vDJmmV4QuScFCA2tBPwg==}

  mdast-util-from-markdown@2.0.2:
    resolution: {integrity: sha512-uZhTV/8NBuw0WHkPTrCqDOl0zVe1BIng5ZtHoDk49ME1qqcjYmmLmOf0gELgcRMxN4w2iuIeVso5/6QymSrgmA==}

  mdast-util-gfm-autolink-literal@2.0.1:
    resolution: {integrity: sha512-5HVP2MKaP6L+G6YaxPNjuL0BPrq9orG3TsrZ9YXbA3vDw/ACI4MEsnoDpn6ZNm7GnZgtAcONJyPhOP8tNJQavQ==}

  mdast-util-gfm-footnote@2.1.0:
    resolution: {integrity: sha512-sqpDWlsHn7Ac9GNZQMeUzPQSMzR6Wv0WKRNvQRg0KqHh02fpTz69Qc1QSseNX29bhz1ROIyNyxExfawVKTm1GQ==}

  mdast-util-gfm-strikethrough@2.0.0:
    resolution: {integrity: sha512-mKKb915TF+OC5ptj5bJ7WFRPdYtuHv0yTRxK2tJvi+BDqbkiG7h7u/9SI89nRAYcmap2xHQL9D+QG/6wSrTtXg==}

  mdast-util-gfm-table@2.0.0:
    resolution: {integrity: sha512-78UEvebzz/rJIxLvE7ZtDd/vIQ0RHv+3Mh5DR96p7cS7HsBhYIICDBCu8csTNWNO6tBWfqXPWekRuj2FNOGOZg==}

  mdast-util-gfm-task-list-item@2.0.0:
    resolution: {integrity: sha512-IrtvNvjxC1o06taBAVJznEnkiHxLFTzgonUdy8hzFVeDun0uTjxxrRGVaNFqkU1wJR3RBPEfsxmU6jDWPofrTQ==}

  mdast-util-gfm@3.1.0:
    resolution: {integrity: sha512-0ulfdQOM3ysHhCJ1p06l0b0VKlhU0wuQs3thxZQagjcjPrlFRqY215uZGHHJan9GEAXd9MbfPjFJz+qMkVR6zQ==}

  mdast-util-phrasing@4.1.0:
    resolution: {integrity: sha512-TqICwyvJJpBwvGAMZjj4J2n0X8QWp21b9l0o7eXyVJ25YNWYbJDVIyD1bZXE6WtV6RmKJVYmQAKWa0zWOABz2w==}

  mdast-util-to-hast@13.2.0:
    resolution: {integrity: sha512-QGYKEuUsYT9ykKBCMOEDLsU5JRObWQusAolFMeko/tYPufNkRffBAQjIE+99jbA87xv6FgmjLtwjh9wBWajwAA==}

  mdast-util-to-markdown@2.1.2:
    resolution: {integrity: sha512-xj68wMTvGXVOKonmog6LwyJKrYXZPvlwabaryTjLh9LuvovB/KAH+kvi8Gjj+7rJjsFi23nkUxRQv1KqSroMqA==}

  mdast-util-to-string@4.0.0:
    resolution: {integrity: sha512-0H44vDimn51F0YwvxSJSm0eCDOJTRlmN0R1yBh4HLj9wiV1Dn0QoXGbvFAWj2hSItVTlCmBF1hqKlIyUBVFLPg==}

  mdn-data@2.12.2:
    resolution: {integrity: sha512-IEn+pegP1aManZuckezWCO+XZQDplx1366JoVhTpMpBB1sPey/SbveZQUosKiKiGYjg1wH4pMlNgXbCiYgihQA==}

  micromark-core-commonmark@2.0.3:
    resolution: {integrity: sha512-RDBrHEMSxVFLg6xvnXmb1Ayr2WzLAWjeSATAoxwKYJV94TeNavgoIdA0a9ytzDSVzBy2YKFK+emCPOEibLeCrg==}

  micromark-extension-gfm-autolink-literal@2.1.0:
    resolution: {integrity: sha512-oOg7knzhicgQ3t4QCjCWgTmfNhvQbDDnJeVu9v81r7NltNCVmhPy1fJRX27pISafdjL+SVc4d3l48Gb6pbRypw==}

  micromark-extension-gfm-footnote@2.1.0:
    resolution: {integrity: sha512-/yPhxI1ntnDNsiHtzLKYnE3vf9JZ6cAisqVDauhp4CEHxlb4uoOTxOCJ+9s51bIB8U1N1FJ1RXOKTIlD5B/gqw==}

  micromark-extension-gfm-strikethrough@2.1.0:
    resolution: {integrity: sha512-ADVjpOOkjz1hhkZLlBiYA9cR2Anf8F4HqZUO6e5eDcPQd0Txw5fxLzzxnEkSkfnD0wziSGiv7sYhk/ktvbf1uw==}

  micromark-extension-gfm-table@2.1.1:
    resolution: {integrity: sha512-t2OU/dXXioARrC6yWfJ4hqB7rct14e8f7m0cbI5hUmDyyIlwv5vEtooptH8INkbLzOatzKuVbQmAYcbWoyz6Dg==}

  micromark-extension-gfm-tagfilter@2.0.0:
    resolution: {integrity: sha512-xHlTOmuCSotIA8TW1mDIM6X2O1SiX5P9IuDtqGonFhEK0qgRI4yeC6vMxEV2dgyr2TiD+2PQ10o+cOhdVAcwfg==}

  micromark-extension-gfm-task-list-item@2.1.0:
    resolution: {integrity: sha512-qIBZhqxqI6fjLDYFTBIa4eivDMnP+OZqsNwmQ3xNLE4Cxwc+zfQEfbs6tzAo2Hjq+bh6q5F+Z8/cksrLFYWQQw==}

  micromark-extension-gfm@3.0.0:
    resolution: {integrity: sha512-vsKArQsicm7t0z2GugkCKtZehqUm31oeGBV/KVSorWSy8ZlNAv7ytjFhvaryUiCUJYqs+NoE6AFhpQvBTM6Q4w==}

  micromark-factory-destination@2.0.1:
    resolution: {integrity: sha512-Xe6rDdJlkmbFRExpTOmRj9N3MaWmbAgdpSrBQvCFqhezUn4AHqJHbaEnfbVYYiexVSs//tqOdY/DxhjdCiJnIA==}

  micromark-factory-label@2.0.1:
    resolution: {integrity: sha512-VFMekyQExqIW7xIChcXn4ok29YE3rnuyveW3wZQWWqF4Nv9Wk5rgJ99KzPvHjkmPXF93FXIbBp6YdW3t71/7Vg==}

  micromark-factory-space@2.0.1:
    resolution: {integrity: sha512-zRkxjtBxxLd2Sc0d+fbnEunsTj46SWXgXciZmHq0kDYGnck/ZSGj9/wULTV95uoeYiK5hRXP2mJ98Uo4cq/LQg==}

  micromark-factory-title@2.0.1:
    resolution: {integrity: sha512-5bZ+3CjhAd9eChYTHsjy6TGxpOFSKgKKJPJxr293jTbfry2KDoWkhBb6TcPVB4NmzaPhMs1Frm9AZH7OD4Cjzw==}

  micromark-factory-whitespace@2.0.1:
    resolution: {integrity: sha512-Ob0nuZ3PKt/n0hORHyvoD9uZhr+Za8sFoP+OnMcnWK5lngSzALgQYKMr9RJVOWLqQYuyn6ulqGWSXdwf6F80lQ==}

  micromark-util-character@2.1.1:
    resolution: {integrity: sha512-wv8tdUTJ3thSFFFJKtpYKOYiGP2+v96Hvk4Tu8KpCAsTMs6yi+nVmGh1syvSCsaxz45J6Jbw+9DD6g97+NV67Q==}

  micromark-util-chunked@2.0.1:
    resolution: {integrity: sha512-QUNFEOPELfmvv+4xiNg2sRYeS/P84pTW0TCgP5zc9FpXetHY0ab7SxKyAQCNCc1eK0459uoLI1y5oO5Vc1dbhA==}

  micromark-util-classify-character@2.0.1:
    resolution: {integrity: sha512-K0kHzM6afW/MbeWYWLjoHQv1sgg2Q9EccHEDzSkxiP/EaagNzCm7T/WMKZ3rjMbvIpvBiZgwR3dKMygtA4mG1Q==}

  micromark-util-combine-extensions@2.0.1:
    resolution: {integrity: sha512-OnAnH8Ujmy59JcyZw8JSbK9cGpdVY44NKgSM7E9Eh7DiLS2E9RNQf0dONaGDzEG9yjEl5hcqeIsj4hfRkLH/Bg==}

  micromark-util-decode-numeric-character-reference@2.0.2:
    resolution: {integrity: sha512-ccUbYk6CwVdkmCQMyr64dXz42EfHGkPQlBj5p7YVGzq8I7CtjXZJrubAYezf7Rp+bjPseiROqe7G6foFd+lEuw==}

  micromark-util-decode-string@2.0.1:
    resolution: {integrity: sha512-nDV/77Fj6eH1ynwscYTOsbK7rR//Uj0bZXBwJZRfaLEJ1iGBR6kIfNmlNqaqJf649EP0F3NWNdeJi03elllNUQ==}

  micromark-util-encode@2.0.1:
    resolution: {integrity: sha512-c3cVx2y4KqUnwopcO9b/SCdo2O67LwJJ/UyqGfbigahfegL9myoEFoDYZgkT7f36T0bLrM9hZTAaAyH+PCAXjw==}

  micromark-util-html-tag-name@2.0.1:
    resolution: {integrity: sha512-2cNEiYDhCWKI+Gs9T0Tiysk136SnR13hhO8yW6BGNyhOC4qYFnwF1nKfD3HFAIXA5c45RrIG1ub11GiXeYd1xA==}

  micromark-util-normalize-identifier@2.0.1:
    resolution: {integrity: sha512-sxPqmo70LyARJs0w2UclACPUUEqltCkJ6PhKdMIDuJ3gSf/Q+/GIe3WKl0Ijb/GyH9lOpUkRAO2wp0GVkLvS9Q==}

  micromark-util-resolve-all@2.0.1:
    resolution: {integrity: sha512-VdQyxFWFT2/FGJgwQnJYbe1jjQoNTS4RjglmSjTUlpUMa95Htx9NHeYW4rGDJzbjvCsl9eLjMQwGeElsqmzcHg==}

  micromark-util-sanitize-uri@2.0.1:
    resolution: {integrity: sha512-9N9IomZ/YuGGZZmQec1MbgxtlgougxTodVwDzzEouPKo3qFWvymFHWcnDi2vzV1ff6kas9ucW+o3yzJK9YB1AQ==}

  micromark-util-subtokenize@2.1.0:
    resolution: {integrity: sha512-XQLu552iSctvnEcgXw6+Sx75GflAPNED1qx7eBJ+wydBb2KCbRZe+NwvIEEMM83uml1+2WSXpBAcp9IUCgCYWA==}

  micromark-util-symbol@2.0.1:
    resolution: {integrity: sha512-vs5t8Apaud9N28kgCrRUdEed4UJ+wWNvicHLPxCa9ENlYuAY31M0ETy5y1vA33YoNPDFTghEbnh6efaE8h4x0Q==}

  micromark-util-types@2.0.2:
    resolution: {integrity: sha512-Yw0ECSpJoViF1qTU4DC6NwtC4aWGt1EkzaQB8KPPyCRR8z9TWeV0HbEFGTO+ZY1wB22zmxnJqhPyTpOVCpeHTA==}

  micromark@4.0.2:
    resolution: {integrity: sha512-zpe98Q6kvavpCr1NPVSCMebCKfD7CA2NqZ+rykeNhONIJBpc1tFKt9hucLGwha3jNTNI8lHpctWJWoimVF4PfA==}

  mrmime@2.0.1:
    resolution: {integrity: sha512-Y3wQdFg2Va6etvQ5I82yUhGdsKrcYox6p7FfL1LbK2J4V01F9TGlepTIhnK24t7koZibmg82KGglhA1XK5IsLQ==}
    engines: {node: '>=10'}

  ms@2.1.3:
    resolution: {integrity: sha512-6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==}

  nanoid@3.3.11:
    resolution: {integrity: sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==}
    engines: {node: ^10 || ^12 || ^13.7 || ^14 || >=15.0.1}
    hasBin: true

  neotraverse@0.6.18:
    resolution: {integrity: sha512-Z4SmBUweYa09+o6pG+eASabEpP6QkQ70yHj351pQoEXIs8uHbaU2DWVmzBANKgflPa47A50PtB2+NgRpQvr7vA==}
    engines: {node: '>= 10'}

  nlcst-to-string@4.0.0:
    resolution: {integrity: sha512-YKLBCcUYKAg0FNlOBT6aI91qFmSiFKiluk655WzPF+DDMA02qIyy8uiRqI8QXtcFpEvll12LpL5MXqEmAZ+dcA==}

  node-fetch-native@1.6.7:
    resolution: {integrity: sha512-g9yhqoedzIUm0nTnTqAQvueMPVOuIY16bqgAJJC8XOOubYFNwz6IER9qs0Gq2Xd0+CecCKFjtdDTMA4u4xG06Q==}

  node-mock-http@1.0.3:
    resolution: {integrity: sha512-jN8dK25fsfnMrVsEhluUTPkBFY+6ybu7jSB1n+ri/vOGjJxU8J9CZhpSGkHXSkFjtUhbmoncG/YG9ta5Ludqog==}

  normalize-path@3.0.0:
    resolution: {integrity: sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==}
    engines: {node: '>=0.10.0'}

  ofetch@1.5.1:
    resolution: {integrity: sha512-2W4oUZlVaqAPAil6FUg/difl6YhqhUR7x2eZY4bQCko22UXg3hptq9KLQdqFClV+Wu85UX7hNtdGTngi/1BxcA==}

  ohash@2.0.11:
    resolution: {integrity: sha512-RdR9FQrFwNBNXAr4GixM8YaRZRJ5PUWbKYbE5eOsrwAjJW0q2REGcf79oYPsLyskQCZG1PLN+S/K1V00joZAoQ==}

  oniguruma-parser@0.12.1:
    resolution: {integrity: sha512-8Unqkvk1RYc6yq2WBYRj4hdnsAxVze8i7iPfQr8e4uSP3tRv0rpZcbGUDvxfQQcdwHt/e9PrMvGCsa8OqG9X3w==}

  oniguruma-to-es@4.3.3:
    resolution: {integrity: sha512-rPiZhzC3wXwE59YQMRDodUwwT9FZ9nNBwQQfsd1wfdtlKEyCdRV0avrTcSZ5xlIvGRVPd/cx6ZN45ECmS39xvg==}

  p-limit@6.2.0:
    resolution: {integrity: sha512-kuUqqHNUqoIWp/c467RI4X6mmyuojY5jGutNU0wVTmEOOfcuwLqyMVoAi9MKi2Ak+5i9+nhmrK4ufZE8069kHA==}
    engines: {node: '>=18'}

  p-queue@8.1.1:
    resolution: {integrity: sha512-aNZ+VfjobsWryoiPnEApGGmf5WmNsCo9xu8dfaYamG5qaLP7ClhLN6NgsFe6SwJ2UbLEBK5dv9x8Mn5+RVhMWQ==}
    engines: {node: '>=18'}

  p-timeout@6.1.4:
    resolution: {integrity: sha512-MyIV3ZA/PmyBN/ud8vV9XzwTrNtR4jFrObymZYnZqMmW0zA8Z17vnT0rBgFE/TlohB+YCHqXMgZzb3Csp49vqg==}
    engines: {node: '>=14.16'}

  package-manager-detector@1.5.0:
    resolution: {integrity: sha512-uBj69dVlYe/+wxj8JOpr97XfsxH/eumMt6HqjNTmJDf/6NO9s+0uxeOneIz3AsPt2m6y9PqzDzd3ATcU17MNfw==}

  pako@0.2.9:
    resolution: {integrity: sha512-NUcwaKxUxWrZLpDG+z/xZaCgQITkA/Dv4V/T6bw7VON6l1Xz/VnrBqrYjZQ12TamKHzITTfOEIYUj48y2KXImA==}

  parse-latin@7.0.0:
    resolution: {integrity: sha512-mhHgobPPua5kZ98EF4HWiH167JWBfl4pvAIXXdbaVohtK7a6YBOy56kvhCqduqyo/f3yrHFWmqmiMg/BkBkYYQ==}

  parse5@7.3.0:
    resolution: {integrity: sha512-IInvU7fabl34qmi9gY8XOVxhYyMyuH2xUNpb2q8/Y+7552KlejkRvqvD19nMoUW/uQGGbqNpA6Tufu5FL5BZgw==}

  picocolors@1.1.1:
    resolution: {integrity: sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==}

  picomatch@2.3.1:
    resolution: {integrity: sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==}
    engines: {node: '>=8.6'}

  picomatch@4.0.3:
    resolution: {integrity: sha512-5gTmgEY/sqK6gFXLIsQNH19lWb4ebPDLA4SdLP7dsWkIXHWlG66oPuVvXSGFPppYZz8ZDZq0dYYrbHfBCVUb1Q==}
    engines: {node: '>=12'}

  postcss@8.5.6:
    resolution: {integrity: sha512-3Ybi1tAuwAP9s0r1UQ2J4n5Y0G05bJkpUIO0/bI9MhwmD70S5aTWbXGBwxHrelT+XM1k6dM0pk+SwNkpTRN7Pg==}
    engines: {node: ^10 || ^12 || >=14}

  prismjs@1.30.0:
    resolution: {integrity: sha512-DEvV2ZF2r2/63V+tK8hQvrR2ZGn10srHbXviTlcv7Kpzw8jWiNTqbVgjO3IY8RxrrOUF8VPMQQFysYYYv0YZxw==}
    engines: {node: '>=6'}

  prompts@2.4.2:
    resolution: {integrity: sha512-NxNv/kLguCA7p3jE8oL2aEBsrJWgAakBpgmgK6lpPWV+WuOmY6r2/zbAVnP+T8bQlA0nzHXSJSJW0Hq7ylaD2Q==}
    engines: {node: '>= 6'}

  property-information@6.5.0:
    resolution: {integrity: sha512-PgTgs/BlvHxOu8QuEN7wi5A0OmXaBcHpmCSTehcs6Uuu9IkDIEo13Hy7n898RHfrQ49vKCoGeWZSaAK01nwVig==}

  property-information@7.1.0:
    resolution: {integrity: sha512-TwEZ+X+yCJmYfL7TPUOcvBZ4QfoT5YenQiJuX//0th53DE6w0xxLEtfK3iyryQFddXuvkIk51EEgrJQ0WJkOmQ==}

  radix3@1.1.2:
    resolution: {integrity: sha512-b484I/7b8rDEdSDKckSSBA8knMpcdsXudlE/LNL639wFoHKwLbEkQFZHWEYwDC0wa0FKUcCY+GAF73Z7wxNVFA==}

  readdirp@4.1.2:
    resolution: {integrity: sha512-GDhwkLfywWL2s6vEjyhri+eXmfH6j1L7JE27WhqLeYzoh/A3DBaYGEj2H/HFZCn/kMfim73FXxEJTw06WtxQwg==}
    engines: {node: '>= 14.18.0'}

  regex-recursion@6.0.2:
    resolution: {integrity: sha512-0YCaSCq2VRIebiaUviZNs0cBz1kg5kVS2UKUfNIx8YVs1cN3AV7NTctO5FOKBA+UT2BPJIWZauYHPqJODG50cg==}

  regex-utilities@2.3.0:
    resolution: {integrity: sha512-8VhliFJAWRaUiVvREIiW2NXXTmHs4vMNnSzuJVhscgmGav3g9VDxLrQndI3dZZVVdp0ZO/5v0xmX516/7M9cng==}

  regex@6.0.1:
    resolution: {integrity: sha512-uorlqlzAKjKQZ5P+kTJr3eeJGSVroLKoHmquUj4zHWuR+hEyNqlXsSKlYYF5F4NI6nl7tWCs0apKJ0lmfsXAPA==}

  rehype-parse@9.0.1:
    resolution: {integrity: sha512-ksCzCD0Fgfh7trPDxr2rSylbwq9iYDkSn8TCDmEJ49ljEUBxDVCzCHv7QNzZOfODanX4+bWQ4WZqLCRWYLfhag==}

  rehype-raw@7.0.0:
    resolution: {integrity: sha512-/aE8hCfKlQeA8LmyeyQvQF3eBiLRGNlfBJEvWH7ivp9sBqs7TNqBL5X3v157rM4IFETqDnIOO+z5M/biZbo9Ww==}

  rehype-stringify@10.0.1:
    resolution: {integrity: sha512-k9ecfXHmIPuFVI61B9DeLPN0qFHfawM6RsuX48hoqlaKSF61RskNjSm1lI8PhBEM0MRdLxVVm4WmTqJQccH9mA==}

  rehype@13.0.2:
    resolution: {integrity: sha512-j31mdaRFrwFRUIlxGeuPXXKWQxet52RBQRvCmzl5eCefn/KGbomK5GMHNMsOJf55fgo3qw5tST5neDuarDYR2A==}

  remark-gfm@4.0.1:
    resolution: {integrity: sha512-1quofZ2RQ9EWdeN34S79+KExV1764+wCUGop5CPL1WGdD0ocPpu91lzPGbwWMECpEpd42kJGQwzRfyov9j4yNg==}

  remark-parse@11.0.0:
    resolution: {integrity: sha512-FCxlKLNGknS5ba/1lmpYijMUzX2esxW5xQqjWxw2eHFfS2MSdaHVINFmhjo+qN1WhZhNimq0dZATN9pH0IDrpA==}

  remark-rehype@11.1.2:
    resolution: {integrity: sha512-Dh7l57ianaEoIpzbp0PC9UKAdCSVklD8E5Rpw7ETfbTl3FqcOOgq5q2LVDhgGCkaBv7p24JXikPdvhhmHvKMsw==}

  remark-smartypants@3.0.2:
    resolution: {integrity: sha512-ILTWeOriIluwEvPjv67v7Blgrcx+LZOkAUVtKI3putuhlZm84FnqDORNXPPm+HY3NdZOMhyDwZ1E+eZB/Df5dA==}
    engines: {node: '>=16.0.0'}

  remark-stringify@11.0.0:
    resolution: {integrity: sha512-1OSmLd3awB/t8qdoEOMazZkNsfVTeY4fTsgzcQFdXNq8ToTN4ZGwrMnlda4K6smTFKD+GRV6O48i6Z4iKgPPpw==}

  restructure@3.0.2:
    resolution: {integrity: sha512-gSfoiOEA0VPE6Tukkrr7I0RBdE0s7H1eFCDBk05l1KIQT1UIKNc5JZy6jdyW6eYH3aR3g5b3PuL77rq0hvwtAw==}

  retext-latin@4.0.0:
    resolution: {integrity: sha512-hv9woG7Fy0M9IlRQloq/N6atV82NxLGveq+3H2WOi79dtIYWN8OaxogDm77f8YnVXJL2VD3bbqowu5E3EMhBYA==}

  retext-smartypants@6.2.0:
    resolution: {integrity: sha512-kk0jOU7+zGv//kfjXEBjdIryL1Acl4i9XNkHxtM7Tm5lFiCog576fjNC9hjoR7LTKQ0DsPWy09JummSsH1uqfQ==}

  retext-stringify@4.0.0:
    resolution: {integrity: sha512-rtfN/0o8kL1e+78+uxPTqu1Klt0yPzKuQ2BfWwwfgIUSayyzxpM1PJzkKt4V8803uB9qSy32MvI7Xep9khTpiA==}

  retext@9.0.0:
    resolution: {integrity: sha512-sbMDcpHCNjvlheSgMfEcVrZko3cDzdbe1x/e7G66dFp0Ff7Mldvi2uv6JkJQzdRcvLYE8CA8Oe8siQx8ZOgTcA==}

  rollup@4.53.2:
    resolution: {integrity: sha512-MHngMYwGJVi6Fmnk6ISmnk7JAHRNF0UkuucA0CUW3N3a4KnONPEZz+vUanQP/ZC/iY1Qkf3bwPWzyY84wEks1g==}
    engines: {node: '>=18.0.0', npm: '>=8.0.0'}
    hasBin: true

  semver@7.7.3:
    resolution: {integrity: sha512-SdsKMrI9TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhVlUOe4BF1tLD7GAj0lIqWVl+dPb/rExr0Btby5loQm20Q==}
    engines: {node: '>=10'}
    hasBin: true

  sharp@0.34.5:
    resolution: {integrity: sha512-Ou9I5Ft9WNcCbXrU9cMgPBcCK8LiwLqcbywW3t4oDV37n1pzpuNLsYiAV8eODnjbtQlSDwZ2cUEeQz4E54Hltg==}
    engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}

  shiki@3.15.0:
    resolution: {integrity: sha512-kLdkY6iV3dYbtPwS9KXU7mjfmDm25f5m0IPNFnaXO7TBPcvbUOY72PYXSuSqDzwp+vlH/d7MXpHlKO/x+QoLXw==}

  sisteransi@1.0.5:
    resolution: {integrity: sha512-bLGGlR1QxBcynn2d5YmDX4MGjlZvy2MRBDRNHLJ8VI6l6+9FUiyTFNJ0IveOSP0bcXgVDPRcfGqA0pjaqUpfVg==}

  smol-toml@1.4.2:
    resolution: {integrity: sha512-rInDH6lCNiEyn3+hH8KVGFdbjc099j47+OSgbMrfDYX1CmXLfdKd7qi6IfcWj2wFxvSVkuI46M+wPGYfEOEj6g==}
    engines: {node: '>= 18'}

  source-map-js@1.2.1:
    resolution: {integrity: sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==}
    engines: {node: '>=0.10.0'}

  space-separated-tokens@2.0.2:
    resolution: {integrity: sha512-PEGlAwrG8yXGXRjW32fGbg66JAlOAwbObuqVoJpv/mRgoWDQfgH1wDPvtzWyUSNAXBGSk8h755YDbbcEy3SH2Q==}

  string-width@4.2.3:
    resolution: {integrity: sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==}
    engines: {node: '>=8'}

  string-width@7.2.0:
    resolution: {integrity: sha512-tsaTIkKW9b4N+AEj+SVA+WhJzV7/zMhcSu78mLKWSk7cXMOSHsBKFWUs0fWwq8QyK3MgJBQRX6Gbi4kYbdvGkQ==}
    engines: {node: '>=18'}

  stringify-entities@4.0.4:
    resolution: {integrity: sha512-IwfBptatlO+QCJUo19AqvrPNqlVMpW9YEL2LIVY+Rpv2qsjCGxaDLNRgeGsQWJhfItebuJhsGSLjaBbNSQ+ieg==}

  strip-ansi@6.0.1:
    resolution: {integrity: sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==}
    engines: {node: '>=8'}

  strip-ansi@7.1.2:
    resolution: {integrity: sha512-gmBGslpoQJtgnMAvOVqGZpEz9dyoKTCzy2nfz/n8aIFhN/jCE/rCmcxabB6jOOHV+0WNnylOxaxBQPSvcWklhA==}
    engines: {node: '>=12'}

  strnum@2.1.1:
    resolution: {integrity: sha512-7ZvoFTiCnGxBtDqJ//Cu6fWtZtc7Y3x+QOirG15wztbdngGSkht27o2pyGWrVy0b4WAy3jbKmnoK6g5VlVNUUw==}

  tailwind-merge@3.4.0:
    resolution: {integrity: sha512-uSaO4gnW+b3Y2aWoWfFpX62vn2sR3skfhbjsEnaBI81WD1wBLlHZe5sWf0AqjksNdYTbGBEd0UasQMT3SNV15g==}

  tailwindcss@4.1.17:
    resolution: {integrity: sha512-j9Ee2YjuQqYT9bbRTfTZht9W/ytp5H+jJpZKiYdP/bpnXARAuELt9ofP0lPnmHjbga7SNQIxdTAXCmtKVYjN+Q==}

  tapable@2.3.0:
    resolution: {integrity: sha512-g9ljZiwki/LfxmQADO3dEY1CbpmXT5Hm2fJ+QaGKwSXUylMybePR7/67YW7jOrrvjEgL1Fmz5kzyAjWVWLlucg==}
    engines: {node: '>=6'}

  tiny-inflate@1.0.3:
    resolution: {integrity: sha512-pkY1fj1cKHb2seWDy0B16HeWyczlJA9/WW3u3c4z/NiWDsO3DOU5D7nhTLE9CF0yXv/QZFY7sEJmj24dK+Rrqw==}

  tinyexec@1.0.2:
    resolution: {integrity: sha512-W/KYk+NFhkmsYpuHq5JykngiOCnxeVL8v8dFnqxSD8qEEdRfXk1SDM6JzNqcERbcGYj9tMrDQBYV9cjgnunFIg==}
    engines: {node: '>=18'}

  tinyglobby@0.2.15:
    resolution: {integrity: sha512-j2Zq4NyQYG5XMST4cbs02Ak8iJUdxRM0XI5QyxXuZOzKOINmWurp3smXu3y5wDcJrptwpSjgXHzIQxR0omXljQ==}
    engines: {node: '>=12.0.0'}

  trim-lines@3.0.1:
    resolution: {integrity: sha512-kRj8B+YHZCc9kQYdWfJB2/oUl9rA99qbowYYBtr4ui4mZyAQ2JpvVBd/6U2YloATfqBhBTSMhTpgBHtU0Mf3Rg==}

  trough@2.2.0:
    resolution: {integrity: sha512-tmMpK00BjZiUyVyvrBK7knerNgmgvcV/KLVyuma/SC+TQN167GrMRciANTz09+k3zW8L8t60jWO1GpfkZdjTaw==}

  tsconfck@3.1.6:
    resolution: {integrity: sha512-ks6Vjr/jEw0P1gmOVwutM3B7fWxoWBL2KRDb1JfqGVawBmO5UsvmWOQFGHBPl5yxYz4eERr19E6L7NMv+Fej4w==}
    engines: {node: ^18 || >=20}
    hasBin: true
    peerDependencies:
      typescript: ^5.0.0
    peerDependenciesMeta:
      typescript:
        optional: true

  tslib@2.8.1:
    resolution: {integrity: sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==}

  tw-animate-css@1.4.0:
    resolution: {integrity: sha512-7bziOlRqH0hJx80h/3mbicLW7o8qLsH5+RaLR2t+OHM3D0JlWGODQKQ4cxbK7WlvmUxpcj6Kgu6EKqjrGFe3QQ==}

  type-fest@4.41.0:
    resolution: {integrity: sha512-TeTSQ6H5YHvpqVwBRcnLDCBnDOHWYu7IvGbHT6N8AOymcr9PJGjc1GTtiWZTYg0NCgYwvnYWEkVChQAr9bjfwA==}
    engines: {node: '>=16'}

  typescript@5.9.3:
    resolution: {integrity: sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw==}
    engines: {node: '>=14.17'}
    hasBin: true

  ufo@1.6.1:
    resolution: {integrity: sha512-9a4/uxlTWJ4+a5i0ooc1rU7C7YOw3wT+UGqdeNNHWnOF9qcMBgLRS+4IYUqbczewFx4mLEig6gawh7X6mFlEkA==}

  ultrahtml@1.6.0:
    resolution: {integrity: sha512-R9fBn90VTJrqqLDwyMph+HGne8eqY1iPfYhPzZrvKpIfwkWZbcYlfpsb8B9dTvBfpy1/hqAD7Wi8EKfP9e8zdw==}

  uncrypto@0.1.3:
    resolution: {integrity: sha512-Ql87qFHB3s/De2ClA9e0gsnS6zXG27SkTiSJwjCc9MebbfapQfuPzumMIUMi38ezPZVNFcHI9sUIepeQfw8J8Q==}

  undici-types@7.16.0:
    resolution: {integrity: sha512-Zz+aZWSj8LE6zoxD+xrjh4VfkIG8Ya6LvYkZqtUQGJPZjYl53ypCaUwWqo7eI0x66KBGeRo+mlBEkMSeSZ38Nw==}

  unicode-properties@1.4.1:
    resolution: {integrity: sha512-CLjCCLQ6UuMxWnbIylkisbRj31qxHPAurvena/0iwSVbQ2G1VY5/HjV0IRabOEbDHlzZlRdCrD4NhB0JtU40Pg==}

  unicode-trie@2.0.0:
    resolution: {integrity: sha512-x7bc76x0bm4prf1VLg79uhAzKw8DVboClSN5VxJuQ+LKDOVEW9CdH+VY7SP+vX7xCYQqzzgQpFqz15zeLvAtZQ==}

  unified@11.0.5:
    resolution: {integrity: sha512-xKvGhPWw3k84Qjh8bI3ZeJjqnyadK+GEFtazSfZv/rKeTkTjOJho6mFqh2SM96iIcZokxiOpg78GazTSg8+KHA==}

  unifont@0.6.0:
    resolution: {integrity: sha512-5Fx50fFQMQL5aeHyWnZX9122sSLckcDvcfFiBf3QYeHa7a1MKJooUy52b67moi2MJYkrfo/TWY+CoLdr/w0tTA==}

  unist-util-find-after@5.0.0:
    resolution: {integrity: sha512-amQa0Ep2m6hE2g72AugUItjbuM8X8cGQnFoHk0pGfrFeT9GZhzN5SW8nRsiGKK7Aif4CrACPENkA6P/Lw6fHGQ==}

  unist-util-is@6.0.1:
    resolution: {integrity: sha512-LsiILbtBETkDz8I9p1dQ0uyRUWuaQzd/cuEeS1hoRSyW5E5XGmTzlwY1OrNzzakGowI9Dr/I8HVaw4hTtnxy8g==}

  unist-util-modify-children@4.0.0:
    resolution: {integrity: sha512-+tdN5fGNddvsQdIzUF3Xx82CU9sMM+fA0dLgR9vOmT0oPT2jH+P1nd5lSqfCfXAw+93NhcXNY2qqvTUtE4cQkw==}

  unist-util-position@5.0.0:
    resolution: {integrity: sha512-fucsC7HjXvkB5R3kTCO7kUjRdrS0BJt3M/FPxmHMBOm8JQi2BsHAHFsy27E0EolP8rp0NzXsJ+jNPyDWvOJZPA==}

  unist-util-remove-position@5.0.0:
    resolution: {integrity: sha512-Hp5Kh3wLxv0PHj9m2yZhhLt58KzPtEYKQQ4yxfYFEO7EvHwzyDYnduhHnY1mDxoqr7VUwVuHXk9RXKIiYS1N8Q==}

  unist-util-stringify-position@4.0.0:
    resolution: {integrity: sha512-0ASV06AAoKCDkS2+xw5RXJywruurpbC4JZSm7nr7MOt1ojAzvyyaO+UxZf18j8FCF6kmzCZKcAgN/yu2gm2XgQ==}

  unist-util-visit-children@3.0.0:
    resolution: {integrity: sha512-RgmdTfSBOg04sdPcpTSD1jzoNBjt9a80/ZCzp5cI9n1qPzLZWF9YdvWGN2zmTumP1HWhXKdUWexjy/Wy/lJ7tA==}

  unist-util-visit-parents@6.0.2:
    resolution: {integrity: sha512-goh1s1TBrqSqukSc8wrjwWhL0hiJxgA8m4kFxGlQ+8FYQ3C/m11FcTs4YYem7V664AhHVvgoQLk890Ssdsr2IQ==}

  unist-util-visit@5.0.0:
    resolution: {integrity: sha512-MR04uvD+07cwl/yhVuVWAtw+3GOR/knlL55Nd/wAdblk27GCVt3lqpTivy/tkJcZoNPzTwS1Y+KMojlLDhoTzg==}

  unstorage@1.17.2:
    resolution: {integrity: sha512-cKEsD6iBWJgOMJ6vW1ID/SYuqNf8oN4yqRk8OYqaVQ3nnkJXOT1PSpaMh2QfzLs78UN5kSNRD2c/mgjT8tX7+w==}
    peerDependencies:
      '@azure/app-configuration': ^1.8.0
      '@azure/cosmos': ^4.2.0
      '@azure/data-tables': ^13.3.0
      '@azure/identity': ^4.6.0
      '@azure/keyvault-secrets': ^4.9.0
      '@azure/storage-blob': ^12.26.0
      '@capacitor/preferences': ^6.0.3 || ^7.0.0
      '@deno/kv': '>=0.9.0'
      '@netlify/blobs': ^6.5.0 || ^7.0.0 || ^8.1.0 || ^9.0.0 || ^10.0.0
      '@planetscale/database': ^1.19.0
      '@upstash/redis': ^1.34.3
      '@vercel/blob': '>=0.27.1'
      '@vercel/functions': ^2.2.12 || ^3.0.0
      '@vercel/kv': ^1.0.1
      aws4fetch: ^1.0.20
      db0: '>=0.2.1'
      idb-keyval: ^6.2.1
      ioredis: ^5.4.2
      uploadthing: ^7.4.4
    peerDependenciesMeta:
      '@azure/app-configuration':
        optional: true
      '@azure/cosmos':
        optional: true
      '@azure/data-tables':
        optional: true
      '@azure/identity':
        optional: true
      '@azure/keyvault-secrets':
        optional: true
      '@azure/storage-blob':
        optional: true
      '@capacitor/preferences':
        optional: true
      '@deno/kv':
        optional: true
      '@netlify/blobs':
        optional: true
      '@planetscale/database':
        optional: true
      '@upstash/redis':
        optional: true
      '@vercel/blob':
        optional: true
      '@vercel/functions':
        optional: true
      '@vercel/kv':
        optional: true
      aws4fetch:
        optional: true
      db0:
        optional: true
      idb-keyval:
        optional: true
      ioredis:
        optional: true
      uploadthing:
        optional: true

  vfile-location@5.0.3:
    resolution: {integrity: sha512-5yXvWDEgqeiYiBe1lbxYF7UMAIm/IcopxMHrMQDq3nvKcjPKIhZklUKL+AE7J7uApI4kwe2snsK+eI6UTj9EHg==}

  vfile-message@4.0.3:
    resolution: {integrity: sha512-QTHzsGd1EhbZs4AsQ20JX1rC3cOlt/IWJruk893DfLRr57lcnOeMaWG4K0JrRta4mIJZKth2Au3mM3u03/JWKw==}

  vfile@6.0.3:
    resolution: {integrity: sha512-KzIbH/9tXat2u30jf+smMwFCsno4wHVdNmzFyL+T/L3UGqqk6JKfVqOFOZEpZSHADH1k40ab6NUIXZq422ov3Q==}

  vite@6.4.1:
    resolution: {integrity: sha512-+Oxm7q9hDoLMyJOYfUYBuHQo+dkAloi33apOPP56pzj+vsdJDzr+j1NISE5pyaAuKL4A3UD34qd0lx5+kfKp2g==}
    engines: {node: ^18.0.0 || ^20.0.0 || >=22.0.0}
    hasBin: true
    peerDependencies:
      '@types/node': ^18.0.0 || ^20.0.0 || >=22.0.0
      jiti: '>=1.21.0'
      less: '*'
      lightningcss: ^1.21.0
      sass: '*'
      sass-embedded: '*'
      stylus: '*'
      sugarss: '*'
      terser: ^5.16.0
      tsx: ^4.8.1
      yaml: ^2.4.2
    peerDependenciesMeta:
      '@types/node':
        optional: true
      jiti:
        optional: true
      less:
        optional: true
      lightningcss:
        optional: true
      sass:
        optional: true
      sass-embedded:
        optional: true
      stylus:
        optional: true
      sugarss:
        optional: true
      terser:
        optional: true
      tsx:
        optional: true
      yaml:
        optional: true

  vitefu@1.1.1:
    resolution: {integrity: sha512-B/Fegf3i8zh0yFbpzZ21amWzHmuNlLlmJT6n7bu5e+pCHUKQIfXSYokrqOBGEMMe9UG2sostKQF9mml/vYaWJQ==}
    peerDependencies:
      vite: ^3.0.0 || ^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0-beta.0
    peerDependenciesMeta:
      vite:
        optional: true

  web-namespaces@2.0.1:
    resolution: {integrity: sha512-bKr1DkiNa2krS7qxNtdrtHAmzuYGFQLiQ13TsorsdT6ULTkPLKuu5+GsFpDlg6JFjUTwX2DyhMPG2be8uPrqsQ==}

  which-pm-runs@1.1.0:
    resolution: {integrity: sha512-n1brCuqClxfFfq/Rb0ICg9giSZqCS+pLtccdag6C2HyufBrh3fBOiy9nb6ggRMvWOVH5GrdJskj5iGTZNxd7SA==}
    engines: {node: '>=4'}

  widest-line@5.0.0:
    resolution: {integrity: sha512-c9bZp7b5YtRj2wOe6dlj32MK+Bx/M/d+9VB2SHM1OtsUHR0aV0tdP6DWh/iMt0kWi1t5g1Iudu6hQRNd1A4PVA==}
    engines: {node: '>=18'}

  wrap-ansi@9.0.2:
    resolution: {integrity: sha512-42AtmgqjV+X1VpdOfyTGOYRi0/zsoLqtXQckTmqTeybT+BDIbM/Guxo7x3pE2vtpr1ok6xRqM9OpBe+Jyoqyww==}
    engines: {node: '>=18'}

  xxhash-wasm@1.1.0:
    resolution: {integrity: sha512-147y/6YNh+tlp6nd/2pWq38i9h6mz/EuQ6njIrmW8D1BS5nCqs0P6DG+m6zTGnNz5I+uhZ0SHxBs9BsPrwcKDA==}

  yargs-parser@21.1.1:
    resolution: {integrity: sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==}
    engines: {node: '>=12'}

  yocto-queue@1.2.2:
    resolution: {integrity: sha512-4LCcse/U2MHZ63HAJVE+v71o7yOdIe4cZ70Wpf8D/IyjDKYQLV5GD46B+hSTjJsvV5PztjvHoU580EftxjDZFQ==}
    engines: {node: '>=12.20'}

  yocto-spinner@0.2.3:
    resolution: {integrity: sha512-sqBChb33loEnkoXte1bLg45bEBsOP9N1kzQh5JZNKj/0rik4zAPTNSAVPj3uQAdc6slYJ0Ksc403G2XgxsJQFQ==}
    engines: {node: '>=18.19'}

  yoctocolors@2.1.2:
    resolution: {integrity: sha512-CzhO+pFNo8ajLM2d2IW/R93ipy99LWjtwblvC1RsoSUMZgyLbYFr221TnSNT7GjGdYui6P459mw9JH/g/zW2ug==}
    engines: {node: '>=18'}

  zod-to-json-schema@3.24.6:
    resolution: {integrity: sha512-h/z3PKvcTcTetyjl1fkj79MHNEjm+HpD6NXheWjzOekY7kV+lwDYnHw+ivHkijnCSMz1yJaWBD9vu/Fcmk+vEg==}
    peerDependencies:
      zod: ^3.24.1

  zod-to-ts@1.2.0:
    resolution: {integrity: sha512-x30XE43V+InwGpvTySRNz9kB7qFU8DlyEy7BsSTCHPH1R0QasMmHWZDCzYm6bVXtj/9NNJAZF3jW8rzFvH5OFA==}
    peerDependencies:
      typescript: ^4.9.4 || ^5.0.2
      zod: ^3

  zod@3.25.76:
    resolution: {integrity: sha512-gzUt/qt81nXsFGKIFcC3YnfEAx5NkunCfnDlvuBSSFS02bcXu4Lmea0AFIUwbLWxWPx3d9p8S5QoaujKcNQxcQ==}

  zwitch@2.0.4:
    resolution: {integrity: sha512-bXE4cR/kVZhKZX/RjPEflHaKVhUVl85noU3v6b8apfQEc1x4A+zBxjZ4lN8LqGd6WZ3dl98pY4o717VFmoPp+A==}

snapshots:

  '@astrojs/compiler@2.13.0': {}

  '@astrojs/internal-helpers@0.7.4': {}

  '@astrojs/markdown-remark@6.3.8':
    dependencies:
      '@astrojs/internal-helpers': 0.7.4
      '@astrojs/prism': 3.3.0
      github-slugger: 2.0.0
      hast-util-from-html: 2.0.3
      hast-util-to-text: 4.0.2
      import-meta-resolve: 4.2.0
      js-yaml: 4.1.0
      mdast-util-definitions: 6.0.0
      rehype-raw: 7.0.0
      rehype-stringify: 10.0.1
      remark-gfm: 4.0.1
      remark-parse: 11.0.0
      remark-rehype: 11.1.2
      remark-smartypants: 3.0.2
      shiki: 3.15.0
      smol-toml: 1.4.2
      unified: 11.0.5
      unist-util-remove-position: 5.0.0
      unist-util-visit: 5.0.0
      unist-util-visit-parents: 6.0.2
      vfile: 6.0.3
    transitivePeerDependencies:
      - supports-color

  '@astrojs/prism@3.3.0':
    dependencies:
      prismjs: 1.30.0

  '@astrojs/rss@4.0.13':
    dependencies:
      fast-xml-parser: 5.3.1
      picocolors: 1.1.1

  '@astrojs/telemetry@3.3.0':
    dependencies:
      ci-info: 4.3.1
      debug: 4.4.3
      dlv: 1.1.3
      dset: 3.1.4
      is-docker: 3.0.0
      is-wsl: 3.1.0
      which-pm-runs: 1.1.0
    transitivePeerDependencies:
      - supports-color

  '@babel/helper-string-parser@7.27.1': {}

  '@babel/helper-validator-identifier@7.28.5': {}

  '@babel/parser@7.28.5':
    dependencies:
      '@babel/types': 7.28.5

  '@babel/types@7.28.5':
    dependencies:
      '@babel/helper-string-parser': 7.27.1
      '@babel/helper-validator-identifier': 7.28.5

  '@capsizecss/unpack@3.0.0':
    dependencies:
      fontkit: 2.0.4

  '@emnapi/runtime@1.7.0':
    dependencies:
      tslib: 2.8.1
    optional: true

  '@esbuild/aix-ppc64@0.25.12':
    optional: true

  '@esbuild/android-arm64@0.25.12':
    optional: true

  '@esbuild/android-arm@0.25.12':
    optional: true

  '@esbuild/android-x64@0.25.12':
    optional: true

  '@esbuild/darwin-arm64@0.25.12':
    optional: true

  '@esbuild/darwin-x64@0.25.12':
    optional: true

  '@esbuild/freebsd-arm64@0.25.12':
    optional: true

  '@esbuild/freebsd-x64@0.25.12':
    optional: true

  '@esbuild/linux-arm64@0.25.12':
    optional: true

  '@esbuild/linux-arm@0.25.12':
    optional: true

  '@esbuild/linux-ia32@0.25.12':
    optional: true

  '@esbuild/linux-loong64@0.25.12':
    optional: true

  '@esbuild/linux-mips64el@0.25.12':
    optional: true

  '@esbuild/linux-ppc64@0.25.12':
    optional: true

  '@esbuild/linux-riscv64@0.25.12':
    optional: true

  '@esbuild/linux-s390x@0.25.12':
    optional: true

  '@esbuild/linux-x64@0.25.12':
    optional: true

  '@esbuild/netbsd-arm64@0.25.12':
    optional: true

  '@esbuild/netbsd-x64@0.25.12':
    optional: true

  '@esbuild/openbsd-arm64@0.25.12':
    optional: true

  '@esbuild/openbsd-x64@0.25.12':
    optional: true

  '@esbuild/openharmony-arm64@0.25.12':
    optional: true

  '@esbuild/sunos-x64@0.25.12':
    optional: true

  '@esbuild/win32-arm64@0.25.12':
    optional: true

  '@esbuild/win32-ia32@0.25.12':
    optional: true

  '@esbuild/win32-x64@0.25.12':
    optional: true

  '@img/colour@1.0.0':
    optional: true

  '@img/sharp-darwin-arm64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-darwin-arm64': 1.2.4
    optional: true

  '@img/sharp-darwin-x64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-darwin-x64': 1.2.4
    optional: true

  '@img/sharp-libvips-darwin-arm64@1.2.4':
    optional: true

  '@img/sharp-libvips-darwin-x64@1.2.4':
    optional: true

  '@img/sharp-libvips-linux-arm64@1.2.4':
    optional: true

  '@img/sharp-libvips-linux-arm@1.2.4':
    optional: true

  '@img/sharp-libvips-linux-ppc64@1.2.4':
    optional: true

  '@img/sharp-libvips-linux-riscv64@1.2.4':
    optional: true

  '@img/sharp-libvips-linux-s390x@1.2.4':
    optional: true

  '@img/sharp-libvips-linux-x64@1.2.4':
    optional: true

  '@img/sharp-libvips-linuxmusl-arm64@1.2.4':
    optional: true

  '@img/sharp-libvips-linuxmusl-x64@1.2.4':
    optional: true

  '@img/sharp-linux-arm64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linux-arm64': 1.2.4
    optional: true

  '@img/sharp-linux-arm@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linux-arm': 1.2.4
    optional: true

  '@img/sharp-linux-ppc64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linux-ppc64': 1.2.4
    optional: true

  '@img/sharp-linux-riscv64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linux-riscv64': 1.2.4
    optional: true

  '@img/sharp-linux-s390x@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linux-s390x': 1.2.4
    optional: true

  '@img/sharp-linux-x64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linux-x64': 1.2.4
    optional: true

  '@img/sharp-linuxmusl-arm64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linuxmusl-arm64': 1.2.4
    optional: true

  '@img/sharp-linuxmusl-x64@0.34.5':
    optionalDependencies:
      '@img/sharp-libvips-linuxmusl-x64': 1.2.4
    optional: true

  '@img/sharp-wasm32@0.34.5':
    dependencies:
      '@emnapi/runtime': 1.7.0
    optional: true

  '@img/sharp-win32-arm64@0.34.5':
    optional: true

  '@img/sharp-win32-ia32@0.34.5':
    optional: true

  '@img/sharp-win32-x64@0.34.5':
    optional: true

  '@jridgewell/gen-mapping@0.3.13':
    dependencies:
      '@jridgewell/sourcemap-codec': 1.5.5
      '@jridgewell/trace-mapping': 0.3.31

  '@jridgewell/remapping@2.3.5':
    dependencies:
      '@jridgewell/gen-mapping': 0.3.13
      '@jridgewell/trace-mapping': 0.3.31

  '@jridgewell/resolve-uri@3.1.2': {}

  '@jridgewell/sourcemap-codec@1.5.5': {}

  '@jridgewell/trace-mapping@0.3.31':
    dependencies:
      '@jridgewell/resolve-uri': 3.1.2
      '@jridgewell/sourcemap-codec': 1.5.5

  '@oslojs/encoding@1.1.0': {}

  '@rollup/pluginutils@5.3.0(rollup@4.53.2)':
    dependencies:
      '@types/estree': 1.0.8
      estree-walker: 2.0.2
      picomatch: 4.0.3
    optionalDependencies:
      rollup: 4.53.2

  '@rollup/rollup-android-arm-eabi@4.53.2':
    optional: true

  '@rollup/rollup-android-arm64@4.53.2':
    optional: true

  '@rollup/rollup-darwin-arm64@4.53.2':
    optional: true

  '@rollup/rollup-darwin-x64@4.53.2':
    optional: true

  '@rollup/rollup-freebsd-arm64@4.53.2':
    optional: true

  '@rollup/rollup-freebsd-x64@4.53.2':
    optional: true

  '@rollup/rollup-linux-arm-gnueabihf@4.53.2':
    optional: true

  '@rollup/rollup-linux-arm-musleabihf@4.53.2':
    optional: true

  '@rollup/rollup-linux-arm64-gnu@4.53.2':
    optional: true

  '@rollup/rollup-linux-arm64-musl@4.53.2':
    optional: true

  '@rollup/rollup-linux-loong64-gnu@4.53.2':
    optional: true

  '@rollup/rollup-linux-ppc64-gnu@4.53.2':
    optional: true

  '@rollup/rollup-linux-riscv64-gnu@4.53.2':
    optional: true

  '@rollup/rollup-linux-riscv64-musl@4.53.2':
    optional: true

  '@rollup/rollup-linux-s390x-gnu@4.53.2':
    optional: true

  '@rollup/rollup-linux-x64-gnu@4.53.2':
    optional: true

  '@rollup/rollup-linux-x64-musl@4.53.2':
    optional: true

  '@rollup/rollup-openharmony-arm64@4.53.2':
    optional: true

  '@rollup/rollup-win32-arm64-msvc@4.53.2':
    optional: true

  '@rollup/rollup-win32-ia32-msvc@4.53.2':
    optional: true

  '@rollup/rollup-win32-x64-gnu@4.53.2':
    optional: true

  '@rollup/rollup-win32-x64-msvc@4.53.2':
    optional: true

  '@shikijs/core@3.15.0':
    dependencies:
      '@shikijs/types': 3.15.0
      '@shikijs/vscode-textmate': 10.0.2
      '@types/hast': 3.0.4
      hast-util-to-html: 9.0.5

  '@shikijs/engine-javascript@3.15.0':
    dependencies:
      '@shikijs/types': 3.15.0
      '@shikijs/vscode-textmate': 10.0.2
      oniguruma-to-es: 4.3.3

  '@shikijs/engine-oniguruma@3.15.0':
    dependencies:
      '@shikijs/types': 3.15.0
      '@shikijs/vscode-textmate': 10.0.2

  '@shikijs/langs@3.15.0':
    dependencies:
      '@shikijs/types': 3.15.0

  '@shikijs/themes@3.15.0':
    dependencies:
      '@shikijs/types': 3.15.0

  '@shikijs/types@3.15.0':
    dependencies:
      '@shikijs/vscode-textmate': 10.0.2
      '@types/hast': 3.0.4

  '@shikijs/vscode-textmate@10.0.2': {}

  '@swc/helpers@0.5.17':
    dependencies:
      tslib: 2.8.1

  '@tailwindcss/node@4.1.17':
    dependencies:
      '@jridgewell/remapping': 2.3.5
      enhanced-resolve: 5.18.3
      jiti: 2.6.1
      lightningcss: 1.30.2
      magic-string: 0.30.21
      source-map-js: 1.2.1
      tailwindcss: 4.1.17

  '@tailwindcss/oxide-android-arm64@4.1.17':
    optional: true

  '@tailwindcss/oxide-darwin-arm64@4.1.17':
    optional: true

  '@tailwindcss/oxide-darwin-x64@4.1.17':
    optional: true

  '@tailwindcss/oxide-freebsd-x64@4.1.17':
    optional: true

  '@tailwindcss/oxide-linux-arm-gnueabihf@4.1.17':
    optional: true

  '@tailwindcss/oxide-linux-arm64-gnu@4.1.17':
    optional: true

  '@tailwindcss/oxide-linux-arm64-musl@4.1.17':
    optional: true

  '@tailwindcss/oxide-linux-x64-gnu@4.1.17':
    optional: true

  '@tailwindcss/oxide-linux-x64-musl@4.1.17':
    optional: true

  '@tailwindcss/oxide-wasm32-wasi@4.1.17':
    optional: true

  '@tailwindcss/oxide-win32-arm64-msvc@4.1.17':
    optional: true

  '@tailwindcss/oxide-win32-x64-msvc@4.1.17':
    optional: true

  '@tailwindcss/oxide@4.1.17':
    optionalDependencies:
      '@tailwindcss/oxide-android-arm64': 4.1.17
      '@tailwindcss/oxide-darwin-arm64': 4.1.17
      '@tailwindcss/oxide-darwin-x64': 4.1.17
      '@tailwindcss/oxide-freebsd-x64': 4.1.17
      '@tailwindcss/oxide-linux-arm-gnueabihf': 4.1.17
      '@tailwindcss/oxide-linux-arm64-gnu': 4.1.17
      '@tailwindcss/oxide-linux-arm64-musl': 4.1.17
      '@tailwindcss/oxide-linux-x64-gnu': 4.1.17
      '@tailwindcss/oxide-linux-x64-musl': 4.1.17
      '@tailwindcss/oxide-wasm32-wasi': 4.1.17
      '@tailwindcss/oxide-win32-arm64-msvc': 4.1.17
      '@tailwindcss/oxide-win32-x64-msvc': 4.1.17

  '@tailwindcss/vite@4.1.17(vite@6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2))':
    dependencies:
      '@tailwindcss/node': 4.1.17
      '@tailwindcss/oxide': 4.1.17
      tailwindcss: 4.1.17
      vite: 6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2)

  '@types/debug@4.1.12':
    dependencies:
      '@types/ms': 2.1.0

  '@types/estree@1.0.8': {}

  '@types/fontkit@2.0.8':
    dependencies:
      '@types/node': 24.10.0

  '@types/hast@3.0.4':
    dependencies:
      '@types/unist': 3.0.3

  '@types/mdast@4.0.4':
    dependencies:
      '@types/unist': 3.0.3

  '@types/ms@2.1.0': {}

  '@types/nlcst@2.0.3':
    dependencies:
      '@types/unist': 3.0.3

  '@types/node@24.10.0':
    dependencies:
      undici-types: 7.16.0

  '@types/unist@3.0.3': {}

  '@ungap/structured-clone@1.3.0': {}

  acorn@8.15.0: {}

  ansi-align@3.0.1:
    dependencies:
      string-width: 4.2.3

  ansi-regex@5.0.1: {}

  ansi-regex@6.2.2: {}

  ansi-styles@6.2.3: {}

  anymatch@3.1.3:
    dependencies:
      normalize-path: 3.0.0
      picomatch: 2.3.1

  argparse@2.0.1: {}

  aria-query@5.3.2: {}

  array-iterate@2.0.1: {}

  astro@5.15.5(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2)(rollup@4.53.2)(typescript@5.9.3):
    dependencies:
      '@astrojs/compiler': 2.13.0
      '@astrojs/internal-helpers': 0.7.4
      '@astrojs/markdown-remark': 6.3.8
      '@astrojs/telemetry': 3.3.0
      '@capsizecss/unpack': 3.0.0
      '@oslojs/encoding': 1.1.0
      '@rollup/pluginutils': 5.3.0(rollup@4.53.2)
      acorn: 8.15.0
      aria-query: 5.3.2
      axobject-query: 4.1.0
      boxen: 8.0.1
      ci-info: 4.3.1
      clsx: 2.1.1
      common-ancestor-path: 1.0.1
      cookie: 1.0.2
      cssesc: 3.0.0
      debug: 4.4.3
      deterministic-object-hash: 2.0.2
      devalue: 5.4.2
      diff: 5.2.0
      dlv: 1.1.3
      dset: 3.1.4
      es-module-lexer: 1.7.0
      esbuild: 0.25.12
      estree-walker: 3.0.3
      flattie: 1.1.1
      fontace: 0.3.1
      github-slugger: 2.0.0
      html-escaper: 3.0.3
      http-cache-semantics: 4.2.0
      import-meta-resolve: 4.2.0
      js-yaml: 4.1.0
      magic-string: 0.30.21
      magicast: 0.3.5
      mrmime: 2.0.1
      neotraverse: 0.6.18
      p-limit: 6.2.0
      p-queue: 8.1.1
      package-manager-detector: 1.5.0
      picocolors: 1.1.1
      picomatch: 4.0.3
      prompts: 2.4.2
      rehype: 13.0.2
      semver: 7.7.3
      shiki: 3.15.0
      smol-toml: 1.4.2
      tinyexec: 1.0.2
      tinyglobby: 0.2.15
      tsconfck: 3.1.6(typescript@5.9.3)
      ultrahtml: 1.6.0
      unifont: 0.6.0
      unist-util-visit: 5.0.0
      unstorage: 1.17.2
      vfile: 6.0.3
      vite: 6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2)
      vitefu: 1.1.1(vite@6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2))
      xxhash-wasm: 1.1.0
      yargs-parser: 21.1.1
      yocto-spinner: 0.2.3
      zod: 3.25.76
      zod-to-json-schema: 3.24.6(zod@3.25.76)
      zod-to-ts: 1.2.0(typescript@5.9.3)(zod@3.25.76)
    optionalDependencies:
      sharp: 0.34.5
    transitivePeerDependencies:
      - '@azure/app-configuration'
      - '@azure/cosmos'
      - '@azure/data-tables'
      - '@azure/identity'
      - '@azure/keyvault-secrets'
      - '@azure/storage-blob'
      - '@capacitor/preferences'
      - '@deno/kv'
      - '@netlify/blobs'
      - '@planetscale/database'
      - '@types/node'
      - '@upstash/redis'
      - '@vercel/blob'
      - '@vercel/functions'
      - '@vercel/kv'
      - aws4fetch
      - db0
      - idb-keyval
      - ioredis
      - jiti
      - less
      - lightningcss
      - rollup
      - sass
      - sass-embedded
      - stylus
      - sugarss
      - supports-color
      - terser
      - tsx
      - typescript
      - uploadthing
      - yaml

  axobject-query@4.1.0: {}

  bail@2.0.2: {}

  base-64@1.0.0: {}

  base64-js@1.5.1: {}

  boxen@8.0.1:
    dependencies:
      ansi-align: 3.0.1
      camelcase: 8.0.0
      chalk: 5.6.2
      cli-boxes: 3.0.0
      string-width: 7.2.0
      type-fest: 4.41.0
      widest-line: 5.0.0
      wrap-ansi: 9.0.2

  brotli@1.3.3:
    dependencies:
      base64-js: 1.5.1

  camelcase@8.0.0: {}

  ccount@2.0.1: {}

  chalk@5.6.2: {}

  character-entities-html4@2.1.0: {}

  character-entities-legacy@3.0.0: {}

  character-entities@2.0.2: {}

  chokidar@4.0.3:
    dependencies:
      readdirp: 4.1.2

  ci-info@4.3.1: {}

  class-variance-authority@0.7.1:
    dependencies:
      clsx: 2.1.1

  cli-boxes@3.0.0: {}

  clone@2.1.2: {}

  clsx@2.1.1: {}

  comma-separated-tokens@2.0.3: {}

  common-ancestor-path@1.0.1: {}

  cookie-es@1.2.2: {}

  cookie@1.0.2: {}

  crossws@0.3.5:
    dependencies:
      uncrypto: 0.1.3

  css-tree@3.1.0:
    dependencies:
      mdn-data: 2.12.2
      source-map-js: 1.2.1

  cssesc@3.0.0: {}

  debug@4.4.3:
    dependencies:
      ms: 2.1.3

  decode-named-character-reference@1.2.0:
    dependencies:
      character-entities: 2.0.2

  defu@6.1.4: {}

  dequal@2.0.3: {}

  destr@2.0.5: {}

  detect-libc@2.1.2: {}

  deterministic-object-hash@2.0.2:
    dependencies:
      base-64: 1.0.0

  devalue@5.4.2: {}

  devlop@1.1.0:
    dependencies:
      dequal: 2.0.3

  dfa@1.2.0: {}

  diff@5.2.0: {}

  dlv@1.1.3: {}

  dset@3.1.4: {}

  emoji-regex@10.6.0: {}

  emoji-regex@8.0.0: {}

  enhanced-resolve@5.18.3:
    dependencies:
      graceful-fs: 4.2.11
      tapable: 2.3.0

  entities@6.0.1: {}

  es-module-lexer@1.7.0: {}

  esbuild@0.25.12:
    optionalDependencies:
      '@esbuild/aix-ppc64': 0.25.12
      '@esbuild/android-arm': 0.25.12
      '@esbuild/android-arm64': 0.25.12
      '@esbuild/android-x64': 0.25.12
      '@esbuild/darwin-arm64': 0.25.12
      '@esbuild/darwin-x64': 0.25.12
      '@esbuild/freebsd-arm64': 0.25.12
      '@esbuild/freebsd-x64': 0.25.12
      '@esbuild/linux-arm': 0.25.12
      '@esbuild/linux-arm64': 0.25.12
      '@esbuild/linux-ia32': 0.25.12
      '@esbuild/linux-loong64': 0.25.12
      '@esbuild/linux-mips64el': 0.25.12
      '@esbuild/linux-ppc64': 0.25.12
      '@esbuild/linux-riscv64': 0.25.12
      '@esbuild/linux-s390x': 0.25.12
      '@esbuild/linux-x64': 0.25.12
      '@esbuild/netbsd-arm64': 0.25.12
      '@esbuild/netbsd-x64': 0.25.12
      '@esbuild/openbsd-arm64': 0.25.12
      '@esbuild/openbsd-x64': 0.25.12
      '@esbuild/openharmony-arm64': 0.25.12
      '@esbuild/sunos-x64': 0.25.12
      '@esbuild/win32-arm64': 0.25.12
      '@esbuild/win32-ia32': 0.25.12
      '@esbuild/win32-x64': 0.25.12

  escape-string-regexp@5.0.0: {}

  estree-walker@2.0.2: {}

  estree-walker@3.0.3:
    dependencies:
      '@types/estree': 1.0.8

  eventemitter3@5.0.1: {}

  extend@3.0.2: {}

  fast-deep-equal@3.1.3: {}

  fast-xml-parser@5.3.1:
    dependencies:
      strnum: 2.1.1

  fdir@6.5.0(picomatch@4.0.3):
    optionalDependencies:
      picomatch: 4.0.3

  flattie@1.1.1: {}

  fontace@0.3.1:
    dependencies:
      '@types/fontkit': 2.0.8
      fontkit: 2.0.4

  fontkit@2.0.4:
    dependencies:
      '@swc/helpers': 0.5.17
      brotli: 1.3.3
      clone: 2.1.2
      dfa: 1.2.0
      fast-deep-equal: 3.1.3
      restructure: 3.0.2
      tiny-inflate: 1.0.3
      unicode-properties: 1.4.1
      unicode-trie: 2.0.0

  fsevents@2.3.3:
    optional: true

  get-east-asian-width@1.4.0: {}

  github-slugger@2.0.0: {}

  graceful-fs@4.2.11: {}

  h3@1.15.4:
    dependencies:
      cookie-es: 1.2.2
      crossws: 0.3.5
      defu: 6.1.4
      destr: 2.0.5
      iron-webcrypto: 1.2.1
      node-mock-http: 1.0.3
      radix3: 1.1.2
      ufo: 1.6.1
      uncrypto: 0.1.3

  hast-util-from-html@2.0.3:
    dependencies:
      '@types/hast': 3.0.4
      devlop: 1.1.0
      hast-util-from-parse5: 8.0.3
      parse5: 7.3.0
      vfile: 6.0.3
      vfile-message: 4.0.3

  hast-util-from-parse5@8.0.3:
    dependencies:
      '@types/hast': 3.0.4
      '@types/unist': 3.0.3
      devlop: 1.1.0
      hastscript: 9.0.1
      property-information: 7.1.0
      vfile: 6.0.3
      vfile-location: 5.0.3
      web-namespaces: 2.0.1

  hast-util-is-element@3.0.0:
    dependencies:
      '@types/hast': 3.0.4

  hast-util-parse-selector@4.0.0:
    dependencies:
      '@types/hast': 3.0.4

  hast-util-raw@9.1.0:
    dependencies:
      '@types/hast': 3.0.4
      '@types/unist': 3.0.3
      '@ungap/structured-clone': 1.3.0
      hast-util-from-parse5: 8.0.3
      hast-util-to-parse5: 8.0.0
      html-void-elements: 3.0.0
      mdast-util-to-hast: 13.2.0
      parse5: 7.3.0
      unist-util-position: 5.0.0
      unist-util-visit: 5.0.0
      vfile: 6.0.3
      web-namespaces: 2.0.1
      zwitch: 2.0.4

  hast-util-to-html@9.0.5:
    dependencies:
      '@types/hast': 3.0.4
      '@types/unist': 3.0.3
      ccount: 2.0.1
      comma-separated-tokens: 2.0.3
      hast-util-whitespace: 3.0.0
      html-void-elements: 3.0.0
      mdast-util-to-hast: 13.2.0
      property-information: 7.1.0
      space-separated-tokens: 2.0.2
      stringify-entities: 4.0.4
      zwitch: 2.0.4

  hast-util-to-parse5@8.0.0:
    dependencies:
      '@types/hast': 3.0.4
      comma-separated-tokens: 2.0.3
      devlop: 1.1.0
      property-information: 6.5.0
      space-separated-tokens: 2.0.2
      web-namespaces: 2.0.1
      zwitch: 2.0.4

  hast-util-to-text@4.0.2:
    dependencies:
      '@types/hast': 3.0.4
      '@types/unist': 3.0.3
      hast-util-is-element: 3.0.0
      unist-util-find-after: 5.0.0

  hast-util-whitespace@3.0.0:
    dependencies:
      '@types/hast': 3.0.4

  hastscript@9.0.1:
    dependencies:
      '@types/hast': 3.0.4
      comma-separated-tokens: 2.0.3
      hast-util-parse-selector: 4.0.0
      property-information: 7.1.0
      space-separated-tokens: 2.0.2

  html-escaper@3.0.3: {}

  html-void-elements@3.0.0: {}

  http-cache-semantics@4.2.0: {}

  import-meta-resolve@4.2.0: {}

  iron-webcrypto@1.2.1: {}

  is-docker@3.0.0: {}

  is-fullwidth-code-point@3.0.0: {}

  is-inside-container@1.0.0:
    dependencies:
      is-docker: 3.0.0

  is-plain-obj@4.1.0: {}

  is-wsl@3.1.0:
    dependencies:
      is-inside-container: 1.0.0

  jiti@2.6.1: {}

  js-yaml@4.1.0:
    dependencies:
      argparse: 2.0.1

  kleur@3.0.3: {}

  lightningcss-android-arm64@1.30.2:
    optional: true

  lightningcss-darwin-arm64@1.30.2:
    optional: true

  lightningcss-darwin-x64@1.30.2:
    optional: true

  lightningcss-freebsd-x64@1.30.2:
    optional: true

  lightningcss-linux-arm-gnueabihf@1.30.2:
    optional: true

  lightningcss-linux-arm64-gnu@1.30.2:
    optional: true

  lightningcss-linux-arm64-musl@1.30.2:
    optional: true

  lightningcss-linux-x64-gnu@1.30.2:
    optional: true

  lightningcss-linux-x64-musl@1.30.2:
    optional: true

  lightningcss-win32-arm64-msvc@1.30.2:
    optional: true

  lightningcss-win32-x64-msvc@1.30.2:
    optional: true

  lightningcss@1.30.2:
    dependencies:
      detect-libc: 2.1.2
    optionalDependencies:
      lightningcss-android-arm64: 1.30.2
      lightningcss-darwin-arm64: 1.30.2
      lightningcss-darwin-x64: 1.30.2
      lightningcss-freebsd-x64: 1.30.2
      lightningcss-linux-arm-gnueabihf: 1.30.2
      lightningcss-linux-arm64-gnu: 1.30.2
      lightningcss-linux-arm64-musl: 1.30.2
      lightningcss-linux-x64-gnu: 1.30.2
      lightningcss-linux-x64-musl: 1.30.2
      lightningcss-win32-arm64-msvc: 1.30.2
      lightningcss-win32-x64-msvc: 1.30.2

  longest-streak@3.1.0: {}

  lru-cache@10.4.3: {}

  magic-string@0.30.21:
    dependencies:
      '@jridgewell/sourcemap-codec': 1.5.5

  magicast@0.3.5:
    dependencies:
      '@babel/parser': 7.28.5
      '@babel/types': 7.28.5
      source-map-js: 1.2.1

  markdown-table@3.0.4: {}

  mdast-util-definitions@6.0.0:
    dependencies:
      '@types/mdast': 4.0.4
      '@types/unist': 3.0.3
      unist-util-visit: 5.0.0

  mdast-util-find-and-replace@3.0.2:
    dependencies:
      '@types/mdast': 4.0.4
      escape-string-regexp: 5.0.0
      unist-util-is: 6.0.1
      unist-util-visit-parents: 6.0.2

  mdast-util-from-markdown@2.0.2:
    dependencies:
      '@types/mdast': 4.0.4
      '@types/unist': 3.0.3
      decode-named-character-reference: 1.2.0
      devlop: 1.1.0
      mdast-util-to-string: 4.0.0
      micromark: 4.0.2
      micromark-util-decode-numeric-character-reference: 2.0.2
      micromark-util-decode-string: 2.0.1
      micromark-util-normalize-identifier: 2.0.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2
      unist-util-stringify-position: 4.0.0
    transitivePeerDependencies:
      - supports-color

  mdast-util-gfm-autolink-literal@2.0.1:
    dependencies:
      '@types/mdast': 4.0.4
      ccount: 2.0.1
      devlop: 1.1.0
      mdast-util-find-and-replace: 3.0.2
      micromark-util-character: 2.1.1

  mdast-util-gfm-footnote@2.1.0:
    dependencies:
      '@types/mdast': 4.0.4
      devlop: 1.1.0
      mdast-util-from-markdown: 2.0.2
      mdast-util-to-markdown: 2.1.2
      micromark-util-normalize-identifier: 2.0.1
    transitivePeerDependencies:
      - supports-color

  mdast-util-gfm-strikethrough@2.0.0:
    dependencies:
      '@types/mdast': 4.0.4
      mdast-util-from-markdown: 2.0.2
      mdast-util-to-markdown: 2.1.2
    transitivePeerDependencies:
      - supports-color

  mdast-util-gfm-table@2.0.0:
    dependencies:
      '@types/mdast': 4.0.4
      devlop: 1.1.0
      markdown-table: 3.0.4
      mdast-util-from-markdown: 2.0.2
      mdast-util-to-markdown: 2.1.2
    transitivePeerDependencies:
      - supports-color

  mdast-util-gfm-task-list-item@2.0.0:
    dependencies:
      '@types/mdast': 4.0.4
      devlop: 1.1.0
      mdast-util-from-markdown: 2.0.2
      mdast-util-to-markdown: 2.1.2
    transitivePeerDependencies:
      - supports-color

  mdast-util-gfm@3.1.0:
    dependencies:
      mdast-util-from-markdown: 2.0.2
      mdast-util-gfm-autolink-literal: 2.0.1
      mdast-util-gfm-footnote: 2.1.0
      mdast-util-gfm-strikethrough: 2.0.0
      mdast-util-gfm-table: 2.0.0
      mdast-util-gfm-task-list-item: 2.0.0
      mdast-util-to-markdown: 2.1.2
    transitivePeerDependencies:
      - supports-color

  mdast-util-phrasing@4.1.0:
    dependencies:
      '@types/mdast': 4.0.4
      unist-util-is: 6.0.1

  mdast-util-to-hast@13.2.0:
    dependencies:
      '@types/hast': 3.0.4
      '@types/mdast': 4.0.4
      '@ungap/structured-clone': 1.3.0
      devlop: 1.1.0
      micromark-util-sanitize-uri: 2.0.1
      trim-lines: 3.0.1
      unist-util-position: 5.0.0
      unist-util-visit: 5.0.0
      vfile: 6.0.3

  mdast-util-to-markdown@2.1.2:
    dependencies:
      '@types/mdast': 4.0.4
      '@types/unist': 3.0.3
      longest-streak: 3.1.0
      mdast-util-phrasing: 4.1.0
      mdast-util-to-string: 4.0.0
      micromark-util-classify-character: 2.0.1
      micromark-util-decode-string: 2.0.1
      unist-util-visit: 5.0.0
      zwitch: 2.0.4

  mdast-util-to-string@4.0.0:
    dependencies:
      '@types/mdast': 4.0.4

  mdn-data@2.12.2: {}

  micromark-core-commonmark@2.0.3:
    dependencies:
      decode-named-character-reference: 1.2.0
      devlop: 1.1.0
      micromark-factory-destination: 2.0.1
      micromark-factory-label: 2.0.1
      micromark-factory-space: 2.0.1
      micromark-factory-title: 2.0.1
      micromark-factory-whitespace: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-chunked: 2.0.1
      micromark-util-classify-character: 2.0.1
      micromark-util-html-tag-name: 2.0.1
      micromark-util-normalize-identifier: 2.0.1
      micromark-util-resolve-all: 2.0.1
      micromark-util-subtokenize: 2.1.0
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-extension-gfm-autolink-literal@2.1.0:
    dependencies:
      micromark-util-character: 2.1.1
      micromark-util-sanitize-uri: 2.0.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-extension-gfm-footnote@2.1.0:
    dependencies:
      devlop: 1.1.0
      micromark-core-commonmark: 2.0.3
      micromark-factory-space: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-normalize-identifier: 2.0.1
      micromark-util-sanitize-uri: 2.0.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-extension-gfm-strikethrough@2.1.0:
    dependencies:
      devlop: 1.1.0
      micromark-util-chunked: 2.0.1
      micromark-util-classify-character: 2.0.1
      micromark-util-resolve-all: 2.0.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-extension-gfm-table@2.1.1:
    dependencies:
      devlop: 1.1.0
      micromark-factory-space: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-extension-gfm-tagfilter@2.0.0:
    dependencies:
      micromark-util-types: 2.0.2

  micromark-extension-gfm-task-list-item@2.1.0:
    dependencies:
      devlop: 1.1.0
      micromark-factory-space: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-extension-gfm@3.0.0:
    dependencies:
      micromark-extension-gfm-autolink-literal: 2.1.0
      micromark-extension-gfm-footnote: 2.1.0
      micromark-extension-gfm-strikethrough: 2.1.0
      micromark-extension-gfm-table: 2.1.1
      micromark-extension-gfm-tagfilter: 2.0.0
      micromark-extension-gfm-task-list-item: 2.1.0
      micromark-util-combine-extensions: 2.0.1
      micromark-util-types: 2.0.2

  micromark-factory-destination@2.0.1:
    dependencies:
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-factory-label@2.0.1:
    dependencies:
      devlop: 1.1.0
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-factory-space@2.0.1:
    dependencies:
      micromark-util-character: 2.1.1
      micromark-util-types: 2.0.2

  micromark-factory-title@2.0.1:
    dependencies:
      micromark-factory-space: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-factory-whitespace@2.0.1:
    dependencies:
      micromark-factory-space: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-util-character@2.1.1:
    dependencies:
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-util-chunked@2.0.1:
    dependencies:
      micromark-util-symbol: 2.0.1

  micromark-util-classify-character@2.0.1:
    dependencies:
      micromark-util-character: 2.1.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-util-combine-extensions@2.0.1:
    dependencies:
      micromark-util-chunked: 2.0.1
      micromark-util-types: 2.0.2

  micromark-util-decode-numeric-character-reference@2.0.2:
    dependencies:
      micromark-util-symbol: 2.0.1

  micromark-util-decode-string@2.0.1:
    dependencies:
      decode-named-character-reference: 1.2.0
      micromark-util-character: 2.1.1
      micromark-util-decode-numeric-character-reference: 2.0.2
      micromark-util-symbol: 2.0.1

  micromark-util-encode@2.0.1: {}

  micromark-util-html-tag-name@2.0.1: {}

  micromark-util-normalize-identifier@2.0.1:
    dependencies:
      micromark-util-symbol: 2.0.1

  micromark-util-resolve-all@2.0.1:
    dependencies:
      micromark-util-types: 2.0.2

  micromark-util-sanitize-uri@2.0.1:
    dependencies:
      micromark-util-character: 2.1.1
      micromark-util-encode: 2.0.1
      micromark-util-symbol: 2.0.1

  micromark-util-subtokenize@2.1.0:
    dependencies:
      devlop: 1.1.0
      micromark-util-chunked: 2.0.1
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2

  micromark-util-symbol@2.0.1: {}

  micromark-util-types@2.0.2: {}

  micromark@4.0.2:
    dependencies:
      '@types/debug': 4.1.12
      debug: 4.4.3
      decode-named-character-reference: 1.2.0
      devlop: 1.1.0
      micromark-core-commonmark: 2.0.3
      micromark-factory-space: 2.0.1
      micromark-util-character: 2.1.1
      micromark-util-chunked: 2.0.1
      micromark-util-combine-extensions: 2.0.1
      micromark-util-decode-numeric-character-reference: 2.0.2
      micromark-util-encode: 2.0.1
      micromark-util-normalize-identifier: 2.0.1
      micromark-util-resolve-all: 2.0.1
      micromark-util-sanitize-uri: 2.0.1
      micromark-util-subtokenize: 2.1.0
      micromark-util-symbol: 2.0.1
      micromark-util-types: 2.0.2
    transitivePeerDependencies:
      - supports-color

  mrmime@2.0.1: {}

  ms@2.1.3: {}

  nanoid@3.3.11: {}

  neotraverse@0.6.18: {}

  nlcst-to-string@4.0.0:
    dependencies:
      '@types/nlcst': 2.0.3

  node-fetch-native@1.6.7: {}

  node-mock-http@1.0.3: {}

  normalize-path@3.0.0: {}

  ofetch@1.5.1:
    dependencies:
      destr: 2.0.5
      node-fetch-native: 1.6.7
      ufo: 1.6.1

  ohash@2.0.11: {}

  oniguruma-parser@0.12.1: {}

  oniguruma-to-es@4.3.3:
    dependencies:
      oniguruma-parser: 0.12.1
      regex: 6.0.1
      regex-recursion: 6.0.2

  p-limit@6.2.0:
    dependencies:
      yocto-queue: 1.2.2

  p-queue@8.1.1:
    dependencies:
      eventemitter3: 5.0.1
      p-timeout: 6.1.4

  p-timeout@6.1.4: {}

  package-manager-detector@1.5.0: {}

  pako@0.2.9: {}

  parse-latin@7.0.0:
    dependencies:
      '@types/nlcst': 2.0.3
      '@types/unist': 3.0.3
      nlcst-to-string: 4.0.0
      unist-util-modify-children: 4.0.0
      unist-util-visit-children: 3.0.0
      vfile: 6.0.3

  parse5@7.3.0:
    dependencies:
      entities: 6.0.1

  picocolors@1.1.1: {}

  picomatch@2.3.1: {}

  picomatch@4.0.3: {}

  postcss@8.5.6:
    dependencies:
      nanoid: 3.3.11
      picocolors: 1.1.1
      source-map-js: 1.2.1

  prismjs@1.30.0: {}

  prompts@2.4.2:
    dependencies:
      kleur: 3.0.3
      sisteransi: 1.0.5

  property-information@6.5.0: {}

  property-information@7.1.0: {}

  radix3@1.1.2: {}

  readdirp@4.1.2: {}

  regex-recursion@6.0.2:
    dependencies:
      regex-utilities: 2.3.0

  regex-utilities@2.3.0: {}

  regex@6.0.1:
    dependencies:
      regex-utilities: 2.3.0

  rehype-parse@9.0.1:
    dependencies:
      '@types/hast': 3.0.4
      hast-util-from-html: 2.0.3
      unified: 11.0.5

  rehype-raw@7.0.0:
    dependencies:
      '@types/hast': 3.0.4
      hast-util-raw: 9.1.0
      vfile: 6.0.3

  rehype-stringify@10.0.1:
    dependencies:
      '@types/hast': 3.0.4
      hast-util-to-html: 9.0.5
      unified: 11.0.5

  rehype@13.0.2:
    dependencies:
      '@types/hast': 3.0.4
      rehype-parse: 9.0.1
      rehype-stringify: 10.0.1
      unified: 11.0.5

  remark-gfm@4.0.1:
    dependencies:
      '@types/mdast': 4.0.4
      mdast-util-gfm: 3.1.0
      micromark-extension-gfm: 3.0.0
      remark-parse: 11.0.0
      remark-stringify: 11.0.0
      unified: 11.0.5
    transitivePeerDependencies:
      - supports-color

  remark-parse@11.0.0:
    dependencies:
      '@types/mdast': 4.0.4
      mdast-util-from-markdown: 2.0.2
      micromark-util-types: 2.0.2
      unified: 11.0.5
    transitivePeerDependencies:
      - supports-color

  remark-rehype@11.1.2:
    dependencies:
      '@types/hast': 3.0.4
      '@types/mdast': 4.0.4
      mdast-util-to-hast: 13.2.0
      unified: 11.0.5
      vfile: 6.0.3

  remark-smartypants@3.0.2:
    dependencies:
      retext: 9.0.0
      retext-smartypants: 6.2.0
      unified: 11.0.5
      unist-util-visit: 5.0.0

  remark-stringify@11.0.0:
    dependencies:
      '@types/mdast': 4.0.4
      mdast-util-to-markdown: 2.1.2
      unified: 11.0.5

  restructure@3.0.2: {}

  retext-latin@4.0.0:
    dependencies:
      '@types/nlcst': 2.0.3
      parse-latin: 7.0.0
      unified: 11.0.5

  retext-smartypants@6.2.0:
    dependencies:
      '@types/nlcst': 2.0.3
      nlcst-to-string: 4.0.0
      unist-util-visit: 5.0.0

  retext-stringify@4.0.0:
    dependencies:
      '@types/nlcst': 2.0.3
      nlcst-to-string: 4.0.0
      unified: 11.0.5

  retext@9.0.0:
    dependencies:
      '@types/nlcst': 2.0.3
      retext-latin: 4.0.0
      retext-stringify: 4.0.0
      unified: 11.0.5

  rollup@4.53.2:
    dependencies:
      '@types/estree': 1.0.8
    optionalDependencies:
      '@rollup/rollup-android-arm-eabi': 4.53.2
      '@rollup/rollup-android-arm64': 4.53.2
      '@rollup/rollup-darwin-arm64': 4.53.2
      '@rollup/rollup-darwin-x64': 4.53.2
      '@rollup/rollup-freebsd-arm64': 4.53.2
      '@rollup/rollup-freebsd-x64': 4.53.2
      '@rollup/rollup-linux-arm-gnueabihf': 4.53.2
      '@rollup/rollup-linux-arm-musleabihf': 4.53.2
      '@rollup/rollup-linux-arm64-gnu': 4.53.2
      '@rollup/rollup-linux-arm64-musl': 4.53.2
      '@rollup/rollup-linux-loong64-gnu': 4.53.2
      '@rollup/rollup-linux-ppc64-gnu': 4.53.2
      '@rollup/rollup-linux-riscv64-gnu': 4.53.2
      '@rollup/rollup-linux-riscv64-musl': 4.53.2
      '@rollup/rollup-linux-s390x-gnu': 4.53.2
      '@rollup/rollup-linux-x64-gnu': 4.53.2
      '@rollup/rollup-linux-x64-musl': 4.53.2
      '@rollup/rollup-openharmony-arm64': 4.53.2
      '@rollup/rollup-win32-arm64-msvc': 4.53.2
      '@rollup/rollup-win32-ia32-msvc': 4.53.2
      '@rollup/rollup-win32-x64-gnu': 4.53.2
      '@rollup/rollup-win32-x64-msvc': 4.53.2
      fsevents: 2.3.3

  semver@7.7.3: {}

  sharp@0.34.5:
    dependencies:
      '@img/colour': 1.0.0
      detect-libc: 2.1.2
      semver: 7.7.3
    optionalDependencies:
      '@img/sharp-darwin-arm64': 0.34.5
      '@img/sharp-darwin-x64': 0.34.5
      '@img/sharp-libvips-darwin-arm64': 1.2.4
      '@img/sharp-libvips-darwin-x64': 1.2.4
      '@img/sharp-libvips-linux-arm': 1.2.4
      '@img/sharp-libvips-linux-arm64': 1.2.4
      '@img/sharp-libvips-linux-ppc64': 1.2.4
      '@img/sharp-libvips-linux-riscv64': 1.2.4
      '@img/sharp-libvips-linux-s390x': 1.2.4
      '@img/sharp-libvips-linux-x64': 1.2.4
      '@img/sharp-libvips-linuxmusl-arm64': 1.2.4
      '@img/sharp-libvips-linuxmusl-x64': 1.2.4
      '@img/sharp-linux-arm': 0.34.5
      '@img/sharp-linux-arm64': 0.34.5
      '@img/sharp-linux-ppc64': 0.34.5
      '@img/sharp-linux-riscv64': 0.34.5
      '@img/sharp-linux-s390x': 0.34.5
      '@img/sharp-linux-x64': 0.34.5
      '@img/sharp-linuxmusl-arm64': 0.34.5
      '@img/sharp-linuxmusl-x64': 0.34.5
      '@img/sharp-wasm32': 0.34.5
      '@img/sharp-win32-arm64': 0.34.5
      '@img/sharp-win32-ia32': 0.34.5
      '@img/sharp-win32-x64': 0.34.5
    optional: true

  shiki@3.15.0:
    dependencies:
      '@shikijs/core': 3.15.0
      '@shikijs/engine-javascript': 3.15.0
      '@shikijs/engine-oniguruma': 3.15.0
      '@shikijs/langs': 3.15.0
      '@shikijs/themes': 3.15.0
      '@shikijs/types': 3.15.0
      '@shikijs/vscode-textmate': 10.0.2
      '@types/hast': 3.0.4

  sisteransi@1.0.5: {}

  smol-toml@1.4.2: {}

  source-map-js@1.2.1: {}

  space-separated-tokens@2.0.2: {}

  string-width@4.2.3:
    dependencies:
      emoji-regex: 8.0.0
      is-fullwidth-code-point: 3.0.0
      strip-ansi: 6.0.1

  string-width@7.2.0:
    dependencies:
      emoji-regex: 10.6.0
      get-east-asian-width: 1.4.0
      strip-ansi: 7.1.2

  stringify-entities@4.0.4:
    dependencies:
      character-entities-html4: 2.1.0
      character-entities-legacy: 3.0.0

  strip-ansi@6.0.1:
    dependencies:
      ansi-regex: 5.0.1

  strip-ansi@7.1.2:
    dependencies:
      ansi-regex: 6.2.2

  strnum@2.1.1: {}

  tailwind-merge@3.4.0: {}

  tailwindcss@4.1.17: {}

  tapable@2.3.0: {}

  tiny-inflate@1.0.3: {}

  tinyexec@1.0.2: {}

  tinyglobby@0.2.15:
    dependencies:
      fdir: 6.5.0(picomatch@4.0.3)
      picomatch: 4.0.3

  trim-lines@3.0.1: {}

  trough@2.2.0: {}

  tsconfck@3.1.6(typescript@5.9.3):
    optionalDependencies:
      typescript: 5.9.3

  tslib@2.8.1: {}

  tw-animate-css@1.4.0: {}

  type-fest@4.41.0: {}

  typescript@5.9.3: {}

  ufo@1.6.1: {}

  ultrahtml@1.6.0: {}

  uncrypto@0.1.3: {}

  undici-types@7.16.0: {}

  unicode-properties@1.4.1:
    dependencies:
      base64-js: 1.5.1
      unicode-trie: 2.0.0

  unicode-trie@2.0.0:
    dependencies:
      pako: 0.2.9
      tiny-inflate: 1.0.3

  unified@11.0.5:
    dependencies:
      '@types/unist': 3.0.3
      bail: 2.0.2
      devlop: 1.1.0
      extend: 3.0.2
      is-plain-obj: 4.1.0
      trough: 2.2.0
      vfile: 6.0.3

  unifont@0.6.0:
    dependencies:
      css-tree: 3.1.0
      ofetch: 1.5.1
      ohash: 2.0.11

  unist-util-find-after@5.0.0:
    dependencies:
      '@types/unist': 3.0.3
      unist-util-is: 6.0.1

  unist-util-is@6.0.1:
    dependencies:
      '@types/unist': 3.0.3

  unist-util-modify-children@4.0.0:
    dependencies:
      '@types/unist': 3.0.3
      array-iterate: 2.0.1

  unist-util-position@5.0.0:
    dependencies:
      '@types/unist': 3.0.3

  unist-util-remove-position@5.0.0:
    dependencies:
      '@types/unist': 3.0.3
      unist-util-visit: 5.0.0

  unist-util-stringify-position@4.0.0:
    dependencies:
      '@types/unist': 3.0.3

  unist-util-visit-children@3.0.0:
    dependencies:
      '@types/unist': 3.0.3

  unist-util-visit-parents@6.0.2:
    dependencies:
      '@types/unist': 3.0.3
      unist-util-is: 6.0.1

  unist-util-visit@5.0.0:
    dependencies:
      '@types/unist': 3.0.3
      unist-util-is: 6.0.1
      unist-util-visit-parents: 6.0.2

  unstorage@1.17.2:
    dependencies:
      anymatch: 3.1.3
      chokidar: 4.0.3
      destr: 2.0.5
      h3: 1.15.4
      lru-cache: 10.4.3
      node-fetch-native: 1.6.7
      ofetch: 1.5.1
      ufo: 1.6.1

  vfile-location@5.0.3:
    dependencies:
      '@types/unist': 3.0.3
      vfile: 6.0.3

  vfile-message@4.0.3:
    dependencies:
      '@types/unist': 3.0.3
      unist-util-stringify-position: 4.0.0

  vfile@6.0.3:
    dependencies:
      '@types/unist': 3.0.3
      vfile-message: 4.0.3

  vite@6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2):
    dependencies:
      esbuild: 0.25.12
      fdir: 6.5.0(picomatch@4.0.3)
      picomatch: 4.0.3
      postcss: 8.5.6
      rollup: 4.53.2
      tinyglobby: 0.2.15
    optionalDependencies:
      '@types/node': 24.10.0
      fsevents: 2.3.3
      jiti: 2.6.1
      lightningcss: 1.30.2

  vitefu@1.1.1(vite@6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2)):
    optionalDependencies:
      vite: 6.4.1(@types/node@24.10.0)(jiti@2.6.1)(lightningcss@1.30.2)

  web-namespaces@2.0.1: {}

  which-pm-runs@1.1.0: {}

  widest-line@5.0.0:
    dependencies:
      string-width: 7.2.0

  wrap-ansi@9.0.2:
    dependencies:
      ansi-styles: 6.2.3
      string-width: 7.2.0
      strip-ansi: 7.1.2

  xxhash-wasm@1.1.0: {}

  yargs-parser@21.1.1: {}

  yocto-queue@1.2.2: {}

  yocto-spinner@0.2.3:
    dependencies:
      yoctocolors: 2.1.2

  yoctocolors@2.1.2: {}

  zod-to-json-schema@3.24.6(zod@3.25.76):
    dependencies:
      zod: 3.25.76

  zod-to-ts@1.2.0(typescript@5.9.3)(zod@3.25.76):
    dependencies:
      typescript: 5.9.3
      zod: 3.25.76

  zod@3.25.76: {}

  zwitch@2.0.4: {}

```

---
### `pnpm-workspace.yaml`
```yaml
onlyBuiltDependencies:
  - esbuild
  - sharp

```

---
### `README.md`
```md
# Coughy.Net

## 🚀 Project Structure



```text
/
├── public/
│   └── favicon.svg
├── src
│   ├── assets
│   │   └── astro.svg
│   ├── components
│   │   └── Welcome.astro
│   ├── layouts
│   │   └── Layout.astro
│   └── pages
│       └── index.astro
└── package.json
```



## 🧞 Commands



| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `pnpm install`             | Installs dependencies                            |
| `pnpm dev`             | Starts local dev server at `localhost:4321`      |
| `pnpm build`           | Build your production site to `./dist/`          |
| `pnpm preview`         | Preview your build locally, before deploying     |
| `pnpm astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm astro -- --help` | Get help using the Astro CLI                     |

[Astro's documentation](https://docs.astro)

## Bug fixes

after installing tailwindcss there was a strange bug inside astro.js.config `./astro.js.config`  and I got it fixed.
if same thing happened, press ```shortcut ctrl+shift+p``` (if you use vscode) and run this command below: 

```vscode TypeScript: Restart TS server```
```

---
### `registry.json`
```json
{
  "$schema": "https://ui.shadcn.com/schema/registry.json",
  "name": "my-registry",
  "homepage": "https://mycomponents.com",
  "items": []
}
```

---
### `tsconfig.json`
```json
{
  // Use Astro's recommended strict base configuration
  "extends": "astro/tsconfigs/strict",

  "include": [
    ".astro/types.d.ts",
    "src/**/*",
    "astro.config.*"
, "public/scripts/nav-effects.js"  ],

  "exclude": [
    "dist",
    "node_modules"
  ],

  "compilerOptions": {
    /* === Core Settings === */
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "allowJs": true,
    "checkJs": false,

    /* === JSX / Framework Neutral === */
    "jsx": "preserve",                // Let Astro or any renderer decide

    /* === Paths / Imports === */
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },

    /* === Type Safety & Quality === */
    "strict": true,
    "noImplicitAny": true,
    "noUncheckedIndexedAccess": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true,             // Faster build
    "isolatedModules": true,

    /* === Output === */
    "noEmit": true
  }
}

```

---
### `src\categoryMapFa.ts`
```ts
// Import the glob loader
import { glob } from "astro/loaders";
// Import utilities from `astro:content`
import { z, defineCollection } from "astro:content";

// =========================
// BLOG COLLECTION (existing)
// =========================
const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.md", base: "./src/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    author: z.string(),
    image: z.object({
      url: z.string(),
      alt: z.string(),
    }),
    tags: z.array(z.string()),
  }),
});


const stories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories" }),
  schema: z.object({
  title: z.string().optional(),
  description: z.string().optional(),
  published: z.date().optional(),
  }),
});

const poetry = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/poems",
  }),
  schema: z.object({
    title: z.string(),
    poet: z.string().optional(),
    date: z.string().optional(),
    loyalty: z.string().optional(),
    image: z.string().optional(),
  }),
});

const storiesFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories-fa" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    file: z.string().optional(),
    image: z.string().optional(),
    link: z.string().optional(),
    date: z.string().optional(),
    published: z.boolean().default(true),
  }),
});

const wiki = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),   // perception, states, tools...
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});

const wikiFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});




export const collections = {
  blog,
  stories,
  poetry,
  storiesFa,
  wiki,
  wikiFa,
};

```

---
### `src\content.config.ts`
```ts
// Import the glob loader
import { glob } from "astro/loaders";
// Import utilities from `astro:content`
import { z, defineCollection } from "astro:content";

// =========================
// BLOG COLLECTION (existing)
// =========================
const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.md", base: "./src/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    author: z.string(),
    image: z.object({
      url: z.string(),
      alt: z.string(),
    }),
    tags: z.array(z.string()),
  }),
});


const stories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories" }),
  schema: z.object({
  title: z.string().optional(),
  description: z.string().optional(),
  published: z.date().optional(),
  }),
});

const poetry = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/poems",
  }),
  schema: z.object({
    title: z.string(),
    poet: z.string().optional(),
    date: z.string().optional(),
    loyalty: z.string().optional(),
    image: z.string().optional(),
  }),
});

const storiesFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories-fa" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    file: z.string().optional(),
    image: z.string().optional(),
    link: z.string().optional(),
    date: z.string().optional(),
    published: z.boolean().default(true),
  }),
});

const wiki = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),   // perception, states, tools...
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});

const wikiFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});




export const collections = {
  blog,
  stories,
  poetry,
  storiesFa,
  wiki,
  wikiFa,
};

```

---
### `src\blog\post-1.md`
```md
---
title: 'My First Blog Post'
pubDate: 2022-07-01
description: 'This is the first post of my new Astro blog.'
author: 'Astro Learner'
image:
    url: 'https://docs.astro.build/assets/rose.webp'
    alt: 'The Astro logo on a dark background with a pink glow.'
tags: ["Vibe Coding", "Animation", "Coughy Net"]
---




Welcome to my _new blog_ about learning Astro! Here, I will share my learning journey as I build a new website.

## What I've accomplished

1. **Installing Astro**: First, I created a new Astro project and set up my online accounts.

2. **Making Pages**: I then learned how to make pages by creating new `.astro` files and placing them in the `src/pages/` folder.

3. **Making Blog Posts**: This is my first blog post! I now have Astro pages and Markdown posts!

## What's next

I will finish the Astro tutorial, and then keep adding more posts. Watch this space for more to come.
```

---
### `src\blog\post-2.md`
```md
---
title: My Second Blog Post
author: Astro Learner
description: "After learning some Astro, I couldn't stop!"
image:
    url: "https://docs.astro.build/assets/arc.webp"
    alt: "The Astro logo on a dark background with a purple gradient arc."
pubDate: 2022-07-08
tags: ["astro", "literature", "Coughy Net", "Ali Ghorbani"]
---
After a successful first week learning Astro, I decided to try some more. I wrote and imported a small component from memory!
```

---
### `src\blog\post-3.md`
```md
---
title: My Third Blog Post
author: Astro Learner
description: "I had some challenges, but asking in the community really helped!"
image:
    url: "https://docs.astro.build/assets/rays.webp"
    alt: "The Astro logo on a dark background with rainbow rays."
pubDate: 2022-07-15
tags: ["astro", "learning in public", "setbacks", "community"]
---
It wasn't always smooth sailing, but I'm enjoying building with Astro. And, the [Discord community](https://astro.build/chat) is really friendly and helpful!
```

---
### `src\blog\post-4.md`
```md
---
title: My Fourth Blog Post
author: Astro Learner
description: "This post will show up on its own!"
image:
    url: "https://docs.astro.build/default-og-image.png"
    alt: "The word astro against an illustration of planets and stars."
pubDate: 2022-08-08
tags: ["astro", "successes"]
---
This post should show up with my other blog posts, because `import.meta.glob()` is returning a list of all my posts in order to create my list.
```

---
### `src\data\nav.ts`
```ts
export const navLinks: [string, string][] = [
  ["Home", "/"],
  ["Blog", "/blog"],
  ["Literature", "/literature"],
  ["Projects", "/projects"],
  ["Research", "/research"],
  ["Partners", "/partners"],
  ["Wiki", "/wiki"],
  ["About", "/about"],
]as const;
 
export const wikiLinks: [string, string][] = [
  ["Substances", "/wiki/substances"],
  ["Effects", "/wiki/effects"],
  ["Interactions", "/wiki/interactions"],
  ["Harm Reduction", "/wiki/harm_reduction"],
  ["Reports", "/wiki/reports"],
  ["About", "/wiki/about"],
  ["Coughy.net", "/"],
]as const;
 
export const farLinks: [string, string][] = [
  ["خانه", "/fa/"],
  ["بلاگ", "/fa/blog"],
  ["داستان", "/fa/stories"],
  ["پروژه ها", "/fa/projects"],
  ["تحقیقات", "/fa/research"],
  ["شرکا", "/fa/partners"],
  ["ویکی", "/fa/wiki"],
  ["درباره", "/fa/about"],
]as const;
 
export const farWikiLinks: [string, string][] = [
  ["مواد", "/fa/wiki/substances"],
  ["تأثیرات", "/fa/wiki/effects"],
  ["تداخلات", "/fa/wiki/interactions"],
  ["کاهش آسیب", "/fa/wiki/harm_reduction"],
  ["گزارش‌ها", "/fa/wiki/reports"],
  ["درباره", "/fa/wiki/about"],
  ["کافی‌نت", "/fa/"],
]as const;
 


```

---
### `src\lib\utils.ts`
```ts
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

```

---
### `src\pages\rss.xml.js`
```js
import rss from '@astrojs/rss';

import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection("blog");
  return rss({
    title: 'Astro Learner | Blog',
    description: 'My journey learning Astro',
    site: 'https://coughy.net',
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.pubDate,
      description: post.data.description,
      link: `/posts/${post.id}/`,
    })),
    customData: `<language>en-us</language>`,
  })
}
```

---
### `src\poems\Sum Things Up.md`
```md
---
title: "Sum Things Up"
poet: "Coughy"
date: "11 Nov 2025"
loyalty: 'Inspired by a poem known as Bokonim, by <a href="https://ekhtesari.com" target="_blank">Fatehem Ekhtesari</a>'
image: "/public/images/sum.png"
---
<pre>
   W
           ∑ things ⇧
 O
S
</pre>



  


Eeny, meeny, miney, moe! hands out, it's your turn! 
Big, bad, you’re wolf now! Let’s play some "wild" thing

Way past the backyards, houses and barnyards
No time for check things: heads up! just "run" thing

No phone, no backpacks, chase me like wolf packs
Don’t eat me just yet... play me like a “prey” thing

Lure me through sub-ways, slip out of sightses
come hide in lush here, hush… feel our 'this' thing

Your taste lingers on, teeth on my tongue
Heart-rate is punching, chewed up like 'pun' thing

waiting for a bus, with no extra fuss
Door slides to the left, climb up for "ride" thing

Tough seats, our soft ass, rear-view is dim glass
let nerves be nervous, restless for "wait" thing

got "nowhere" from "where?", “what now?” we're here
Less light at evening, trains are on "rail" thing


"two" with no tickets, destined to do tricks
hums syncs with rail sound, makes it like a “song” thing 


Pick some full pockets, don't wake them "up" thing
slip through their shadow, they will miss"Not" thing

Back into the crowds, city light and crows
Freeways and fast lanes, make haste on “walk” thing

Thin way through cars, no red/green lights 
Steps are predestined, death can be a "will" thing

Stay close and keep right, don't lose my sight 
No rush, no reason, we’re down for a 'late' thing

Sandwiched by hunger, devoured by the burger
lunching and dining, fold'em as "one" thing

Night seeps in slowly, darkness glow coldly
Crawl back to the shelter, warm me with a "hug" thing

moon shines on “lust” thing, "no one but us" thing
Life can be dealt with, but "fuck" makes it "fun" thing

you touch my back now, whisper me "some"-thing:
-my turn is over, wolf up, do a "what?" thing
      
```

---
### `src\poems\Violent Bloom.md`
```md
---
title: "Violent Bloom"
poet: "Coughy"
date: "20 Oct 2024"
image: "/public/gifs/bloom.mp4"
loyalty: 'gif made by <a href="https://www.reddit.com/user/StingrayZ" target="_blank">StingrayZ</a>'
---

Violets are red, and Roses are blue
Life can be violent, yet flowers get through
Unleash your petals, get injured by thorns
When pain is built up, just try shifting hue

      
```

---
### `src\stories\cry_as_punishment.md`
```md
---
title: "Cry as Punishment"
description: "(English version not published)"
category: "flash fiction"
---






The moment I opened the door, I couldn’t believe my eyes.
 My whole world collapsed upon my head within seconds.  
 Never ... ever... in a million years did I expect something like that from Tyler and Olivia.  
 And there they were: those filthy scumbags, standing frozen, staring back at me like deers in headlights.

God, I wish I hadn’t seen them.  
And the worst part? My dad saw it too.

I don’t remember how we got into the car.  
 One moment we were living the moment of truth—one that nearly gave my father a stroke—and the next, we were driving.  
 I splashed some water on my face using the little sink inside the dashboard.  
 Still stunned. Still spinning. My lungs felt crushed. I couldn’t even look dad in the eyes.

He was more rattled than I was—still hadn’t processed what we saw.  
 After a long, sick silence, he turned to me and growled:

-  “This what you wanted? Huh? Is *this* what you wanted? I told you they’re not our kind. Rotten, sleazy fucks.”

I couldn’t take it anymore. I broke.  
 Tears burst out like a cracked pipe.

I had trusted Tyler and Olivia with all my heart.  
 We were just a normal little three-way family.  
 I never thought it would end up like this.

- “Maybe… just maybe, we could give them another cha—”  
-  “Shut. Your. God. Fucking. Damn. Mouth. I don’t want to hear a single word.”  
- “But they—”  
-  “Aaagh god. now you tryna defend a lowlife cuck and a shameless bitch? you could've married better people Sarah... I knew they were not decent since folks. I knew it.” 

Every time I blinked, the scene came back.  
 Sharp. Vivid. Unshakable.

When we pulled up to the house, Dad hung the car beside the house on the car-hanger and we climbed out.  
 Mr. Dickson, our overly cheerful neighbor, was walking over.

-  “Not a word in front of him. Capiche?

Dad muttered through his teeth.

I nodded. “Okay.”

Mr. Dickson said Hi and made out with dad. I reluctantly took down his pants and sucked him off as a sign of respect.

 He seemed satisfied, placed a hand gently on my head, fingers grazing my scalp, and asked with false concern:

-  “Something bothering you sweetheart?”

I didn’t reply.  
 Just covered my eyes with my elbow, pushed open the front door through tears, and brushed past Mom—who was carrying a plate of rice.  
 I went straight to my room and locked the door behind.  
 Sat down to keep on crying.

A little later, I heard the door slam.  
 Then the shouting began.

I clamped both hands over my ears, but could still hear everything.

-  “What happened, Clint? What’s wrong with Sarah? Did something happen?”  
-  “What do you *think* happened? That fucking bastard… in his own fucking house.”  
- “In his own house *what*? Just say it.”  
- “they were…”

The sound of the plate of rice falling and shattering, *split my chest open.*

-  “No. No. No. I don’t believe it. I just can’t.”  
- “Sarah opened the door. We saw everything.”  
- “You’re lying.”  
- “I wish I was. But it’s true — the guy was fucking his own wife. In their own fucking house.”

The end.
```

---
### `src\stories\make love, not with eggs.md`
```md
---
title: "make love, not with eggs"
description: "A love story about ordinary fish - (not published)"
---


          
          
  
    
      
       






Most of the time, it's like… I don't know. It's like there's this thick, black cloud covering everything. Like we see the world, but we don't really see the world, you know?  
We're all just stumbling around. Directionless.No sense of meaning.No sense of purpose. I know that might sound super depressing, but honestly, I think it's a good thing. Because it makes us appreciate the other times.  
Those brief, transcendent moments when the lights flicker on, the black cloud parts, and you see the world for what it really is.

     - Oh…

And suddenly there's meaning. Suddenly there's purpose.

     - So, uh, do you… Oh, shit. Shit. Shit, shit, shit.

If you're lucky, you'll experience this once in your lifetime.

     - Oops! 
Goddamn, that was…

     - That was smooth.  
     - wait, what?

For me… So smooth… It happened three times.  
The **first** was the day I met her.

     - Uh, Sorry for the eggs.  
     - It’s okay. Happens to all females.  
     - so… wanna try them or?

And the **second** one… was the day I ate her.

She had been avoiding me for days, maybe weeks. I lost track of time in the chase, in the ache of wanting something I couldn’t have. Then, suddenly, she stopped running. I found her hovering near a fallen branch, her gills flaring, her body still.

    - You don’t swim with me anymore.

    - Maybe I’m tired.

    - Of me?

    - Of everything.

She flicked her tail—not for me, but to go ahead, like she was already somewhere else. And yet, for the first time, she didn’t try to disappear. She swam slowly, deliberately, as if waiting to see if I would follow.

And I did.

I trailed her through the water, watching the way she moved her taled ass. She wasn’t running. Nor she was hiding. But something in her seemed… resigned. I wanted to reach out, to press against her side, to make her *feel* something—anything—but all I could do was stay close, my shadow slipping over hers in the dim light.

    - Why are you doing this?

    - Doing what?

    - This. Following me. Chasing me. Why don’t you do what everybody else does?

She turned to face me then, and for this time, I saw a different kind of exhaustion in her eyes.

    - Because I fucking love you.

She let out a sharp exhale, something between a laugh and a sigh.

    - Me? For what?

    - I don’t know.

    - Don’t I leave enough eggs for you? Just do your thing like everybody else. It’s the way it has been forever.

    - Now you’re starting to sound like everybody else.

    - Maybe I *am* like everybody else. *Maybe you’re* the one with the problem.

Her voice cut through the water, sharp and cold.

    - Just don’t talk to me anymore. Iwish I never laid eggs while you were around. just Have fun with the eggs—mine or any other one’s eggs—but don’t creep me out following my tailed ass everywhere. 

   - is that it? You want me to get laid over anybody’s dirty eggs and get drowned by a meaningless lust and pleasure on top of that slimey goo and let myself go? 

She turned away, clearly offended. Swam forward. And this time, she wasn’t waiting for me to follow.

But I did.

I don’t know why. Maybe I had to apologize to change her mind. Maybe I wanted her to take back what she said. Maybe I wanted to understand why she looked at me like that—like I was something she didn’t recognize. But the thing is: I really did mean what I actually said. No regrets. maybe I was just ready to let go and do what others do. Just fucking colds eggs, or better to say: jerking off to eggs to make them fertile to reproduce what evolution has destined.

But I kept following.

Not beside her, not like before. This time, I stayed back, drifting just far enough to keep her butt in sight without making her turn and snap at me again. She didn’t look back. Maybe she thought I’d finally given up. Maybe she wanted to believe that.

But I hadn’t.

She moved like she always did—fluid, effortless, her silver-speckled tail cutting through the water like a ribbon unraveling into the dark. It was hypnotic. The slow flicks, the slight curves, her butthole, the way the currents shaped themselves behinf her ass. I had spent so long wanting her, chasing her, aching for the moments she let me be near, and now… now I was invisible.

And somehow, that made it easier.

I let myself enjoy it. The sight of her tail ahead of me, the shimmer of her scales catching faint light from the surface. The way the water bent around her body, parting gently before closing in again, like it belonged to her. Also she was pooping out eggs and feces off his anus from time to time. But since that moment, I didn’t keep myself from having a bit of pleasure while swimming through her excrement eggs. Her eggs smelled like her body.

I could have stayed like that forever.

But then—

Something shifted.

A pulse, deep inside me. Not a thought, not a feeling—something older, something nameless, something I couldn’t stop even if I tried.

I got wildly turned on. 

My body moved before I even knew what I was doing.

One second, I was following her ass. The next, I was trying to rip her body off part by part.

And she—

She didn’t see it coming.

I felt her before I even understood. The familiar shape, the fins, the soft press of her against the roof of my mouth. She struggled, but gave up. Every single one of  her body folding into the dark.

And then—

For the second time in my life, I felt a joyful enlightenment. While she was dead and ready to be eaten. Also the thirt time this happened was when I pooped her out and had a moment of clarity while contemplating about the philosophy of love. Flowing out smoothly from my anus.

                                    The end
```

---
### `src\stories-fa\bedoone_khodahafezi.md`
```md
---
title: "بدون خداحافظی"
description: "منتشر شده در جلد دوم کتاب «فاطمه فاطمه است» - صفحه‌ی ۱۰۲"

published: true
date: "2025-01-01"

file: "/pdf/bedoone_khodahafezi.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/bedoone_khodahafezi.jpg"
---

```

---
### `src\stories-fa\khianat_va_mokafat.md`
```md
---
title: "خیانت و مکافات"
description: "منتشر شده در ویژه‌نامه‌ی طنز مجله‌ی مستقل ادبیات ایران - صفحه‌ی ۱۱۶"

published: true
date: "2025-01-01"

file: "/pdf/bedoone_khodahafezi.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/Cry As Punishment Fa.jpg"
---

          
  
    
      
       






Most of the time, it's like… I don't know. It's like there's this thick, black cloud covering everything. Like we see the world, but we don't really see the world, you know?  
We're all just stumbling around. Directionless.No sense of meaning.No sense of purpose. I know that might sound super depressing, but honestly, I think it's a good thing. Because it makes us appreciate the other times.  
Those brief, transcendent moments when the lights flicker on, the black cloud parts, and you see the world for what it really is.

     - Oh…

And suddenly there's meaning. Suddenly there's purpose.

     - So, uh, do you… Oh, shit. Shit. Shit, shit, shit.

If you're lucky, you'll experience this once in your lifetime.

     - Oops! 
Goddamn, that was…

     - That was smooth.  
     - wait, what?

For me… So smooth… It happened three times.  
The **first** was the day I met her.

     - Uh, Sorry for the eggs.  
     - It’s okay. Happens to all females.  
     - so… wanna try them or?

And the **second** one… was the day I ate her.

She had been avoiding me for days, maybe weeks. I lost track of time in the chase, in the ache of wanting something I couldn’t have. Then, suddenly, she stopped running. I found her hovering near a fallen branch, her gills flaring, her body still.

    - You don’t swim with me anymore.

    - Maybe I’m tired.

    - Of me?

    - Of everything.

She flicked her tail—not for me, but to go ahead, like she was already somewhere else. And yet, for the first time, she didn’t try to disappear. She swam slowly, deliberately, as if waiting to see if I would follow.

And I did.

I trailed her through the water, watching the way she moved her taled ass. She wasn’t running. Nor she was hiding. But something in her seemed… resigned. I wanted to reach out, to press against her side, to make her *feel* something—anything—but all I could do was stay close, my shadow slipping over hers in the dim light.

    - Why are you doing this?

    - Doing what?

    - This. Following me. Chasing me. Why don’t you do what everybody else does?

She turned to face me then, and for this time, I saw a different kind of exhaustion in her eyes.

    - Because I fucking love you.

She let out a sharp exhale, something between a laugh and a sigh.

    - Me? For what?

    - I don’t know.

    - Don’t I leave enough eggs for you? Just do your thing like everybody else. It’s the way it has been forever.

    - Now you’re starting to sound like everybody else.

    - Maybe I *am* like everybody else. *Maybe you’re* the one with the problem.

Her voice cut through the water, sharp and cold.

    - Just don’t talk to me anymore. Iwish I never laid eggs while you were around. just Have fun with the eggs—mine or any other one’s eggs—but don’t creep me out following my tailed ass everywhere. 

   - is that it? You want me to get laid over anybody’s dirty eggs and get drowned by a meaningless lust and pleasure on top of that slimey goo and let myself go? 

She turned away, clearly offended. Swam forward. And this time, she wasn’t waiting for me to follow.

But I did.

I don’t know why. Maybe I had to apologize to change her mind. Maybe I wanted her to take back what she said. Maybe I wanted to understand why she looked at me like that—like I was something she didn’t recognize. But the thing is: I really did mean what I actually said. No regrets. maybe I was just ready to let go and do what others do. Just fucking colds eggs, or better to say: jerking off to eggs to make them fertile to reproduce what evolution has destined.

But I kept following.

Not beside her, not like before. This time, I stayed back, drifting just far enough to keep her butt in sight without making her turn and snap at me again. She didn’t look back. Maybe she thought I’d finally given up. Maybe she wanted to believe that.

But I hadn’t.

She moved like she always did—fluid, effortless, her silver-speckled tail cutting through the water like a ribbon unraveling into the dark. It was hypnotic. The slow flicks, the slight curves, her butthole, the way the currents shaped themselves behinf her ass. I had spent so long wanting her, chasing her, aching for the moments she let me be near, and now… now I was invisible.

And somehow, that made it easier.

I let myself enjoy it. The sight of her tail ahead of me, the shimmer of her scales catching faint light from the surface. The way the water bent around her body, parting gently before closing in again, like it belonged to her. Also she was pooping out eggs and feces off his anus from time to time. But since that moment, I didn’t keep myself from having a bit of pleasure while swimming through her excrement eggs. Her eggs smelled like her body.

I could have stayed like that forever.

But then—

Something shifted.

A pulse, deep inside me. Not a thought, not a feeling—something older, something nameless, something I couldn’t stop even if I tried.

I got wildly turned on. 

My body moved before I even knew what I was doing.

One second, I was following her ass. The next, I was trying to rip her body off part by part.

And she—

She didn’t see it coming.

I felt her before I even understood. The familiar shape, the fins, the soft press of her against the roof of my mouth. She struggled, but gave up. Every single one of  her body folding into the dark.

And then—

For the second time in my life, I felt a joyful enlightenment. While she was dead and ready to be eaten. Also the thirt time this happened was when I pooped her out and had a moment of clarity while contemplating about the philosophy of love. Flowing out smoothly from my anus.

                                    The end
```

---
### `src\stories-fa\tasmim_baraye_cobra_11.md`
```md
---
title: "تصمیم برای کبری ۱۱"
description: "منتشر شده در  در کتاب همسایه ۳ -  صفحه‌ی ۳۱۳"

published: true
date: "2025-01-01"

file: "/pdf/bedoone_khodahafezi.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/tasmim 11.jpg" 
---

          
  






Most of the time, it's like… I don't know. It's like there's this thick, black cloud covering everything. Like we see the world, but we don't really see the world, you know?  
We're all just stumbling around. Directionless.No sense of meaning.No sense of purpose. I know that might sound super depressing, but honestly, I think it's a good thing. Because it makes us appreciate the other times.  
Those brief, transcendent moments when the lights flicker on, the black cloud parts, and you see the world for what it really is.

     - Oh…

And suddenly there's meaning. Suddenly there's purpose.

     - So, uh, do you… Oh, shit. Shit. Shit, shit, shit.

If you're lucky, you'll experience this once in your lifetime.

     - Oops! 
Goddamn, that was…

     - That was smooth.  
     - wait, what?

For me… So smooth… It happened three times.  
The **first** was the day I met her.

     - Uh, Sorry for the eggs.  
     - It’s okay. Happens to all females.  
     - so… wanna try them or?

And the **second** one… was the day I ate her.

She had been avoiding me for days, maybe weeks. I lost track of time in the chase, in the ache of wanting something I couldn’t have. Then, suddenly, she stopped running. I found her hovering near a fallen branch, her gills flaring, her body still.

    - You don’t swim with me anymore.

    - Maybe I’m tired.

    - Of me?

    - Of everything.

She flicked her tail—not for me, but to go ahead, like she was already somewhere else. And yet, for the first time, she didn’t try to disappear. She swam slowly, deliberately, as if waiting to see if I would follow.

And I did.

I trailed her through the water, watching the way she moved her taled ass. She wasn’t running. Nor she was hiding. But something in her seemed… resigned. I wanted to reach out, to press against her side, to make her *feel* something—anything—but all I could do was stay close, my shadow slipping over hers in the dim light.

    - Why are you doing this?

    - Doing what?

    - This. Following me. Chasing me. Why don’t you do what everybody else does?

She turned to face me then, and for this time, I saw a different kind of exhaustion in her eyes.

    - Because I fucking love you.

She let out a sharp exhale, something between a laugh and a sigh.

    - Me? For what?

    - I don’t know.

    - Don’t I leave enough eggs for you? Just do your thing like everybody else. It’s the way it has been forever.

    - Now you’re starting to sound like everybody else.

    - Maybe I *am* like everybody else. *Maybe you’re* the one with the problem.

Her voice cut through the water, sharp and cold.

    - Just don’t talk to me anymore. Iwish I never laid eggs while you were around. just Have fun with the eggs—mine or any other one’s eggs—but don’t creep me out following my tailed ass everywhere. 

   - is that it? You want me to get laid over anybody’s dirty eggs and get drowned by a meaningless lust and pleasure on top of that slimey goo and let myself go? 

She turned away, clearly offended. Swam forward. And this time, she wasn’t waiting for me to follow.

But I did.

I don’t know why. Maybe I had to apologize to change her mind. Maybe I wanted her to take back what she said. Maybe I wanted to understand why she looked at me like that—like I was something she didn’t recognize. But the thing is: I really did mean what I actually said. No regrets. maybe I was just ready to let go and do what others do. Just fucking colds eggs, or better to say: jerking off to eggs to make them fertile to reproduce what evolution has destined.

But I kept following.

Not beside her, not like before. This time, I stayed back, drifting just far enough to keep her butt in sight without making her turn and snap at me again. She didn’t look back. Maybe she thought I’d finally given up. Maybe she wanted to believe that.

But I hadn’t.

She moved like she always did—fluid, effortless, her silver-speckled tail cutting through the water like a ribbon unraveling into the dark. It was hypnotic. The slow flicks, the slight curves, her butthole, the way the currents shaped themselves behinf her ass. I had spent so long wanting her, chasing her, aching for the moments she let me be near, and now… now I was invisible.

And somehow, that made it easier.

I let myself enjoy it. The sight of her tail ahead of me, the shimmer of her scales catching faint light from the surface. The way the water bent around her body, parting gently before closing in again, like it belonged to her. Also she was pooping out eggs and feces off his anus from time to time. But since that moment, I didn’t keep myself from having a bit of pleasure while swimming through her excrement eggs. Her eggs smelled like her body.

I could have stayed like that forever.

But then—

Something shifted.

A pulse, deep inside me. Not a thought, not a feeling—something older, something nameless, something I couldn’t stop even if I tried.

I got wildly turned on. 

My body moved before I even knew what I was doing.

One second, I was following her ass. The next, I was trying to rip her body off part by part.

And she—

She didn’t see it coming.

I felt her before I even understood. The familiar shape, the fins, the soft press of her against the roof of my mouth. She struggled, but gave up. Every single one of  her body folding into the dark.

And then—

For the second time in my life, I felt a joyful enlightenment. While she was dead and ready to be eaten. Also the thirt time this happened was when I pooped her out and had a moment of clarity while contemplating about the philosophy of love. Flowing out smoothly from my anus.

                                    The end
```

---
### `src\stories-fa\vincenzo.md`
```md
---
title: "vincenzo"
description: "منتشر نشده - پیش‌نویس"

published: false
date: "2025-01-01"

file: "/pdf/vincenzo.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/vincenzo.png" 
---

          
  
```

---
### `src\stories-fa\اثاثیاست یک دست میز و صندلی نگران.md`
```md
---
title: "اثاثیاست یک دست میز و صندلی نگران"
description: "منتشر نشده - پیش‌نویس"

published: false
date: "2025-01-01"

file: "/pdf/اثاثیاست یک دست میز و صندلی نگران.pdf"

image: "/images/اثاثیاست یک دست میز و صندلی نگران.png" 
---

          
  
```

---
### `src\stories-fa\محل تبلیغات شما.md`
```md
---
title: "محل تبلیغات شما"
description: "منتشر نشده - پیش‌نویس"

published: false
date: "2025-01-01"

file: "/pdf/محل تبلیغات شما.pdf"
link: "https://example.com/fateme_fateme_ast"
image: "/images/محل تبلیغات شما.png" 
---

          
  
```

---
### `src\styles\global.css`
```css
/* -------------------------------------------------
   Tailwind Base Imports
------------------------------------------------- */
@import "tailwindcss";
@import "tw-animate-css";

/* -------------------------------------------------
   Light/Dark Variant Definition
------------------------------------------------- */
@custom-variant dark (&:is(.dark *));

/* -------------------------------------------------
   Theme Tokens (Tailwind v4 @theme)
------------------------------------------------- */
@theme {
  /* Background / Foreground */
  --color-background: rgb(var(--background));
  --color-foreground: rgb(var(--foreground));

  /* Main UI Colors */
  --color-primary: rgb(var(--primary));
  --color-primary-foreground: rgb(var(--primary-foreground));
  --color-secondary: rgb(var(--secondary));
  --color-secondary-foreground: rgb(var(--secondary-foreground));

  /* Borders / Inputs */
  --color-border: rgb(var(--border));
  --color-input: rgb(var(--input));

  /* Misc */
  --radius: 0.625rem;
}

/* -------------------------------------------------
   Light Theme
------------------------------------------------- */
:root {
  --background: 255 255 255;
  --foreground: 17 17 17;

  --primary: 90 106 255;
  --primary-foreground: 255 255 255;

  --secondary: 230 230 230;
  --secondary-foreground: 17 17 17;

  --border: 220 220 220;
  --input: 230 230 230;
}

/* -------------------------------------------------
   Dark Theme
------------------------------------------------- */
.dark {
  --background: 18 18 18;
  --foreground: 235 235 235;

  --primary: 150 170 255;
  --primary-foreground: 18 18 18;

  --secondary: 60 60 60;
  --secondary-foreground: 235 235 235;

  --border: 80 80 80;
  --input: 100 100 100;
}

/* -------------------------------------------------
   Base Layer
------------------------------------------------- */
@layer base {
  *, *::before, *::after {
    border-color: var(--color-border);
  }

  body {
    background-color: var(--color-background);
    color: var(--color-foreground);
  }
}

/* -------------------------------------------------
   Fix for Astro Code Blocks
------------------------------------------------- */
.astro-code {
  color: inherit !important;
}


```

---
### `src\utils\formatDate.ts`
```ts
export function formatDate(
  date: Date,
  lang: "en" | "fa" = "en",
  mode: "full" | "short" = "full"
) {
  if (!(date instanceof Date) || isNaN(date.getTime())) {
    return "";
  }

  if (lang === "fa") {
    // Persian (Jalali)
    return date.toLocaleDateString("fa-IR", {
      year: "numeric",
      month: mode === "full" ? "long" : "numeric",
      day: "numeric",
    });
  }

  // English (Gregorian)
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: mode === "full" ? "long" : "short",
    day: "numeric",
  });
}

```

---
### `src\wiki\Effects\effects.fa.md`
```md
---
title: 'Effects'
slug: "effects"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Effects

_Page coming soon._

```

---
### `src\wiki\Effects\effects.md`
```md
---
title: 'Effects'
slug: "effects"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Effects

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Psychoactives.fa.md`
```md
---
title: 'Psychoactives'
slug: "psychoactives"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Substances

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Psychoactives.md`
```md
---
title: 'Psychoactives'
slug: "psychoactives"
lang: "en"
category: ''
weight: 1000
template: "wiki"
summary: ''
---

# Substances

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-b.fa.md`
```md
---
title: '2C-B'
slug: "2c-b"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-b.md`
```md
---
title: '2C-B'
slug: "2c-b"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-c.fa.md`
```md
---
title: '2C-C'
slug: "2c-c"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-C

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-c.md`
```md
---
title: '2C-C'
slug: "2c-c"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-C

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-d.fa.md`
```md
---
title: '2C-D'
slug: "2c-d"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-D

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-d.md`
```md
---
title: '2C-D'
slug: "2c-d"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-D

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-e.fa.md`
```md
---
title: '2C-E'
slug: "2c-e"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-E

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-e.md`
```md
---
title: '2C-E'
slug: "2c-e"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-E

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-h.fa.md`
```md
---
title: '2C-H'
slug: "2c-h"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-H

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-h.md`
```md
---
title: '2C-H'
slug: "2c-h"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-H

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-i.fa.md`
```md
---
title: '2C-I'
slug: "2c-i"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-I

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-i.md`
```md
---
title: '2C-I'
slug: "2c-i"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-I

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-p.fa.md`
```md
---
title: '2C-P'
slug: "2c-p"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-P

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-p.md`
```md
---
title: '2C-P'
slug: "2c-p"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-P

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-2.fa.md`
```md
---
title: '2C-T-2'
slug: "2c-t-2"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-2

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-2.md`
```md
---
title: '2C-T-2'
slug: "2c-t-2"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-2

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-21.fa.md`
```md
---
title: '2C-T-21'
slug: "2c-t-21"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-21

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-21.md`
```md
---
title: '2C-T-21'
slug: "2c-t-21"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-21

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-7.fa.md`
```md
---
title: '2C-T-7'
slug: "2c-t-7"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-7

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-7.md`
```md
---
title: '2C-T-7'
slug: "2c-t-7"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-7

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-x.fa.md`
```md
---
title: '2C-T-x'
slug: "2c-t-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-x

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t-x.md`
```md
---
title: '2C-T-x'
slug: "2c-t-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T-x

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t.fa.md`
```md
---
title: '2C-T'
slug: "2c-t"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-t.md`
```md
---
title: '2C-T'
slug: "2c-t"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-T

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-x.fa.md`
```md
---
title: '2C-x'
slug: "2c-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-x

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-x.md`
```md
---
title: '2C-x'
slug: "2c-x"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-x

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-xderivatives.fa.md`
```md
---
title: '2C-xـderivatives'
slug: "2c-xderivatives"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-xـderivatives

_Page coming soon._

```

---
### `src\wiki\Psychoactives\2C-x\2c-xderivatives.md`
```md
---
title: '2C-xـderivatives'
slug: "2c-xderivatives"
lang: "en"
category: '2C-x'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-xـderivatives

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\5f-akb48.fa.md`
```md
---
title: '5F-AKB48'
slug: "5f-akb48"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-AKB48

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\5f-akb48.md`
```md
---
title: '5F-AKB48'
slug: "5f-akb48"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-AKB48

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\5f-pb-22.fa.md`
```md
---
title: '5F-PB-22'
slug: "5f-pb-22"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-PB-22

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\5f-pb-22.md`
```md
---
title: '5F-PB-22'
slug: "5f-pb-22"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# 5F-PB-22

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\ab-fubinaca.fa.md`
```md
---
title: 'AB-FUBINACA'
slug: "ab-fubinaca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# AB-FUBINACA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\ab-fubinaca.md`
```md
---
title: 'AB-FUBINACA'
slug: "ab-fubinaca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# AB-FUBINACA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\apica.fa.md`
```md
---
title: 'APICA'
slug: "apica"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# APICA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\apica.md`
```md
---
title: 'APICA'
slug: "apica"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# APICA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cannabinoids.fa.md`
```md
---
title: 'Cannabinoids'
slug: "cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cannabinoids.md`
```md
---
title: 'Cannabinoids'
slug: "cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbd.fa.md`
```md
---
title: 'CBD'
slug: "cbd"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbd.md`
```md
---
title: 'CBD'
slug: "cbd"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbda.fa.md`
```md
---
title: 'CBDA'
slug: "cbda"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbda.md`
```md
---
title: 'CBDA'
slug: "cbda"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbdh.fa.md`
```md
---
title: 'CBDH'
slug: "cbdh"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbdh.md`
```md
---
title: 'CBDH'
slug: "cbdh"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbdp.fa.md`
```md
---
title: 'CBDP'
slug: "cbdp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\cbdp.md`
```md
---
title: 'CBDP'
slug: "cbdp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# CBDP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\delta-10-thc.fa.md`
```md
---
title: 'delta-10-THC'
slug: "delta-10-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-10-THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\delta-10-thc.md`
```md
---
title: 'delta-10-THC'
slug: "delta-10-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-10-THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\delta-11-thc.fa.md`
```md
---
title: 'delta-11-THC'
slug: "delta-11-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-11-THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\delta-11-thc.md`
```md
---
title: 'delta-11-THC'
slug: "delta-11-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-11-THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\delta-8-thc.fa.md`
```md
---
title: 'delta-8-THC'
slug: "delta-8-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-8-THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\delta-8-thc.md`
```md
---
title: 'delta-8-THC'
slug: "delta-8-thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# delta-8-THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\hhc.fa.md`
```md
---
title: 'HHC'
slug: "hhc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# HHC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\hhc.md`
```md
---
title: 'HHC'
slug: "hhc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# HHC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\jwh-018.fa.md`
```md
---
title: 'JWH-018'
slug: "jwh-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-018

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\jwh-018.md`
```md
---
title: 'JWH-018'
slug: "jwh-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-018

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\jwh-073.fa.md`
```md
---
title: 'JWH-073'
slug: "jwh-073"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-073

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\jwh-073.md`
```md
---
title: 'JWH-073'
slug: "jwh-073"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# JWH-073

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\phytocannabinoids.fa.md`
```md
---
title: 'Phytocannabinoids'
slug: "phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Phytocannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\phytocannabinoids.md`
```md
---
title: 'Phytocannabinoids'
slug: "phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Phytocannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\semi-synthetic-phytocannabinoids.fa.md`
```md
---
title: 'Semi-synthetic phytocannabinoids'
slug: "semi-synthetic-phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Semi-synthetic phytocannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\semi-synthetic-phytocannabinoids.md`
```md
---
title: 'Semi-synthetic phytocannabinoids'
slug: "semi-synthetic-phytocannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Semi-synthetic phytocannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\sts-135.fa.md`
```md
---
title: 'STS-135'
slug: "sts-135"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# STS-135

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\sts-135.md`
```md
---
title: 'STS-135'
slug: "sts-135"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# STS-135

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\synthetic-cannabinoids.fa.md`
```md
---
title: 'Synthetic cannabinoids'
slug: "synthetic-cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Synthetic cannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\synthetic-cannabinoids.md`
```md
---
title: 'Synthetic cannabinoids'
slug: "synthetic-cannabinoids"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# Synthetic cannabinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thc-o-acetate.fa.md`
```md
---
title: 'THC-O-acetate'
slug: "thc-o-acetate"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC-O-acetate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thc-o-acetate.md`
```md
---
title: 'THC-O-acetate'
slug: "thc-o-acetate"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC-O-acetate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thc.fa.md`
```md
---
title: 'THC'
slug: "thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thc.md`
```md
---
title: 'THC'
slug: "thc"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thca.fa.md`
```md
---
title: 'THCA'
slug: "thca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thca.md`
```md
---
title: 'THCA'
slug: "thca"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thcb.fa.md`
```md
---
title: 'THCB'
slug: "thcb"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thcb.md`
```md
---
title: 'THCB'
slug: "thcb"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thch.fa.md`
```md
---
title: 'THCH'
slug: "thch"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thch.md`
```md
---
title: 'THCH'
slug: "thch"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thcp.fa.md`
```md
---
title: 'THCP'
slug: "thcp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thcp.md`
```md
---
title: 'THCP'
slug: "thcp"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thj-018.fa.md`
```md
---
title: 'THJ-018'
slug: "thj-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-018

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thj-018.md`
```md
---
title: 'THJ-018'
slug: "thj-018"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-018

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thj-2201.fa.md`
```md
---
title: 'THJ-2201'
slug: "thj-2201"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-2201

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Cannabinoids\thj-2201.md`
```md
---
title: 'THJ-2201'
slug: "thj-2201"
lang: "en"
category: 'Cannabinoids'
weight: 1000
template: "wiki"
summary: ''
---

# THJ-2201

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Classical_psychedelics\classical-psychedelics.fa.md`
```md
---
title: 'Classical_psychedelics'
slug: "classical-psychedelics"
lang: "en"
category: 'Classical_psychedelics'
weight: 1000
template: "wiki"
summary: ''
---

# Classical_psychedelics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Classical_psychedelics\classical-psychedelics.md`
```md
---
title: 'Classical_psychedelics'
slug: "classical-psychedelics"
lang: "en"
category: 'Classical_psychedelics'
weight: 1000
template: "wiki"
summary: ''
---

# Classical_psychedelics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\antihistamines.fa.md`
```md
---
title: 'Antihistamines'
slug: "antihistamines"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Antihistamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\antihistamines.md`
```md
---
title: 'Antihistamines'
slug: "antihistamines"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Antihistamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\atropine.fa.md`
```md
---
title: 'Atropine'
slug: "atropine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Atropine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\atropine.md`
```md
---
title: 'Atropine'
slug: "atropine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Atropine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\benzydamine.fa.md`
```md
---
title: 'Benzydamine'
slug: "benzydamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzydamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\benzydamine.md`
```md
---
title: 'Benzydamine'
slug: "benzydamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzydamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\deliriants.fa.md`
```md
---
title: 'Deliriants'
slug: "deliriants"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Deliriants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\deliriants.md`
```md
---
title: 'Deliriants'
slug: "deliriants"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Deliriants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\elemicin.fa.md`
```md
---
title: 'Elemicin'
slug: "elemicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Elemicin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\elemicin.md`
```md
---
title: 'Elemicin'
slug: "elemicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Elemicin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\hyoscyamine.fa.md`
```md
---
title: 'Hyoscyamine'
slug: "hyoscyamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Hyoscyamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\hyoscyamine.md`
```md
---
title: 'Hyoscyamine'
slug: "hyoscyamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Hyoscyamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\myristicin.fa.md`
```md
---
title: 'Myristicin'
slug: "myristicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Myristicin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\myristicin.md`
```md
---
title: 'Myristicin'
slug: "myristicin"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Myristicin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\promethazine.fa.md`
```md
---
title: 'Promethazine'
slug: "promethazine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Promethazine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\promethazine.md`
```md
---
title: 'Promethazine'
slug: "promethazine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Promethazine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\scopolamine.fa.md`
```md
---
title: 'Scopolamine'
slug: "scopolamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Scopolamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\scopolamine.md`
```md
---
title: 'Scopolamine'
slug: "scopolamine"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Scopolamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\tropane-alkaloids.fa.md`
```md
---
title: 'Tropane alkaloids'
slug: "tropane-alkaloids"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropane alkaloids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Deliriants\tropane-alkaloids.md`
```md
---
title: 'Tropane alkaloids'
slug: "tropane-alkaloids"
lang: "en"
category: 'Deliriants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropane alkaloids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\14-butanediol.fa.md`
```md
---
title: '1,4-Butanediol'
slug: "14-butanediol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 1,4-Butanediol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\14-butanediol.md`
```md
---
title: '1,4-Butanediol'
slug: "14-butanediol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 1,4-Butanediol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\2-methyl-2-butanol.fa.md`
```md
---
title: '2-Methyl-2-butanol'
slug: "2-methyl-2-butanol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Methyl-2-butanol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\2-methyl-2-butanol.md`
```md
---
title: '2-Methyl-2-butanol'
slug: "2-methyl-2-butanol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Methyl-2-butanol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\7-hydroxymitragynine.fa.md`
```md
---
title: '7-Hydroxymitragynine'
slug: "7-hydroxymitragynine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 7-Hydroxymitragynine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\7-hydroxymitragynine.md`
```md
---
title: '7-Hydroxymitragynine'
slug: "7-hydroxymitragynine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# 7-Hydroxymitragynine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\acetylfentanyl.fa.md`
```md
---
title: 'Acetylfentanyl'
slug: "acetylfentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylfentanyl

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\acetylfentanyl.md`
```md
---
title: 'Acetylfentanyl'
slug: "acetylfentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylfentanyl

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\alcohol.fa.md`
```md
---
title: 'Alcohol'
slug: "alcohol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\alcohol.md`
```md
---
title: 'Alcohol'
slug: "alcohol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\alcohols.fa.md`
```md
---
title: 'Alcohols'
slug: "alcohols"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohols

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\alcohols.md`
```md
---
title: 'Alcohols'
slug: "alcohols"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alcohols

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\alprazolam.fa.md`
```md
---
title: 'Alprazolam'
slug: "alprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alprazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\alprazolam.md`
```md
---
title: 'Alprazolam'
slug: "alprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Alprazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\baclofen.fa.md`
```md
---
title: 'Baclofen'
slug: "baclofen"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Baclofen

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\baclofen.md`
```md
---
title: 'Baclofen'
slug: "baclofen"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Baclofen

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\barbiturates.fa.md`
```md
---
title: 'Barbiturates'
slug: "barbiturates"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Barbiturates

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\barbiturates.md`
```md
---
title: 'Barbiturates'
slug: "barbiturates"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Barbiturates

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\benzodiazepines.fa.md`
```md
---
title: 'Benzodiazepines'
slug: "benzodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzodiazepines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\benzodiazepines.md`
```md
---
title: 'Benzodiazepines'
slug: "benzodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Benzodiazepines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\bromazepam.fa.md`
```md
---
title: 'Bromazepam'
slug: "bromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Bromazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\bromazepam.md`
```md
---
title: 'Bromazepam'
slug: "bromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Bromazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\buprenorphine.fa.md`
```md
---
title: 'Buprenorphine'
slug: "buprenorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Buprenorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\buprenorphine.md`
```md
---
title: 'Buprenorphine'
slug: "buprenorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Buprenorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\carisoprodol.fa.md`
```md
---
title: 'Carisoprodol'
slug: "carisoprodol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Carisoprodol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\carisoprodol.md`
```md
---
title: 'Carisoprodol'
slug: "carisoprodol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Carisoprodol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\clonazepam.fa.md`
```md
---
title: 'Clonazepam'
slug: "clonazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\clonazepam.md`
```md
---
title: 'Clonazepam'
slug: "clonazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\clonazolam.fa.md`
```md
---
title: 'Clonazolam'
slug: "clonazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\clonazolam.md`
```md
---
title: 'Clonazolam'
slug: "clonazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\clonidine.fa.md`
```md
---
title: 'Clonidine'
slug: "clonidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\clonidine.md`
```md
---
title: 'Clonidine'
slug: "clonidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Clonidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\codeine.fa.md`
```md
---
title: 'Codeine'
slug: "codeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Codeine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\codeine.md`
```md
---
title: 'Codeine'
slug: "codeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Codeine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\depressants.fa.md`
```md
---
title: 'Depressants'
slug: "depressants"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Depressants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\depressants.md`
```md
---
title: 'Depressants'
slug: "depressants"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Depressants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\deschloroetizolam.fa.md`
```md
---
title: 'Deschloroetizolam'
slug: "deschloroetizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Deschloroetizolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\deschloroetizolam.md`
```md
---
title: 'Deschloroetizolam'
slug: "deschloroetizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Deschloroetizolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\desomorphine.fa.md`
```md
---
title: 'Desomorphine'
slug: "desomorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Desomorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\desomorphine.md`
```md
---
title: 'Desomorphine'
slug: "desomorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Desomorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\dextropropoxyphene.fa.md`
```md
---
title: 'Dextropropoxyphene'
slug: "dextropropoxyphene"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextropropoxyphene

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\dextropropoxyphene.md`
```md
---
title: 'Dextropropoxyphene'
slug: "dextropropoxyphene"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextropropoxyphene

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diacetylmorphine.fa.md`
```md
---
title: 'Diacetylmorphine'
slug: "diacetylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diacetylmorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diacetylmorphine.md`
```md
---
title: 'Diacetylmorphine'
slug: "diacetylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diacetylmorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diazepam.fa.md`
```md
---
title: 'Diazepam'
slug: "diazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diazepam.md`
```md
---
title: 'Diazepam'
slug: "diazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diclazepam.fa.md`
```md
---
title: 'Diclazepam'
slug: "diclazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diclazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diclazepam.md`
```md
---
title: 'Diclazepam'
slug: "diclazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diclazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\dihydrocodeine.fa.md`
```md
---
title: 'Dihydrocodeine'
slug: "dihydrocodeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dihydrocodeine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\dihydrocodeine.md`
```md
---
title: 'Dihydrocodeine'
slug: "dihydrocodeine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Dihydrocodeine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diphenhydramine.fa.md`
```md
---
title: 'Diphenhydramine'
slug: "diphenhydramine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenhydramine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\diphenhydramine.md`
```md
---
title: 'Diphenhydramine'
slug: "diphenhydramine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenhydramine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\eszopiclone.fa.md`
```md
---
title: 'Eszopiclone'
slug: "eszopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Eszopiclone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\eszopiclone.md`
```md
---
title: 'Eszopiclone'
slug: "eszopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Eszopiclone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\ethylmorphine.fa.md`
```md
---
title: 'Ethylmorphine'
slug: "ethylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylmorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\ethylmorphine.md`
```md
---
title: 'Ethylmorphine'
slug: "ethylmorphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylmorphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\etizolam.fa.md`
```md
---
title: 'Etizolam'
slug: "etizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Etizolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\etizolam.md`
```md
---
title: 'Etizolam'
slug: "etizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Etizolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\f-phenibut.fa.md`
```md
---
title: 'F-Phenibut'
slug: "f-phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# F-Phenibut

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\f-phenibut.md`
```md
---
title: 'F-Phenibut'
slug: "f-phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# F-Phenibut

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\fentanyl.fa.md`
```md
---
title: 'Fentanyl'
slug: "fentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Fentanyl

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\fentanyl.md`
```md
---
title: 'Fentanyl'
slug: "fentanyl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Fentanyl

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flualprazolam.fa.md`
```md
---
title: 'Flualprazolam'
slug: "flualprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flualprazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flualprazolam.md`
```md
---
title: 'Flualprazolam'
slug: "flualprazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flualprazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flubromazepam.fa.md`
```md
---
title: 'Flubromazepam'
slug: "flubromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flubromazepam.md`
```md
---
title: 'Flubromazepam'
slug: "flubromazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flubromazolam.fa.md`
```md
---
title: 'Flubromazolam'
slug: "flubromazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flubromazolam.md`
```md
---
title: 'Flubromazolam'
slug: "flubromazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flubromazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flunitrazepam.fa.md`
```md
---
title: 'Flunitrazepam'
slug: "flunitrazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flunitrazepam.md`
```md
---
title: 'Flunitrazepam'
slug: "flunitrazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flunitrazolam.fa.md`
```md
---
title: 'Flunitrazolam'
slug: "flunitrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\flunitrazolam.md`
```md
---
title: 'Flunitrazolam'
slug: "flunitrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Flunitrazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gabaa-1-agonists.fa.md`
```md
---
title: 'GABAA-α1 agonists'
slug: "gabaa-1-agonists"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GABAA-α1 agonists

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gabaa-1-agonists.md`
```md
---
title: 'GABAA-α1 agonists'
slug: "gabaa-1-agonists"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GABAA-α1 agonists

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gabapentin.fa.md`
```md
---
title: 'Gabapentin'
slug: "gabapentin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gabapentin.md`
```md
---
title: 'Gabapentin'
slug: "gabapentin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gabapentinoids.fa.md`
```md
---
title: 'Gabapentinoids'
slug: "gabapentinoids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gabapentinoids.md`
```md
---
title: 'Gabapentinoids'
slug: "gabapentinoids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gabapentinoids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gaboxadol.fa.md`
```md
---
title: 'Gaboxadol'
slug: "gaboxadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gaboxadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gaboxadol.md`
```md
---
title: 'Gaboxadol'
slug: "gaboxadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Gaboxadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gbl.fa.md`
```md
---
title: 'GBL'
slug: "gbl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GBL

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\gbl.md`
```md
---
title: 'GBL'
slug: "gbl"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GBL

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\ghb.fa.md`
```md
---
title: 'GHB'
slug: "ghb"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GHB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\ghb.md`
```md
---
title: 'GHB'
slug: "ghb"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# GHB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\hydrocodone.fa.md`
```md
---
title: 'Hydrocodone'
slug: "hydrocodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydrocodone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\hydrocodone.md`
```md
---
title: 'Hydrocodone'
slug: "hydrocodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydrocodone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\hydromorphone.fa.md`
```md
---
title: 'Hydromorphone'
slug: "hydromorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydromorphone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\hydromorphone.md`
```md
---
title: 'Hydromorphone'
slug: "hydromorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Hydromorphone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\ibotenic-acid.fa.md`
```md
---
title: 'Ibotenic acid'
slug: "ibotenic-acid"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ibotenic acid

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\ibotenic-acid.md`
```md
---
title: 'Ibotenic acid'
slug: "ibotenic-acid"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Ibotenic acid

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\kava.fa.md`
```md
---
title: 'Kava'
slug: "kava"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kava

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\kava.md`
```md
---
title: 'Kava'
slug: "kava"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kava

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\kratom.fa.md`
```md
---
title: 'Kratom'
slug: "kratom"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kratom

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\kratom.md`
```md
---
title: 'Kratom'
slug: "kratom"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Kratom

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\lorazepam.fa.md`
```md
---
title: 'Lorazepam'
slug: "lorazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lorazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\lorazepam.md`
```md
---
title: 'Lorazepam'
slug: "lorazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lorazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\lormetazepam.fa.md`
```md
---
title: 'Lormetazepam'
slug: "lormetazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lormetazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\lormetazepam.md`
```md
---
title: 'Lormetazepam'
slug: "lormetazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Lormetazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\methadone.fa.md`
```md
---
title: 'Methadone'
slug: "methadone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methadone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\methadone.md`
```md
---
title: 'Methadone'
slug: "methadone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methadone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\methaqualone.fa.md`
```md
---
title: 'Methaqualone'
slug: "methaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methaqualone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\methaqualone.md`
```md
---
title: 'Methaqualone'
slug: "methaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Methaqualone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\metizolam.fa.md`
```md
---
title: 'Metizolam'
slug: "metizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Metizolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\metizolam.md`
```md
---
title: 'Metizolam'
slug: "metizolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Metizolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\midazolam.fa.md`
```md
---
title: 'Midazolam'
slug: "midazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Midazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\midazolam.md`
```md
---
title: 'Midazolam'
slug: "midazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Midazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\mirtazapine.fa.md`
```md
---
title: 'Mirtazapine'
slug: "mirtazapine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Mirtazapine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\mirtazapine.md`
```md
---
title: 'Mirtazapine'
slug: "mirtazapine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Mirtazapine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\morphine.fa.md`
```md
---
title: 'Morphine'
slug: "morphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Morphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\morphine.md`
```md
---
title: 'Morphine'
slug: "morphine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Morphine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\muscimol.fa.md`
```md
---
title: 'Muscimol'
slug: "muscimol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Muscimol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\muscimol.md`
```md
---
title: 'Muscimol'
slug: "muscimol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Muscimol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\nifoxipam.fa.md`
```md
---
title: 'Nifoxipam'
slug: "nifoxipam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nifoxipam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\nifoxipam.md`
```md
---
title: 'Nifoxipam'
slug: "nifoxipam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nifoxipam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\nitromethaqualone.fa.md`
```md
---
title: 'Nitromethaqualone'
slug: "nitromethaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nitromethaqualone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\nitromethaqualone.md`
```md
---
title: 'Nitromethaqualone'
slug: "nitromethaqualone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Nitromethaqualone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\o-desmethyltramadol.fa.md`
```md
---
title: 'O-Desmethyltramadol'
slug: "o-desmethyltramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# O-Desmethyltramadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\o-desmethyltramadol.md`
```md
---
title: 'O-Desmethyltramadol'
slug: "o-desmethyltramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# O-Desmethyltramadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\opioids.fa.md`
```md
---
title: 'Opioids'
slug: "opioids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Opioids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\opioids.md`
```md
---
title: 'Opioids'
slug: "opioids"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Opioids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\other-gabaergics.fa.md`
```md
---
title: 'Other GABAergics'
slug: "other-gabaergics"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Other GABAergics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\other-gabaergics.md`
```md
---
title: 'Other GABAergics'
slug: "other-gabaergics"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Other GABAergics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\oxycodone.fa.md`
```md
---
title: 'Oxycodone'
slug: "oxycodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxycodone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\oxycodone.md`
```md
---
title: 'Oxycodone'
slug: "oxycodone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxycodone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\oxymorphone.fa.md`
```md
---
title: 'Oxymorphone'
slug: "oxymorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxymorphone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\oxymorphone.md`
```md
---
title: 'Oxymorphone'
slug: "oxymorphone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Oxymorphone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pentobarbital.fa.md`
```md
---
title: 'Pentobarbital'
slug: "pentobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentobarbital

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pentobarbital.md`
```md
---
title: 'Pentobarbital'
slug: "pentobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentobarbital

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pethidine.fa.md`
```md
---
title: 'Pethidine'
slug: "pethidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pethidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pethidine.md`
```md
---
title: 'Pethidine'
slug: "pethidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pethidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\phenibut.fa.md`
```md
---
title: 'Phenibut'
slug: "phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenibut

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\phenibut.md`
```md
---
title: 'Phenibut'
slug: "phenibut"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenibut

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\phenobarbital.fa.md`
```md
---
title: 'Phenobarbital'
slug: "phenobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenobarbital

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\phenobarbital.md`
```md
---
title: 'Phenobarbital'
slug: "phenobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenobarbital

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pregabalin.fa.md`
```md
---
title: 'Pregabalin'
slug: "pregabalin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pregabalin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pregabalin.md`
```md
---
title: 'Pregabalin'
slug: "pregabalin"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pregabalin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pyrazolam.fa.md`
```md
---
title: 'Pyrazolam'
slug: "pyrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\pyrazolam.md`
```md
---
title: 'Pyrazolam'
slug: "pyrazolam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrazolam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\secobarbital.fa.md`
```md
---
title: 'Secobarbital'
slug: "secobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Secobarbital

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\secobarbital.md`
```md
---
title: 'Secobarbital'
slug: "secobarbital"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Secobarbital

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\sufentanil.fa.md`
```md
---
title: 'Sufentanil'
slug: "sufentanil"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Sufentanil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\sufentanil.md`
```md
---
title: 'Sufentanil'
slug: "sufentanil"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Sufentanil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\tapentadol.fa.md`
```md
---
title: 'Tapentadol'
slug: "tapentadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tapentadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\tapentadol.md`
```md
---
title: 'Tapentadol'
slug: "tapentadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tapentadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\temazepam.fa.md`
```md
---
title: 'Temazepam'
slug: "temazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Temazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\temazepam.md`
```md
---
title: 'Temazepam'
slug: "temazepam"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Temazepam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\thienodiazepines.fa.md`
```md
---
title: 'Thienodiazepines'
slug: "thienodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Thienodiazepines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\thienodiazepines.md`
```md
---
title: 'Thienodiazepines'
slug: "thienodiazepines"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Thienodiazepines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\tizanidine.fa.md`
```md
---
title: 'Tizanidine'
slug: "tizanidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tizanidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\tizanidine.md`
```md
---
title: 'Tizanidine'
slug: "tizanidine"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tizanidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\tramadol.fa.md`
```md
---
title: 'Tramadol'
slug: "tramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tramadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\tramadol.md`
```md
---
title: 'Tramadol'
slug: "tramadol"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Tramadol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\u-47700.fa.md`
```md
---
title: 'U-47700'
slug: "u-47700"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# U-47700

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\u-47700.md`
```md
---
title: 'U-47700'
slug: "u-47700"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# U-47700

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\zolpidem.fa.md`
```md
---
title: 'Zolpidem'
slug: "zolpidem"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zolpidem

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\zolpidem.md`
```md
---
title: 'Zolpidem'
slug: "zolpidem"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zolpidem

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\zopiclone.fa.md`
```md
---
title: 'Zopiclone'
slug: "zopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zopiclone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Depressants\zopiclone.md`
```md
---
title: 'Zopiclone'
slug: "zopiclone"
lang: "en"
category: 'Depressants'
weight: 1000
template: "wiki"
summary: ''
---

# Zopiclone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\2-fluorodeschloroketamine.fa.md`
```md
---
title: '2-Fluorodeschloroketamine'
slug: "2-fluorodeschloroketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Fluorodeschloroketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\2-fluorodeschloroketamine.md`
```md
---
title: '2-Fluorodeschloroketamine'
slug: "2-fluorodeschloroketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2-Fluorodeschloroketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\2-oxo-pce.fa.md`
```md
---
title: '2''-Oxo-PCE'
slug: "2-oxo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCE

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\2-oxo-pce.md`
```md
---
title: '2''-Oxo-PCE'
slug: "2-oxo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCE

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\2-oxo-pcm.fa.md`
```md
---
title: '2''-Oxo-PCM'
slug: "2-oxo-pcm"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\2-oxo-pcm.md`
```md
---
title: '2''-Oxo-PCM'
slug: "2-oxo-pcm"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 2'-Oxo-PCM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-cl-pcp.fa.md`
```md
---
title: '3-Cl-PCP'
slug: "3-cl-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-Cl-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-cl-pcp.md`
```md
---
title: '3-Cl-PCP'
slug: "3-cl-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-Cl-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-ho-pce.fa.md`
```md
---
title: '3-HO-PCE'
slug: "3-ho-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCE

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-ho-pce.md`
```md
---
title: '3-HO-PCE'
slug: "3-ho-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCE

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-ho-pcp.fa.md`
```md
---
title: '3-HO-PCP'
slug: "3-ho-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-ho-pcp.md`
```md
---
title: '3-HO-PCP'
slug: "3-ho-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-HO-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-meo-pce.fa.md`
```md
---
title: '3-MeO-PCE'
slug: "3-meo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCE

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-meo-pce.md`
```md
---
title: '3-MeO-PCE'
slug: "3-meo-pce"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCE

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-meo-pcmo.fa.md`
```md
---
title: '3-MeO-PCMo'
slug: "3-meo-pcmo"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCMo

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-meo-pcmo.md`
```md
---
title: '3-MeO-PCMo'
slug: "3-meo-pcmo"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCMo

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-meo-pcp.fa.md`
```md
---
title: '3-MeO-PCP'
slug: "3-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\3-meo-pcp.md`
```md
---
title: '3-MeO-PCP'
slug: "3-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MeO-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\4-meo-pcp.fa.md`
```md
---
title: '4-MeO-PCP'
slug: "4-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 4-MeO-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\4-meo-pcp.md`
```md
---
title: '4-MeO-PCP'
slug: "4-meo-pcp"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# 4-MeO-PCP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\adamantanes.fa.md`
```md
---
title: 'Adamantanes'
slug: "adamantanes"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Adamantanes

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\adamantanes.md`
```md
---
title: 'Adamantanes'
slug: "adamantanes"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Adamantanes

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\arylcyclohexylamines.fa.md`
```md
---
title: 'Arylcyclohexylamines'
slug: "arylcyclohexylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Arylcyclohexylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\arylcyclohexylamines.md`
```md
---
title: 'Arylcyclohexylamines'
slug: "arylcyclohexylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Arylcyclohexylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\dextromethorphan.fa.md`
```md
---
title: 'Dextromethorphan'
slug: "dextromethorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextromethorphan

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\dextromethorphan.md`
```md
---
title: 'Dextromethorphan'
slug: "dextromethorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextromethorphan

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\dextrorphan.fa.md`
```md
---
title: 'Dextrorphan'
slug: "dextrorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextrorphan

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\dextrorphan.md`
```md
---
title: 'Dextrorphan'
slug: "dextrorphan"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dextrorphan

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\diarylethylamines.fa.md`
```md
---
title: 'Diarylethylamines'
slug: "diarylethylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diarylethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\diarylethylamines.md`
```md
---
title: 'Diarylethylamines'
slug: "diarylethylamines"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diarylethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\diphenidine.fa.md`
```md
---
title: 'Diphenidine'
slug: "diphenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\diphenidine.md`
```md
---
title: 'Diphenidine'
slug: "diphenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Diphenidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\dissociatives.fa.md`
```md
---
title: 'Dissociatives'
slug: "dissociatives"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dissociatives

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\dissociatives.md`
```md
---
title: 'Dissociatives'
slug: "dissociatives"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Dissociatives

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\ephenidine.fa.md`
```md
---
title: 'Ephenidine'
slug: "ephenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ephenidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\ephenidine.md`
```md
---
title: 'Ephenidine'
slug: "ephenidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ephenidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\eticyclidine.fa.md`
```md
---
title: 'Eticyclidine'
slug: "eticyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Eticyclidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\eticyclidine.md`
```md
---
title: 'Eticyclidine'
slug: "eticyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Eticyclidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\hydroxetamine.fa.md`
```md
---
title: 'Hydroxetamine'
slug: "hydroxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Hydroxetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\hydroxetamine.md`
```md
---
title: 'Hydroxetamine'
slug: "hydroxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Hydroxetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\ketamine.fa.md`
```md
---
title: 'Ketamine'
slug: "ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\ketamine.md`
```md
---
title: 'Ketamine'
slug: "ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Ketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\methoxetamine.fa.md`
```md
---
title: 'Methoxetamine'
slug: "methoxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Methoxetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\methoxetamine.md`
```md
---
title: 'Methoxetamine'
slug: "methoxetamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Methoxetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\morphinans.fa.md`
```md
---
title: 'Morphinans'
slug: "morphinans"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Morphinans

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\morphinans.md`
```md
---
title: 'Morphinans'
slug: "morphinans"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Morphinans

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\phencyclidine.fa.md`
```md
---
title: 'Phencyclidine'
slug: "phencyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Phencyclidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\phencyclidine.md`
```md
---
title: 'Phencyclidine'
slug: "phencyclidine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# Phencyclidine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\r-ketamine.fa.md`
```md
---
title: 'R-Ketamine'
slug: "r-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# R-Ketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\r-ketamine.md`
```md
---
title: 'R-Ketamine'
slug: "r-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# R-Ketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\s-ketamine.fa.md`
```md
---
title: 'S-Ketamine'
slug: "s-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# S-Ketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Dissociatives\s-ketamine.md`
```md
---
title: 'S-Ketamine'
slug: "s-ketamine"
lang: "en"
category: 'Dissociatives'
weight: 1000
template: "wiki"
summary: ''
---

# S-Ketamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\25-dma.fa.md`
```md
---
title: '2,5-DMA'
slug: "25-dma"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# 2,5-DMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\25-dma.md`
```md
---
title: '2,5-DMA'
slug: "25-dma"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# 2,5-DMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\dob.fa.md`
```md
---
title: 'DOB'
slug: "dob"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\dob.md`
```md
---
title: 'DOB'
slug: "dob"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\doc.fa.md`
```md
---
title: 'DOC'
slug: "doc"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\doc.md`
```md
---
title: 'DOC'
slug: "doc"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\doi.fa.md`
```md
---
title: 'DOI'
slug: "doi"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\doi.md`
```md
---
title: 'DOI'
slug: "doi"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\dom.fa.md`
```md
---
title: 'DOM'
slug: "dom"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\dom.md`
```md
---
title: 'DOM'
slug: "dom"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\dox.fa.md`
```md
---
title: 'DOx'
slug: "dox"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOx

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\dox.md`
```md
---
title: 'DOx'
slug: "dox"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOx

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\doxderivatives.fa.md`
```md
---
title: 'DOxـderivatives'
slug: "doxderivatives"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOxـderivatives

_Page coming soon._

```

---
### `src\wiki\Psychoactives\DOx\doxderivatives.md`
```md
---
title: 'DOxـderivatives'
slug: "doxderivatives"
lang: "en"
category: 'DOx'
weight: 1000
template: "wiki"
summary: ''
---

# DOxـderivatives

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\5-apb.fa.md`
```md
---
title: '5-APB'
slug: "5-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-APB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\5-apb.md`
```md
---
title: '5-APB'
slug: "5-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-APB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\5-mapb.fa.md`
```md
---
title: '5-MAPB'
slug: "5-mapb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MAPB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\5-mapb.md`
```md
---
title: '5-MAPB'
slug: "5-mapb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MAPB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\6-apb.fa.md`
```md
---
title: '6-APB'
slug: "6-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\6-apb.md`
```md
---
title: '6-APB'
slug: "6-apb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\6-apdb.fa.md`
```md
---
title: '6-APDB'
slug: "6-apdb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APDB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\6-apdb.md`
```md
---
title: '6-APDB'
slug: "6-apdb"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# 6-APDB

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\benzofurans.fa.md`
```md
---
title: 'Benzofurans'
slug: "benzofurans"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Benzofurans

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\benzofurans.md`
```md
---
title: 'Benzofurans'
slug: "benzofurans"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Benzofurans

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\empathogens.fa.md`
```md
---
title: 'Empathogens'
slug: "empathogens"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Empathogens

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\empathogens.md`
```md
---
title: 'Empathogens'
slug: "empathogens"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Empathogens

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mda.fa.md`
```md
---
title: 'MDA'
slug: "mda"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mda.md`
```md
---
title: 'MDA'
slug: "mda"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdai.fa.md`
```md
---
title: 'MDAI'
slug: "mdai"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDAI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdai.md`
```md
---
title: 'MDAI'
slug: "mdai"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDAI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdea.fa.md`
```md
---
title: 'MDEA'
slug: "mdea"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDEA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdea.md`
```md
---
title: 'MDEA'
slug: "mdea"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDEA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdma.fa.md`
```md
---
title: 'MDMA'
slug: "mdma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdma.md`
```md
---
title: 'MDMA'
slug: "mdma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdxx.fa.md`
```md
---
title: 'MDxx'
slug: "mdxx"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDxx

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\mdxx.md`
```md
---
title: 'MDxx'
slug: "mdxx"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# MDxx

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\methylone.fa.md`
```md
---
title: 'Methylone'
slug: "methylone"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Methylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\methylone.md`
```md
---
title: 'Methylone'
slug: "methylone"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# Methylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\pma.fa.md`
```md
---
title: 'PMA'
slug: "pma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\pma.md`
```md
---
title: 'PMA'
slug: "pma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\pmma.fa.md`
```md
---
title: 'PMMA'
slug: "pmma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Empathogens\pmma.md`
```md
---
title: 'PMMA'
slug: "pmma"
lang: "en"
category: 'Empathogens'
weight: 1000
template: "wiki"
summary: ''
---

# PMMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\acacia-confusa.fa.md`
```md
---
title: 'Acacia confusa'
slug: "acacia-confusa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Acacia confusa

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\acacia-confusa.md`
```md
---
title: 'Acacia confusa'
slug: "acacia-confusa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Acacia confusa

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\amanita-muscaria.fa.md`
```md
---
title: 'Amanita muscaria'
slug: "amanita-muscaria"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Amanita muscaria

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\amanita-muscaria.md`
```md
---
title: 'Amanita muscaria'
slug: "amanita-muscaria"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Amanita muscaria

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\argyreia-nervosa.fa.md`
```md
---
title: 'Argyreia nervosa'
slug: "argyreia-nervosa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Argyreia nervosa

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\argyreia-nervosa.md`
```md
---
title: 'Argyreia nervosa'
slug: "argyreia-nervosa"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Argyreia nervosa

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\banisteriopsis-caapi.fa.md`
```md
---
title: 'Banisteriopsis caapi'
slug: "banisteriopsis-caapi"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Banisteriopsis caapi

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\banisteriopsis-caapi.md`
```md
---
title: 'Banisteriopsis caapi'
slug: "banisteriopsis-caapi"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Banisteriopsis caapi

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\blue-lotus.fa.md`
```md
---
title: 'Blue Lotus'
slug: "blue-lotus"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Blue Lotus

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\blue-lotus.md`
```md
---
title: 'Blue Lotus'
slug: "blue-lotus"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Blue Lotus

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\cannabis.fa.md`
```md
---
title: 'Cannabis'
slug: "cannabis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabis

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\cannabis.md`
```md
---
title: 'Cannabis'
slug: "cannabis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Cannabis

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\datura.fa.md`
```md
---
title: 'Datura'
slug: "datura"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Datura

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\datura.md`
```md
---
title: 'Datura'
slug: "datura"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Datura

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\entheogens.fa.md`
```md
---
title: 'Entheogens'
slug: "entheogens"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Entheogens

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\entheogens.md`
```md
---
title: 'Entheogens'
slug: "entheogens"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Entheogens

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\iboga.fa.md`
```md
---
title: 'Iboga'
slug: "iboga"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Iboga

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\iboga.md`
```md
---
title: 'Iboga'
slug: "iboga"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Iboga

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\ipomoea-tricolor.fa.md`
```md
---
title: 'Ipomoea tricolor'
slug: "ipomoea-tricolor"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Ipomoea tricolor

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\ipomoea-tricolor.md`
```md
---
title: 'Ipomoea tricolor'
slug: "ipomoea-tricolor"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Ipomoea tricolor

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\mimosa-hostilis.fa.md`
```md
---
title: 'Mimosa hostilis'
slug: "mimosa-hostilis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Mimosa hostilis

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\mimosa-hostilis.md`
```md
---
title: 'Mimosa hostilis'
slug: "mimosa-hostilis"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Mimosa hostilis

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\nicotiana.fa.md`
```md
---
title: 'Nicotiana'
slug: "nicotiana"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotiana

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\nicotiana.md`
```md
---
title: 'Nicotiana'
slug: "nicotiana"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotiana

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\peyote.fa.md`
```md
---
title: 'Peyote'
slug: "peyote"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Peyote

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\peyote.md`
```md
---
title: 'Peyote'
slug: "peyote"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Peyote

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\psilocybin-mushrooms.fa.md`
```md
---
title: 'Psilocybin mushrooms'
slug: "psilocybin-mushrooms"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin mushrooms

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\psilocybin-mushrooms.md`
```md
---
title: 'Psilocybin mushrooms'
slug: "psilocybin-mushrooms"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin mushrooms

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\salvia-divinorum.fa.md`
```md
---
title: 'Salvia divinorum'
slug: "salvia-divinorum"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Salvia divinorum

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\salvia-divinorum.md`
```md
---
title: 'Salvia divinorum'
slug: "salvia-divinorum"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Salvia divinorum

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\san-pedro.fa.md`
```md
---
title: 'San Pedro'
slug: "san-pedro"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# San Pedro

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\san-pedro.md`
```md
---
title: 'San Pedro'
slug: "san-pedro"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# San Pedro

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\syrian-rue.fa.md`
```md
---
title: 'Syrian rue'
slug: "syrian-rue"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Syrian rue

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\syrian-rue.md`
```md
---
title: 'Syrian rue'
slug: "syrian-rue"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Syrian rue

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\yopo.fa.md`
```md
---
title: 'Yopo'
slug: "yopo"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Yopo

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Entheogens\yopo.md`
```md
---
title: 'Yopo'
slug: "yopo"
lang: "en"
category: 'Entheogens'
weight: 1000
template: "wiki"
summary: ''
---

# Yopo

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1b-lsd.fa.md`
```md
---
title: '1B-LSD'
slug: "1b-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1B-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1b-lsd.md`
```md
---
title: '1B-LSD'
slug: "1b-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1B-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1cp-al-lad.fa.md`
```md
---
title: '1cP-AL-LAD'
slug: "1cp-al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-AL-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1cp-al-lad.md`
```md
---
title: '1cP-AL-LAD'
slug: "1cp-al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-AL-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1cp-lsd.fa.md`
```md
---
title: '1cP-LSD'
slug: "1cp-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1cp-lsd.md`
```md
---
title: '1cP-LSD'
slug: "1cp-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1cp-mipla.fa.md`
```md
---
title: '1cP-MiPLA'
slug: "1cp-mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-MiPLA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1cp-mipla.md`
```md
---
title: '1cP-MiPLA'
slug: "1cp-mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1cP-MiPLA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1p-eth-lad.fa.md`
```md
---
title: '1P-ETH-LAD'
slug: "1p-eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-ETH-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1p-eth-lad.md`
```md
---
title: '1P-ETH-LAD'
slug: "1p-eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-ETH-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1p-lsd.fa.md`
```md
---
title: '1P-LSD'
slug: "1p-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1p-lsd.md`
```md
---
title: '1P-LSD'
slug: "1p-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1P-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1v-lsd.fa.md`
```md
---
title: '1V-LSD'
slug: "1v-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1V-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\1v-lsd.md`
```md
---
title: '1V-LSD'
slug: "1v-lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# 1V-LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\al-lad.fa.md`
```md
---
title: 'AL-LAD'
slug: "al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# AL-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\al-lad.md`
```md
---
title: 'AL-LAD'
slug: "al-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# AL-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\ald-52.fa.md`
```md
---
title: 'ALD-52'
slug: "ald-52"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ALD-52

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\ald-52.md`
```md
---
title: 'ALD-52'
slug: "ald-52"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ALD-52

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\eth-lad.fa.md`
```md
---
title: 'ETH-LAD'
slug: "eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ETH-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\eth-lad.md`
```md
---
title: 'ETH-LAD'
slug: "eth-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# ETH-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lae-32.fa.md`
```md
---
title: 'LAE-32'
slug: "lae-32"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LAE-32

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lae-32.md`
```md
---
title: 'LAE-32'
slug: "lae-32"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LAE-32

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsa.fa.md`
```md
---
title: 'LSA'
slug: "lsa"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsa.md`
```md
---
title: 'LSA'
slug: "lsa"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsd.fa.md`
```md
---
title: 'LSD'
slug: "lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsd.md`
```md
---
title: 'LSD'
slug: "lsd"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsh.fa.md`
```md
---
title: 'LSH'
slug: "lsh"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsh.md`
```md
---
title: 'LSH'
slug: "lsh"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsm-775.fa.md`
```md
---
title: 'LSM-775'
slug: "lsm-775"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSM-775

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsm-775.md`
```md
---
title: 'LSM-775'
slug: "lsm-775"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSM-775

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsz.fa.md`
```md
---
title: 'LSZ'
slug: "lsz"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSZ

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lsz.md`
```md
---
title: 'LSZ'
slug: "lsz"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# LSZ

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lysergamides.fa.md`
```md
---
title: 'Lysergamides'
slug: "lysergamides"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# Lysergamides

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\lysergamides.md`
```md
---
title: 'Lysergamides'
slug: "lysergamides"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# Lysergamides

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\mipla.fa.md`
```md
---
title: 'MiPLA'
slug: "mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# MiPLA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\mipla.md`
```md
---
title: 'MiPLA'
slug: "mipla"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# MiPLA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\pargy-lad.fa.md`
```md
---
title: 'PARGY-LAD'
slug: "pargy-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PARGY-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\pargy-lad.md`
```md
---
title: 'PARGY-LAD'
slug: "pargy-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PARGY-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\pro-lad.fa.md`
```md
---
title: 'PRO-LAD'
slug: "pro-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PRO-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Lysergamides\pro-lad.md`
```md
---
title: 'PRO-LAD'
slug: "pro-lad"
lang: "en"
category: 'Lysergamides'
weight: 1000
template: "wiki"
summary: ''
---

# PRO-LAD

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\3c-e.fa.md`
```md
---
title: '3C-E'
slug: "3c-e"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-E

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\3c-e.md`
```md
---
title: '3C-E'
slug: "3c-e"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-E

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\3c-p.fa.md`
```md
---
title: '3C-P'
slug: "3c-p"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-P

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\3c-p.md`
```md
---
title: '3C-P'
slug: "3c-p"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# 3C-P

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\allylescaline.fa.md`
```md
---
title: 'Allylescaline'
slug: "allylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Allylescaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\allylescaline.md`
```md
---
title: 'Allylescaline'
slug: "allylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Allylescaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\escaline.fa.md`
```md
---
title: 'Escaline'
slug: "escaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Escaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\escaline.md`
```md
---
title: 'Escaline'
slug: "escaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Escaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\mescaline-homologues.fa.md`
```md
---
title: 'Mescaline_homologues'
slug: "mescaline-homologues"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline_homologues

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\mescaline-homologues.md`
```md
---
title: 'Mescaline_homologues'
slug: "mescaline-homologues"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline_homologues

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\mescaline.fa.md`
```md
---
title: 'Mescaline'
slug: "mescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\mescaline.md`
```md
---
title: 'Mescaline'
slug: "mescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Mescaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\methallylescaline.fa.md`
```md
---
title: 'Methallylescaline'
slug: "methallylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Methallylescaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\methallylescaline.md`
```md
---
title: 'Methallylescaline'
slug: "methallylescaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Methallylescaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\proscaline.fa.md`
```md
---
title: 'Proscaline'
slug: "proscaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Proscaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Mescaline_homologues\proscaline.md`
```md
---
title: 'Proscaline'
slug: "proscaline"
lang: "en"
category: 'Mescaline_homologues'
weight: 1000
template: "wiki"
summary: ''
---

# Proscaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\5-hydroxytryptophan.fa.md`
```md
---
title: '5-Hydroxytryptophan'
slug: "5-hydroxytryptophan"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# 5-Hydroxytryptophan

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\5-hydroxytryptophan.md`
```md
---
title: '5-Hydroxytryptophan'
slug: "5-hydroxytryptophan"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# 5-Hydroxytryptophan

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\acetylcholine-boosters.fa.md`
```md
---
title: 'Acetylcholine boosters'
slug: "acetylcholine-boosters"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine boosters

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\acetylcholine-boosters.md`
```md
---
title: 'Acetylcholine boosters'
slug: "acetylcholine-boosters"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine boosters

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\acetylcholinesterase-inhibitors.fa.md`
```md
---
title: 'Acetylcholinesterase inhibitors'
slug: "acetylcholinesterase-inhibitors"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholinesterase inhibitors

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\acetylcholinesterase-inhibitors.md`
```md
---
title: 'Acetylcholinesterase inhibitors'
slug: "acetylcholinesterase-inhibitors"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholinesterase inhibitors

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\alkyl-nitrites.fa.md`
```md
---
title: 'Alkyl nitrites'
slug: "alkyl-nitrites"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Alkyl nitrites

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\alkyl-nitrites.md`
```md
---
title: 'Alkyl nitrites'
slug: "alkyl-nitrites"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Alkyl nitrites

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\amyl-nitrite.fa.md`
```md
---
title: 'Amyl nitrite'
slug: "amyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Amyl nitrite

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\amyl-nitrite.md`
```md
---
title: 'Amyl nitrite'
slug: "amyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Amyl nitrite

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\ayahuasca.fa.md`
```md
---
title: 'Ayahuasca'
slug: "ayahuasca"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ayahuasca

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\ayahuasca.md`
```md
---
title: 'Ayahuasca'
slug: "ayahuasca"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ayahuasca

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\calea-ternifolia.fa.md`
```md
---
title: 'Calea ternifolia'
slug: "calea-ternifolia"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Calea ternifolia

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\calea-ternifolia.md`
```md
---
title: 'Calea ternifolia'
slug: "calea-ternifolia"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Calea ternifolia

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\changa.fa.md`
```md
---
title: 'Changa'
slug: "changa"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Changa

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\changa.md`
```md
---
title: 'Changa'
slug: "changa"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Changa

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\chloroform.fa.md`
```md
---
title: 'Chloroform'
slug: "chloroform"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Chloroform

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\chloroform.md`
```md
---
title: 'Chloroform'
slug: "chloroform"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Chloroform

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\diethyl-ether.fa.md`
```md
---
title: 'Diethyl ether'
slug: "diethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Diethyl ether

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\diethyl-ether.md`
```md
---
title: 'Diethyl ether'
slug: "diethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Diethyl ether

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\dxm-and-dph.fa.md`
```md
---
title: 'DXM & DPH'
slug: "dxm-and-dph"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM & DPH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\dxm-and-dph.md`
```md
---
title: 'DXM & DPH'
slug: "dxm-and-dph"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM & DPH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\dxm.fa.md`
```md
---
title: 'DXM'
slug: "dxm"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\dxm.md`
```md
---
title: 'DXM'
slug: "dxm"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# DXM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\entada-rheedii.fa.md`
```md
---
title: 'Entada rheedii'
slug: "entada-rheedii"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Entada rheedii

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\entada-rheedii.md`
```md
---
title: 'Entada rheedii'
slug: "entada-rheedii"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Entada rheedii

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\galantamine.fa.md`
```md
---
title: 'Galantamine'
slug: "galantamine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Galantamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\galantamine.md`
```md
---
title: 'Galantamine'
slug: "galantamine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Galantamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\ibogaine.fa.md`
```md
---
title: 'Ibogaine'
slug: "ibogaine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ibogaine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\ibogaine.md`
```md
---
title: 'Ibogaine'
slug: "ibogaine"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Ibogaine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\inhalants.fa.md`
```md
---
title: 'Inhalants'
slug: "inhalants"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Inhalants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\inhalants.md`
```md
---
title: 'Inhalants'
slug: "inhalants"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Inhalants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\isobutyl-nitrite.fa.md`
```md
---
title: 'Isobutyl nitrite'
slug: "isobutyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isobutyl nitrite

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\isobutyl-nitrite.md`
```md
---
title: 'Isobutyl nitrite'
slug: "isobutyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isobutyl nitrite

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\isopropyl-nitrite.fa.md`
```md
---
title: 'Isopropyl nitrite'
slug: "isopropyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropyl nitrite

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\isopropyl-nitrite.md`
```md
---
title: 'Isopropyl nitrite'
slug: "isopropyl-nitrite"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropyl nitrite

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\miscellaneous.fa.md`
```md
---
title: 'Miscellaneous'
slug: "miscellaneous"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneous

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\miscellaneous.md`
```md
---
title: 'Miscellaneous'
slug: "miscellaneous"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneous

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\nitrous-oxide.fa.md`
```md
---
title: 'Nitrous oxide'
slug: "nitrous-oxide"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Nitrous oxide

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\nitrous-oxide.md`
```md
---
title: 'Nitrous oxide'
slug: "nitrous-oxide"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Nitrous oxide

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\oneirogens.fa.md`
```md
---
title: 'Oneirogens'
slug: "oneirogens"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Oneirogens

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\oneirogens.md`
```md
---
title: 'Oneirogens'
slug: "oneirogens"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Oneirogens

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\opioid-receptor-agonists.fa.md`
```md
---
title: 'κ-Opioid receptor agonists'
slug: "opioid-receptor-agonists"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# κ-Opioid receptor agonists

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\opioid-receptor-agonists.md`
```md
---
title: 'κ-Opioid receptor agonists'
slug: "opioid-receptor-agonists"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# κ-Opioid receptor agonists

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\polysubstance-combinations.fa.md`
```md
---
title: 'Polysubstance combinations'
slug: "polysubstance-combinations"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Polysubstance combinations

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\polysubstance-combinations.md`
```md
---
title: 'Polysubstance combinations'
slug: "polysubstance-combinations"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Polysubstance combinations

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\progesterone.fa.md`
```md
---
title: 'Progesterone'
slug: "progesterone"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Progesterone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\progesterone.md`
```md
---
title: 'Progesterone'
slug: "progesterone"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Progesterone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\salvinorin-a.fa.md`
```md
---
title: 'Salvinorin A'
slug: "salvinorin-a"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin A

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\salvinorin-a.md`
```md
---
title: 'Salvinorin A'
slug: "salvinorin-a"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin A

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\salvinorin-b-methoxymethyl-ether.fa.md`
```md
---
title: 'Salvinorin B methoxymethyl ether'
slug: "salvinorin-b-methoxymethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin B methoxymethyl ether

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\salvinorin-b-methoxymethyl-ether.md`
```md
---
title: 'Salvinorin B methoxymethyl ether'
slug: "salvinorin-b-methoxymethyl-ether"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Salvinorin B methoxymethyl ether

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\sigmaergics.fa.md`
```md
---
title: 'Sigmaergics'
slug: "sigmaergics"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Sigmaergics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\sigmaergics.md`
```md
---
title: 'Sigmaergics'
slug: "sigmaergics"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Sigmaergics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\various.fa.md`
```md
---
title: 'Various'
slug: "various"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Various

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\various.md`
```md
---
title: 'Various'
slug: "various"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Various

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\xenon.fa.md`
```md
---
title: 'Xenon'
slug: "xenon"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Xenon

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneous\xenon.md`
```md
---
title: 'Xenon'
slug: "xenon"
lang: "en"
category: 'Miscellaneous'
weight: 1000
template: "wiki"
summary: ''
---

# Xenon

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\2c-b-fly.fa.md`
```md
---
title: '2C-B-FLY'
slug: "2c-b-fly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B-FLY

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\2c-b-fly.md`
```md
---
title: '2C-B-FLY'
slug: "2c-b-fly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 2C-B-FLY

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\bromo-dragonfly.fa.md`
```md
---
title: 'Bromo-DragonFLY'
slug: "bromo-dragonfly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bromo-DragonFLY

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\bromo-dragonfly.md`
```md
---
title: 'Bromo-DragonFLY'
slug: "bromo-dragonfly"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bromo-DragonFLY

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\k-2c-b.fa.md`
```md
---
title: 'βk-2C-B'
slug: "k-2c-b"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# βk-2C-B

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\k-2c-b.md`
```md
---
title: 'βk-2C-B'
slug: "k-2c-b"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# βk-2C-B

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\miscellaneousphenethylamines.fa.md`
```md
---
title: 'Miscellaneousـphenethylamines'
slug: "miscellaneousphenethylamines"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneousـphenethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\miscellaneousphenethylamines.md`
```md
---
title: 'Miscellaneousـphenethylamines'
slug: "miscellaneousphenethylamines"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# Miscellaneousـphenethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\tma-2.fa.md`
```md
---
title: 'TMA-2'
slug: "tma-2"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-2

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\tma-2.md`
```md
---
title: 'TMA-2'
slug: "tma-2"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-2

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\tma-6.fa.md`
```md
---
title: 'TMA-6'
slug: "tma-6"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-6

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Miscellaneousـphenethylamines\tma-6.md`
```md
---
title: 'TMA-6'
slug: "tma-6"
lang: "en"
category: 'Miscellaneousـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# TMA-6

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25b-nboh.fa.md`
```md
---
title: '25B-NBOH'
slug: "25b-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25b-nboh.md`
```md
---
title: '25B-NBOH'
slug: "25b-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25b-nbome.fa.md`
```md
---
title: '25B-NBOMe'
slug: "25b-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25b-nbome.md`
```md
---
title: '25B-NBOMe'
slug: "25b-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25B-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25c-nboh.fa.md`
```md
---
title: '25C-NBOH'
slug: "25c-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25c-nboh.md`
```md
---
title: '25C-NBOH'
slug: "25c-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25c-nbome.fa.md`
```md
---
title: '25C-NBOMe'
slug: "25c-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25c-nbome.md`
```md
---
title: '25C-NBOMe'
slug: "25c-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25C-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25d-nbome.fa.md`
```md
---
title: '25D-NBOMe'
slug: "25d-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25D-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25d-nbome.md`
```md
---
title: '25D-NBOMe'
slug: "25d-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25D-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25e-nboh.fa.md`
```md
---
title: '25E-NBOH'
slug: "25e-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25E-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25e-nboh.md`
```md
---
title: '25E-NBOH'
slug: "25e-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25E-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25i-nboh.fa.md`
```md
---
title: '25I-NBOH'
slug: "25i-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25i-nboh.md`
```md
---
title: '25I-NBOH'
slug: "25i-nboh"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25i-nbome.fa.md`
```md
---
title: '25I-NBOMe'
slug: "25i-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25i-nbome.md`
```md
---
title: '25I-NBOMe'
slug: "25i-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25I-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25n-nbome.fa.md`
```md
---
title: '25N-NBOMe'
slug: "25n-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25N-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\25n-nbome.md`
```md
---
title: '25N-NBOMe'
slug: "25n-nbome"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# 25N-NBOMe

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\n-benzylphenethylamines.fa.md`
```md
---
title: 'N-Benzylـphenethylamines'
slug: "n-benzylphenethylamines"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# N-Benzylـphenethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\N-Benzylـphenethylamines\n-benzylphenethylamines.md`
```md
---
title: 'N-Benzylـphenethylamines'
slug: "n-benzylphenethylamines"
lang: "en"
category: 'N-Benzylـphenethylamines'
weight: 1000
template: "wiki"
summary: ''
---

# N-Benzylـphenethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\acetylcholine.fa.md`
```md
---
title: 'Acetylcholine'
slug: "acetylcholine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\acetylcholine.md`
```md
---
title: 'Acetylcholine'
slug: "acetylcholine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Acetylcholine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\amino-acids.fa.md`
```md
---
title: 'Amino acids'
slug: "amino-acids"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Amino acids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\amino-acids.md`
```md
---
title: 'Amino acids'
slug: "amino-acids"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Amino acids

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\aminobutyric-acid.fa.md`
```md
---
title: 'γ-Aminobutyric acid'
slug: "aminobutyric-acid"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# γ-Aminobutyric acid

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\aminobutyric-acid.md`
```md
---
title: 'γ-Aminobutyric acid'
slug: "aminobutyric-acid"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# γ-Aminobutyric acid

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\catecholamines.fa.md`
```md
---
title: 'Catecholamines'
slug: "catecholamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Catecholamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\catecholamines.md`
```md
---
title: 'Catecholamines'
slug: "catecholamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Catecholamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\dopamine.fa.md`
```md
---
title: 'Dopamine'
slug: "dopamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Dopamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\dopamine.md`
```md
---
title: 'Dopamine'
slug: "dopamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Dopamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\epinephrine.fa.md`
```md
---
title: 'Epinephrine'
slug: "epinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Epinephrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\epinephrine.md`
```md
---
title: 'Epinephrine'
slug: "epinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Epinephrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\histamine.fa.md`
```md
---
title: 'Histamine'
slug: "histamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Histamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\histamine.md`
```md
---
title: 'Histamine'
slug: "histamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Histamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\l-glutamate.fa.md`
```md
---
title: 'L-Glutamate'
slug: "l-glutamate"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# L-Glutamate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\l-glutamate.md`
```md
---
title: 'L-Glutamate'
slug: "l-glutamate"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# L-Glutamate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\melatonin.fa.md`
```md
---
title: 'Melatonin'
slug: "melatonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Melatonin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\melatonin.md`
```md
---
title: 'Melatonin'
slug: "melatonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Melatonin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\monoamines.fa.md`
```md
---
title: 'Monoamines'
slug: "monoamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Monoamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\monoamines.md`
```md
---
title: 'Monoamines'
slug: "monoamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Monoamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\neurotransmitters.fa.md`
```md
---
title: 'Neurotransmitters'
slug: "neurotransmitters"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Neurotransmitters

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\neurotransmitters.md`
```md
---
title: 'Neurotransmitters'
slug: "neurotransmitters"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Neurotransmitters

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\norepinephrine.fa.md`
```md
---
title: 'Norepinephrine'
slug: "norepinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Norepinephrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\norepinephrine.md`
```md
---
title: 'Norepinephrine'
slug: "norepinephrine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Norepinephrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\other.fa.md`
```md
---
title: 'Other'
slug: "other"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Other

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\other.md`
```md
---
title: 'Other'
slug: "other"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Other

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\peptides.fa.md`
```md
---
title: 'Peptides'
slug: "peptides"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Peptides

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\peptides.md`
```md
---
title: 'Peptides'
slug: "peptides"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Peptides

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\phenethylamine.fa.md`
```md
---
title: 'Phenethylamine'
slug: "phenethylamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\phenethylamine.md`
```md
---
title: 'Phenethylamine'
slug: "phenethylamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\phenethylamines.fa.md`
```md
---
title: 'Phenethylamines'
slug: "phenethylamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\phenethylamines.md`
```md
---
title: 'Phenethylamines'
slug: "phenethylamines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Phenethylamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\semax.fa.md`
```md
---
title: 'Semax'
slug: "semax"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Semax

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\semax.md`
```md
---
title: 'Semax'
slug: "semax"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Semax

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\serotonin.fa.md`
```md
---
title: 'Serotonin'
slug: "serotonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Serotonin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\serotonin.md`
```md
---
title: 'Serotonin'
slug: "serotonin"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Serotonin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\trace-amines.fa.md`
```md
---
title: 'Trace amines'
slug: "trace-amines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Trace amines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\trace-amines.md`
```md
---
title: 'Trace amines'
slug: "trace-amines"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Trace amines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\tryptamine.fa.md`
```md
---
title: 'Tryptamine'
slug: "tryptamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Tryptamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Neurotransmitters\tryptamine.md`
```md
---
title: 'Tryptamine'
slug: "tryptamine"
lang: "en"
category: 'Neurotransmitters'
weight: 1000
template: "wiki"
summary: ''
---

# Tryptamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\5-htp.fa.md`
```md
---
title: '5-HTP'
slug: "5-htp"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# 5-HTP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\5-htp.md`
```md
---
title: '5-HTP'
slug: "5-htp"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# 5-HTP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\adrafinil.fa.md`
```md
---
title: 'Adrafinil'
slug: "adrafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Adrafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\adrafinil.md`
```md
---
title: 'Adrafinil'
slug: "adrafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Adrafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\alpha-gpc.fa.md`
```md
---
title: 'Alpha-GPC'
slug: "alpha-gpc"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Alpha-GPC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\alpha-gpc.md`
```md
---
title: 'Alpha-GPC'
slug: "alpha-gpc"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Alpha-GPC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\aniracetam.fa.md`
```md
---
title: 'Aniracetam'
slug: "aniracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Aniracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\aniracetam.md`
```md
---
title: 'Aniracetam'
slug: "aniracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Aniracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\armodafinil.fa.md`
```md
---
title: 'Armodafinil'
slug: "armodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Armodafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\armodafinil.md`
```md
---
title: 'Armodafinil'
slug: "armodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Armodafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\bromantane.fa.md`
```md
---
title: 'Bromantane'
slug: "bromantane"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Bromantane

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\bromantane.md`
```md
---
title: 'Bromantane'
slug: "bromantane"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Bromantane

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\choline-bitartrate.fa.md`
```md
---
title: 'Choline bitartrate'
slug: "choline-bitartrate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline bitartrate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\choline-bitartrate.md`
```md
---
title: 'Choline bitartrate'
slug: "choline-bitartrate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline bitartrate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\choline.fa.md`
```md
---
title: 'Choline'
slug: "choline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\choline.md`
```md
---
title: 'Choline'
slug: "choline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Choline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\citicoline.fa.md`
```md
---
title: 'Citicoline'
slug: "citicoline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Citicoline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\citicoline.md`
```md
---
title: 'Citicoline'
slug: "citicoline"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Citicoline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\coluracetam.fa.md`
```md
---
title: 'Coluracetam'
slug: "coluracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Coluracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\coluracetam.md`
```md
---
title: 'Coluracetam'
slug: "coluracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Coluracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\creatine.fa.md`
```md
---
title: 'Creatine'
slug: "creatine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Creatine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\creatine.md`
```md
---
title: 'Creatine'
slug: "creatine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Creatine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\dietary-supplements.fa.md`
```md
---
title: 'Dietary supplements'
slug: "dietary-supplements"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Dietary supplements

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\dietary-supplements.md`
```md
---
title: 'Dietary supplements'
slug: "dietary-supplements"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Dietary supplements

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\eugeroics.fa.md`
```md
---
title: 'Eugeroics'
slug: "eugeroics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Eugeroics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\eugeroics.md`
```md
---
title: 'Eugeroics'
slug: "eugeroics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Eugeroics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\gaba.fa.md`
```md
---
title: 'GABA'
slug: "gaba"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# GABA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\gaba.md`
```md
---
title: 'GABA'
slug: "gaba"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# GABA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\l-theanine.fa.md`
```md
---
title: 'L-Theanine'
slug: "l-theanine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Theanine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\l-theanine.md`
```md
---
title: 'L-Theanine'
slug: "l-theanine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Theanine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\l-tyrosine.fa.md`
```md
---
title: 'L-Tyrosine'
slug: "l-tyrosine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Tyrosine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\l-tyrosine.md`
```md
---
title: 'L-Tyrosine'
slug: "l-tyrosine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# L-Tyrosine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\meclofenoxate.fa.md`
```md
---
title: 'Meclofenoxate'
slug: "meclofenoxate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Meclofenoxate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\meclofenoxate.md`
```md
---
title: 'Meclofenoxate'
slug: "meclofenoxate"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Meclofenoxate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\memantine.fa.md`
```md
---
title: 'Memantine'
slug: "memantine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Memantine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\memantine.md`
```md
---
title: 'Memantine'
slug: "memantine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Memantine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\modafinil.fa.md`
```md
---
title: 'Modafinil'
slug: "modafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Modafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\modafinil.md`
```md
---
title: 'Modafinil'
slug: "modafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Modafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\n-acetylcysteine.fa.md`
```md
---
title: 'N-Acetylcysteine'
slug: "n-acetylcysteine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Acetylcysteine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\n-acetylcysteine.md`
```md
---
title: 'N-Acetylcysteine'
slug: "n-acetylcysteine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Acetylcysteine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\n-methylbisfluoromodafinil.fa.md`
```md
---
title: 'N-Methylbisfluoromodafinil'
slug: "n-methylbisfluoromodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Methylbisfluoromodafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\n-methylbisfluoromodafinil.md`
```md
---
title: 'N-Methylbisfluoromodafinil'
slug: "n-methylbisfluoromodafinil"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# N-Methylbisfluoromodafinil

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\noopept.fa.md`
```md
---
title: 'Noopept'
slug: "noopept"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Noopept

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\noopept.md`
```md
---
title: 'Noopept'
slug: "noopept"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Noopept

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\nootropics.fa.md`
```md
---
title: 'Nootropics'
slug: "nootropics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Nootropics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\nootropics.md`
```md
---
title: 'Nootropics'
slug: "nootropics"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Nootropics

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\others.fa.md`
```md
---
title: 'Others'
slug: "others"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Others

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\others.md`
```md
---
title: 'Others'
slug: "others"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Others

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\oxiracetam.fa.md`
```md
---
title: 'Oxiracetam'
slug: "oxiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Oxiracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\oxiracetam.md`
```md
---
title: 'Oxiracetam'
slug: "oxiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Oxiracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\phenylpiracetam.fa.md`
```md
---
title: 'Phenylpiracetam'
slug: "phenylpiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Phenylpiracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\phenylpiracetam.md`
```md
---
title: 'Phenylpiracetam'
slug: "phenylpiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Phenylpiracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\piracetam.fa.md`
```md
---
title: 'Piracetam'
slug: "piracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Piracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\piracetam.md`
```md
---
title: 'Piracetam'
slug: "piracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Piracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\pramiracetam.fa.md`
```md
---
title: 'Pramiracetam'
slug: "pramiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Pramiracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\pramiracetam.md`
```md
---
title: 'Pramiracetam'
slug: "pramiracetam"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Pramiracetam

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\racetams.fa.md`
```md
---
title: 'Racetams'
slug: "racetams"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Racetams

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\racetams.md`
```md
---
title: 'Racetams'
slug: "racetams"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Racetams

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\s-adenosyl-methionine.fa.md`
```md
---
title: 'S-Adenosyl methionine'
slug: "s-adenosyl-methionine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# S-Adenosyl methionine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\s-adenosyl-methionine.md`
```md
---
title: 'S-Adenosyl methionine'
slug: "s-adenosyl-methionine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# S-Adenosyl methionine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\tianeptine.fa.md`
```md
---
title: 'Tianeptine'
slug: "tianeptine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Tianeptine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Nootropics\tianeptine.md`
```md
---
title: 'Tianeptine'
slug: "tianeptine"
lang: "en"
category: 'Nootropics'
weight: 1000
template: "wiki"
summary: ''
---

# Tianeptine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Others\5-meo-dibf.fa.md`
```md
---
title: '5-MeO-DiBF'
slug: "5-meo-dibf"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiBF

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Others\5-meo-dibf.md`
```md
---
title: '5-MeO-DiBF'
slug: "5-meo-dibf"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiBF

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Others\efavirenz.fa.md`
```md
---
title: 'Efavirenz'
slug: "efavirenz"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# Efavirenz

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Others\efavirenz.md`
```md
---
title: 'Efavirenz'
slug: "efavirenz"
lang: "en"
category: 'Others'
weight: 1000
template: "wiki"
summary: ''
---

# Efavirenz

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-ai.fa.md`
```md
---
title: '2-AI'
slug: "2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-AI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-ai.md`
```md
---
title: '2-AI'
slug: "2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-AI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-fa.fa.md`
```md
---
title: '2-FA'
slug: "2-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-fa.md`
```md
---
title: '2-FA'
slug: "2-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-fea.fa.md`
```md
---
title: '2-FEA'
slug: "2-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FEA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-fea.md`
```md
---
title: '2-FEA'
slug: "2-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FEA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-fma.fa.md`
```md
---
title: '2-FMA'
slug: "2-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\2-fma.md`
```md
---
title: '2-FMA'
slug: "2-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 2-FMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fa.fa.md`
```md
---
title: '3-FA'
slug: "3-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fa.md`
```md
---
title: '3-FA'
slug: "3-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fea.fa.md`
```md
---
title: '3-FEA'
slug: "3-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FEA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fea.md`
```md
---
title: '3-FEA'
slug: "3-fea"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FEA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fma.fa.md`
```md
---
title: '3-FMA'
slug: "3-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fma.md`
```md
---
title: '3-FMA'
slug: "3-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fpm.fa.md`
```md
---
title: '3-FPM'
slug: "3-fpm"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FPM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-fpm.md`
```md
---
title: '3-FPM'
slug: "3-fpm"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-FPM

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-mmc.fa.md`
```md
---
title: '3-MMC'
slug: "3-mmc"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MMC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\3-mmc.md`
```md
---
title: '3-MMC'
slug: "3-mmc"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3-MMC

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\34-ctmp.fa.md`
```md
---
title: '3,4-CTMP'
slug: "34-ctmp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3,4-CTMP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\34-ctmp.md`
```md
---
title: '3,4-CTMP'
slug: "34-ctmp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 3,4-CTMP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4-fa.fa.md`
```md
---
title: '4-FA'
slug: "4-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4-fa.md`
```md
---
title: '4-FA'
slug: "4-fa"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4-fma.fa.md`
```md
---
title: '4-FMA'
slug: "4-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4-fma.md`
```md
---
title: '4-FMA'
slug: "4-fma"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4-FMA

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4f-eph.fa.md`
```md
---
title: '4F-EPH'
slug: "4f-eph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-EPH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4f-eph.md`
```md
---
title: '4F-EPH'
slug: "4f-eph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-EPH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4f-mph.fa.md`
```md
---
title: '4F-MPH'
slug: "4f-mph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-MPH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\4f-mph.md`
```md
---
title: '4F-MPH'
slug: "4f-mph"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 4F-MPH

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\8-chlorotheophylline.fa.md`
```md
---
title: '8-Chlorotheophylline'
slug: "8-chlorotheophylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 8-Chlorotheophylline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\8-chlorotheophylline.md`
```md
---
title: '8-Chlorotheophylline'
slug: "8-chlorotheophylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# 8-Chlorotheophylline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\aminorexes.fa.md`
```md
---
title: 'Aminorexes'
slug: "aminorexes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Aminorexes

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\aminorexes.md`
```md
---
title: 'Aminorexes'
slug: "aminorexes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Aminorexes

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\amphetamine.fa.md`
```md
---
title: 'Amphetamine'
slug: "amphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\amphetamine.md`
```md
---
title: 'Amphetamine'
slug: "amphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\amphetamines.fa.md`
```md
---
title: 'Amphetamines'
slug: "amphetamines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\amphetamines.md`
```md
---
title: 'Amphetamines'
slug: "amphetamines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Amphetamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\butylone.fa.md`
```md
---
title: 'Butylone'
slug: "butylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Butylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\butylone.md`
```md
---
title: 'Butylone'
slug: "butylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Butylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\caffeine.fa.md`
```md
---
title: 'Caffeine'
slug: "caffeine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Caffeine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\caffeine.md`
```md
---
title: 'Caffeine'
slug: "caffeine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Caffeine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cathinone.fa.md`
```md
---
title: 'Cathinone'
slug: "cathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cathinone.md`
```md
---
title: 'Cathinone'
slug: "cathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cathinones.fa.md`
```md
---
title: 'Cathinones'
slug: "cathinones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinones

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cathinones.md`
```md
---
title: 'Cathinones'
slug: "cathinones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cathinones

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cocaine.fa.md`
```md
---
title: 'Cocaine'
slug: "cocaine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cocaine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cocaine.md`
```md
---
title: 'Cocaine'
slug: "cocaine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cocaine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cyclazodone.fa.md`
```md
---
title: 'Cyclazodone'
slug: "cyclazodone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cyclazodone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\cyclazodone.md`
```md
---
title: 'Cyclazodone'
slug: "cyclazodone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Cyclazodone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\desoxypipradrol.fa.md`
```md
---
title: 'Desoxypipradrol'
slug: "desoxypipradrol"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Desoxypipradrol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\desoxypipradrol.md`
```md
---
title: 'Desoxypipradrol'
slug: "desoxypipradrol"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Desoxypipradrol

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\dexmethylphenidate.fa.md`
```md
---
title: 'Dexmethylphenidate'
slug: "dexmethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dexmethylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\dexmethylphenidate.md`
```md
---
title: 'Dexmethylphenidate'
slug: "dexmethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dexmethylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\dextroamphetamine.fa.md`
```md
---
title: 'Dextroamphetamine'
slug: "dextroamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextroamphetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\dextroamphetamine.md`
```md
---
title: 'Dextroamphetamine'
slug: "dextroamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Dextroamphetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ephedrine.fa.md`
```md
---
title: 'Ephedrine'
slug: "ephedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephedrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ephedrine.md`
```md
---
title: 'Ephedrine'
slug: "ephedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephedrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ephylone.fa.md`
```md
---
title: 'Ephylone'
slug: "ephylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ephylone.md`
```md
---
title: 'Ephylone'
slug: "ephylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ephylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ethcathinone.fa.md`
```md
---
title: 'Ethcathinone'
slug: "ethcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethcathinone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ethcathinone.md`
```md
---
title: 'Ethcathinone'
slug: "ethcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethcathinone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ethylone.fa.md`
```md
---
title: 'Ethylone'
slug: "ethylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ethylone.md`
```md
---
title: 'Ethylone'
slug: "ethylone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ethylphenidate.fa.md`
```md
---
title: 'Ethylphenidate'
slug: "ethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\ethylphenidate.md`
```md
---
title: 'Ethylphenidate'
slug: "ethylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Ethylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\fenethylline.fa.md`
```md
---
title: 'Fenethylline'
slug: "fenethylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Fenethylline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\fenethylline.md`
```md
---
title: 'Fenethylline'
slug: "fenethylline"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Fenethylline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\hexedrone.fa.md`
```md
---
title: 'Hexedrone'
slug: "hexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Hexedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\hexedrone.md`
```md
---
title: 'Hexedrone'
slug: "hexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Hexedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\isopropylphenidate.fa.md`
```md
---
title: 'Isopropylphenidate'
slug: "isopropylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\isopropylphenidate.md`
```md
---
title: 'Isopropylphenidate'
slug: "isopropylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Isopropylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\lisdexamfetamine.fa.md`
```md
---
title: 'Lisdexamfetamine'
slug: "lisdexamfetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Lisdexamfetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\lisdexamfetamine.md`
```md
---
title: 'Lisdexamfetamine'
slug: "lisdexamfetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Lisdexamfetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mcpp.fa.md`
```md
---
title: 'mCPP'
slug: "mcpp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# mCPP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mcpp.md`
```md
---
title: 'mCPP'
slug: "mcpp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# mCPP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mdpv.fa.md`
```md
---
title: 'MDPV'
slug: "mdpv"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# MDPV

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mdpv.md`
```md
---
title: 'MDPV'
slug: "mdpv"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# MDPV

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mephedrone.fa.md`
```md
---
title: 'Mephedrone'
slug: "mephedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mephedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mephedrone.md`
```md
---
title: 'Mephedrone'
slug: "mephedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mephedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methamphetamine.fa.md`
```md
---
title: 'Methamphetamine'
slug: "methamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methamphetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methamphetamine.md`
```md
---
title: 'Methamphetamine'
slug: "methamphetamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methamphetamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methcathinone.fa.md`
```md
---
title: 'Methcathinone'
slug: "methcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methcathinone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methcathinone.md`
```md
---
title: 'Methcathinone'
slug: "methcathinone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methcathinone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methiopropamine.fa.md`
```md
---
title: 'Methiopropamine'
slug: "methiopropamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methiopropamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methiopropamine.md`
```md
---
title: 'Methiopropamine'
slug: "methiopropamine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methiopropamine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methylnaphthidate.fa.md`
```md
---
title: 'Methylnaphthidate'
slug: "methylnaphthidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylnaphthidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methylnaphthidate.md`
```md
---
title: 'Methylnaphthidate'
slug: "methylnaphthidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylnaphthidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methylphenidate.fa.md`
```md
---
title: 'Methylphenidate'
slug: "methylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\methylphenidate.md`
```md
---
title: 'Methylphenidate'
slug: "methylphenidate"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Methylphenidate

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mexedrone.fa.md`
```md
---
title: 'Mexedrone'
slug: "mexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mexedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\mexedrone.md`
```md
---
title: 'Mexedrone'
slug: "mexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Mexedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\n-ethylhexedrone.fa.md`
```md
---
title: 'N-Ethylhexedrone'
slug: "n-ethylhexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylhexedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\n-ethylhexedrone.md`
```md
---
title: 'N-Ethylhexedrone'
slug: "n-ethylhexedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylhexedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\n-ethylpentedrone.fa.md`
```md
---
title: 'N-Ethylpentedrone'
slug: "n-ethylpentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylpentedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\n-ethylpentedrone.md`
```md
---
title: 'N-Ethylpentedrone'
slug: "n-ethylpentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# N-Ethylpentedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\nicotine.fa.md`
```md
---
title: 'Nicotine'
slug: "nicotine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\nicotine.md`
```md
---
title: 'Nicotine'
slug: "nicotine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Nicotine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\nm-2-ai.fa.md`
```md
---
title: 'NM-2-AI'
slug: "nm-2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# NM-2-AI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\nm-2-ai.md`
```md
---
title: 'NM-2-AI'
slug: "nm-2-ai"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# NM-2-AI

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\pentedrone.fa.md`
```md
---
title: 'Pentedrone'
slug: "pentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\pentedrone.md`
```md
---
title: 'Pentedrone'
slug: "pentedrone"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pentedrone

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\phenidates.fa.md`
```md
---
title: 'Phenidates'
slug: "phenidates"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenidates

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\phenidates.md`
```md
---
title: 'Phenidates'
slug: "phenidates"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenidates

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\phenmetrazines.fa.md`
```md
---
title: 'Phenmetrazines'
slug: "phenmetrazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenmetrazines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\phenmetrazines.md`
```md
---
title: 'Phenmetrazines'
slug: "phenmetrazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Phenmetrazines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\php.fa.md`
```md
---
title: 'α-PHP'
slug: "php"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PHP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\php.md`
```md
---
title: 'α-PHP'
slug: "php"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PHP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\piperazines.fa.md`
```md
---
title: 'Piperazines'
slug: "piperazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Piperazines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\piperazines.md`
```md
---
title: 'Piperazines'
slug: "piperazines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Piperazines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\prolintane.fa.md`
```md
---
title: 'Prolintane'
slug: "prolintane"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Prolintane

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\prolintane.md`
```md
---
title: 'Prolintane'
slug: "prolintane"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Prolintane

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\propylhexedrine.fa.md`
```md
---
title: 'Propylhexedrine'
slug: "propylhexedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Propylhexedrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\propylhexedrine.md`
```md
---
title: 'Propylhexedrine'
slug: "propylhexedrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Propylhexedrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\pvp.fa.md`
```md
---
title: 'α-PVP'
slug: "pvp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PVP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\pvp.md`
```md
---
title: 'α-PVP'
slug: "pvp"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# α-PVP

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\pyrrolidinophenones.fa.md`
```md
---
title: 'Pyrrolidinophenones'
slug: "pyrrolidinophenones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrrolidinophenones

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\pyrrolidinophenones.md`
```md
---
title: 'Pyrrolidinophenones'
slug: "pyrrolidinophenones"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Pyrrolidinophenones

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\rti-111.fa.md`
```md
---
title: 'RTI-111'
slug: "rti-111"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# RTI-111

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\rti-111.md`
```md
---
title: 'RTI-111'
slug: "rti-111"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# RTI-111

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\stimulants.fa.md`
```md
---
title: 'Stimulants'
slug: "stimulants"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\stimulants.md`
```md
---
title: 'Stimulants'
slug: "stimulants"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulants

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\theacrine.fa.md`
```md
---
title: 'Theacrine'
slug: "theacrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Theacrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\theacrine.md`
```md
---
title: 'Theacrine'
slug: "theacrine"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Theacrine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\tropanes.fa.md`
```md
---
title: 'Tropanes'
slug: "tropanes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropanes

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\tropanes.md`
```md
---
title: 'Tropanes'
slug: "tropanes"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Tropanes

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\xanthines.fa.md`
```md
---
title: 'Xanthines'
slug: "xanthines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Xanthines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Stimulants\xanthines.md`
```md
---
title: 'Xanthines'
slug: "xanthines"
lang: "en"
category: 'Stimulants'
weight: 1000
template: "wiki"
summary: ''
---

# Xanthines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\carbolines.fa.md`
```md
---
title: 'β-Carbolines'
slug: "carbolines"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# β-Carbolines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\carbolines.md`
```md
---
title: 'β-Carbolines'
slug: "carbolines"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# β-Carbolines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\harmaline.fa.md`
```md
---
title: 'Harmaline'
slug: "harmaline"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\harmaline.md`
```md
---
title: 'Harmaline'
slug: "harmaline"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmaline

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\harmine.fa.md`
```md
---
title: 'Harmine'
slug: "harmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\harmine.md`
```md
---
title: 'Harmine'
slug: "harmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Harmine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\tetrahydroharmine.fa.md`
```md
---
title: 'Tetrahydroharmine'
slug: "tetrahydroharmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Tetrahydroharmine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\β-Carbolines\tetrahydroharmine.md`
```md
---
title: 'Tetrahydroharmine'
slug: "tetrahydroharmine"
lang: "en"
category: 'β-Carbolines'
weight: 1000
template: "wiki"
summary: ''
---

# Tetrahydroharmine

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\amt.fa.md`
```md
---
title: 'aMT'
slug: "amt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# aMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\amt.md`
```md
---
title: 'aMT'
slug: "amt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# aMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\det.fa.md`
```md
---
title: 'DET'
slug: "det"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\det.md`
```md
---
title: 'DET'
slug: "det"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\dipt.fa.md`
```md
---
title: 'DiPT'
slug: "dipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\dipt.md`
```md
---
title: 'DiPT'
slug: "dipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\dmt.fa.md`
```md
---
title: 'DMT'
slug: "dmt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\dmt.md`
```md
---
title: 'DMT'
slug: "dmt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\dpt.fa.md`
```md
---
title: 'DPT'
slug: "dpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\dpt.md`
```md
---
title: 'DPT'
slug: "dpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# DPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\ept.fa.md`
```md
---
title: 'EPT'
slug: "ept"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# EPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\ept.md`
```md
---
title: 'EPT'
slug: "ept"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# EPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\met.fa.md`
```md
---
title: 'MET'
slug: "met"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\met.md`
```md
---
title: 'MET'
slug: "met"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\mipt.fa.md`
```md
---
title: 'MiPT'
slug: "mipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\mipt.md`
```md
---
title: 'MiPT'
slug: "mipt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\mpt.fa.md`
```md
---
title: 'MPT'
slug: "mpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\mpt.md`
```md
---
title: 'MPT'
slug: "mpt"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# MPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\tryptamines.fa.md`
```md
---
title: 'Tryptamines'
slug: "tryptamines"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# Tryptamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Base Tryptamines\tryptamines.md`
```md
---
title: 'Tryptamines'
slug: "tryptamines"
lang: "en"
category: "Base Tryptamines"
weight: 1000
template: "wiki"
summary: "tryptamines"
---

# Tryptamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-det.fa.md`
```md
---
title: '4-AcO-DET'
slug: "4-aco-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-det.md`
```md
---
title: '4-AcO-DET'
slug: "4-aco-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-dipt.fa.md`
```md
---
title: '4-AcO-DiPT'
slug: "4-aco-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-dipt.md`
```md
---
title: '4-AcO-DiPT'
slug: "4-aco-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-dmt.fa.md`
```md
---
title: '4-AcO-DMT'
slug: "4-aco-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-dmt.md`
```md
---
title: '4-AcO-DMT'
slug: "4-aco-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-met.fa.md`
```md
---
title: '4-AcO-MET'
slug: "4-aco-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-met.md`
```md
---
title: '4-AcO-MET'
slug: "4-aco-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-mipt.fa.md`
```md
---
title: '4-AcO-MiPT'
slug: "4-aco-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-aco-mipt.md`
```md
---
title: '4-AcO-MiPT'
slug: "4-aco-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-AcO-MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-det.fa.md`
```md
---
title: '4-HO-DET'
slug: "4-ho-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-det.md`
```md
---
title: '4-HO-DET'
slug: "4-ho-det"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-dipt.fa.md`
```md
---
title: '4-HO-DiPT'
slug: "4-ho-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-dipt.md`
```md
---
title: '4-HO-DiPT'
slug: "4-ho-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-dpt.fa.md`
```md
---
title: '4-HO-DPT'
slug: "4-ho-dpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-dpt.md`
```md
---
title: '4-HO-DPT'
slug: "4-ho-dpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-DPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-ept.fa.md`
```md
---
title: '4-HO-EPT'
slug: "4-ho-ept"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-EPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-ept.md`
```md
---
title: '4-HO-EPT'
slug: "4-ho-ept"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-EPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-met.fa.md`
```md
---
title: '4-HO-MET'
slug: "4-ho-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-met.md`
```md
---
title: '4-HO-MET'
slug: "4-ho-met"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MET

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-mipt.fa.md`
```md
---
title: '4-HO-MiPT'
slug: "4-ho-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-mipt.md`
```md
---
title: '4-HO-MiPT'
slug: "4-ho-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-mpt.fa.md`
```md
---
title: '4-HO-MPT'
slug: "4-ho-mpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\4-ho-mpt.md`
```md
---
title: '4-HO-MPT'
slug: "4-ho-mpt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 4-HO-MPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-dalt.fa.md`
```md
---
title: '5-MeO-DALT'
slug: "5-meo-dalt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DALT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-dalt.md`
```md
---
title: '5-MeO-DALT'
slug: "5-meo-dalt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DALT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-dipt.fa.md`
```md
---
title: '5-MeO-DiPT'
slug: "5-meo-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-dipt.md`
```md
---
title: '5-MeO-DiPT'
slug: "5-meo-dipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-dmt.fa.md`
```md
---
title: '5-MeO-DMT'
slug: "5-meo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-dmt.md`
```md
---
title: '5-MeO-DMT'
slug: "5-meo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-mipt.fa.md`
```md
---
title: '5-MeO-MiPT'
slug: "5-meo-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\5-meo-mipt.md`
```md
---
title: '5-MeO-MiPT'
slug: "5-meo-mipt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5-MeO-MiPT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\56-mdo-dmt.fa.md`
```md
---
title: '5,6-MDO-DMT'
slug: "56-mdo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5,6-MDO-DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\56-mdo-dmt.md`
```md
---
title: '5,6-MDO-DMT'
slug: "56-mdo-dmt"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# 5,6-MDO-DMT

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\baeocystin.fa.md`
```md
---
title: 'Baeocystin'
slug: "baeocystin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Baeocystin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\baeocystin.md`
```md
---
title: 'Baeocystin'
slug: "baeocystin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Baeocystin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\bufotenin.fa.md`
```md
---
title: 'Bufotenin'
slug: "bufotenin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bufotenin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\bufotenin.md`
```md
---
title: 'Bufotenin'
slug: "bufotenin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Bufotenin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\psilocin.fa.md`
```md
---
title: 'Psilocin'
slug: "psilocin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\psilocin.md`
```md
---
title: 'Psilocin'
slug: "psilocin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\psilocybin.fa.md`
```md
---
title: 'Psilocybin'
slug: "psilocybin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\psilocybin.md`
```md
---
title: 'Psilocybin'
slug: "psilocybin"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Psilocybin

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\substituted-tryptamines.fa.md`
```md
---
title: 'Substituted tryptamines'
slug: "substituted-tryptamines"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Substituted tryptamines

_Page coming soon._

```

---
### `src\wiki\Psychoactives\Tryptamines\Substituted tryptamines\substituted-tryptamines.md`
```md
---
title: 'Substituted tryptamines'
slug: "substituted-tryptamines"
lang: "en"
category: 'Substituted tryptamines'
weight: 1000
template: "wiki"
summary: ''
---

# Substituted tryptamines

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-acuity-enhancement.fa.md`
```md
---
title: 'Auditory acuity enhancement'
slug: "auditory-acuity-enhancement"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-acuity-enhancement.md`
```md
---
title: 'Auditory acuity enhancement'
slug: "auditory-acuity-enhancement"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-acuity-suppression.fa.md`
```md
---
title: 'Auditory acuity suppression'
slug: "auditory-acuity-suppression"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-acuity-suppression.md`
```md
---
title: 'Auditory acuity suppression'
slug: "auditory-acuity-suppression"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory acuity suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-effects.fa.md`
```md
---
title: 'Auditory_effects'
slug: "auditory-effects"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-effects.md`
```md
---
title: 'Auditory_effects'
slug: "auditory-effects"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-hallucination.fa.md`
```md
---
title: 'Auditory hallucination'
slug: "auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-hallucination.md`
```md
---
title: 'Auditory hallucination'
slug: "auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-misinterpretation.fa.md`
```md
---
title: 'Auditory misinterpretation'
slug: "auditory-misinterpretation"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory misinterpretation

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\auditory-misinterpretation.md`
```md
---
title: 'Auditory misinterpretation'
slug: "auditory-misinterpretation"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Auditory misinterpretation

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\autonomous-voice-communication.fa.md`
```md
---
title: 'Autonomous voice communication'
slug: "autonomous-voice-communication"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous voice communication

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\autonomous-voice-communication.md`
```md
---
title: 'Autonomous voice communication'
slug: "autonomous-voice-communication"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous voice communication

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\external-auditory-hallucination.fa.md`
```md
---
title: 'External auditory hallucination'
slug: "external-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External auditory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\external-auditory-hallucination.md`
```md
---
title: 'External auditory hallucination'
slug: "external-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External auditory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\internal-auditory-hallucination.fa.md`
```md
---
title: 'Internal auditory hallucination'
slug: "internal-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal auditory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\internal-auditory-hallucination.md`
```md
---
title: 'Internal auditory hallucination'
slug: "internal-auditory-hallucination"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal auditory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\temporal-scaling.fa.md`
```md
---
title: 'Temporal scaling'
slug: "temporal-scaling"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporal scaling

_Page coming soon._

```

---
### `src\wiki\Effects\Auditory_effects\temporal-scaling.md`
```md
---
title: 'Temporal scaling'
slug: "temporal-scaling"
lang: "en"
category: 'Auditory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporal scaling

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\addiction-suppression.fa.md`
```md
---
title: 'Addiction suppression'
slug: "addiction-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Addiction suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\addiction-suppression.md`
```md
---
title: 'Addiction suppression'
slug: "addiction-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Addiction suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\amnesia.fa.md`
```md
---
title: 'Amnesia'
slug: "amnesia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amnesia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\amnesia.md`
```md
---
title: 'Amnesia'
slug: "amnesia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amnesia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\analysis-depression.fa.md`
```md
---
title: 'Analysis depression'
slug: "analysis-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\analysis-depression.md`
```md
---
title: 'Analysis depression'
slug: "analysis-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\analysis-enhancement.fa.md`
```md
---
title: 'Analysis enhancement'
slug: "analysis-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\analysis-enhancement.md`
```md
---
title: 'Analysis enhancement'
slug: "analysis-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Analysis enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\anhedonia.fa.md`
```md
---
title: 'Anhedonia'
slug: "anhedonia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anhedonia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\anhedonia.md`
```md
---
title: 'Anhedonia'
slug: "anhedonia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anhedonia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\anxiety-suppression.fa.md`
```md
---
title: 'Anxiety suppression'
slug: "anxiety-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\anxiety-suppression.md`
```md
---
title: 'Anxiety suppression'
slug: "anxiety-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\anxiety.fa.md`
```md
---
title: 'Anxiety'
slug: "anxiety"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\anxiety.md`
```md
---
title: 'Anxiety'
slug: "anxiety"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anxiety

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\atemporality.fa.md`
```md
---
title: 'Atemporality'
slug: "atemporality"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Atemporality

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\atemporality.md`
```md
---
title: 'Atemporality'
slug: "atemporality"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Atemporality

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\catharsis.fa.md`
```md
---
title: 'Catharsis'
slug: "catharsis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Catharsis

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\catharsis.md`
```md
---
title: 'Catharsis'
slug: "catharsis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Catharsis

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-dysphoria.fa.md`
```md
---
title: 'Cognitive dysphoria'
slug: "cognitive-dysphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive dysphoria

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-dysphoria.md`
```md
---
title: 'Cognitive dysphoria'
slug: "cognitive-dysphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive dysphoria

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-effects.fa.md`
```md
---
title: 'Cognitive_effects'
slug: "cognitive-effects"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-effects.md`
```md
---
title: 'Cognitive_effects'
slug: "cognitive-effects"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-euphoria.fa.md`
```md
---
title: 'Cognitive euphoria'
slug: "cognitive-euphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive euphoria

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-euphoria.md`
```md
---
title: 'Cognitive euphoria'
slug: "cognitive-euphoria"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive euphoria

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-fatigue.fa.md`
```md
---
title: 'Cognitive fatigue'
slug: "cognitive-fatigue"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive fatigue

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\cognitive-fatigue.md`
```md
---
title: 'Cognitive fatigue'
slug: "cognitive-fatigue"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive fatigue

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\compulsive-redosing.fa.md`
```md
---
title: 'Compulsive redosing'
slug: "compulsive-redosing"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Compulsive redosing

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\compulsive-redosing.md`
```md
---
title: 'Compulsive redosing'
slug: "compulsive-redosing"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Compulsive redosing

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\conceptual-thinking.fa.md`
```md
---
title: 'Conceptual thinking'
slug: "conceptual-thinking"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Conceptual thinking

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\conceptual-thinking.md`
```md
---
title: 'Conceptual thinking'
slug: "conceptual-thinking"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Conceptual thinking

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\confusion.fa.md`
```md
---
title: 'Confusion'
slug: "confusion"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Confusion

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\confusion.md`
```md
---
title: 'Confusion'
slug: "confusion"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Confusion

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\creativity-depression.fa.md`
```md
---
title: 'Creativity depression'
slug: "creativity-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\creativity-depression.md`
```md
---
title: 'Creativity depression'
slug: "creativity-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\creativity-enhancement.fa.md`
```md
---
title: 'Creativity enhancement'
slug: "creativity-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\creativity-enhancement.md`
```md
---
title: 'Creativity enhancement'
slug: "creativity-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Creativity enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\delirium.fa.md`
```md
---
title: 'Delirium'
slug: "delirium"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delirium

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\delirium.md`
```md
---
title: 'Delirium'
slug: "delirium"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delirium

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\delusions.fa.md`
```md
---
title: 'Delusions'
slug: "delusions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delusions

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\delusions.md`
```md
---
title: 'Delusions'
slug: "delusions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Delusions

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depersonalization.fa.md`
```md
---
title: 'Depersonalization'
slug: "depersonalization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depersonalization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depersonalization.md`
```md
---
title: 'Depersonalization'
slug: "depersonalization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depersonalization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depression-reduction.fa.md`
```md
---
title: 'Depression reduction'
slug: "depression-reduction"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression reduction

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depression-reduction.md`
```md
---
title: 'Depression reduction'
slug: "depression-reduction"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression reduction

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depression.fa.md`
```md
---
title: 'Depression'
slug: "depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depression.md`
```md
---
title: 'Depression'
slug: "depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depressions.fa.md`
```md
---
title: 'Depressions'
slug: "depressions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depressions

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\depressions.md`
```md
---
title: 'Depressions'
slug: "depressions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Depressions

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\derealization.fa.md`
```md
---
title: 'Derealization'
slug: "derealization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Derealization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\derealization.md`
```md
---
title: 'Derealization'
slug: "derealization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Derealization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\disinhibition.fa.md`
```md
---
title: 'Disinhibition'
slug: "disinhibition"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disinhibition

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\disinhibition.md`
```md
---
title: 'Disinhibition'
slug: "disinhibition"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disinhibition

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\dream-potentiation.fa.md`
```md
---
title: 'Dream potentiation'
slug: "dream-potentiation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream potentiation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\dream-potentiation.md`
```md
---
title: 'Dream potentiation'
slug: "dream-potentiation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream potentiation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\dream-suppression.fa.md`
```md
---
title: 'Dream suppression'
slug: "dream-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\dream-suppression.md`
```md
---
title: 'Dream suppression'
slug: "dream-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dream suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\ego-dissolution.fa.md`
```md
---
title: 'Ego dissolution'
slug: "ego-dissolution"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego dissolution

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\ego-dissolution.md`
```md
---
title: 'Ego dissolution'
slug: "ego-dissolution"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego dissolution

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\ego-inflation.fa.md`
```md
---
title: 'Ego inflation'
slug: "ego-inflation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego inflation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\ego-inflation.md`
```md
---
title: 'Ego inflation'
slug: "ego-inflation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego inflation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\ego-replacement.fa.md`
```md
---
title: 'Ego replacement'
slug: "ego-replacement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego replacement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\ego-replacement.md`
```md
---
title: 'Ego replacement'
slug: "ego-replacement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Ego replacement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\emotion-intensification.fa.md`
```md
---
title: 'Emotion intensification'
slug: "emotion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\emotion-intensification.md`
```md
---
title: 'Emotion intensification'
slug: "emotion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\emotion-suppression.fa.md`
```md
---
title: 'Emotion suppression'
slug: "emotion-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\emotion-suppression.md`
```md
---
title: 'Emotion suppression'
slug: "emotion-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Emotion suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\empathy-affection-and-sociability-enhancement.fa.md`
```md
---
title: 'Empathy, affection, and sociability enhancement'
slug: "empathy-affection-and-sociability-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Empathy, affection, and sociability enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\empathy-affection-and-sociability-enhancement.md`
```md
---
title: 'Empathy, affection, and sociability enhancement'
slug: "empathy-affection-and-sociability-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Empathy, affection, and sociability enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\enhancements.fa.md`
```md
---
title: 'Enhancements'
slug: "enhancements"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Enhancements

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\enhancements.md`
```md
---
title: 'Enhancements'
slug: "enhancements"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Enhancements

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\euthymia.fa.md`
```md
---
title: 'Euthymia'
slug: "euthymia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Euthymia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\euthymia.md`
```md
---
title: 'Euthymia'
slug: "euthymia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Euthymia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\existential-self-realization.fa.md`
```md
---
title: 'Existential self-realization'
slug: "existential-self-realization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Existential self-realization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\existential-self-realization.md`
```md
---
title: 'Existential self-realization'
slug: "existential-self-realization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Existential self-realization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\feelings-of-impending-doom.fa.md`
```md
---
title: 'Feelings of impending doom'
slug: "feelings-of-impending-doom"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Feelings of impending doom

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\feelings-of-impending-doom.md`
```md
---
title: 'Feelings of impending doom'
slug: "feelings-of-impending-doom"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Feelings of impending doom

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\focus-intensification.fa.md`
```md
---
title: 'Focus intensification'
slug: "focus-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\focus-intensification.md`
```md
---
title: 'Focus intensification'
slug: "focus-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\focus-suppression.fa.md`
```md
---
title: 'Focus suppression'
slug: "focus-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\focus-suppression.md`
```md
---
title: 'Focus suppression'
slug: "focus-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Focus suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\glossolalia.fa.md`
```md
---
title: 'Glossolalia'
slug: "glossolalia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Glossolalia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\glossolalia.md`
```md
---
title: 'Glossolalia'
slug: "glossolalia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Glossolalia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\identity-alteration.fa.md`
```md
---
title: 'Identity alteration'
slug: "identity-alteration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Identity alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\identity-alteration.md`
```md
---
title: 'Identity alteration'
slug: "identity-alteration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Identity alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\immersion-intensification.fa.md`
```md
---
title: 'Immersion intensification'
slug: "immersion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Immersion intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\immersion-intensification.md`
```md
---
title: 'Immersion intensification'
slug: "immersion-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Immersion intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\increased-introspection.fa.md`
```md
---
title: 'Increased introspection'
slug: "increased-introspection"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased introspection

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\increased-introspection.md`
```md
---
title: 'Increased introspection'
slug: "increased-introspection"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased introspection

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\increased-music-appreciation.fa.md`
```md
---
title: 'Increased music appreciation'
slug: "increased-music-appreciation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased music appreciation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\increased-music-appreciation.md`
```md
---
title: 'Increased music appreciation'
slug: "increased-music-appreciation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased music appreciation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\increased-sense-of-humor.fa.md`
```md
---
title: 'Increased sense of humor'
slug: "increased-sense-of-humor"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased sense of humor

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\increased-sense-of-humor.md`
```md
---
title: 'Increased sense of humor'
slug: "increased-sense-of-humor"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased sense of humor

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\intensifications.fa.md`
```md
---
title: 'Intensifications'
slug: "intensifications"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Intensifications

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\intensifications.md`
```md
---
title: 'Intensifications'
slug: "intensifications"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Intensifications

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\irritability.fa.md`
```md
---
title: 'Irritability'
slug: "irritability"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Irritability

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\irritability.md`
```md
---
title: 'Irritability'
slug: "irritability"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Irritability

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\language-depression.fa.md`
```md
---
title: 'Language depression'
slug: "language-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Language depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\language-depression.md`
```md
---
title: 'Language depression'
slug: "language-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Language depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\mania.fa.md`
```md
---
title: 'Mania'
slug: "mania"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mania

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\mania.md`
```md
---
title: 'Mania'
slug: "mania"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mania

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\memory-enhancement.fa.md`
```md
---
title: 'Memory enhancement'
slug: "memory-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\memory-enhancement.md`
```md
---
title: 'Memory enhancement'
slug: "memory-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\memory-suppression.fa.md`
```md
---
title: 'Memory suppression'
slug: "memory-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\memory-suppression.md`
```md
---
title: 'Memory suppression'
slug: "memory-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\mindfulness.fa.md`
```md
---
title: 'Mindfulness'
slug: "mindfulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mindfulness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\mindfulness.md`
```md
---
title: 'Mindfulness'
slug: "mindfulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mindfulness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\motivation-depression.fa.md`
```md
---
title: 'Motivation depression'
slug: "motivation-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\motivation-depression.md`
```md
---
title: 'Motivation depression'
slug: "motivation-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\motivation-enhancement.fa.md`
```md
---
title: 'Motivation enhancement'
slug: "motivation-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\motivation-enhancement.md`
```md
---
title: 'Motivation enhancement'
slug: "motivation-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motivation enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\multiple-thought-streams.fa.md`
```md
---
title: 'Multiple thought streams'
slug: "multiple-thought-streams"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multiple thought streams

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\multiple-thought-streams.md`
```md
---
title: 'Multiple thought streams'
slug: "multiple-thought-streams"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multiple thought streams

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\no-umbrella-reviews-done-below-this-line.fa.md`
```md
---
title: 'No umbrella reviews done below this line'
slug: "no-umbrella-reviews-done-below-this-line"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# No umbrella reviews done below this line

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\no-umbrella-reviews-done-below-this-line.md`
```md
---
title: 'No umbrella reviews done below this line'
slug: "no-umbrella-reviews-done-below-this-line"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# No umbrella reviews done below this line

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\novel.fa.md`
```md
---
title: 'Novel'
slug: "novel"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novel

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\novel.md`
```md
---
title: 'Novel'
slug: "novel"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novel

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\novelty-enhancement.fa.md`
```md
---
title: 'Novelty enhancement'
slug: "novelty-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novelty enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\novelty-enhancement.md`
```md
---
title: 'Novelty enhancement'
slug: "novelty-enhancement"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Novelty enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\panic-attack.fa.md`
```md
---
title: 'Panic attack'
slug: "panic-attack"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Panic attack

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\panic-attack.md`
```md
---
title: 'Panic attack'
slug: "panic-attack"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Panic attack

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\paranoia.fa.md`
```md
---
title: 'Paranoia'
slug: "paranoia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Paranoia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\paranoia.md`
```md
---
title: 'Paranoia'
slug: "paranoia"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Paranoia

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perceived-exposure-to-inner-mechanics-of-consciousness.fa.md`
```md
---
title: 'Perceived exposure to inner mechanics of consciousness'
slug: "perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perceived-exposure-to-inner-mechanics-of-consciousness.md`
```md
---
title: 'Perceived exposure to inner mechanics of consciousness'
slug: "perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-eternalism.fa.md`
```md
---
title: 'Perception of eternalism'
slug: "perception-of-eternalism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of eternalism

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-eternalism.md`
```md
---
title: 'Perception of eternalism'
slug: "perception-of-eternalism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of eternalism

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-interdependent-opposites.fa.md`
```md
---
title: 'Perception of interdependent opposites'
slug: "perception-of-interdependent-opposites"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of interdependent opposites

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-interdependent-opposites.md`
```md
---
title: 'Perception of interdependent opposites'
slug: "perception-of-interdependent-opposites"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of interdependent opposites

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-predeterminism.fa.md`
```md
---
title: 'Perception of predeterminism'
slug: "perception-of-predeterminism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of predeterminism

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-predeterminism.md`
```md
---
title: 'Perception of predeterminism'
slug: "perception-of-predeterminism"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of predeterminism

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-self-design.fa.md`
```md
---
title: 'Perception of self-design'
slug: "perception-of-self-design"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of self-design

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\perception-of-self-design.md`
```md
---
title: 'Perception of self-design'
slug: "perception-of-self-design"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of self-design

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\personal-bias-suppression.fa.md`
```md
---
title: 'Personal bias suppression'
slug: "personal-bias-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal bias suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\personal-bias-suppression.md`
```md
---
title: 'Personal bias suppression'
slug: "personal-bias-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal bias suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\personal-meaning-intensification.fa.md`
```md
---
title: 'Personal meaning intensification'
slug: "personal-meaning-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal meaning intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\personal-meaning-intensification.md`
```md
---
title: 'Personal meaning intensification'
slug: "personal-meaning-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personal meaning intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\personality-regression.fa.md`
```md
---
title: 'Personality regression'
slug: "personality-regression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personality regression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\personality-regression.md`
```md
---
title: 'Personality regression'
slug: "personality-regression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Personality regression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\psychological.fa.md`
```md
---
title: 'Psychological'
slug: "psychological"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychological

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\psychological.md`
```md
---
title: 'Psychological'
slug: "psychological"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychological

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\psychosis.fa.md`
```md
---
title: 'Psychosis'
slug: "psychosis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychosis

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\psychosis.md`
```md
---
title: 'Psychosis'
slug: "psychosis"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Psychosis

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\rejuvenation.fa.md`
```md
---
title: 'Rejuvenation'
slug: "rejuvenation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Rejuvenation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\rejuvenation.md`
```md
---
title: 'Rejuvenation'
slug: "rejuvenation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Rejuvenation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\simultaneous-emotions.fa.md`
```md
---
title: 'Simultaneous emotions'
slug: "simultaneous-emotions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Simultaneous emotions

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\simultaneous-emotions.md`
```md
---
title: 'Simultaneous emotions'
slug: "simultaneous-emotions"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Simultaneous emotions

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\sleepiness.fa.md`
```md
---
title: 'Sleepiness'
slug: "sleepiness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sleepiness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\sleepiness.md`
```md
---
title: 'Sleepiness'
slug: "sleepiness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sleepiness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\sociability-depression.fa.md`
```md
---
title: 'Sociability depression'
slug: "sociability-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sociability depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\sociability-depression.md`
```md
---
title: 'Sociability depression'
slug: "sociability-depression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sociability depression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\spirituality-intensification.fa.md`
```md
---
title: 'Spirituality intensification'
slug: "spirituality-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spirituality intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\spirituality-intensification.md`
```md
---
title: 'Spirituality intensification'
slug: "spirituality-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spirituality intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\suggestibility-intensification.fa.md`
```md
---
title: 'Suggestibility intensification'
slug: "suggestibility-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\suggestibility-intensification.md`
```md
---
title: 'Suggestibility intensification'
slug: "suggestibility-intensification"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\suggestibility-suppression.fa.md`
```md
---
title: 'Suggestibility suppression'
slug: "suggestibility-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\suggestibility-suppression.md`
```md
---
title: 'Suggestibility suppression'
slug: "suggestibility-suppression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suggestibility suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\suicidal-ideation.fa.md`
```md
---
title: 'Suicidal ideation'
slug: "suicidal-ideation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suicidal ideation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\suicidal-ideation.md`
```md
---
title: 'Suicidal ideation'
slug: "suicidal-ideation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suicidal ideation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-acceleration.fa.md`
```md
---
title: 'Thought acceleration'
slug: "thought-acceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought acceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-acceleration.md`
```md
---
title: 'Thought acceleration'
slug: "thought-acceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought acceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-connectivity.fa.md`
```md
---
title: 'Thought connectivity'
slug: "thought-connectivity"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought connectivity

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-connectivity.md`
```md
---
title: 'Thought connectivity'
slug: "thought-connectivity"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought connectivity

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-deceleration.fa.md`
```md
---
title: 'Thought deceleration'
slug: "thought-deceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought deceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-deceleration.md`
```md
---
title: 'Thought deceleration'
slug: "thought-deceleration"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought deceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-disorganization.fa.md`
```md
---
title: 'Thought disorganization'
slug: "thought-disorganization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought disorganization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-disorganization.md`
```md
---
title: 'Thought disorganization'
slug: "thought-disorganization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought disorganization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-loop.fa.md`
```md
---
title: 'Thought loop'
slug: "thought-loop"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought loop

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-loop.md`
```md
---
title: 'Thought loop'
slug: "thought-loop"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought loop

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-organization.fa.md`
```md
---
title: 'Thought organization'
slug: "thought-organization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought organization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\thought-organization.md`
```md
---
title: 'Thought organization'
slug: "thought-organization"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Thought organization

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\time-compression.fa.md`
```md
---
title: 'Time compression'
slug: "time-compression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time compression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\time-compression.md`
```md
---
title: 'Time compression'
slug: "time-compression"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time compression

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\time-dilation.fa.md`
```md
---
title: 'Time dilation'
slug: "time-dilation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time dilation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\time-dilation.md`
```md
---
title: 'Time dilation'
slug: "time-dilation"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time dilation

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\time-reversal.fa.md`
```md
---
title: 'Time reversal'
slug: "time-reversal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time reversal

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\time-reversal.md`
```md
---
title: 'Time reversal'
slug: "time-reversal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Time reversal

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\transpersonal.fa.md`
```md
---
title: 'Transpersonal'
slug: "transpersonal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transpersonal

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\transpersonal.md`
```md
---
title: 'Transpersonal'
slug: "transpersonal"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transpersonal

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\unity-and-interconnectedness.fa.md`
```md
---
title: 'Unity and interconnectedness'
slug: "unity-and-interconnectedness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unity and interconnectedness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\unity-and-interconnectedness.md`
```md
---
title: 'Unity and interconnectedness'
slug: "unity-and-interconnectedness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unity and interconnectedness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\wakefulness.fa.md`
```md
---
title: 'Wakefulness'
slug: "wakefulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wakefulness

_Page coming soon._

```

---
### `src\wiki\Effects\Cognitive_effects\wakefulness.md`
```md
---
title: 'Wakefulness'
slug: "wakefulness"
lang: "en"
category: 'Cognitive_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wakefulness

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\cognitive-disconnection.fa.md`
```md
---
title: 'Cognitive disconnection'
slug: "cognitive-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive disconnection

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\cognitive-disconnection.md`
```md
---
title: 'Cognitive disconnection'
slug: "cognitive-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cognitive disconnection

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\detachment-plateaus.fa.md`
```md
---
title: 'Detachment plateaus'
slug: "detachment-plateaus"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Detachment plateaus

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\detachment-plateaus.md`
```md
---
title: 'Detachment plateaus'
slug: "detachment-plateaus"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Detachment plateaus

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\disconnective-effects.fa.md`
```md
---
title: 'Disconnective_effects'
slug: "disconnective-effects"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disconnective_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\disconnective-effects.md`
```md
---
title: 'Disconnective_effects'
slug: "disconnective-effects"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Disconnective_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\dj-vu.fa.md`
```md
---
title: 'Déjà vu'
slug: "dj-vu"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Déjà vu

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\dj-vu.md`
```md
---
title: 'Déjà vu'
slug: "dj-vu"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Déjà vu

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\holes-spaces-and-voids.fa.md`
```md
---
title: 'Holes, spaces and voids'
slug: "holes-spaces-and-voids"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Holes, spaces and voids

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\holes-spaces-and-voids.md`
```md
---
title: 'Holes, spaces and voids'
slug: "holes-spaces-and-voids"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Holes, spaces and voids

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\physical-disconnection.fa.md`
```md
---
title: 'Physical disconnection'
slug: "physical-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical disconnection

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\physical-disconnection.md`
```md
---
title: 'Physical disconnection'
slug: "physical-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical disconnection

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\structures.fa.md`
```md
---
title: 'Structures'
slug: "structures"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Structures

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\structures.md`
```md
---
title: 'Structures'
slug: "structures"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Structures

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\visual-disconnection.fa.md`
```md
---
title: 'Visual disconnection'
slug: "visual-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual disconnection

_Page coming soon._

```

---
### `src\wiki\Effects\Disconnective_effects\visual-disconnection.md`
```md
---
title: 'Visual disconnection'
slug: "visual-disconnection"
lang: "en"
category: 'Disconnective_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual disconnection

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-and-olfactory-effects.fa.md`
```md
---
title: 'Gustatory_and_olfactory_effects'
slug: "gustatory-and-olfactory-effects"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory_and_olfactory_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-and-olfactory-effects.md`
```md
---
title: 'Gustatory_and_olfactory_effects'
slug: "gustatory-and-olfactory-effects"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory_and_olfactory_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-depression.fa.md`
```md
---
title: 'Gustatory depression'
slug: "gustatory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory depression

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-depression.md`
```md
---
title: 'Gustatory depression'
slug: "gustatory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory depression

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-hallucination.fa.md`
```md
---
title: 'Gustatory hallucination'
slug: "gustatory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-hallucination.md`
```md
---
title: 'Gustatory hallucination'
slug: "gustatory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-intensification.fa.md`
```md
---
title: 'Gustatory intensification'
slug: "gustatory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\gustatory-intensification.md`
```md
---
title: 'Gustatory intensification'
slug: "gustatory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Gustatory intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\olfactory-depression.fa.md`
```md
---
title: 'Olfactory depression'
slug: "olfactory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory depression

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\olfactory-depression.md`
```md
---
title: 'Olfactory depression'
slug: "olfactory-depression"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory depression

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\olfactory-hallucination.fa.md`
```md
---
title: 'Olfactory hallucination'
slug: "olfactory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\olfactory-hallucination.md`
```md
---
title: 'Olfactory hallucination'
slug: "olfactory-hallucination"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\olfactory-intensification.fa.md`
```md
---
title: 'Olfactory intensification'
slug: "olfactory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Gustatory_and_olfactory_effects\olfactory-intensification.md`
```md
---
title: 'Olfactory intensification'
slug: "olfactory-intensification"
lang: "en"
category: 'Gustatory_and_olfactory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Olfactory intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\anticipatory-response.fa.md`
```md
---
title: 'Anticipatory response'
slug: "anticipatory-response"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anticipatory response

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\anticipatory-response.md`
```md
---
title: 'Anticipatory response'
slug: "anticipatory-response"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Anticipatory response

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\component-controllability.fa.md`
```md
---
title: 'Component controllability'
slug: "component-controllability"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Component controllability

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\component-controllability.md`
```md
---
title: 'Component controllability'
slug: "component-controllability"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Component controllability

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\dosage-independent-intensity.fa.md`
```md
---
title: 'Dosage independent intensity'
slug: "dosage-independent-intensity"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dosage independent intensity

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\dosage-independent-intensity.md`
```md
---
title: 'Dosage independent intensity'
slug: "dosage-independent-intensity"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dosage independent intensity

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\machinescapes.fa.md`
```md
---
title: 'Machinescapes'
slug: "machinescapes"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Machinescapes

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\machinescapes.md`
```md
---
title: 'Machinescapes'
slug: "machinescapes"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Machinescapes

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\memory-replays.fa.md`
```md
---
title: 'Memory replays'
slug: "memory-replays"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory replays

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\memory-replays.md`
```md
---
title: 'Memory replays'
slug: "memory-replays"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Memory replays

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\multisensory-effects.fa.md`
```md
---
title: 'Multisensory_effects'
slug: "multisensory-effects"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multisensory_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\multisensory-effects.md`
```md
---
title: 'Multisensory_effects'
slug: "multisensory-effects"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Multisensory_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\scenarios-and-plots.fa.md`
```md
---
title: 'Scenarios and plots'
slug: "scenarios-and-plots"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenarios and plots

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\scenarios-and-plots.md`
```md
---
title: 'Scenarios and plots'
slug: "scenarios-and-plots"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenarios and plots

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\spatial-disorientation.fa.md`
```md
---
title: 'Spatial disorientation'
slug: "spatial-disorientation"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spatial disorientation

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\spatial-disorientation.md`
```md
---
title: 'Spatial disorientation'
slug: "spatial-disorientation"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spatial disorientation

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\spontaneous-physical-movements.fa.md`
```md
---
title: 'Spontaneous physical movements'
slug: "spontaneous-physical-movements"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous physical movements

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\spontaneous-physical-movements.md`
```md
---
title: 'Spontaneous physical movements'
slug: "spontaneous-physical-movements"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous physical movements

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\synaesthesia.fa.md`
```md
---
title: 'Synaesthesia'
slug: "synaesthesia"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Synaesthesia

_Page coming soon._

```

---
### `src\wiki\Effects\Multisensory_effects\synaesthesia.md`
```md
---
title: 'Synaesthesia'
slug: "synaesthesia"
lang: "en"
category: 'Multisensory_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Synaesthesia

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\alterations.fa.md`
```md
---
title: 'Alterations'
slug: "alterations"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Alterations

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\alterations.md`
```md
---
title: 'Alterations'
slug: "alterations"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Alterations

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\amplifications.fa.md`
```md
---
title: 'Amplifications'
slug: "amplifications"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amplifications

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\amplifications.md`
```md
---
title: 'Amplifications'
slug: "amplifications"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Amplifications

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\appetite-intensification.fa.md`
```md
---
title: 'Appetite intensification'
slug: "appetite-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\appetite-intensification.md`
```md
---
title: 'Appetite intensification'
slug: "appetite-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\appetite-suppression.fa.md`
```md
---
title: 'Appetite suppression'
slug: "appetite-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\appetite-suppression.md`
```md
---
title: 'Appetite suppression'
slug: "appetite-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Appetite suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\bodily-control-enhancement.fa.md`
```md
---
title: 'Bodily control enhancement'
slug: "bodily-control-enhancement"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily control enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\bodily-control-enhancement.md`
```md
---
title: 'Bodily control enhancement'
slug: "bodily-control-enhancement"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily control enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\body-odor-alteration.fa.md`
```md
---
title: 'Body odor alteration'
slug: "body-odor-alteration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Body odor alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\body-odor-alteration.md`
```md
---
title: 'Body odor alteration'
slug: "body-odor-alteration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Body odor alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\bronchodilation.fa.md`
```md
---
title: 'Bronchodilation'
slug: "bronchodilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bronchodilation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\bronchodilation.md`
```md
---
title: 'Bronchodilation'
slug: "bronchodilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bronchodilation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\changes-in-felt-bodily-form.fa.md`
```md
---
title: 'Changes in felt bodily form'
slug: "changes-in-felt-bodily-form"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt bodily form

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\changes-in-felt-bodily-form.md`
```md
---
title: 'Changes in felt bodily form'
slug: "changes-in-felt-bodily-form"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt bodily form

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\changes-in-felt-gravity.fa.md`
```md
---
title: 'Changes in felt gravity'
slug: "changes-in-felt-gravity"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt gravity

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\changes-in-felt-gravity.md`
```md
---
title: 'Changes in felt gravity'
slug: "changes-in-felt-gravity"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Changes in felt gravity

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\cough-suppression.fa.md`
```md
---
title: 'Cough suppression'
slug: "cough-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cough suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\cough-suppression.md`
```md
---
title: 'Cough suppression'
slug: "cough-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cough suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\decreased-libido.fa.md`
```md
---
title: 'Decreased libido'
slug: "decreased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased libido

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\decreased-libido.md`
```md
---
title: 'Decreased libido'
slug: "decreased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased libido

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\excessive-yawning.fa.md`
```md
---
title: 'Excessive yawning'
slug: "excessive-yawning"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Excessive yawning

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\excessive-yawning.md`
```md
---
title: 'Excessive yawning'
slug: "excessive-yawning"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Excessive yawning

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\increased-libido.fa.md`
```md
---
title: 'Increased libido'
slug: "increased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased libido

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\increased-libido.md`
```md
---
title: 'Increased libido'
slug: "increased-libido"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased libido

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\increased-respiration.fa.md`
```md
---
title: 'Increased respiration'
slug: "increased-respiration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased respiration

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\increased-respiration.md`
```md
---
title: 'Increased respiration'
slug: "increased-respiration"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased respiration

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\increased-salivation.fa.md`
```md
---
title: 'Increased salivation'
slug: "increased-salivation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased salivation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\increased-salivation.md`
```md
---
title: 'Increased salivation'
slug: "increased-salivation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased salivation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\laughter-fits.fa.md`
```md
---
title: 'Laughter fits'
slug: "laughter-fits"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Laughter fits

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\laughter-fits.md`
```md
---
title: 'Laughter fits'
slug: "laughter-fits"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Laughter fits

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\motor-control-loss.fa.md`
```md
---
title: 'Motor control loss'
slug: "motor-control-loss"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motor control loss

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\motor-control-loss.md`
```md
---
title: 'Motor control loss'
slug: "motor-control-loss"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Motor control loss

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\mouth-numbing.fa.md`
```md
---
title: 'Mouth numbing'
slug: "mouth-numbing"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mouth numbing

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\mouth-numbing.md`
```md
---
title: 'Mouth numbing'
slug: "mouth-numbing"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Mouth numbing

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\muscle-relaxation.fa.md`
```md
---
title: 'Muscle relaxation'
slug: "muscle-relaxation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle relaxation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\muscle-relaxation.md`
```md
---
title: 'Muscle relaxation'
slug: "muscle-relaxation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle relaxation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\nausea-suppression.fa.md`
```md
---
title: 'Nausea suppression'
slug: "nausea-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\nausea-suppression.md`
```md
---
title: 'Nausea suppression'
slug: "nausea-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\orgasm-depression.fa.md`
```md
---
title: 'Orgasm depression'
slug: "orgasm-depression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Orgasm depression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\orgasm-depression.md`
```md
---
title: 'Orgasm depression'
slug: "orgasm-depression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Orgasm depression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\pain-relief.fa.md`
```md
---
title: 'Pain relief'
slug: "pain-relief"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pain relief

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\pain-relief.md`
```md
---
title: 'Pain relief'
slug: "pain-relief"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pain relief

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\perception-of-bodily-heaviness.fa.md`
```md
---
title: 'Perception of bodily heaviness'
slug: "perception-of-bodily-heaviness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily heaviness

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\perception-of-bodily-heaviness.md`
```md
---
title: 'Perception of bodily heaviness'
slug: "perception-of-bodily-heaviness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily heaviness

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\perception-of-bodily-lightness.fa.md`
```md
---
title: 'Perception of bodily lightness'
slug: "perception-of-bodily-lightness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily lightness

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\perception-of-bodily-lightness.md`
```md
---
title: 'Perception of bodily lightness'
slug: "perception-of-bodily-lightness"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perception of bodily lightness

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\physical-autonomy.fa.md`
```md
---
title: 'Physical autonomy'
slug: "physical-autonomy"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical autonomy

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\physical-autonomy.md`
```md
---
title: 'Physical autonomy'
slug: "physical-autonomy"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical autonomy

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\physical-effects.fa.md`
```md
---
title: 'Physical_effects'
slug: "physical-effects"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\physical-effects.md`
```md
---
title: 'Physical_effects'
slug: "physical-effects"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\physical-euphoria.fa.md`
```md
---
title: 'Physical euphoria'
slug: "physical-euphoria"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical euphoria

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\physical-euphoria.md`
```md
---
title: 'Physical euphoria'
slug: "physical-euphoria"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical euphoria

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\pupil-constriction.fa.md`
```md
---
title: 'Pupil constriction'
slug: "pupil-constriction"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil constriction

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\pupil-constriction.md`
```md
---
title: 'Pupil constriction'
slug: "pupil-constriction"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil constriction

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\pupil-dilation.fa.md`
```md
---
title: 'Pupil dilation'
slug: "pupil-dilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil dilation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\pupil-dilation.md`
```md
---
title: 'Pupil dilation'
slug: "pupil-dilation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pupil dilation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\sedation.fa.md`
```md
---
title: 'Sedation'
slug: "sedation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sedation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\sedation.md`
```md
---
title: 'Sedation'
slug: "sedation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Sedation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\seizure-suppression.fa.md`
```md
---
title: 'Seizure suppression'
slug: "seizure-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\seizure-suppression.md`
```md
---
title: 'Seizure suppression'
slug: "seizure-suppression"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\stamina-intensification.fa.md`
```md
---
title: 'Stamina intensification'
slug: "stamina-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stamina intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\stamina-intensification.md`
```md
---
title: 'Stamina intensification'
slug: "stamina-intensification"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stamina intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\stimulation.fa.md`
```md
---
title: 'Stimulation'
slug: "stimulation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\stimulation.md`
```md
---
title: 'Stimulation'
slug: "stimulation"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stimulation

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\suppressions.fa.md`
```md
---
title: 'Suppressions'
slug: "suppressions"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suppressions

_Page coming soon._

```

---
### `src\wiki\Effects\Physical_effects\suppressions.md`
```md
---
title: 'Suppressions'
slug: "suppressions"
lang: "en"
category: 'Physical_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Suppressions

_Page coming soon._

```

---
### `src\wiki\Effects\Smell & taste effects\smell-and-taste-effects.fa.md`
```md
---
title: 'Smell & taste effects'
slug: "smell-and-taste-effects"
lang: "en"
category: 'Smell & taste effects'
weight: 1000
template: "wiki"
summary: ''
---

# Smell & taste effects

_Page coming soon._

```

---
### `src\wiki\Effects\Smell & taste effects\smell-and-taste-effects.md`
```md
---
title: 'Smell & taste effects'
slug: "smell-and-taste-effects"
lang: "en"
category: 'Smell & taste effects'
weight: 1000
template: "wiki"
summary: ''
---

# Smell & taste effects

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\spontaneous-bodily-sensations.fa.md`
```md
---
title: 'Spontaneous bodily sensations'
slug: "spontaneous-bodily-sensations"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous bodily sensations

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\spontaneous-bodily-sensations.md`
```md
---
title: 'Spontaneous bodily sensations'
slug: "spontaneous-bodily-sensations"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Spontaneous bodily sensations

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-effects.fa.md`
```md
---
title: 'Tactile_effects'
slug: "tactile-effects"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-effects.md`
```md
---
title: 'Tactile_effects'
slug: "tactile-effects"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-hallucination.fa.md`
```md
---
title: 'Tactile hallucination'
slug: "tactile-hallucination"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-hallucination.md`
```md
---
title: 'Tactile hallucination'
slug: "tactile-hallucination"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-intensification.fa.md`
```md
---
title: 'Tactile intensification'
slug: "tactile-intensification"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-intensification.md`
```md
---
title: 'Tactile intensification'
slug: "tactile-intensification"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile intensification

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-suppression.fa.md`
```md
---
title: 'Tactile suppression'
slug: "tactile-suppression"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Tactile_effects\tactile-suppression.md`
```md
---
title: 'Tactile suppression'
slug: "tactile-suppression"
lang: "en"
category: 'Tactile_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tactile suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\abnormal-heartbeat.fa.md`
```md
---
title: 'Abnormal heartbeat'
slug: "abnormal-heartbeat"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Abnormal heartbeat

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\abnormal-heartbeat.md`
```md
---
title: 'Abnormal heartbeat'
slug: "abnormal-heartbeat"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Abnormal heartbeat

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\back-pain.fa.md`
```md
---
title: 'Back pain'
slug: "back-pain"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Back pain

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\back-pain.md`
```md
---
title: 'Back pain'
slug: "back-pain"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Back pain

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\bodily-pressures.fa.md`
```md
---
title: 'Bodily pressures'
slug: "bodily-pressures"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily pressures

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\bodily-pressures.md`
```md
---
title: 'Bodily pressures'
slug: "bodily-pressures"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily pressures

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\bodily.fa.md`
```md
---
title: 'Bodily'
slug: "bodily"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\bodily.md`
```md
---
title: 'Bodily'
slug: "bodily"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Bodily

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\brain-zaps.fa.md`
```md
---
title: 'Brain zaps'
slug: "brain-zaps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brain zaps

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\brain-zaps.md`
```md
---
title: 'Brain zaps'
slug: "brain-zaps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brain zaps

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\cardiovascular.fa.md`
```md
---
title: 'Cardiovascular'
slug: "cardiovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cardiovascular

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\cardiovascular.md`
```md
---
title: 'Cardiovascular'
slug: "cardiovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cardiovascular

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\cerebrovascular.fa.md`
```md
---
title: 'Cerebrovascular'
slug: "cerebrovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cerebrovascular

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\cerebrovascular.md`
```md
---
title: 'Cerebrovascular'
slug: "cerebrovascular"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Cerebrovascular

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\constipation.fa.md`
```md
---
title: 'Constipation'
slug: "constipation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Constipation

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\constipation.md`
```md
---
title: 'Constipation'
slug: "constipation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Constipation

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\decreased-blood-pressure.fa.md`
```md
---
title: 'Decreased blood pressure'
slug: "decreased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased blood pressure

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\decreased-blood-pressure.md`
```md
---
title: 'Decreased blood pressure'
slug: "decreased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased blood pressure

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\decreased-heart-rate.fa.md`
```md
---
title: 'Decreased heart rate'
slug: "decreased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased heart rate

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\decreased-heart-rate.md`
```md
---
title: 'Decreased heart rate'
slug: "decreased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Decreased heart rate

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\dehydration.fa.md`
```md
---
title: 'Dehydration'
slug: "dehydration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dehydration

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\dehydration.md`
```md
---
title: 'Dehydration'
slug: "dehydration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dehydration

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\diarrhea.fa.md`
```md
---
title: 'Diarrhea'
slug: "diarrhea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diarrhea

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\diarrhea.md`
```md
---
title: 'Diarrhea'
slug: "diarrhea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diarrhea

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\difficulty-urinating.fa.md`
```md
---
title: 'Difficulty urinating'
slug: "difficulty-urinating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Difficulty urinating

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\difficulty-urinating.md`
```md
---
title: 'Difficulty urinating'
slug: "difficulty-urinating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Difficulty urinating

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\dizziness.fa.md`
```md
---
title: 'Dizziness'
slug: "dizziness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dizziness

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\dizziness.md`
```md
---
title: 'Dizziness'
slug: "dizziness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dizziness

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\dry-mouth.fa.md`
```md
---
title: 'Dry mouth'
slug: "dry-mouth"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dry mouth

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\dry-mouth.md`
```md
---
title: 'Dry mouth'
slug: "dry-mouth"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Dry mouth

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\frequent-urination.fa.md`
```md
---
title: 'Frequent urination'
slug: "frequent-urination"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Frequent urination

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\frequent-urination.md`
```md
---
title: 'Frequent urination'
slug: "frequent-urination"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Frequent urination

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\headache.fa.md`
```md
---
title: 'Headache'
slug: "headache"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Headache

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\headache.md`
```md
---
title: 'Headache'
slug: "headache"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Headache

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-blood-pressure.fa.md`
```md
---
title: 'Increased blood pressure'
slug: "increased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased blood pressure

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-blood-pressure.md`
```md
---
title: 'Increased blood pressure'
slug: "increased-blood-pressure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased blood pressure

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-bodily-temperature.fa.md`
```md
---
title: 'Increased bodily temperature'
slug: "increased-bodily-temperature"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased bodily temperature

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-bodily-temperature.md`
```md
---
title: 'Increased bodily temperature'
slug: "increased-bodily-temperature"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased bodily temperature

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-heart-rate.fa.md`
```md
---
title: 'Increased heart rate'
slug: "increased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased heart rate

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-heart-rate.md`
```md
---
title: 'Increased heart rate'
slug: "increased-heart-rate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased heart rate

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-perspiration.fa.md`
```md
---
title: 'Increased perspiration'
slug: "increased-perspiration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased perspiration

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-perspiration.md`
```md
---
title: 'Increased perspiration'
slug: "increased-perspiration"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased perspiration

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-phlegm-production.fa.md`
```md
---
title: 'Increased phlegm production'
slug: "increased-phlegm-production"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased phlegm production

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\increased-phlegm-production.md`
```md
---
title: 'Increased phlegm production'
slug: "increased-phlegm-production"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Increased phlegm production

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\itchiness.fa.md`
```md
---
title: 'Itchiness'
slug: "itchiness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Itchiness

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\itchiness.md`
```md
---
title: 'Itchiness'
slug: "itchiness"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Itchiness

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-contractions.fa.md`
```md
---
title: 'Muscle contractions'
slug: "muscle-contractions"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle contractions

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-contractions.md`
```md
---
title: 'Muscle contractions'
slug: "muscle-contractions"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle contractions

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-cramps.fa.md`
```md
---
title: 'Muscle cramps'
slug: "muscle-cramps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle cramps

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-cramps.md`
```md
---
title: 'Muscle cramps'
slug: "muscle-cramps"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle cramps

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-tension.fa.md`
```md
---
title: 'Muscle tension'
slug: "muscle-tension"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle tension

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-tension.md`
```md
---
title: 'Muscle tension'
slug: "muscle-tension"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle tension

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-twitching.fa.md`
```md
---
title: 'Muscle twitching'
slug: "muscle-twitching"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle twitching

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\muscle-twitching.md`
```md
---
title: 'Muscle twitching'
slug: "muscle-twitching"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Muscle twitching

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\nausea.fa.md`
```md
---
title: 'Nausea'
slug: "nausea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\nausea.md`
```md
---
title: 'Nausea'
slug: "nausea"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Nausea

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\optical-sliding.fa.md`
```md
---
title: 'Optical sliding'
slug: "optical-sliding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Optical sliding

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\optical-sliding.md`
```md
---
title: 'Optical sliding'
slug: "optical-sliding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Optical sliding

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\photophobia.fa.md`
```md
---
title: 'Photophobia'
slug: "photophobia"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Photophobia

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\photophobia.md`
```md
---
title: 'Photophobia'
slug: "photophobia"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Photophobia

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\physical-fatigue.fa.md`
```md
---
title: 'Physical fatigue'
slug: "physical-fatigue"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical fatigue

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\physical-fatigue.md`
```md
---
title: 'Physical fatigue'
slug: "physical-fatigue"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Physical fatigue

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\respiratory-depression.fa.md`
```md
---
title: 'Respiratory depression'
slug: "respiratory-depression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Respiratory depression

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\respiratory-depression.md`
```md
---
title: 'Respiratory depression'
slug: "respiratory-depression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Respiratory depression

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\restless-legs.fa.md`
```md
---
title: 'Restless legs'
slug: "restless-legs"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Restless legs

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\restless-legs.md`
```md
---
title: 'Restless legs'
slug: "restless-legs"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Restless legs

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\runny-nose.fa.md`
```md
---
title: 'Runny nose'
slug: "runny-nose"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Runny nose

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\runny-nose.md`
```md
---
title: 'Runny nose'
slug: "runny-nose"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Runny nose

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\seizure.fa.md`
```md
---
title: 'Seizure'
slug: "seizure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\seizure.md`
```md
---
title: 'Seizure'
slug: "seizure"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Seizure

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\skin-flushing.fa.md`
```md
---
title: 'Skin flushing'
slug: "skin-flushing"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Skin flushing

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\skin-flushing.md`
```md
---
title: 'Skin flushing'
slug: "skin-flushing"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Skin flushing

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\stomach-bloating.fa.md`
```md
---
title: 'Stomach bloating'
slug: "stomach-bloating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach bloating

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\stomach-bloating.md`
```md
---
title: 'Stomach bloating'
slug: "stomach-bloating"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach bloating

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\stomach-cramp.fa.md`
```md
---
title: 'Stomach cramp'
slug: "stomach-cramp"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach cramp

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\stomach-cramp.md`
```md
---
title: 'Stomach cramp'
slug: "stomach-cramp"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Stomach cramp

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\teeth-grinding.fa.md`
```md
---
title: 'Teeth grinding'
slug: "teeth-grinding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Teeth grinding

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\teeth-grinding.md`
```md
---
title: 'Teeth grinding'
slug: "teeth-grinding"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Teeth grinding

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\temperature-regulation-suppression.fa.md`
```md
---
title: 'Temperature regulation suppression'
slug: "temperature-regulation-suppression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temperature regulation suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\temperature-regulation-suppression.md`
```md
---
title: 'Temperature regulation suppression'
slug: "temperature-regulation-suppression"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temperature regulation suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\temporary-erectile-dysfunction.fa.md`
```md
---
title: 'Temporary erectile dysfunction'
slug: "temporary-erectile-dysfunction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporary erectile dysfunction

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\temporary-erectile-dysfunction.md`
```md
---
title: 'Temporary erectile dysfunction'
slug: "temporary-erectile-dysfunction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Temporary erectile dysfunction

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\uncomfortable-physical-effects.fa.md`
```md
---
title: 'Uncomfortable physical effects'
slug: "uncomfortable-physical-effects"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Uncomfortable physical effects

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\uncomfortable-physical-effects.md`
```md
---
title: 'Uncomfortable physical effects'
slug: "uncomfortable-physical-effects"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Uncomfortable physical effects

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vasoconstriction.fa.md`
```md
---
title: 'Vasoconstriction'
slug: "vasoconstriction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasoconstriction

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vasoconstriction.md`
```md
---
title: 'Vasoconstriction'
slug: "vasoconstriction"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasoconstriction

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vasodilation.fa.md`
```md
---
title: 'Vasodilation'
slug: "vasodilation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasodilation

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vasodilation.md`
```md
---
title: 'Vasodilation'
slug: "vasodilation"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vasodilation

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vibrating-vision.fa.md`
```md
---
title: 'Vibrating vision'
slug: "vibrating-vision"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vibrating vision

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vibrating-vision.md`
```md
---
title: 'Vibrating vision'
slug: "vibrating-vision"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vibrating vision

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vomiting.fa.md`
```md
---
title: 'Vomiting'
slug: "vomiting"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vomiting

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\vomiting.md`
```md
---
title: 'Vomiting'
slug: "vomiting"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Vomiting

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\wate.fa.md`
```md
---
title: 'Wate'
slug: "wate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wate

_Page coming soon._

```

---
### `src\wiki\Effects\Uncomfortable physical effects\wate.md`
```md
---
title: 'Wate'
slug: "wate"
lang: "en"
category: 'Uncomfortable physical effects'
weight: 1000
template: "wiki"
summary: ''
---

# Wate

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\8a-perceived-exposure-to-semantic-concept-network.fa.md`
```md
---
title: '8A - Perceived exposure to semantic concept network'
slug: "8a-perceived-exposure-to-semantic-concept-network"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8A - Perceived exposure to semantic concept network

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\8a-perceived-exposure-to-semantic-concept-network.md`
```md
---
title: '8A - Perceived exposure to semantic concept network'
slug: "8a-perceived-exposure-to-semantic-concept-network"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8A - Perceived exposure to semantic concept network

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\8b-perceived-exposure-to-inner-mechanics-of-consciousness.fa.md`
```md
---
title: '8B - Perceived exposure to inner mechanics of consciousness'
slug: "8b-perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8B - Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\8b-perceived-exposure-to-inner-mechanics-of-consciousness.md`
```md
---
title: '8B - Perceived exposure to inner mechanics of consciousness'
slug: "8b-perceived-exposure-to-inner-mechanics-of-consciousness"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# 8B - Perceived exposure to inner mechanics of consciousness

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\after-images.fa.md`
```md
---
title: 'After images'
slug: "after-images"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# After images

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\after-images.md`
```md
---
title: 'After images'
slug: "after-images"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# After images

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\autonomous-entity.fa.md`
```md
---
title: 'Autonomous entity'
slug: "autonomous-entity"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous entity

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\autonomous-entity.md`
```md
---
title: 'Autonomous entity'
slug: "autonomous-entity"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Autonomous entity

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\breathing.fa.md`
```md
---
title: 'Breathing'
slug: "breathing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Breathing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\breathing.md`
```md
---
title: 'Breathing'
slug: "breathing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Breathing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\brightness-alteration.fa.md`
```md
---
title: 'Brightness alteration'
slug: "brightness-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brightness alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\brightness-alteration.md`
```md
---
title: 'Brightness alteration'
slug: "brightness-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Brightness alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-depression.fa.md`
```md
---
title: 'Color depression'
slug: "color-depression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color depression

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-depression.md`
```md
---
title: 'Color depression'
slug: "color-depression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color depression

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-enhancement.fa.md`
```md
---
title: 'Color enhancement'
slug: "color-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-enhancement.md`
```md
---
title: 'Color enhancement'
slug: "color-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-replacement.fa.md`
```md
---
title: 'Color replacement'
slug: "color-replacement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color replacement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-replacement.md`
```md
---
title: 'Color replacement'
slug: "color-replacement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color replacement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-shifting.fa.md`
```md
---
title: 'Color shifting'
slug: "color-shifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color shifting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-shifting.md`
```md
---
title: 'Color shifting'
slug: "color-shifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color shifting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-tinting.fa.md`
```md
---
title: 'Color tinting'
slug: "color-tinting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color tinting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\color-tinting.md`
```md
---
title: 'Color tinting'
slug: "color-tinting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Color tinting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\diffraction.fa.md`
```md
---
title: 'Diffraction'
slug: "diffraction"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diffraction

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\diffraction.md`
```md
---
title: 'Diffraction'
slug: "diffraction"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Diffraction

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\double-vision.fa.md`
```md
---
title: 'Double vision'
slug: "double-vision"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Double vision

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\double-vision.md`
```md
---
title: 'Double vision'
slug: "double-vision"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Double vision

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\drifting.fa.md`
```md
---
title: 'Drifting'
slug: "drifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Drifting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\drifting.md`
```md
---
title: 'Drifting'
slug: "drifting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Drifting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\environmental-cubism.fa.md`
```md
---
title: 'Environmental cubism'
slug: "environmental-cubism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental cubism

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\environmental-cubism.md`
```md
---
title: 'Environmental cubism'
slug: "environmental-cubism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental cubism

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\environmental-orbism.fa.md`
```md
---
title: 'Environmental orbism'
slug: "environmental-orbism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental orbism

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\environmental-orbism.md`
```md
---
title: 'Environmental orbism'
slug: "environmental-orbism"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental orbism

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\environmental-patterning.fa.md`
```md
---
title: 'Environmental patterning'
slug: "environmental-patterning"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental patterning

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\environmental-patterning.md`
```md
---
title: 'Environmental patterning'
slug: "environmental-patterning"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Environmental patterning

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\external-hallucination.fa.md`
```md
---
title: 'External hallucination'
slug: "external-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\external-hallucination.md`
```md
---
title: 'External hallucination'
slug: "external-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# External hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\flowing.fa.md`
```md
---
title: 'Flowing'
slug: "flowing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Flowing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\flowing.md`
```md
---
title: 'Flowing'
slug: "flowing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Flowing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\geometry.fa.md`
```md
---
title: 'Geometry'
slug: "geometry"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Geometry

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\geometry.md`
```md
---
title: 'Geometry'
slug: "geometry"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Geometry

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\hallucinatory-states.fa.md`
```md
---
title: 'Hallucinatory states'
slug: "hallucinatory-states"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Hallucinatory states

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\hallucinatory-states.md`
```md
---
title: 'Hallucinatory states'
slug: "hallucinatory-states"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Hallucinatory states

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\internal-hallucination.fa.md`
```md
---
title: 'Internal hallucination'
slug: "internal-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\internal-hallucination.md`
```md
---
title: 'Internal hallucination'
slug: "internal-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Internal hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\magnification.fa.md`
```md
---
title: 'Magnification'
slug: "magnification"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Magnification

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\magnification.md`
```md
---
title: 'Magnification'
slug: "magnification"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Magnification

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\melting.fa.md`
```md
---
title: 'Melting'
slug: "melting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Melting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\melting.md`
```md
---
title: 'Melting'
slug: "melting"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Melting

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\morphing.fa.md`
```md
---
title: 'Morphing'
slug: "morphing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Morphing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\morphing.md`
```md
---
title: 'Morphing'
slug: "morphing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Morphing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\object-activation.fa.md`
```md
---
title: 'Object activation'
slug: "object-activation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object activation

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\object-activation.md`
```md
---
title: 'Object activation'
slug: "object-activation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object activation

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\object-alteration.fa.md`
```md
---
title: 'Object alteration'
slug: "object-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\object-alteration.md`
```md
---
title: 'Object alteration'
slug: "object-alteration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Object alteration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\pattern-recognition-enhancement.fa.md`
```md
---
title: 'Pattern recognition enhancement'
slug: "pattern-recognition-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\pattern-recognition-enhancement.md`
```md
---
title: 'Pattern recognition enhancement'
slug: "pattern-recognition-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\pattern-recognition-suppression.fa.md`
```md
---
title: 'Pattern recognition suppression'
slug: "pattern-recognition-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\pattern-recognition-suppression.md`
```md
---
title: 'Pattern recognition suppression'
slug: "pattern-recognition-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Pattern recognition suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\peripheral-information-misinterpretation.fa.md`
```md
---
title: 'Peripheral information misinterpretation'
slug: "peripheral-information-misinterpretation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Peripheral information misinterpretation

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\peripheral-information-misinterpretation.md`
```md
---
title: 'Peripheral information misinterpretation'
slug: "peripheral-information-misinterpretation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Peripheral information misinterpretation

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\perspective-hallucination.fa.md`
```md
---
title: 'Perspective hallucination'
slug: "perspective-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perspective hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\perspective-hallucination.md`
```md
---
title: 'Perspective hallucination'
slug: "perspective-hallucination"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Perspective hallucination

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\recursion.fa.md`
```md
---
title: 'Recursion'
slug: "recursion"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Recursion

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\recursion.md`
```md
---
title: 'Recursion'
slug: "recursion"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Recursion

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\scenery-slicing.fa.md`
```md
---
title: 'Scenery slicing'
slug: "scenery-slicing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenery slicing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\scenery-slicing.md`
```md
---
title: 'Scenery slicing'
slug: "scenery-slicing"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Scenery slicing

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\settings-sceneries-and-landscapes.fa.md`
```md
---
title: 'Settings, sceneries, and landscapes'
slug: "settings-sceneries-and-landscapes"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Settings, sceneries, and landscapes

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\settings-sceneries-and-landscapes.md`
```md
---
title: 'Settings, sceneries, and landscapes'
slug: "settings-sceneries-and-landscapes"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Settings, sceneries, and landscapes

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\shadow-people.fa.md`
```md
---
title: 'Shadow people'
slug: "shadow-people"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Shadow people

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\shadow-people.md`
```md
---
title: 'Shadow people'
slug: "shadow-people"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Shadow people

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\symmetrical-texture-repetition.fa.md`
```md
---
title: 'Symmetrical texture repetition'
slug: "symmetrical-texture-repetition"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Symmetrical texture repetition

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\symmetrical-texture-repetition.md`
```md
---
title: 'Symmetrical texture repetition'
slug: "symmetrical-texture-repetition"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Symmetrical texture repetition

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\texture-liquidation.fa.md`
```md
---
title: 'Texture liquidation'
slug: "texture-liquidation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Texture liquidation

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\texture-liquidation.md`
```md
---
title: 'Texture liquidation'
slug: "texture-liquidation"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Texture liquidation

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\tracers.fa.md`
```md
---
title: 'Tracers'
slug: "tracers"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tracers

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\tracers.md`
```md
---
title: 'Tracers'
slug: "tracers"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Tracers

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\transformations.fa.md`
```md
---
title: 'Transformations'
slug: "transformations"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transformations

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\transformations.md`
```md
---
title: 'Transformations'
slug: "transformations"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Transformations

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\unspeakable-horrors.fa.md`
```md
---
title: 'Unspeakable horrors'
slug: "unspeakable-horrors"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unspeakable horrors

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\unspeakable-horrors.md`
```md
---
title: 'Unspeakable horrors'
slug: "unspeakable-horrors"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Unspeakable horrors

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-acuity-enhancement.fa.md`
```md
---
title: 'Visual acuity enhancement'
slug: "visual-acuity-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-acuity-enhancement.md`
```md
---
title: 'Visual acuity enhancement'
slug: "visual-acuity-enhancement"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity enhancement

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-acuity-suppression.fa.md`
```md
---
title: 'Visual acuity suppression'
slug: "visual-acuity-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-acuity-suppression.md`
```md
---
title: 'Visual acuity suppression'
slug: "visual-acuity-suppression"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual acuity suppression

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-effects.fa.md`
```md
---
title: 'Visual_effects'
slug: "visual-effects"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-effects.md`
```md
---
title: 'Visual_effects'
slug: "visual-effects"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual_effects

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-flipping.fa.md`
```md
---
title: 'Visual flipping'
slug: "visual-flipping"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual flipping

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-flipping.md`
```md
---
title: 'Visual flipping'
slug: "visual-flipping"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual flipping

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-haze.fa.md`
```md
---
title: 'Visual haze'
slug: "visual-haze"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual haze

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-haze.md`
```md
---
title: 'Visual haze'
slug: "visual-haze"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual haze

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-processing-acceleration.fa.md`
```md
---
title: 'Visual processing acceleration'
slug: "visual-processing-acceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing acceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-processing-acceleration.md`
```md
---
title: 'Visual processing acceleration'
slug: "visual-processing-acceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing acceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-processing-deceleration.fa.md`
```md
---
title: 'Visual processing deceleration'
slug: "visual-processing-deceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing deceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-processing-deceleration.md`
```md
---
title: 'Visual processing deceleration'
slug: "visual-processing-deceleration"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual processing deceleration

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-stretching.fa.md`
```md
---
title: 'Visual stretching'
slug: "visual-stretching"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual stretching

_Page coming soon._

```

---
### `src\wiki\Effects\Visual_effects\visual-stretching.md`
```md
---
title: 'Visual stretching'
slug: "visual-stretching"
lang: "en"
category: 'Visual_effects'
weight: 1000
template: "wiki"
summary: ''
---

# Visual stretching

_Page coming soon._

```

---
### `src\assets\backgrounds\bwca-dusk.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `src\assets\backgrounds\bwca-night.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `public\images\bedoone_khodahafezi.jpg`
```jpg
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
```

---
### `public\images\Cry As Punishment En.jpg`
```jpg
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
```

---
### `public\images\Cry As Punishment Fa.jpg`
```jpg
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
```

---
### `public\images\gardanravan.jpg`
```jpg
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
```

---
### `public\images\sum.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `public\images\tasmim 11.jpg`
```jpg
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
```

---
### `public\images\Threshold.jpeg`
```jpeg
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte]
```

---
### `public\images\vincenzo.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `public\images\اثاثیاست یک دست میز و صندلی نگران.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `public\images\محل تبلیغات شما.png`
```png
[Error reading file: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte]
```

---
### `public\pdf\bedoone_khodahafezi.pdf`
```pdf
[Error reading file: 'utf-8' codec can't decode byte 0xff in position 159: invalid start byte]
```

---
### `public\pdf\khianat_va_mokafat.pdf`
```pdf
[Error reading file: 'utf-8' codec can't decode byte 0x9c in position 67: invalid start byte]
```

---
### `public\pdf\tasmim_baraye_cobra_11.pdf`
```pdf
[Error reading file: 'utf-8' codec can't decode byte 0x9c in position 67: invalid start byte]
```

---
### `public\pdf\vincenzo.pdf`
```pdf
[Error reading file: 'utf-8' codec can't decode byte 0xb5 in position 11: invalid start byte]
```

---
### `public\pdf\اثاثیاست یک دست میز و صندلی نگران.pdf`
```pdf
[Error reading file: 'utf-8' codec can't decode byte 0xb5 in position 11: invalid start byte]
```

---
### `public\pdf\محل تبلیغات شما.pdf`
```pdf
[Error reading file: 'utf-8' codec can't decode byte 0xb5 in position 11: invalid start byte]
```

---
### `public\scripts\nav-effects.js`
```js
// public/scripts/nav-effects.js

document.addEventListener("DOMContentLoaded", function () {
  var links = document.querySelectorAll("[data-nav-link]");

  links.forEach(function (link) {
    var wave = link.querySelector(".wave");
    if (!wave) return;

    var letters = wave.querySelectorAll(".wave-letter");
    if (!letters.length) return;

    // Store original characters once
    var originals = [];
    letters.forEach(function (l) {
      originals.push(l.textContent || "");
    });

    // ===========================
    // 🌊 HOVER WAVES
    // ===========================
    var waveRunId = 0;
    var hadEntered = false;

    function playWave(direction) {
      waveRunId++;
      var id = waveRunId;

      link.classList.remove("glitch-strong");
      wave.classList.remove("wave-active");
      wave.classList.remove("wave-reverse");

      // force reflow so animation restarts
      void wave.offsetWidth;

      if (direction === "forward") {
        wave.classList.add("wave-active");
      } else {
        wave.classList.add("wave-reverse");
      }

      var total = 800 + letters.length * 120;

      setTimeout(function () {
        if (waveRunId !== id) return; // a newer wave started
        wave.classList.remove("wave-active");
        wave.classList.remove("wave-reverse");
        link.classList.add("glitch-strong");
      }, total);
    }

    link.addEventListener("mouseenter", function () {
      hadEntered = true;
      playWave("forward");
    });

    link.addEventListener("mouseleave", function () {
      if (!hadEntered) return;
      hadEntered = false;
      playWave("reverse");
    });

    // ===========================
    // 🎰 SLOT MACHINE ON CLICK
    // ===========================
    link.addEventListener("click", function (e) {
      // only intercept simple left-clicks
      if (
        e.button !== 0 ||
        e.metaKey ||
        e.ctrlKey ||
        e.shiftKey ||
        e.altKey
      ) {
        return;
      }

      e.preventDefault(); // stop immediate navigation

      var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      var spins = 5;          // how many random chars per letter
      var frame = 70;         // ms between random chars
      var letterDelay = 80;   // stagger between letters

      letters.forEach(function (letter, index) {
        var original = originals[index] || "";
        var startDelay = index * letterDelay;
        var step = 0;

        setTimeout(function runStep() {
          if (step >= spins) {
            letter.textContent = original;
            return;
          }
          var randomIndex = Math.floor(Math.random() * alphabet.length);
          letter.textContent = alphabet.charAt(randomIndex);
          step++;
          setTimeout(runStep, frame);
        }, startDelay);
      });

      // total time until the last letter is done
      var totalDuration =
        (letters.length - 1) * letterDelay +
        spins * frame +
        80;

      var href = link.getAttribute("href");
      if (href) {
        setTimeout(function () {
          window.location.href = href;
        }, totalDuration);
      }
    });
  });
});

```

---
### `public\scripts\navbar.js`
```js
document.addEventListener("DOMContentLoaded", () => { 
  const hamburger =
    document.querySelector("[data-hamburger]") ||
    document.querySelector("button[aria-label='Menu']");

  const sidebar = document.querySelector("[data-sidebar]");
  const backdrop = document.querySelector("[data-sidebar-backdrop]");
  const utilityBg = document.querySelector("[data-utility-bg]");
  const modeWrapper = document.querySelector("[data-mode-wrapper]");
  const mainNav = document.querySelector("[data-main-nav]");

  if (!(hamburger && sidebar && backdrop && utilityBg && modeWrapper && mainNav)) {
    console.warn("[navbar.js] Missing one or more required elements.");
    return;
  }

  const navLinks = mainNav.querySelectorAll("a");

  // ==============================
  // SOCIAL BAR FETCH (async load)
  // ==============================
  let social = null;
  window.addEventListener("load", () => {
    social = document.querySelector("[data-social]") || document.getElementById("social");
  });


  // ==============================
  // HELPER FUNCTIONS
  // ==============================
  const computeShift = () => {
    const sidebarWidth = sidebar.offsetWidth || 300;
    return -(sidebarWidth / 2.4);
  };

  const moveSocialToSidebarCenter = () => {
    if (!social) return;

    const socialRect = social.getBoundingClientRect();
    const sidebarRect = sidebar.getBoundingClientRect();

    const deltaX =
      (sidebarRect.left + sidebarRect.width / 2) -
      (socialRect.left + socialRect.width / 2);

    const base = getComputedStyle(social).transform;
    social.style.transform = `${base === "none" ? "" : base} translateX(${deltaX}px)`;
  };

  const resetSocialPosition = () => {
    if (!social) return;
    social.style.transform = "";
  };

  const disableMainNavTabbing = () => {
    navLinks.forEach(link => {
      link.dataset.oldTabindex = link.getAttribute("tabindex") ?? "";
      link.setAttribute("tabindex", "-1");
    });
  };

  const enableMainNavTabbing = () => {
    navLinks.forEach(link => {
      const old = link.dataset.oldTabindex;
      if (old === "") link.removeAttribute("tabindex");
      else link.setAttribute("tabindex", old);
      delete link.dataset.oldTabindex;
    });
  };

  const disableMainNav = () => {
    disableMainNavTabbing();
    mainNav.setAttribute("aria-hidden", "true");
    mainNav.classList.add("nav-hidden");
  };

  const enableMainNav = () => {
    enableMainNavTabbing();
    mainNav.removeAttribute("aria-hidden");
    mainNav.classList.remove("nav-hidden");
  };


  // ==============================
  // SIDEBAR OPEN/CLOSE
  // ==============================
  const openSidebar = () => {
    sidebar.classList.remove("translate-x-full");
    sidebar.classList.add("translate-x-0");

    backdrop.classList.remove("opacity-0", "pointer-events-none");

    utilityBg.classList.add("fade-out", "expanded");

    sidebar.removeAttribute("inert");
    sidebar.setAttribute("aria-hidden", "false");

    const shift = computeShift();
    modeWrapper.style.transform = `translateX(${shift}px)`;

    disableMainNav();

    setTimeout(() => moveSocialToSidebarCenter(), 400);

    setTimeout(() => {
      const firstLink = sidebar.querySelector("a");
      if (firstLink) firstLink.focus();
    }, 300);

    document.dispatchEvent(new Event("sidebar:open"));
  };

  const closeSidebar = () => {
    sidebar.classList.add("translate-x-full");
    sidebar.classList.remove("translate-x-0");

    backdrop.classList.add("opacity-0", "pointer-events-none");

    utilityBg.classList.remove("fade-out", "expanded");

    sidebar.setAttribute("inert", "");
    sidebar.setAttribute("aria-hidden", "true");

    modeWrapper.style.transform = "";

    // only enable if screen is large
    if (window.innerWidth >= 768) enableMainNav();

    resetSocialPosition();

    document.dispatchEvent(new Event("sidebar:close"));
  };


  // ==============================
  // EVENT LISTENERS
  // ==============================
  hamburger.addEventListener("click", (e) => {
    e.stopPropagation();
    const isOpen = sidebar.classList.contains("translate-x-0");
    isOpen ? closeSidebar() : openSidebar();
  });

  backdrop.addEventListener("click", (e) => {
    if (e.target === backdrop) closeSidebar();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeSidebar();
  });

  window.addEventListener("resize", () => {
    if (sidebar.classList.contains("translate-x-0")) {
      const shift = computeShift();
      modeWrapper.style.transform = `translateX(${shift}px)`;
      moveSocialToSidebarCenter();
    }
    applyResponsiveNavState();
  });


  // ==============================
  // RESPONSIVE NAV LOGIC
  // ==============================
  const applyResponsiveNavState = () => {
    if (window.innerWidth < 768) {
      disableMainNav();
    } else {
      // If sidebar is open → keep nav disabled
      if (!sidebar.classList.contains("translate-x-0")) {
        enableMainNav();
      }
    }
  };

  applyResponsiveNavState();
});

```

